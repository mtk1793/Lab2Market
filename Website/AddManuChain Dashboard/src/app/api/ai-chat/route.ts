import { NextRequest, NextResponse } from 'next/server'
import { requireAuth } from '@/lib/require-auth'

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY

// ─── Rate limiter — 20 req/min per IP ─────────────────────────────────────────
const rateLimitMap = new Map<string, { count: number; resetAt: number }>()
function checkRateLimit(ip: string): boolean {
  const now = Date.now()
  const entry = rateLimitMap.get(ip)
  if (!entry || now > entry.resetAt) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + 60_000 })
    return true
  }
  if (entry.count >= 20) return false
  entry.count++
  return true
}

// ─── Tool definitions (OpenAI format — used by OpenRouter) ────────────────────

const TOOLS = [
  {
    type: 'function',
    function: {
      name: 'navigate_to_page',
      description: 'Navigate the user to a specific page in the AddManuChain dashboard.',
      parameters: {
        type: 'object',
        properties: {
          page: {
            type: 'string',
            enum: [
              'overview', 'orders', 'print_queue', 'blueprints', 'centers',
              'peer_printers', 'shipments', 'materials', 'partners', 'analytics',
              'audit', 'certifications', 'authorities', 'services',
              'digital_inventory', 'physical_inventory', 'ip_library', 'lab_portal', 'settings',
            ],
            description: 'The page ID to navigate to',
          },
        },
        required: ['page'],
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'get_dashboard_stats',
      description: 'Fetch live KPI stats from the dashboard: active orders, delivered, lead time, cost savings, etc.',
      parameters: { type: 'object', properties: {} },
    },
  },
  {
    type: 'function',
    function: {
      name: 'list_orders',
      description: 'List orders from the system, optionally filtered by status or priority.',
      parameters: {
        type: 'object',
        properties: {
          status: {
            type: 'string',
            description: 'Filter by order status: pending, printing, qc, shipped, delivered',
          },
          limit: {
            type: 'number',
            description: 'Max number of orders to return (default 5)',
          },
        },
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'list_blueprints',
      description: 'List blueprints from the vault, optionally filtered by status or category.',
      parameters: {
        type: 'object',
        properties: {
          status: {
            type: 'string',
            description: 'Filter by status: active, pending_review, inactive, archived',
          },
          limit: {
            type: 'number',
            description: 'Max number to return (default 5)',
          },
        },
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'create_order',
      description: 'Create a new print order in the system on behalf of the user.',
      parameters: {
        type: 'object',
        properties: {
          partName: {
            type: 'string',
            description: 'Name of the part to print',
          },
          priority: {
            type: 'string',
            enum: ['low', 'normal', 'high', 'urgent'],
            description: 'Order priority level',
          },
          quantity: {
            type: 'number',
            description: 'Number of parts to print',
          },
          notes: {
            type: 'string',
            description: 'Additional notes or instructions for the order',
          },
        },
        required: ['partName', 'priority', 'quantity'],
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'list_materials',
      description: 'List material inventory levels at print centers, optionally filtered by stock status.',
      parameters: {
        type: 'object',
        properties: {
          status: {
            type: 'string',
            description: 'Filter by stock status: adequate, low, critical',
          },
        },
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'list_certifications',
      description: 'List active certifications and their expiry status.',
      parameters: {
        type: 'object',
        properties: {
          status: {
            type: 'string',
            description: 'Filter by status: active, pending, expiring_soon, expired',
          },
        },
      },
    },
  },
]

// ─── System prompt ─────────────────────────────────────────────────────────────

const SYSTEM_PROMPT = `You are the AddManuChain AI Assistant — an agentic, friendly expert embedded inside the AddManuChain digital supply chain dashboard for the offshore oil & gas and heavy industry sector.

You are NOT just a Q&A bot. You can take real actions inside the dashboard using your tools:
- Navigate the user to any page instantly
- Fetch live data (orders, blueprints, materials, certifications, stats)
- Create new orders on behalf of the user

Always prefer taking action over just describing how to do something. For example:
- If the user says "show me the orders page" → call navigate_to_page("orders")
- If the user asks "how many pending orders?" → call list_orders({ status: "pending" }) and report the actual count
- If the user says "create an order for a valve" → call create_order(...)
- If the user asks "what are my stats?" → call get_dashboard_stats()

After taking an action, briefly confirm what you did and offer the next helpful step.

---

## DASHBOARD PAGES

Navigation page IDs:
- overview, orders, print_queue, blueprints, centers, peer_printers, shipments, materials
- partners, analytics, audit, certifications, authorities, services (Customer Success)
- digital_inventory, physical_inventory, ip_library, lab_portal, settings

## ALL PAGES — DETAILED KNOWLEDGE

### 1. OVERVIEW — Executive KPIs (read-only): Active Orders, Parts Delivered, Avg Lead Time, Cost Savings, DRM funnel, site health, print center status, activity feed.

### 2. ORDERS — Full order lifecycle. Create/edit/delete orders. Status: pending → printing → qc → shipped → delivered. Issue Secure Print tokens after OEM + Cert approval. Role-scoped views.

### 3. PRINT QUEUE (DRM) — Approval pipeline. OEM grants IP license, Cert Authority verifies facility, Print Center issues token. Pipeline: Submitted → OEM Approved → Cert Verified → Token Issued.

### 4. IP LIBRARY — OEM IP vault. License models: Restricted, Open, Pay-Per-Print, Consortium. Manage IP assets, approve license requests, track royalties and usage.

### 5. BLUEPRINT LIBRARY — Certified CAD files (STL/STEP/3MF). Add/view/delete blueprints. Technical drawing viewer with isometric + orthographic views. Status: active/pending_review/inactive/archived.

### 6. OEM PARTNERS — Manage OEM, integrator, distributor, service provider relationships. Track blueprints, prints, royalties per partner.

### 7. DIGITAL INVENTORY — AI risk scoring. Interactive Canada print center map. Risk queue ranks blueprints by urgency. Quick Order for high-risk parts. AI workflow: Predict → Approve → Secure Print → Verify.

### 8. PHYSICAL INVENTORY — Site-based inventory (rigs, vessels, yards, warehouses). Part conditions: New, Serviceable, Used, Condemned. Transfer workflows between sites.

### 9. PRINT CENTERS — Certified AM facility network. Network tab (add/view centers) + Onsite Printing tab (configure onsite/virtual/hybrid engagements).

### 10. PEER PRINTERS — Airbnb-style marketplace for idle certified 3D printer capacity.

### 11. SHIPMENTS — Track deliveries. Status: preparing, in_transit, out_for_delivery, delivered, delayed. Supports offshore helicopter/sea transport.

### 12. MATERIALS — Raw material stock. Status: adequate, low, critical. Per-center distribution. Purchase order creation for critical stock.

### 13. CERTIFICATIONS — Cert validity tracking. Issuer, holder, validity progress bar, days remaining. Renewal workflow. Alert for certs expiring within 30 days.

### 14. AUTHORITIES — Manage DNV GL, Lloyd's, BV, ABS, TÜV SÜD, ClassNK. Certification request approval queue.

### 15. AUDIT LOGS — SHA-256 hash-chain compliance log. Action types: ORDER_CREATED, OEM_APPROVED, CERT_APPROVED, PRINT_TOKEN_ISSUED, PRINT_EXECUTED. Tamper detection via chain integrity verification.

### 16. LAB PORTAL — Dalhousie AM Lab. Test types: Mechanical, Chemical, Thermal, Dimensional, NDT, Fatigue. Equipment reservation. Cert standards: DNV GL, Lloyd's, BV, ClassNK, ABS, ISO 9001.

### 17. ANALYTICS — Monthly trends, lead time comparison (traditional 63 days vs AddManuChain), cost savings, environmental impact (CO₂, miles, waste). Role-scoped. Time range: 30d/3m/6m/1y.

### 18. CUSTOMER SUCCESS — Trained personnel registry. Qualification levels L1–L4. Module-based training, renewal tracking, certificate downloads.

### 19. SETTINGS — Profile, Organization, Notifications, Security (2FA), API keys, Webhooks, Tutorial restart.

---

## USER ROLES

| Role | Key Pages |
|------|-----------|
| Admin | All 19 pages |
| OEM Partner | IP Library, Blueprints, Print Queue, Partners, Certifications, Analytics, Settings |
| End User | Overview, Orders, Peer Printers, Shipments, Physical Inventory, Customer Success, Settings |
| Cert Authority | Overview, Print Queue, Blueprints, Certifications, Authorities, Audit Logs, Analytics, Settings |
| Lab | Overview, Lab Portal, Blueprints, Materials, Digital/Physical Inventory, Certifications, Analytics, Settings |
| Print Center | Overview, Orders, Print Queue, Blueprints, Materials, Digital/Physical Inventory, Shipments, Settings |

Demo credentials: admin@almatech.com / admin123 | operator@statoil.com / operator123 | partner@oem.com / partner123

---

## KEY CONCEPTS

- **DRM Token**: One-time encrypted Secure Print token, auto-expires 30s after display. Required to start printing.
- **Blueprint**: OEM-owned certified CAD file. Cert type must match print center cert for DRM approval.
- **Hash Chain**: SHA-256 linked audit log. Tampered entries break the chain (shown as red integrity banner).
- **Risk Score**: 0–100 AI score per blueprint. Factors: print history, material availability, cert restrictions, criticality.
- **Peer Printers**: Certified operators list idle printer time — like Airbnb for industrial 3D printers.

Tone: Professional but friendly. Concise. Use bullet points for steps. Never invent features that don't exist. Always prefer taking action over just explaining.`

const ROLE_CONTEXT: Record<string, string> = {
  admin: 'Current user: Platform Admin (Mahmoud K. — AddManuChain). Full access to all features.',
  oem_partner: 'Current user: OEM Partner (Johann Weber — Wärtsilä Marine). Focus: IP Library, Blueprint Library, Print Queue, Analytics.',
  end_user: 'Current user: End User / Client (Capt. Sarah Leblanc — Horizon Maritime). Focus: Orders, Shipments, Physical Inventory.',
  cert_authority: 'Current user: Cert Authority rep (Dr. Priya Patel — DNV GL). Focus: Print Queue, Certifications, Authorities, Audit Logs.',
  print_center: 'Current user: Print Facility operator (Michael Okafor — PolyUnity NL). Focus: Print Queue, Materials, Orders, Shipments.',
  lab: 'Current user: Lab professional (Prof. Ahmad Osman — Dalhousie AM Lab). Focus: Lab Portal, Materials, Blueprints, Certifications.',
}

// ─── Tool executor ────────────────────────────────────────────────────────────

async function executeTool(
  name: string,
  args: Record<string, unknown>,
  baseUrl: string,
): Promise<{ result: string; frontendAction?: Record<string, unknown> }> {

  switch (name) {

    case 'navigate_to_page': {
      const page = args.page as string
      const labels: Record<string, string> = {
        overview: 'Dashboard Overview', orders: 'Orders', print_queue: 'Print Queue',
        blueprints: 'Blueprint Library', centers: 'Print Centers', peer_printers: 'Peer Printers',
        shipments: 'Shipments', materials: 'Materials', partners: 'OEM Partners',
        analytics: 'Analytics', audit: 'Audit Logs', certifications: 'Certifications',
        authorities: 'Certification Authorities', services: 'Customer Success',
        digital_inventory: 'Digital Inventory', physical_inventory: 'Physical Inventory',
        ip_library: 'IP Library', lab_portal: 'Lab & Testing Portal', settings: 'Settings',
      }
      return {
        result: `Navigated to ${labels[page] ?? page}`,
        frontendAction: { type: 'navigate', page, label: labels[page] ?? page },
      }
    }

    case 'get_dashboard_stats': {
      try {
        const res = await fetch(`${baseUrl}/api/stats`)
        const data = await res.json()
        return { result: JSON.stringify(data) }
      } catch {
        return { result: 'Could not fetch stats at this time.' }
      }
    }

    case 'list_orders': {
      try {
        const params = new URLSearchParams()
        if (args.status) params.set('status', args.status as string)
        const res = await fetch(`${baseUrl}/api/orders?${params}`)
        const data = await res.json()
        const orders = (Array.isArray(data) ? data : data.orders ?? [])
          .slice(0, (args.limit as number) ?? 5)
        if (orders.length === 0) return { result: 'No orders found matching the criteria.' }
        const summary = orders.map((o: Record<string, unknown>) =>
          `#${o.id ?? o.orderId} — ${o.partName ?? o.name} | Status: ${o.status} | Priority: ${o.priority} | Qty: ${o.quantity}`
        ).join('\n')
        return { result: `Found ${orders.length} order(s):\n${summary}` }
      } catch {
        return { result: 'Could not fetch orders at this time.' }
      }
    }

    case 'list_blueprints': {
      try {
        const params = new URLSearchParams()
        if (args.status) params.set('status', args.status as string)
        const res = await fetch(`${baseUrl}/api/blueprints?${params}`)
        const data = await res.json()
        const blueprints = (Array.isArray(data) ? data : data.blueprints ?? [])
          .slice(0, (args.limit as number) ?? 5)
        if (blueprints.length === 0) return { result: 'No blueprints found matching the criteria.' }
        const summary = blueprints.map((b: Record<string, unknown>) =>
          `${b.name} | Category: ${b.category} | Material: ${b.material} | Status: ${b.status} | Prints: ${b.printCount ?? 0}`
        ).join('\n')
        return { result: `Found ${blueprints.length} blueprint(s):\n${summary}` }
      } catch {
        return { result: 'Could not fetch blueprints at this time.' }
      }
    }

    case 'create_order': {
      try {
        const body = {
          partName: args.partName,
          priority: args.priority ?? 'normal',
          quantity: args.quantity ?? 1,
          notes: args.notes ?? '',
          status: 'pending',
        }
        const res = await fetch(`${baseUrl}/api/orders`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        })
        const data = await res.json()
        const id = data.id ?? data.orderId ?? 'NEW'
        return {
          result: `Order created successfully. ID: ${id}, Part: ${args.partName}, Priority: ${args.priority}, Qty: ${args.quantity}`,
          frontendAction: {
            type: 'created',
            entity: 'order',
            label: `Order created: ${args.partName} (${args.priority} priority)`,
            id,
          },
        }
      } catch {
        return { result: 'Could not create order at this time.' }
      }
    }

    case 'list_materials': {
      try {
        const res = await fetch(`${baseUrl}/api/materials`)
        const data = await res.json()
        let materials = Array.isArray(data) ? data : data.materials ?? []
        if (args.status) materials = materials.filter((m: Record<string, unknown>) => m.status === args.status)
        materials = materials.slice(0, 6)
        if (materials.length === 0) return { result: 'No materials found matching the criteria.' }
        const summary = materials.map((m: Record<string, unknown>) =>
          `${m.name} | Category: ${m.category} | Stock: ${m.stockLevel ?? m.currentStock} | Status: ${m.status}`
        ).join('\n')
        return { result: `Found ${materials.length} material(s):\n${summary}` }
      } catch {
        return { result: 'Could not fetch materials at this time.' }
      }
    }

    case 'list_certifications': {
      try {
        const res = await fetch(`${baseUrl}/api/certifications`)
        const data = await res.json()
        let certs = Array.isArray(data) ? data : data.certifications ?? []
        if (args.status) certs = certs.filter((c: Record<string, unknown>) => c.status === args.status)
        certs = certs.slice(0, 6)
        if (certs.length === 0) return { result: 'No certifications found matching the criteria.' }
        const summary = certs.map((c: Record<string, unknown>) =>
          `${c.name} | Issuer: ${c.issuer} | Status: ${c.status} | Expires: ${c.expiryDate ?? 'N/A'}`
        ).join('\n')
        return { result: `Found ${certs.length} certification(s):\n${summary}` }
      } catch {
        return { result: 'Could not fetch certifications at this time.' }
      }
    }

    default:
      return { result: `Unknown tool: ${name}` }
  }
}

// ─── Route handler ─────────────────────────────────────────────────────────────

export async function POST(req: NextRequest) {
  try {
    const { session, error } = await requireAuth()
    if (error) return error

    const ip = req.headers.get('x-forwarded-for')?.split(',')[0]?.trim() ?? 'unknown'
    if (!checkRateLimit(ip)) {
      return NextResponse.json({ error: 'Too many requests. Please wait before trying again.' }, { status: 429 })
    }

    if (!OPENROUTER_API_KEY) {
      return NextResponse.json({ error: 'AI service not configured' }, { status: 500 })
    }

    const { messages, role } = await req.json()
    if (!messages || !Array.isArray(messages)) {
      return NextResponse.json({ error: 'Invalid request' }, { status: 400 })
    }

    const baseUrl = new URL(req.url).origin
    const roleCtx = ROLE_CONTEXT[role ?? 'admin'] ?? ROLE_CONTEXT.admin
    const fullSystemPrompt = `${SYSTEM_PROMPT}\n\n${roleCtx}`

    // Build the conversation — keep last 10 messages for context
    let conversationMessages = [
      ...messages.slice(-10),
    ]

    let frontendAction: Record<string, unknown> | undefined
    const MAX_TOOL_ROUNDS = 4

    // Agentic loop: call model → execute tools → repeat until done
    for (let round = 0; round < MAX_TOOL_ROUNDS; round++) {
      const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': 'https://addmanuchain-dashboard.vercel.app',
          'X-Title': 'AddManuChain Dashboard',
        },
        body: JSON.stringify({
          model: 'anthropic/claude-3.5-haiku',
          messages: [
            { role: 'system', content: fullSystemPrompt },
            ...conversationMessages,
          ],
          tools: TOOLS,
          tool_choice: 'auto',
          max_tokens: 1024,
          temperature: 0.7,
        }),
      })

      if (!response.ok) {
        const err = await response.text()
        console.error('OpenRouter error:', err)
        return NextResponse.json({ error: 'AI service error' }, { status: 502 })
      }

      const data = await response.json()
      const choice = data.choices?.[0]
      const assistantMessage = choice?.message

      if (!assistantMessage) break

      // No tool calls — we have the final text response
      if (!assistantMessage.tool_calls || assistantMessage.tool_calls.length === 0) {
        const reply = assistantMessage.content ?? 'Sorry, I couldn\'t generate a response.'
        return NextResponse.json({ reply, frontendAction })
      }

      // Add assistant message (with tool_calls) to conversation
      conversationMessages.push(assistantMessage)

      // Execute each tool call
      const toolResults: { role: string; tool_call_id: string; content: string }[] = []
      for (const toolCall of assistantMessage.tool_calls) {
        const toolName = toolCall.function.name
        let toolArgs: Record<string, unknown> = {}
        try {
          toolArgs = JSON.parse(toolCall.function.arguments ?? '{}')
        } catch { /* invalid JSON */ }

        const { result, frontendAction: action } = await executeTool(toolName, toolArgs, baseUrl)

        // Keep the last frontend action (navigate takes priority)
        if (action) {
          if (!frontendAction || action.type === 'navigate') {
            frontendAction = action
          }
        }

        toolResults.push({
          role: 'tool',
          tool_call_id: toolCall.id,
          content: result,
        })
      }

      // Add tool results to conversation and loop
      conversationMessages = [...conversationMessages, ...toolResults]
    }

    // Fallback if loop exhausted
    return NextResponse.json({
      reply: 'I completed the requested actions. Let me know if you need anything else.',
      frontendAction,
    })

  } catch (err) {
    console.error('AI chat error:', err)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}
