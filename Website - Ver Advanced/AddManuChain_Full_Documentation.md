# AddManuChain Dashboard — Full Technical Documentation
> Prepared for AI-assisted improvement review · March 2026

---

## 1. Executive Summary

**AddManuChain** is a B2B SaaS platform that digitises the spare parts supply chain for the offshore oil & gas and heavy industry sectors using **additive manufacturing (3D printing)**. Instead of ordering physical parts from OEMs with 63-day average lead times, customers print certified parts on-demand at nearby certified print centres — reducing lead times to under 5 days, cutting warehouse costs, and eliminating long-distance shipping.

### Business Model
- **Platform fee** per transaction (order processed through the DRM pipeline)
- **Royalty metering** — OEMs earn per-print royalties on their IP assets
- **SaaS subscription** for print centres and OEM partners
- **Lab testing fees** for certification of new blueprints

### Live URLs
| Site | URL |
|------|-----|
| Dashboard | https://addmanuchain-dashboard.vercel.app |
| Landing Page | https://addmanuchain-landing.vercel.app |
| Main Site | https://addmanuchain.vercel.app |

### Current Status
- MVP complete · Pilot-ready
- 19 fully functional dashboard pages
- Live on Neon PostgreSQL with seeded demo data
- Agentic Claude AI assistant integrated
- GitHub: github.com/mtk1793/Lab2Market

---

## 2. Tech Stack

### Frontend
| Layer | Technology |
|-------|-----------|
| Framework | Next.js 16.1.6 (App Router, Turbopack) |
| Language | TypeScript |
| Styling | Tailwind CSS 3 |
| UI Components | shadcn/ui (Radix UI primitives) |
| Charts | Recharts |
| Animations | Framer Motion |
| Data Fetching | SWR (stale-while-revalidate) |
| Icons | Lucide React |

### Backend
| Layer | Technology |
|-------|-----------|
| API | Next.js Route Handlers (24 routes) |
| ORM | Prisma 6.11 |
| Auth | NextAuth v4 (JWT strategy, CredentialsProvider, bcrypt) |
| Validation | Zod |
| Error Tracking | Sentry |

### Infrastructure
| Layer | Technology |
|-------|-----------|
| Database (prod) | Neon PostgreSQL (serverless, pooled) |
| Database (dev) | SQLite |
| Deployment | Vercel (standalone output) |
| AI | OpenRouter → Claude 3.5 Haiku (agentic tool-calling) |
| Repo | GitHub — mtk1793/Lab2Market |

### Key Dependencies
```
next@16.1.6, react@19, typescript, tailwindcss, @prisma/client@6.11
next-auth@4.24, @next-auth/prisma-adapter, bcryptjs
recharts, framer-motion, swr, lucide-react, zod
@sentry/nextjs, shadcn/ui components
```

---

## 3. All 19 Dashboard Pages

### Navigation Structure (Sidebar)
```
Main          → Overview · Orders · Print Queue
OEM & IP      → IP Library · Blueprint Library · OEM Partners
Supply Chain  → Digital Inventory · Physical Inventory · Print Centers · Peer Printers · Shipments · Materials
Compliance    → Certifications · Authorities · Audit Logs
Lab           → Lab Portal
Insights      → Analytics · Customer Success
System        → Settings
```

---

### 3.1 Overview (`/` → tab: `overview`)
**Purpose:** Executive read-only dashboard — first screen after login.

**Data displayed:**
- KPI cards: Active Orders, Parts Delivered, Avg Lead Time (days), Cost Savings ($) — each with 7-day sparkline trend
- Order Pipeline bar chart: counts by status (pending → printing → QC → shipped → delivered)
- DRM Approval Funnel: orders at each approval stage (locked → partially approved → ready → printing → tokens issued)
- Physical Site Health grid: per-rig/warehouse inventory alert counts and health score
- Print Centers grid: live status (online/busy/offline) with capacity load bars
- Blueprint Vault ring chart: active/pending/archived counts
- Physical Inventory summary: out-of-stock, low stock, condemned counts + total value
- Live Activity Feed: last 8 inventory transactions (action type, location, timestamp)

**Actions:** Read-only — no user actions.

---

### 3.2 Orders (`orders`)
**Purpose:** Full order lifecycle management from creation to delivery.

**Data displayed:**
- Status stats bar: total, pending, printing, QC, shipped, delivered counts
- Orders table columns: Order ID · Part Name · Status badge · Priority · Qty · DRM Approvals (OEM ✓ / Cert ✓) · ETA
- Role-scoped views: admin sees all; end_user sees own; print_center sees assigned; oem_partner sees approval queue

**User actions:**
- Create order — dialog (part name, priority, qty, blueprint, print centre, notes)
- View order details — full DRM approval timeline with timestamps and approver names
- Edit order — status, priority, notes
- Issue Secure Print Token — one-time encrypted key, auto-hides 30s after display
- Delete order
- Search by keyword · Filter by status or priority

**Key workflow:** Customer submits → enters DRM queue → OEM approves IP licence → Cert Authority verifies facility → token issued → printing → QC → shipped → delivered

---

### 3.3 Print Queue / DRM (`print_queue`)
**Purpose:** Digital Rights Management approval pipeline — the core IP protection mechanism.

**Data displayed:**
- Role-specific approval queues (OEM sees licence queue, Cert Authority sees facility queue, Print Centre sees token queue)
- Approval cards: Order ID · Part name · Priority · Blueprint info · Print centre + certification match validation
- Pipeline stepper: Submitted → OEM Approved → Cert Verified → Token Issued (with timestamps)
- Alert banner showing orders ready to print

**User actions:**
- Grant IP licence (OEM role) — confirmation dialog explaining one-time decryption token
- Authorise print centre (Cert Authority role) — validates facility cert matches blueprint cert
- Issue token (Print Centre / Admin)
- View full pipeline status per order

**Key concept — DRM Token:** One-time encrypted Secure Print token. Generated only after both OEM + Cert Authority approve. Auto-expires 30 seconds after display. Required to start any print job.

---

### 3.4 IP Library (`ip_library`)
**Purpose:** OEM intellectual property vault, licensing, and royalty management.

**Data displayed:**
- Stats: Active IP assets · Total prints · Pending requests · Royalties earned
- IP assets table: Part name · Status · License type · Royalty rate · Print count · Authorised printers · Revenue generated
- License requests tab: pending/approved/rejected/info_requested queue
- Revenue tab: royalty earnings breakdown
- Usage tab: print volume per asset over time

**License models:**
- **Restricted** — pre-approved printers only, flat fee per print
- **Open** — no royalty, any certified printer
- **Pay-Per-Print** — percentage royalty per job
- **Consortium** — members-only access

**User actions:**
- Register new IP asset (part details, tech type, material, license model, royalty %, cert level, file upload, tags)
- Review and approve/reject licence requests
- Export IP assets
- View revenue reports and usage analytics

---

### 3.5 Blueprint Library (`blueprints`)
**Purpose:** Certified CAD file vault — the source of truth for printable part specifications.

**Data displayed:**
- Stats: Total blueprints · Active · Pending Review · Total Prints
- Blueprint list/grid: Blueprint ID · Name · Category · Material · OEM · Certification · Status · Print Count · File format
- Blueprint detail modal — 3 tabs:
  - **Drawing**: SVG technical drawing with isometric 3D view and orthographic views (Front/Top/Side)
  - **Details**: Category, material, OEM, certification standard, print count, description
  - **File**: CAD file preview, size, format (STL/STEP/3MF)

**User actions:**
- Add new blueprint (form + drag-and-drop file upload)
- Toggle list/grid view
- Search by name, part number, OEM, or tags
- Filter by status, category
- Delete · Export/download blueprint

**Status types:** `active` · `pending_review` · `inactive` · `archived`

**Role access:** Admins/OEM partners/labs can add and edit. End users and print centres browse only.

---

### 3.6 OEM Partners (`partners`)
**Purpose:** Manage OEM, integrator, distributor, and service provider relationships.

**Data displayed:**
- Stats: Total partners · Active count · Total blueprints · Total royalties earned
- Partners table: Name · Type · Status · Blueprints registered · Total Prints · Royalties

**Partner types:** OEM · Integrator · Distributor · Service Provider

**User actions:**
- Add new partner (company name, email, phone, type, location, notes)
- View/edit partner details (modal with contact info, stats, notes)
- Delete partner
- Search and filter by name, email, type, status

---

### 3.7 Digital Inventory (`digital_inventory`)
**Purpose:** AI-powered blueprint risk scoring and intelligent print queue management.

**Data displayed:**
- Stats: High-risk parts · DRM locked · Ready to print · Now printing · Material alerts
- Interactive Canada network map: SVG showing 5 print centres with status pins, capacity arcs, connection lines
- DRM pipeline funnel: visual funnel with order counts at each stage
- AI-ranked blueprint risk queue: Risk score bar · Blueprint name · Material · Stock status · OEM/Cert approval status · Print count · Quick Order button
- Material stock alert cards: low/critical materials with reorder details

**AI workflow:** Predict → Approve → Secure Print → Verify & Close

**Risk scoring factors:** print history, material availability, certification restrictions, part criticality (0–100 score)

**Action tiers:** Monitor (low) · Review (medium) · Queue (high) · Pre-print now (critical)

**User actions:**
- Click map pins → view centre details (capacity, status, certification)
- Quick Order on high-risk blueprints (pre-fills order form)
- Confirm order submission to DRM pipeline

---

### 3.8 Physical Inventory (`physical_inventory`)
**Purpose:** Site-based warehouse management for physical spare parts.

**Data displayed:**
- Inventory by site: offshore rigs, vessels, onshore yards, warehouses
- Part condition breakdown: New · Serviceable · Used · Condemned
- Stock transaction log: Received · Consumed · Condemned · Transferred In/Out · Inspected
- Stock level alerts per site

**User actions:**
- Transfer parts between sites
- Condemn parts (with reason)
- Log stock transactions
- Search and filter by site, part, condition

---

### 3.9 Print Centres (`centers`)
**Purpose:** Manage the certified additive manufacturing facility network.

**Two tabs:**

**Network tab:**
- Stats: Total · Online · Busy · Offline · Avg capacity %
- Centre cards: Name · Location · Capacity % · Active/Total printers · Current jobs · Completed today · Certification
- Actions: Add new centre · View details · Search/filter

**Onsite Printing tab:**
- Form to configure onsite printing engagement
- Fields: Mode (onsite/virtual/hybrid) · Site location · Access window · Safety requirements · Equipment needs · Support contacts · Notes

---

### 3.10 Peer Printers (`peer_printers`)
**Purpose:** Airbnb-style marketplace for idle certified 3D printer capacity.

Certified operators can list available printer time. Customers book specific printers for their jobs. Enables decentralised printing without requiring a dedicated certified facility.

---

### 3.11 Shipments (`shipments`)
**Purpose:** Track parts in transit from print centre to destination.

**Data displayed:**
- Stats: Total · In transit · Delivered · Delayed
- Shipment cards: Tracking ID · Part name · Status badge · Route (origin → destination) · Progress % · Distance · Carrier · ETA

**Status types:** `preparing` · `in_transit` · `out_for_delivery` · `delivered` · `delayed`

**User actions:**
- Search by tracking ID or destination
- Filter by status
- View full tracking details
- Refresh status

Supports offshore helicopter and sea transport tracking.

---

### 3.12 Materials (`materials`)
**Purpose:** Raw material stock management at print centres.

**Data displayed:**
- Stats: Total materials · Adequate · Low stock · Critical · Total inventory value
- Materials table: Name · Category · Stock level (global + per-centre) · Status · Distribution across centres · Unit cost · Lead time
- Alert banner for critical stock

**User actions:**
- Create purchase order for critical stock
- View per-centre stock breakdown
- Search and filter
- Role-scoped: print_centre users see only their facility's materials

**Stock status:** `adequate` · `low` · `critical`

---

### 3.13 Certifications (`certifications`)
**Purpose:** Track certification validity and manage renewals.

**Data displayed:**
- Stats: Total · Active · Pending · Expiring soon · Expired
- Table: Name · Type · Issuer · Holder · Validity progress bar · Days remaining · Status

**User actions:**
- Download certification documents
- View external certification links
- Start renewal process (for expiring certs)
- Refresh

Alert banner for certs expiring within 30 days. Colour coding: active (green) · pending (blue) · expiring soon (amber) · expired (red).

---

### 3.14 Certification Authorities (`authorities`)
**Purpose:** Manage relationships with certification bodies (DNV GL, Lloyd's, BV, ABS, TÜV SÜD, ClassNK).

**Data displayed:**
- Stats: Total · Active · Approved parts · Avg lead time · Pending requests
- Authorities table: Name · Type · Contact · Approved Parts · Avg Lead Time · Status
- Certification requests tab: pending/approved/rejected/info_requested queue

**Authority types:** Marine & Offshore · Marine & Industrial · Marine & Aerospace · Quality Standards · Oil & Gas · Aerospace

**User actions:**
- Add new authority (name, acronym, type, contact, website, specialisations)
- View/edit details
- Approve or reject certification requests
- Delete authority

---

### 3.15 Audit Logs (`audit`)
**Purpose:** Immutable cryptographic compliance log for regulatory requirements (DNV GL, Lloyd's, NORSOK).

**Data displayed:**
- Chain integrity status banner: green = verified · red = tampered
- Stats: Total logs · Orders created · OEM approvals · Cert approvals · Tokens issued
- Log entries: Action type · Order ID · Details · Timestamp · Part name · Hash verification · Hash chain preview

**Action types logged:** `ORDER_CREATED` · `ORDER_UPDATED` · `OEM_APPROVED` · `CERT_APPROVED` · `PRINT_TOKEN_ISSUED` · `PRINT_EXECUTED`

**User actions:**
- Filter by action type
- Refresh
- View full hash chain per entry

**Key concept — Hash Chain:** SHA-256 linked entries. Each entry contains the hash of the previous one. Any tampering breaks the chain (shown as red integrity banner). Provides tamper-evident audit trail for compliance.

---

### 3.16 Lab & Testing Portal (`lab_portal`)
**Purpose:** Dalhousie University AM Lab — test request management and equipment scheduling.

**Three tabs:**

**Test Requests:**
- Columns: ID · Status · Priority · Part info · Test types · Samples · Due date · Technician
- Actions: New test request (part name, number, test types checklist, sample count, priority, cert standard, file upload, notes) · Assign technician · Log results · Finalize reports

**Equipment:**
- Cards: Name · Type · Status · Utilisation % · Current job · Reserve button

**Reports:**
- Completed reports: result (pass/fail/conditional) · Issuer · Cert standard · Download PDF

**Test types:** Mechanical · Chemical · Thermal · Dimensional · NDT · Fatigue

**Certification standards:** DNV GL · Lloyd's · Bureau Veritas · ClassNK · ABS · ISO 9001

---

### 3.17 Analytics (`analytics`)
**Purpose:** Business intelligence, ROI demonstration, and comparative metrics.

**Data displayed:**
- KPI cards: Total orders · Avg lead time · Cost savings · Print efficiency
- Monthly orders & deliveries bar chart
- Lead time comparison line chart: traditional (63 days flat) vs AddManuChain (4–6 days)
- Blueprints by category donut chart
- Orders by status horizontal bar chart
- Print centre performance cards (jobs, avg time, quality %)
- Comparative section (when DB has data):
  - Lead time reduction (traditional vs AddManuChain side-by-side)
  - Warehouse cost savings
  - Part repair rate vs replacement rate
  - Design flexibility (custom iterations)
  - Environmental impact: CO₂ saved (kg) · Miles avoided · Waste reduced (kg)

**Time range selector:** 30 days · 3 months · 6 months · 1 year

**Role-scoped views:** end_user → own order impact; print_centre → facility utilisation; oem_partner → royalties; admin → platform-wide

---

### 3.18 Customer Success (`services`)
**Purpose:** Trained personnel registry and engagement tracking.

**Data displayed:**
- Personnel list: Name · Organisation · Role · Qualification level (L1–L4) · Modules completed · Authorised actions · Status
- Training sessions with dates and technician assignments
- Engagement tracking by organisation

**Qualification levels:**
- L1 — Basic operator
- L2 — Advanced operator
- L3 — Expert / supervisor
- L4 — Trainer / certifier

**User actions:**
- Register new trained personnel
- Assign training modules
- Track compliance and renewal dates
- Download training certificates
- View authorised actions per qualification level

---

### 3.19 Settings (`settings`)
**Purpose:** User profile, organisation, and system configuration.

**Six sections:**
1. **Profile** — First/last name, email, role
2. **Organisation** — Company name, sector, location, timezone
3. **Notifications** — Toggle: order updates, print completion, QC results, weekly reports, email alerts
4. **Security** — 2FA setup, password change, active session management
5. **API Access** — API key management, webhook URL configuration
6. **Help & Support** — Restart onboarding tutorial, documentation links, contact support

---

## 4. User Roles & Permissions Matrix

| Page | Admin | OEM Partner | End User | Cert Authority | Lab | Print Centre |
|------|:-----:|:-----------:|:--------:|:--------------:|:---:|:------------:|
| Overview | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Orders | ✓ | — | ✓ | — | — | ✓ |
| Print Queue (DRM) | ✓ | ✓ | — | ✓ | — | ✓ |
| IP Library | ✓ | ✓ | — | — | — | — |
| Blueprint Library | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| OEM Partners | ✓ | — | — | — | — | — |
| Digital Inventory | ✓ | — | — | — | ✓ | ✓ |
| Physical Inventory | ✓ | — | ✓ | — | ✓ | ✓ |
| Print Centres | ✓ | — | — | — | — | — |
| Peer Printers | ✓ | — | ✓ | — | — | — |
| Shipments | ✓ | — | ✓ | — | — | ✓ |
| Materials | ✓ | — | — | — | ✓ | ✓ |
| Certifications | ✓ | ✓ | — | ✓ | ✓ | — |
| Authorities | ✓ | — | — | ✓ | — | — |
| Audit Logs | ✓ | — | — | ✓ | — | — |
| Lab Portal | ✓ | — | — | — | ✓ | — |
| Analytics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Customer Success | ✓ | — | ✓ | — | — | — |
| Settings | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Demo Accounts
| Role | Email | Password |
|------|-------|----------|
| Admin | admin@almatech.com | admin123 |
| Operator | operator@statoil.com | operator123 |
| OEM Partner | partner@oem.com | partner123 |

---

## 5. API Routes (24 Routes)

All routes are protected by `requireAuth()` (returns 401 if no valid session) except `/api/auth/**` and `/api/contact`.

| Route | Methods | Purpose |
|-------|---------|---------|
| `/api/auth/[...nextauth]` | GET, POST | NextAuth session management (public) |
| `/api/contact` | POST | Public marketing contact form (public) |
| `/api/stats` | GET | Dashboard KPI aggregates |
| `/api/orders` | GET, POST | List and create orders |
| `/api/orders/[id]` | GET, PUT, DELETE | Single order CRUD |
| `/api/blueprints` | GET, POST | List and create blueprints |
| `/api/blueprints/[id]` | GET, PUT, DELETE | Single blueprint CRUD |
| `/api/centers` | GET, POST | List and create print centres |
| `/api/centers/[id]` | GET, PUT, DELETE | Single centre CRUD |
| `/api/partners` | GET, POST | List and create OEM partners |
| `/api/partners/[id]` | GET, PUT, DELETE | Single partner CRUD |
| `/api/shipments` | GET | List shipments |
| `/api/materials` | GET | List materials with stock levels |
| `/api/audit` | GET | List audit log entries |
| `/api/certifications` | GET | List certifications |
| `/api/cert-requests` | GET, POST, PUT | Certification request workflow |
| `/api/authorities` | GET, POST, DELETE | Certification authority CRUD |
| `/api/engagements` | GET, POST, PUT, DELETE | Customer engagement records |
| `/api/training` | GET, POST, PUT, DELETE | Training session records |
| `/api/customization` | GET, POST, PUT, DELETE | Blueprint customisation requests |
| `/api/comparative` | GET, POST | Comparative metrics (lead time, cost) |
| `/api/environmental` | GET, POST | Environmental impact records |
| `/api/ai-chat` | POST | Agentic Claude AI chat (+ rate limiting) |
| `/api` | GET | API health check |

---

## 6. Database Models (Prisma Schema)

### Core Models
| Model | Key Fields | Purpose |
|-------|-----------|---------|
| `User` | id, email, password (bcrypt), name, role, company, image | Platform users |
| `Account` | provider, providerAccountId | OAuth accounts (NextAuth) |
| `Session` | sessionToken, userId, expires | DB sessions (NextAuth) |
| `VerificationToken` | identifier, token, expires | Email verification |
| `Blueprint` | name, category, material, oem, certification, status, printCount, fileUrl | CAD file registry |
| `BlueprintVersion` | blueprintId, version, changes, fileUrl | Blueprint version history |
| `PrintCenter` | name, location, certification, capacity, totalPrinters, status | AM facility registry |
| `Order` | orderId, partName, status, priority, quantity, requesterId, blueprintId, centerId, oemApproved, certApproved, tokenIssued | Order lifecycle |
| `AuditLog` | action, orderId, userId, details, hash, previousHash | Cryptographic audit trail |
| `Shipment` | trackingId, orderId, status, origin, destination, carrier, progress, eta | Delivery tracking |
| `Partner` | name, type, email, phone, status, blueprints, totalPrints, royalties | OEM partner registry |
| `Material` | name, category, stockLevel, minLevel, reorderPoint, status, unitCost, leadTime | Raw material inventory |
| `MaterialStock` | materialId, centerId, stockLevel | Per-centre stock levels |
| `Certification` | name, type, issuer, holder, standard, status, expiryDate, documentUrl | Cert tracking |
| `DashboardStats` | totalOrders, deliveredParts, avgLeadTime, costSavings, activeOrders | Cached KPI snapshot |
| `CertificationAuthority` | name, acronym, type, contact, website, specializations, status | Authority registry |
| `CertificationRequest` | blueprintId, authorityId, requesterId, status, notes | Cert approval queue |
| `CustomerEngagement` | customerId, companyName, engagementType, status, value | Customer tracking |
| `TrainingSession` | engagementId, personnelName, qualificationLevel, modulesCompleted, status | Personnel training |
| `ComparativeMetrics` | customerId, traditionalLeadTime, almatechLeadTime, leadTimeReduction, warehouseSavings | ROI data |
| `EnvironmentalImpact` | orderId, co2SavedKg, milesAvoided, wasteReduced | Environmental data |
| `CustomizationRequest` | blueprintId, requesterId, description, justification, status | Custom design requests |

---

## 7. AI Assistant

### Overview
Floating chat widget (purple sparkle button, bottom-right corner of every page). Powered by **Claude 3.5 Haiku** via OpenRouter API.

### Capabilities — Agentic Tool Calling
The AI is not just a Q&A bot — it executes real actions via a tool-calling loop (up to 4 rounds):

| Tool | What it does |
|------|-------------|
| `navigate_to_page(page)` | Instantly switches to any of the 19 dashboard pages |
| `get_dashboard_stats()` | Fetches live KPIs from `/api/stats` |
| `list_orders(status?, limit?)` | Fetches real order data from DB |
| `list_blueprints(status?, limit?)` | Fetches blueprints from vault |
| `create_order(partName, priority, qty, notes)` | Creates a real order via POST `/api/orders` |
| `list_materials(status?)` | Fetches material inventory levels |
| `list_certifications(status?)` | Fetches certifications with expiry status |

### Example Interactions
- "Take me to the audit logs" → navigates instantly, teal pill confirms action
- "How many pending orders do I have?" → fetches live data, reports real count
- "Create an urgent order for a Pump Impeller, qty 2" → creates the order, returns order ID
- "Which materials are critical?" → queries DB, lists critical materials

### Rate Limiting
20 requests per minute per IP (in-memory Map, resets on serverless cold starts).

### Role Context
The system prompt is enriched with the current user's role context (6 personas), so answers are scoped to what that role can see and do.

---

## 8. Security Measures

### Authentication
- NextAuth v4, JWT strategy, 30-day session
- CredentialsProvider with bcrypt password hashing
- `requireAuth()` helper at `src/lib/require-auth.ts` — wraps `getServerSession(authOptions)`
- Login page at `/login` with branded dark theme + collapsible demo account panel

### API Protection
- 42 handler functions across 21 route files all call `requireAuth()` as first step
- Returns `{ error: "Unauthorized" }` with HTTP 401 if no valid session
- Only `/api/auth/**` and `/api/contact` are public

### Middleware
- Currently a pass-through (`NextResponse.next()`) — auth wall temporarily disabled due to bcrypt/seed issue
- `withAuth()` implementation is ready in `src/lib/auth.ts` to re-enable

### Security Headers (applied to all routes via `next.config.ts`)
```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'; frame-ancestors 'none'; ...
```

### Other
- `productionBrowserSourceMaps: false` — minified JS not reverse-engineerable
- Rate limiting on AI endpoint
- Vercel deployment with encrypted env vars

---

## 9. Key Workflows

### DRM Approval Pipeline (most complex workflow)
```
1. Customer creates order (selects blueprint + print centre)
2. Order enters DRM queue with status "pending"
3. OEM Partner reviews → grants IP licence (oemApproved = true)
4. Cert Authority reviews → verifies facility cert matches blueprint cert (certApproved = true)
5. Once both approved → Admin/Print Centre can issue Secure Print Token
6. Token delivered to print centre → printing begins
7. Print Centre logs completion → QC check
8. Shipment created → tracked to delivery
9. Every step creates an immutable audit log entry with SHA-256 hash chain
```

### Blueprint Lifecycle
```
Upload (STL/STEP/3MF) → Pending Review → OEM approval →
Certification Authority approval → Active → Available for orders
```

### Onboarding Tutorial
- First-time users see a full-screen `OnboardingTutorial` overlay
- Completed status stored in localStorage
- Can be restarted from Settings → Help & Support
- Per-section tutorial tooltips via `SectionTutorial` component (triggered by "?" button in Header)

---

## 10. Known Gaps & Current Limitations

| Area | Issue | Severity |
|------|-------|----------|
| Auth middleware | `withAuth()` disabled — dashboard accessible without login | High |
| Login passwords | bcrypt seed may not have propagated to all production users | High |
| Rate limiting | In-memory Map resets on Vercel cold starts — not persistent across instances | Medium |
| CSP | `unsafe-inline` and `unsafe-eval` required by Next.js — weakens CSP | Medium |
| Role enforcement | Sidebar role permissions are frontend-only — no server-side row-level filtering | Medium |
| Real-time updates | No WebSocket/SSE — SWR polls every 30s by default | Low |
| Demo personas | Role switching (sidebar) is UI-only — session still uses the logged-in user's real role | Low |
| Analytics data | Comparative & environmental charts only render if DB has seeded records | Low |
| Source maps | Disabled in prod, but dev builds still expose full source | Low |
| Peer Printers | Page exists in sidebar but content is minimal/placeholder | Low |
| Mobile | Responsive layout exists but not fully optimised for small screens | Low |
| No search global | No platform-wide search across all pages | Low |
| No notifications | Notification toggles exist in Settings but no actual notification delivery system | Low |
| No email | No transactional emails (order updates, cert expiry alerts, etc.) | Low |
| No payment | Royalty tracking exists but no payment gateway integration | Low |

---

## 11. File Structure

```
Website/AddManuChain Dashboard/
├── src/
│   ├── app/
│   │   ├── page.tsx                    # Main dashboard shell (state, routing, layout)
│   │   ├── layout.tsx                  # Root layout with Providers wrapper
│   │   ├── globals.css
│   │   ├── login/
│   │   │   └── page.tsx               # Branded login page
│   │   └── api/
│   │       ├── ai-chat/route.ts        # Agentic Claude API (tool-calling loop)
│   │       ├── auth/[...nextauth]/     # NextAuth handler
│   │       ├── orders/route.ts         # + [id]/route.ts
│   │       ├── blueprints/route.ts     # + [id]/route.ts
│   │       ├── centers/route.ts        # + [id]/route.ts
│   │       ├── partners/route.ts       # + [id]/route.ts
│   │       └── [16 more routes]
│   ├── components/
│   │   ├── dashboard/
│   │   │   ├── AIAssistant.tsx         # Floating chat widget
│   │   │   ├── Sidebar.tsx             # Navigation + role switcher
│   │   │   ├── Header.tsx              # Top bar + tutorial button
│   │   │   ├── OverviewPage.tsx
│   │   │   ├── OrdersPage.tsx
│   │   │   ├── PrintApprovalPage.tsx   # DRM queue
│   │   │   ├── IPLibraryPage.tsx
│   │   │   ├── BlueprintsPage.tsx
│   │   │   ├── PartnersPage.tsx
│   │   │   ├── DigitalInventoryPage.tsx
│   │   │   ├── PhysicalInventoryPage.tsx
│   │   │   ├── CentersPage.tsx
│   │   │   ├── PeerPrintersPage.tsx
│   │   │   ├── ShipmentsPage.tsx
│   │   │   ├── MaterialsPage.tsx
│   │   │   ├── CertificationsPage.tsx
│   │   │   ├── AuthoritiesPage.tsx
│   │   │   ├── AuditLogPage.tsx
│   │   │   ├── LabPage.tsx
│   │   │   ├── AnalyticsPage.tsx
│   │   │   ├── CustomerSuccessPage.tsx
│   │   │   ├── SettingsPage.tsx
│   │   │   ├── RoleDashboard.tsx       # Role-specific overview wrapper
│   │   │   ├── OnboardingTutorial.tsx  # First-time user walkthrough
│   │   │   └── SectionTutorial.tsx     # Per-page tooltip tutorials
│   │   ├── ui/                         # shadcn/ui components (40+ components)
│   │   └── Providers.tsx               # SessionProvider wrapper
│   ├── hooks/
│   │   └── use-dashboard.ts            # SWR data hooks for all entities
│   ├── lib/
│   │   ├── auth.ts                     # NextAuth config (authOptions)
│   │   ├── db.ts                       # Prisma client singleton
│   │   └── require-auth.ts             # Auth guard helper
│   ├── middleware.ts                   # Route protection (currently pass-through)
│   └── types/
│       └── next-auth.d.ts              # Session type augmentation (id, role, company)
├── prisma/
│   ├── schema.prisma                   # 22 models
│   └── seed.ts                         # Demo data seeder
├── public/
│   ├── robots.txt                      # Allow: /
│   ├── manifest.json
│   └── sw.js
├── next.config.ts                      # Security headers, no source maps
├── tailwind.config.ts
└── package.json
```

---

## 12. Deployment & Environment

### Vercel Project
- **Project:** `mtk1793s-projects/addmanuchain-dashboard`
- **Production URL:** https://addmanuchain-dashboard.vercel.app
- **Node version:** 24.x
- **Output:** `standalone`

### Required Environment Variables
```bash
DATABASE_URL=           # Neon PostgreSQL pooled connection string
DATABASE_URL_UNPOOLED=  # Neon PostgreSQL direct connection (for migrations)
NEXTAUTH_SECRET=        # Random base64 string (openssl rand -base64 32)
NEXTAUTH_URL=           # https://addmanuchain-dashboard.vercel.app
OPENROUTER_API_KEY=     # sk-or-v1-... (for Claude AI assistant)
NEON_PROJECT_ID=        # Neon project ID
POSTGRES_*=             # Neon connection parts (host, user, password, db)
```

### Deploy Commands
```bash
# Deploy to production
cd "Website/AddManuChain Dashboard"
vercel --prod

# Re-seed production database
DATABASE_URL="postgresql://..." npx tsx prisma/seed.ts

# Pull production env vars locally
vercel env pull .env.production.local --environment=production
```

### GitHub → Vercel
Currently using **manual CLI deploys** (`vercel --prod`). GitHub Actions auto-deploy is not configured — each deploy is triggered manually from the local machine.
