# AddManuChain Dashboard — Complete User Tutorial

> **Live URL:** https://addmanuchain-dashboard.vercel.app  
> **Stack:** Next.js · TypeScript · Tailwind CSS · shadcn/ui · Framer Motion  
> **Last Updated:** February 28, 2026

---

## Table of Contents

1. [What is AddManuChain?](#1-what-is-addmanuchain)
2. [Getting Started — Navigation & Layout](#2-getting-started--navigation--layout)
3. [Onboarding Tutorial & Help System](#3-onboarding-tutorial--help-system)
4. [AI Assistant](#4-ai-assistant)
5. [Page-by-Page Guide](#5-page-by-page-guide)
   - [5.01 Overview (Dashboard Home)](#501-overview-dashboard-home)
   - [5.02 Orders](#502-orders)
   - [5.03 Print Queue (DRM Approval Pipeline)](#503-print-queue-drm-approval-pipeline)
   - [5.04 IP Library](#504-ip-library)
   - [5.05 Blueprint Library](#505-blueprint-library)
   - [5.06 OEM Partners](#506-oem-partners)
   - [5.07 Digital Inventory](#507-digital-inventory)
   - [5.08 Physical Inventory](#508-physical-inventory)
   - [5.09 Print Centers](#509-print-centers)
   - [5.10 Peer Printers](#510-peer-printers)
   - [5.11 Shipments](#511-shipments)
   - [5.12 Materials](#512-materials)
   - [5.13 Certifications](#513-certifications)
   - [5.14 Authorities](#514-authorities)
   - [5.15 Audit Logs](#515-audit-logs)
   - [5.16 Analytics](#516-analytics)
   - [5.17 Lab Portal](#517-lab-portal)
   - [5.18 Customer Success](#518-customer-success)
     - [Trained Personnel Registry](#trained-personnel-registry)
   - [5.19 Settings](#519-settings)
6. [Core Workflow — End-to-End Print Order](#6-core-workflow--end-to-end-print-order)
7. [DRM (Digital Rights Management) Explained](#7-drm-digital-rights-management-explained)
8. [User Roles & Permissions](#8-user-roles--permissions)
9. [Status Reference Tables](#9-status-reference-tables)
10. [Keyboard Shortcuts & Tips](#10-keyboard-shortcuts--tips)
11. [FAQ](#11-faq)

---

## 1. What is AddManuChain?

AddManuChain is a **blockchain-secured additive manufacturing (AM) supply chain platform** that connects:

| Actor | Role |
|---|---|
| **OEMs** (Original Equipment Manufacturers) | Own the IP (CAD blueprints), license them securely |
| **Certification Authorities** | Audit and certify print centers to industry standards |
| **Print Centers** | Certified facilities that execute 3D printing jobs |
| **Peer Printers** | Airbnb-style peer-to-peer 3D printer network |
| **Operators / Buyers** | Request parts, track orders, manage inventory |

**Core value proposition:** Eliminate the need to hold physical spare parts inventory by printing certified parts on-demand, anywhere in the world — with full IP protection, traceability, and regulatory compliance.

**Key concepts you will encounter throughout the dashboard:**

- **DRM Token** — A one-time cryptographic key that unlocks a blueprint for exactly one print job. Without it, the printer cannot access the CAD file.
- **Blueprint** — An encrypted CAD file stored in the IP Library, accessed only through the DRM pipeline.
- **Print Queue** — The approval pipeline where OEM and Certification Authority must both sign off before a DRM token is issued.
- **AI Risk Score** — An automated score (0–100) that evaluates each order's risk based on material criticality, print center compliance history, and certification status.

---

## 2. Getting Started — Navigation & Layout

### Sidebar (Left Panel)

The sidebar is the primary navigation. It is organized into **5 sections**:

| Section | Pages |
|---|---|
| **Core Operations** | Overview, Orders, Print Queue |
| **IP & Blueprints** | IP Library, Blueprint Library, OEM Partners |
| **Operations** | Digital Inventory, Physical Inventory, Print Centers, Peer Printers, Shipments, Materials |
| **Compliance** | Certifications, Authorities, Audit Logs |
| **Intelligence & Support** | Analytics, Lab Portal, Customer Success, Settings |

**Collapse the sidebar** by clicking the arrow button (`◀`) at the bottom of the sidebar. When collapsed, icons remain visible for quick navigation. Re-expand by clicking the same button.

**On mobile**, use the hamburger menu (≡) in the top-left of the header to open the sidebar drawer. It closes automatically when you tap any navigation item.

**Notification badges** on sidebar items (e.g., `Orders: 3`, `Print Queue: 5`) indicate items requiring attention.

### Header (Top Bar)

The header shows the **current page title and subtitle**. It also contains:

- **Search icon** — global search across orders, blueprints, contacts
- **Notifications bell** — system alerts and approval requests
- **? (Help) button** — triggers the interactive step-by-step tutorial for the current section
- **User avatar / profile** — quick access to profile and settings

---

## 3. Onboarding Tutorial & Help System

### First-Time Welcome Tour

When you first visit the dashboard, an **Onboarding Tutorial** modal automatically appears. It walks you through 5 core sections:

1. Welcome to AddManuChain
2. Navigation overview
3. Creating your first order
4. Understanding the DRM pipeline
5. Analytics and insights

Click **Next** to advance or the **×** to skip. Progress is saved in your browser (`localStorage`) so the tour only appears once per device.

### Per-Section Tutorials

Every section has its own **interactive tutorial** (4–5 steps) that explains that specific page in detail.

- **Auto-shows** the first time you visit a section
- **Re-trigger** anytime by clicking the **`?` button** in the top-right of the header
- Tutorials include **Tip cards** (amber) with power-user hints
- Navigate between steps with the **dot indicators** at the bottom of the card

### Restarting All Tutorials

Go to **Settings → Tutorial & Help → Restart Tutorial**. This resets both the onboarding tour and all 19 per-section tutorials. The next page you navigate to will show its tutorial fresh.

---

## 4. AI Assistant

A **floating AI chat widget** lives in the bottom-right corner of every page — look for the violet ✦ (Sparkles) button.

### How to use it

1. Click the violet **Sparkles (✦)** button to open the chat panel
2. Type your question or click one of the **suggestion chips** to get started instantly
3. Press **Enter** to send (or **Shift + Enter** for a new line)
4. The AI responds using full context of all 19 dashboard sections
5. Hover over any AI response to reveal a **Copy** button
6. Click the **trash icon** in the panel header to clear the conversation

### What the AI knows

The AI assistant is trained on the full AddManuChain context including:
- All 19 dashboard sections and their workflows
- DRM token pipeline and approval stages
- Blueprint and IP management procedures
- Certification standards (AS9100, ISO 9001, DNV, NADCAP, etc.)
- User roles and permissions
- Common troubleshooting scenarios

### Tips

- The assistant maintains the **last 10 messages** as context within a session
- Ask follow-up questions — it remembers earlier turns
- Use it for **troubleshooting** (e.g., "Why is my blueprint showing Pending Review?") or **how-to guidance** (e.g., "How do I issue a DRM token?")

---

## 5. Page-by-Page Guide

---

### 5.01 Overview (Dashboard Home)

**Sidebar label:** Overview  
**Purpose:** High-level health snapshot of the entire platform.

#### KPI Cards (top row)

| Metric | What it measures |
|---|---|
| **Active Orders** | Orders currently in progress (ring = % of total orders) |
| **Parts Delivered** | Certified completed deliveries YTD |
| **Avg Lead Time** | Average days from order to delivery vs. traditional supply chain |
| **Cost Savings** | Year-to-date cost savings vs. traditional sourcing |

Each KPI card shows a **sparkline** (mini trend chart) of the last 7 data points, and a **ring chart** showing completion percentage.

#### Panel Grid (main body)

| Panel | Contents |
|---|---|
| **Recent Orders** | Last 5 orders with status badges and quick-link |
| **DRM Pipeline** | Live count of orders at each DRM stage |
| **Print Center Status** | Online/offline/maintenance breakdown with status bars |
| **Blueprint Utilization** | Most-used blueprints with usage sparklines |
| **Materials Alert** | Inventory items below reorder threshold |
| **Certification Expiry** | Upcoming cert renewals within 60 days |

**No actions can be taken directly from Overview** — it is read-only. Click any panel's items to navigate to the relevant section.

---

### 5.02 Orders

**Sidebar label:** Orders (badge shows pending count)  
**Purpose:** Create and manage all part print orders.

#### Filters & Search

- **Search bar** — filters by Order ID, part name, customer, or print center
- **Status filter** — All / Pending / Printing / Quality Check / Shipped / Delivered
- **Priority filter** — All / Critical / High / Medium / Low

#### Status Flow

Orders always move in one direction through this pipeline:

```
Pending → Printing → Quality Check → Shipped → Delivered
```

You can manually **advance the status** of an order by opening its detail panel and clicking the advance button (visible only when the order is ready for the next stage).

#### Creating a New Order

1. Click **+ New Order** (top-right)
2. Fill in the form:
   - **Part Name** — descriptive name for the part
   - **Blueprint** — select from approved blueprints in the IP Library
   - **Print Center** — select a certified, online print center
   - **Quantity** — number of units
   - **Priority** — Critical / High / Medium / Low
   - **Due Date** — target delivery date
   - **Notes** — any special instructions
3. Click **Submit Order**

The order is created with status `Pending` and automatically enters the DRM approval pipeline (Print Queue).

#### Order Detail Panel

Click any order row to expand its detail panel:
- Full order metadata (ID, timestamps, assigned center)
- **Approval Stepper** showing current DRM pipeline stage
- **AI Risk Score** (0–100) — higher = more risk
- OEM and Cert approval status with timestamps
- Print Auth Token (shown only after token is issued)
- Action buttons: Advance Status, Cancel Order

#### Table Columns

`Order ID` · `Part Name` · `Blueprint` · `Print Center` · `Qty` · `Status` · `Priority` · `Due Date` · `Risk Score` · `Actions`

---

### 5.03 Print Queue (DRM Approval Pipeline)

**Sidebar label:** Print Queue (badge shows awaiting approval count)  
**Purpose:** Manage the DRM approval workflow before any print job can execute.

#### The 4-Step DRM Pipeline

Every order must pass through all 4 stages before printing:

```
[1] OEM Approved   →   [2] Cert Verified   →   [3] Print Token Issued   →   [4] Printing
```

| Stage | Who acts | What happens |
|---|---|---|
| **OEM Approved** | OEM partner | Grants IP license for this specific print job |
| **Cert Verified** | Certification Authority | Confirms the assigned print center meets the standard for this part |
| **Print Token Issued** | System (auto) | A one-time cryptographic decryption key is generated once both approvals are in |
| **Printing** | Print Center | The printer receives the token, decrypts the blueprint, and executes the job |

#### Approving an Order (OEM or Cert Authority role)

1. Find the order in the Print Queue table (filter by "Awaiting Approval")
2. Click the **Approve** button next to your role (OEM or Cert)
3. Optionally add an approval note
4. Confirm — your approval timestamp is permanently recorded

#### Rejecting an Order

Click **Reject** and enter a rejection reason. The order status reverts to `Pending` and the requester is notified. The reason is stored in the Audit Log.

#### Issuing a Print Token Manually

If both approvals are in but the token has not been auto-issued (edge case):
1. Open the order detail
2. Click **Issue Token**
3. The system generates a `TOKEN-XXXXXX` string
4. The print center is notified automatically

#### Queue Filters

- **Stage filter** — show only orders at a specific pipeline step
- **Priority filter** — surface Critical orders first
- **Search** — by Order ID or part name

---

### 5.04 IP Library

**Sidebar label:** IP Library  
**Purpose:** Central repository for all OEM intellectual property assets — the source of truth for which blueprints exist, who owns them, and how they are licensed.

#### IP Asset Record

Each IP asset contains:

| Field | Description |
|---|---|
| **Asset ID** | Unique identifier (e.g., `ip-001`) |
| **Part Name** | Human-readable name |
| **OEM Owner** | Which OEM holds the IP (e.g., Wärtsilä, GE, Siemens) |
| **License Type** | `restricted` · `open` · `pay_per_print` · `consortium` |
| **Royalty Rate** | Percentage of job cost paid to OEM per print |
| **Royalty Flat** | Fixed fee (CAD) per print job |
| **Total Royalties** | Cumulative royalties earned on this asset |
| **Print Count** | Number of times this blueprint has been printed |
| **Description** | Technical notes and part specifications |

#### License Types Explained

| Type | Meaning |
|---|---|
| `restricted` | Only pre-approved partners can request this blueprint |
| `open` | Any certified print center can use this blueprint |
| `pay_per_print` | Usage allowed but each print triggers a royalty payment to the OEM |
| `consortium` | Available only to members of a specific industry consortium |

#### License Request Workflow

1. Find the IP asset you need
2. Click **Request License**
3. Select your print center and intended print quantity
4. Submit — the request goes to the OEM for approval
5. OEM approves or rejects (visible in the Requests panel)
6. Once approved, the blueprint becomes available for order creation

#### Royalty Tracking

The IP Library tracks all royalty payments automatically. The OEM dashboard view shows:
- Per-asset royalty earnings
- Total platform royalty revenue
- Print history per asset

---

### 5.05 Blueprint Library

**Sidebar label:** Blueprint Library  
**Purpose:** Manage the encrypted CAD blueprint files that power the print jobs.

#### Grid vs. List View

Toggle between **grid view** (visual blueprint cards with CAD preview drawings) and **list view** (table format) using the icons in the top-right of the section header.

#### Blueprint Card (Grid View)

Each card shows:
- **Auto-generated CAD preview** — a technical drawing rendered from the blueprint metadata
- **Blueprint ID** (monospace, e.g., `BP-2024-001`)
- **Status badge**
- **Part name and OEM owner**
- **View** (👁) and **Delete** (🗑) action buttons

#### Blueprint Statuses

| Status | Meaning |
|---|---|
| `active` | Cleared for use in orders |
| `pending_review` | Awaiting OEM or Cert Authority review |
| `certified` | Passed all certification checks |
| `deprecated` | No longer in active use, retained for audit purposes |
| `revoked` | IP license revoked by OEM, cannot be used |

#### Uploading a New Blueprint

1. Click **+ Add Blueprint**
2. Fill in the metadata form:
   - Part Name, Blueprint ID, OEM owner, Certification standard
   - Material type, Description
3. **Drag and drop a CAD file** (or click to browse) into the upload zone — accepts `.stl`, `.step`, `.obj`, `.gltf`
4. Click **Upload Blueprint**

The blueprint enters `pending_review` status and awaits approval before it can be used in orders.

#### Viewing Blueprint Details

Click the **eye (👁) icon** on any blueprint card or row to open the detail sheet with full metadata, certification info, usage history, and the CAD preview drawing.

#### Filtering Blueprints

- Search by name, ID, OEM, or material
- Filter by status badge
- Filter by certification standard

---

### 5.06 OEM Partners

**Sidebar label:** OEM Partners  
**Purpose:** Manage relationships, contracts, and communication with OEM partners.

#### Partner Record

Each OEM partner record includes:
- Company name, primary contact, country
- Active contract count and royalty revenue
- Certification standards supported
- Integration status (API-connected or manual)
- Relationship health score

#### Actions

- **View Partner** — detailed profile with contract history, IP assets, and royalty ledger
- **Add Contact** — add a new point of contact at the OEM
- **Create Partner** — onboard a new OEM organization

#### Partner Filters

- Search by name or country
- Filter by integration type (API / manual)
- Filter by certification standard

---

### 5.07 Digital Inventory

**Sidebar label:** Digital Inventory  
**Purpose:** AI-driven forecasting and management of the digital parts portfolio — which blueprints are "on-shelf" digitally.

#### What is Digital Inventory?

Instead of physically warehousing spare parts, AddManuChain maintains a **digital inventory** of certified blueprints that can be printed on-demand. The Digital Inventory page tracks:

- Which blueprints are available for immediate printing
- Forecasted demand per part (AI-powered)
- Readiness score per part (blueprint certified + print center available + materials in stock)
- Parts that need blueprint certification or material stock replenishment

#### AI Demand Forecast

The AI engine analyzes historical order data, seasonal patterns, and equipment maintenance schedules to generate a **30/60/90-day demand forecast** for each part. This helps operators plan material procurement and print center capacity ahead of need.

#### Readiness Score

Each digital part gets a **Readiness Score (0–100)**:
- 100 = Blueprint certified + materials stocked + print center available = can print immediately
- Below 70 = At least one blocker exists (shown as a warning flag)

#### Actions

- **Request Print** — shortcut to create an order directly from a digital inventory item
- **Update Forecast** — manually adjust demand estimates
- **View Blueprint** — jump to the blueprint in the Blueprint Library

---

### 5.08 Physical Inventory

**Sidebar label:** Physical Inventory  
**Purpose:** Manage physical spare parts that are stocked at various sites (for parts not yet fully digitized).

#### Inventory Table

Columns: `Part Name` · `Part Number` · `Site / Location` · `Qty on Hand` · `Min Stock` · `Unit Cost` · `Total Value` · `Status`

#### Stock Statuses

| Status | Meaning |
|---|---|
| `In Stock` | Above minimum threshold |
| `Low Stock` | Below minimum — reorder recommended |
| `Critical` | Either at zero or below safety stock |
| `On Order` | Replenishment order already placed |

#### Actions

- **Add Stock Entry** — record new physical inventory at a site
- **Edit Quantity** — adjust current stock count after physical audit
- **Set Reorder Point** — configure minimum stock threshold per item
- **Transfer** — move stock between sites

#### Integration with Digital Inventory

When physical stock falls to zero for a part that has a certified digital blueprint, the system suggests **switching to on-demand AM** with a one-click **Request Print** action.

---

### 5.09 Print Centers

**Sidebar label:** Print Centers  
**Purpose:** Monitor, manage, and certify the network of AM facilities that execute print jobs.

#### Center Status

| Status | Meaning |
|---|---|
| `online` | Operational and accepting jobs |
| `offline` | Not accepting jobs (maintenance, shutdown) |
| `maintenance` | Temporary downtime, returning soon |
| `suspended` | Certification suspended — cannot accept jobs |

#### Center Profile

Each center record contains:
- Location (city, country)
- Certifications held (AS9100, DNV, ISO 9001, etc.)
- Printer types (FDM, SLS, DMLS, EBM, etc.)
- Current job capacity and queue depth
- Compliance score and audit history (tabs)
- Contact information

#### Tabs inside Center Profile

| Tab | Content |
|---|---|
| **Overview** | Key metrics, recent jobs, capacity gauge |
| **Certifications** | List of held certifications with expiry dates |
| **Audit History** | Inspection results and compliance events timeline |
| **Equipment** | Printer inventory with model, capabilities, maintenance status |

#### Adding a New Print Center

1. Click **+ Add Center**
2. Fill in: Name, Address, Country, Contact, Printer types, Initial certifications
3. Submit — the center enters `pending` status until a Certification Authority approves it

#### Filtering

- Search by name, city, or country
- Filter by status
- Filter by certification standard

---

### 5.10 Peer Printers

**Sidebar label:** Peer Printers  
**Purpose:** Manage the Airbnb-style peer-to-peer 3D printer sharing network — individual or small-shop printers that can accept certified jobs.

#### How Peer Printers Work

Peer printers are **individually owned printers** registered on the platform. They can:
- List their machine (type, build volume, materials supported)
- Set their availability schedule and pricing
- Accept certified print jobs routed through the platform
- Earn revenue per completed job

#### Peer Printer Record

| Field | Description |
|---|---|
| **Printer ID** | Unique identifier |
| **Owner Name** | Registered printer owner |
| **Machine Type** | FDM / SLS / Resin / etc. |
| **Location** | City and country |
| **Availability** | Calendar-based availability |
| **Certification Level** | Basic / Advanced / Certified (determines job types eligible for) |
| **Jobs Completed** | Historical job count and rating |
| **Hourly Rate / Job Rate** | Pricing configured by owner |

#### Routing Jobs to Peer Printers

From the Orders page, when creating an order, set **Print Center Type = Peer Printer** and the platform matches available, certified peer printers near the delivery address.

#### Becoming a Peer Printer

Owners self-register via a separate onboarding flow (not in this dashboard). Admins can manage registrations and certification upgrades from this page.

---

### 5.11 Shipments

**Sidebar label:** Shipments  
**Purpose:** Track delivery logistics for completed print jobs.

#### Shipment Table

Columns: `Shipment ID` · `Order ID` · `Part Name` · `Origin (Print Center)` · `Destination` · `Carrier` · `Tracking #` · `Status` · `ETA`

#### Shipment Statuses

| Status | Meaning |
|---|---|
| `Preparing` | Part printed, packaging in progress |
| `Picked Up` | Carrier has collected the package |
| `In Transit` | On the way to destination |
| `Out for Delivery` | Last-mile delivery active |
| `Delivered` | Confirmed received |
| `Exception` | Delay or issue with carrier — requires attention |

#### Actions

- **View Tracking** — opens the carrier tracking page
- **Update Status** — manually advance shipment status
- **Report Exception** — flag a delivery issue for follow-up

#### Filtering

- Search by Shipment ID, Order ID, or tracking number
- Filter by status
- Filter by carrier
- Date range filter for ETA

---

### 5.12 Materials

**Sidebar label:** Materials  
**Purpose:** Manage raw material inventory (powders, filaments, resins) across print centers.

#### Material Record

| Field | Description |
|---|---|
| **Material ID** | Unique identifier |
| **Name** | Material name (e.g., Ti-6Al-4V, PA12, Inconel 718) |
| **Type** | Metal powder / Polymer filament / Resin / Composite |
| **Supplier** | Approved supplier name |
| **Batch Number** | For traceability (required for certified parts) |
| **Qty on Hand** | Current stock in kg or units |
| **Min Threshold** | Reorder point |
| **Location** | Which print center holds this stock |
| **Certification** | Material certification document reference |
| **Expiry Date** | Material shelf-life expiry |

#### Material Statuses

- `In Stock` · `Low Stock` · `Critical` · `Expired` · `Quarantined`

#### Ordering Materials

1. Click **+ Order Material**
2. Select material, supplier, quantity
3. Choose destination print center
4. The purchase order is generated and tracked here

#### Traceability

Each material batch used in a print job is recorded against that job's order ID, providing full **material traceability chain** from supplier → material batch → print job → delivered part.

---

### 5.13 Certifications

**Sidebar label:** Certifications  
**Purpose:** Track compliance certifications for print centers, materials, and processes.

#### Certification KPI Cards

At the top of the page:
- **Total Certifications** held across the network
- **Active** — currently valid
- **Pending** — under review or renewal
- **Expiring Soon** — renewing within 60 days (highlighted in amber)
- **Expired** — require immediate action (highlighted in red)

#### Certification Table

Columns: `Cert ID` · `Standard` · `Holder` (center or partner) · `Issued By` · `Issue Date` · `Expiry Date` · `Status` · `Actions`

#### Certification Standards

Common standards tracked in the platform:

| Standard | Scope |
|---|---|
| **AS9100** | Aerospace quality management |
| **ISO 9001** | General quality management |
| **NADCAP** | Aerospace special processes |
| **DNV GL** | Marine and offshore |
| **ISO/ASTM 52900** | AM process standards |
| **NAS9300** | Aerospace AM qualification |

#### Actions

- **View Certificate** — open the certificate document
- **Request Renewal** — initiate renewal with the issuing authority
- **Upload New Cert** — upload a newly received certificate document

#### Cert Filtering

- Filter by standard type
- Filter by status
- Filter by holder (print center or partner)
- Filter by expiry date range

---

### 5.14 Authorities

**Sidebar label:** Authorities  
**Purpose:** Manage relationships with certification bodies that approve and audit print centers.

#### Authority Record

| Field | Description |
|---|---|
| **Authority ID** | Unique identifier |
| **Name** | Certifying body name (e.g., DNV, Lloyd's Register, Bureau Veritas) |
| **Type** | Industry body / Government agency / Standards body |
| **Country** | Jurisdiction |
| **Standards Issued** | Which certification standards this body issues |
| **Active Certifications** | Count of currently valid certs issued by this authority |
| **Pending Requests** | Certification requests awaiting this authority's review |
| **Status** | Active / Suspended / Under Review |

#### Request Management

Each authority has an embedded **Requests panel** showing all open certification requests submitted to that body. Action options: View Request · Follow Up · Mark Resolved.

#### Adding a Certification Authority

1. Click **+ Add Authority**
2. Fill in organization details, contact person, standards they issue
3. Submit for admin approval

#### Filtering

- Filter by type (industry / government / standards body)
- Filter by status
- Search by name or country

---

### 5.15 Audit Logs

**Sidebar label:** Audit Logs  
**Purpose:** Immutable record of all system actions for compliance, traceability, and security investigation.

#### What is Logged

Every significant action in the platform generates an audit event:

| Category | Examples |
|---|---|
| **Order** | Created, status changed, cancelled |
| **DRM** | OEM approval, Cert approval, token issued, token used |
| **Blueprint** | Uploaded, approved, deprecated, revoked |
| **Certification** | Issued, renewed, expired, suspended |
| **User** | Login, role change, settings updated |
| **System** | API calls, integration events, errors |

#### Audit Log Table

Columns: `Event ID` · `Timestamp` · `Category` · `Action` · `Actor` (user or system) · `Target` (order/blueprint/cert ID) · `IP Address` · `Details`

#### Non-Repudiable Records

Audit logs **cannot be edited or deleted** — not even by admins. They are append-only and cryptographically chained (each record includes a hash of the previous entry) to detect tampering.

#### Filtering & Export

- **Date range** picker
- **Category** filter (Order / DRM / Blueprint / Cert / User / System)
- **Actor** filter (search by user or system)
- **Keyword** search in the Details field
- **Export CSV** button (top-right) — exports the filtered view

---

### 5.16 Analytics

**Sidebar label:** Analytics  
**Purpose:** Performance intelligence, comparative metrics, and environmental impact reporting.

#### KPI Summary (top)

The same 4 core KPIs from Overview, but with trend context:
- Active Orders · Parts Delivered · Avg Lead Time · Cost Savings

#### Sections

| Section | Description |
|---|---|
| **Order Performance** | Volume over time, status breakdown donut chart, on-time delivery rate |
| **Lead Time Analysis** | AddManuChain lead time vs. traditional supply chain (bar comparison) |
| **Cost Savings** | Cost avoidance breakdown: inventory, logistics, obsolescence |
| **Comparative Metrics** | Customer-specific comparison — select a customer to see their AM vs. traditional metrics |
| **Print Center Utilization** | Capacity utilization per center, queue depth trends |
| **Blueprint Usage** | Top blueprints by print volume, royalty revenue generated |
| **Environmental Impact** | CO₂ savings, waste reduction, logistics optimization vs. traditional supply chain |

#### Comparative Metrics (Customer-Level)

Select a customer from the dropdown to load their specific metrics:
- Lead time reduction (%)
- Warehouse cost savings (CAD)
- Logistics cost savings (CAD)
- Obsolescence cost avoidance (CAD)
- Total ROI (%)

This section is useful for **account reviews and renewal conversations**.

#### Environmental Impact Panel

Shows the sustainability benefit of AM vs. traditional spare parts:
- CO₂ reduction (tonnes)
- Material waste reduction (kg, from near-net-shape AM vs. subtractive machining)
- Shipping distance eliminated (km, by printing locally)

---

### 5.17 Lab Portal

**Sidebar label:** Lab Portal  
**Purpose:** Submit and track AM testing requests, schedule equipment, and manage certification test reports.

#### Test Request Workflow

1. **Submit** a new test request (button: `+ New Test Request`)
2. Select the part / material / blueprint to test
3. Choose **test types** (multi-select):
   - `Mechanical` — tensile, compression, hardness
   - `Chemical` — material composition verification
   - `Thermal` — heat resistance, thermal cycling
   - `Dimensional` — geometric accuracy vs. CAD tolerance
   - `NDT` — non-destructive testing (X-ray, CT-scan, ultrasound)
   - `Fatigue` — cyclic loading life testing
4. Select the **required certification standard** the results must support
5. Assign to a lab (from the equipment schedule)
6. Submit — lab receives the request and schedules testing

#### Test Request Statuses

| Status | Meaning |
|---|---|
| `pending` | Submitted, awaiting lab scheduling |
| `in_progress` | Testing underway |
| `review` | Results ready, under engineering review |
| `passed` | All tests passed — part cleared for certification |
| `failed` | One or more tests failed — part flagged, investigation required |

#### Equipment Schedule

The **Equipment** tab shows all lab instruments with:
- Equipment name and type
- Current status (Available / In Use / Maintenance)
- Next available slot
- Booking calendar

Click **Book Slot** to reserve equipment time for an upcoming test.

#### Test Reports

The **Reports** tab shows completed test reports:
- Report ID and date
- Linked order and blueprint
- Test results summary (pass/fail per test type)
- Certification standard met
- Digital signature of approving engineer
- **Download PDF** button

---

### 5.18 Customer Success

**Sidebar label:** Customer Success  
**Purpose:** End-to-end service management — onboarding, training, support tickets, and account health.

#### Customer Health Dashboard

Each customer account has a **Health Score** (0–100) computed from:
- Platform adoption (active users, features used)
- Order volume trend
- Support ticket frequency and resolution time
- NPS survey responses

#### Sections

| Section | Content |
|---|---|
| **Onboarding Tracker** | Progress bar per customer through onboarding milestones |
| **Trained Personnel Registry** | All users qualified and authorized for each platform function |
| **Training Completions** | Module-by-module completion status per user |
| **Support Tickets** | Open and resolved tickets, SLA compliance |
| **Account Reviews** | Scheduled review meetings and outcomes |
| **NPS & CSAT** | Net Promoter Score and satisfaction survey results |

---

#### Trained Personnel Registry

The **Trained Personnel Registry** is a live record of every user who has been formally trained and cleared to perform specific actions on the platform. Certain operations — such as initiating a DRM approval, operating a print center, or issuing a certificate — require that the acting user appears in the registry with the relevant qualification.

##### Why It Matters

- **Regulatory compliance** — aviation (AS9100), marine (DNV), and defence standards require proof that personnel performing quality-critical actions were trained and qualified
- **Audit trail** — every DRM approval, quality sign-off, and cert issuance is linked to the qualified person in the registry
- **Access gating** — users without the required training flag cannot complete certain actions (the button is disabled with a tooltip explaining the missing qualification)

##### Personnel Record Fields

| Field | Description |
|---|---|
| **User ID** | Platform user account identifier |
| **Full Name** | Legal name as registered |
| **Organization** | Employer / print center / OEM / authority |
| **Role** | Platform role (see Section 8) |
| **Training Modules Completed** | List of all passed modules with date and score |
| **Qualifications Held** | Formal qualifications (e.g., AM Operator L2, DRM Approver, Quality Inspector) |
| **Authorized Actions** | Which platform actions this person is cleared to perform |
| **Qualified Since** | Date of first qualification on this platform |
| **Renewal Due** | Date by which re-training or re-certification is required |
| **Status** | Active · Suspended · Pending Renewal · Expired |

##### Training Modules

All users must complete the relevant modules before their role permissions are fully activated:

| Module | Required For | Duration |
|---|---|---|
| **Platform Fundamentals** | All roles | 1 hour |
| **DRM Workflow & IP Compliance** | OEM, Operator, Admin | 2 hours |
| **Blueprint Management** | OEM, Operator, Admin | 1.5 hours |
| **DRM Approver Certification** | OEM role (approval actions) | 3 hours + assessment |
| **Certification Authority Procedures** | Cert Authority role | 3 hours + assessment |
| **Print Center Operations** | Print Center role | 2 hours |
| **Quality Inspection Protocol** | Print Center, Lab Portal users | 2 hours |
| **Audit Log Interpretation** | Compliance officers, Admins | 1 hour |
| **Materials Traceability** | Print Center, Operator | 1.5 hours |
| **Lab & Testing Procedures** | Lab Portal users | 2 hours + practical |

##### Qualification Levels

| Level | Name | Description |
|---|---|---|
| `L1` | Awareness | Completed fundamentals only — view access |
| `L2` | Operator | Full module set for assigned role — write access |
| `L3` | Senior / Approver | Role modules + approver assessment — can approve DRM, certs, quality |
| `L4` | Administrator | All modules + admin training — full platform access |

##### Managing Trained Personnel

**Adding a trained person:**
1. Go to **Customer Success → Trained Personnel Registry → + Add Person**
2. Search for the user account or create a new one
3. Assign their organization and role
4. Record completed training modules (upload certificate or mark module as passed)
5. The system automatically calculates their qualification level and authorized actions
6. Save — the user's action permissions are updated immediately

**Viewing training status:**
- Green checkmark = module completed and current
- Amber clock = renewal due within 30 days
- Red × = expired or not completed — user is restricted from that action

**Suspending a trained person:**
If a person leaves the organization or their qualifications are revoked, click **Suspend** on their registry record. All DRM approvals and cert sign-offs they completed remain in the Audit Log (non-repudiable), but they lose action permissions immediately.

**Bulk Import:**
Use the **Import CSV** button to upload a batch of trained personnel from an existing HR or training management system. The CSV template is downloadable from the same button.

##### Training Renewal

Qualifications are not permanent. The platform tracks renewal due dates and:
- Sends **email reminders** at 60 days, 30 days, and 7 days before expiry
- Shows an **amber warning badge** on the person's record from 30 days out
- **Auto-restricts** approver actions when a qualification expires (the user is downgraded to L1 until renewed)
- Logs the expiry event in the Audit Log

#### Creating a Support Ticket

1. Click **+ New Ticket**
2. Select customer and contact
3. Category: Technical / Billing / Training / Feature Request / Other
4. Priority: P1 (Critical) → P4 (Low)
5. Description and steps to reproduce (for technical issues)
6. Assign to a customer success manager
7. Submit — customer is notified automatically

#### Escalation

P1 tickets escalate automatically after 2 hours without a response. P2 tickets escalate after 8 hours. Escalations are visible as a red badge on the Customer Success sidebar item.

---

### 5.19 Settings

**Sidebar label:** Settings  
**Purpose:** Manage profile, notifications, appearance, integrations, and tutorial state.

#### Sections

| Section | What you can configure |
|---|---|
| **Profile Settings** | Name, email, role, company, phone number |
| **Appearance** | Dark mode toggle (when available), density (compact / comfortable / spacious) |
| **Notifications** | Email notifications on/off per event type (new orders, approvals, cert expiry, etc.) |
| **Security** | Change password, manage sessions, 2FA setup |
| **Integrations** | Connect ERP (SAP, Oracle), PLM (PTC Windchill, Siemens Teamcenter), logistics APIs |
| **Tutorial & Help** | **Restart Tutorial** button — resets all 19 section tutorials and onboarding tour |

#### Restarting Tutorials

Click **Settings → Tutorial & Help → Restart Tutorial**. This:
1. Clears `onboarding_complete` from localStorage
2. Clears all 19 `section_seen_*` flags from localStorage
3. The next time you visit the dashboard or navigate to any section, the tutorials appear fresh

---

## 6. Core Workflow — End-to-End Print Order

Here is the complete lifecycle of a part request from need identification to delivery:

```
1. IDENTIFY NEED
   └─ Physical inventory falls below threshold OR maintenance team raises request

2. CHECK DIGITAL INVENTORY
   └─ Is there a certified blueprint available?
      ├─ YES → proceed to step 3
      └─ NO  → submit blueprint for OEM licensing (IP Library → Request License)

3. CREATE ORDER (Orders → + New Order)
   └─ Select: Part, Blueprint, Print Center, Quantity, Priority, Due Date

4. DRM APPROVAL PIPELINE (Print Queue)
   ├─ Step 1: OEM reviews and approves IP license for this specific job
   ├─ Step 2: Certification Authority confirms print center is cleared
   └─ Step 3: System auto-issues DRM token (one-time decryption key)

5. PRINT EXECUTION
   └─ Print center receives token, decrypts blueprint, executes print job
      └─ In-process inspection logged in Lab Portal (if required)

6. QUALITY CHECK
   └─ Physical inspection + dimensional/mechanical testing (Lab Portal)
      ├─ PASS → order advances to Shipped
      └─ FAIL → order flagged, re-print or escalation

7. SHIPMENT (Shipments)
   └─ Carrier picks up, tracking updated in real-time

8. DELIVERY & AUDIT
   └─ Order marked Delivered
   └─ All events (DRM, approvals, material batch, test results) written to Audit Log permanently
```

---

## 7. DRM (Digital Rights Management) Explained

### Why DRM?

CAD blueprints for critical industrial parts represent enormous IP value. Without protection:
- A print center could print unlimited copies and sell them
- Counterfeit or out-of-spec parts could enter the supply chain without audit trail
- OEMs lose royalty revenue and quality control

### How the AddManuChain DRM System Works

1. **Blueprints are stored encrypted** — the raw CAD file is AES-256 encrypted at rest. No one can print from it without a valid token.

2. **A print token is a one-time key** — each token is cryptographically linked to:
   - A specific order ID
   - A specific blueprint version
   - A specific print center machine ID
   - A specific print quantity
   - An expiry timestamp (typically 24 hours)

3. **Token burns after use** — once the printer uses the token to decrypt and begin the job, it is invalidated. Cannot be reused or copied to print more units.

4. **Immutable audit trail** — every token issuance, use, and expiry is logged to the Audit Log with cryptographic chaining.

### Token States

| State | Meaning |
|---|---|
| Not yet issued | Both approvals pending |
| Issued | Active, not yet used |
| Active | Print job in progress |
| Consumed | Token used, job complete |
| Expired | Token generated but never used, timed out |
| Revoked | Admin or OEM cancelled the token before use |

---

## 8. User Roles & Permissions

The sidebar and available actions are filtered based on the user's assigned role:

| Role | Full Name | Key Permissions |
|---|---|---|
| `operator` | Operator / Buyer | Create orders, view inventory, track shipments |
| `oem` | OEM Partner | Approve DRM pipeline (OEM step), manage IP Library, view royalties |
| `cert_authority` | Certification Authority | Approve DRM pipeline (Cert step), manage certifications, view audit logs |
| `print_center` | Print Center Manager | View assigned jobs, update print status, manage equipment |
| `admin` | Platform Administrator | Full access to all sections, user management, system settings |
| `viewer` | Read-Only Stakeholder | View-only across allowed sections, no write actions |

Role is configured in **Settings → Profile Settings → Role**.

> **Important:** Having a role assigned is not sufficient on its own for actions that require formal training. Users must also appear in the **Trained Personnel Registry** (Customer Success) with the appropriate qualification level for their role. See [Section 5.18](#518-customer-success) for details.

---

## 9. Status Reference Tables

### Order Statuses

| Status | Color | Meaning |
|---|---|---|
| `pending` | Blue | Created, awaiting DRM approval |
| `printing` | Amber | DRM approved, print in progress |
| `quality_check` | Purple | Print complete, QC inspection |
| `shipped` | Teal | Passed QC, with carrier |
| `delivered` | Green | Confirmed received |
| `cancelled` | Red | Order cancelled |

### Blueprint Statuses

| Status | Color | Meaning |
|---|---|---|
| `active` | Green | Ready for use |
| `pending_review` | Amber | Awaiting approval |
| `certified` | Blue | Full certification achieved |
| `deprecated` | Grey | Superseded, no new orders |
| `revoked` | Red | IP revoked |

### Certification Statuses

| Status | Color | Meaning |
|---|---|---|
| `active` | Green | Valid and current |
| `pending` | Amber | Under review / renewal |
| `expiring_soon` | Orange | Expires within 60 days |
| `expired` | Red | Lapsed, requires immediate renewal |
| `suspended` | Red | Suspended by authority |

### DRM Token States

| State | Color | Meaning |
|---|---|---|
| `awaiting_approvals` | Blue | One or both approvals pending |
| `issued` | Green | Token ready, not yet used |
| `active` | Amber | Print job in progress |
| `consumed` | Grey | Used, job complete |
| `expired` | Red | Timed out unused |
| `revoked` | Red | Cancelled by admin/OEM |

---

## 10. Keyboard Shortcuts & Tips

| Shortcut / Action | Effect |
|---|---|
| Click sidebar item | Navigate to section |
| `Click sidebar arrow ◀` | Collapse / expand sidebar |
| `Click ? in header` | Open section tutorial |
| `Click ✦ (Sparkles FAB)` | Open AI Assistant chat |
| `Enter` in AI chat | Send message |
| `Shift + Enter` in AI chat | New line in message |
| `Click trash in AI panel` | Clear chat history |
| `Hover AI message` | Reveal Copy button |
| `Click × on tutorial card` | Dismiss tutorial for this session |
| `Click dot indicators` | Jump to any tutorial step |

### Power-User Tips

- **Notification badges** on sidebar items are your "to-do" list — work through them at the start of each day
- **Print Queue badge** is the most time-sensitive — DRM approvals unlock revenue-critical jobs
- **Certifications expiring soon** appear in both the Overview panel and the header notification bell — set a calendar reminder 30 days before expiry
- **AI Assistant** can explain any field, status, or workflow — it's faster than re-reading this guide
- **Audit Logs** are your compliance evidence — export a filtered CSV before any regulatory audit
- **Analytics → Environmental Impact** panel is useful for ESG reporting and sustainability KPIs

---

## 11. FAQ

**Q: Why can't I select a blueprint when creating an order?**  
A: The blueprint must have status `active` or `certified`. If it shows `pending_review`, it has not yet been approved by the OEM. If it shows `revoked` or `deprecated`, it cannot be used for new orders.

**Q: Why is my order stuck in Print Queue with no approvals?**  
A: Both the OEM and the Certification Authority must approve independently. Either one may be waiting. Check the Print Queue detail panel — it shows which specific approval is outstanding. Contact the OEM or CA directly if it has been waiting more than your agreed SLA.

**Q: What happens if a print center goes offline mid-job?**  
A: The DRM token remains valid for its full TTL (typically 24 hours). If the center comes back online within that window, the job can resume. If the token expires, another must be issued (requires re-approval). This event is logged in the Audit Log.

**Q: Can I reuse a DRM token?**  
A: No. Tokens are single-use by design. Each print job requires its own token, which requires its own OEM + Cert approval cycle. This ensures full traceability and prevents unauthorized copies.

**Q: How do I add a new certification to a print center?**  
A: Go to Print Centers → click the center → Certifications tab → Upload New Cert. The cert enters `pending` state until the issuing authority confirms it (via the Authorities page).

**Q: My blueprint upload succeeded but it's not showing in the order creation dropdown.**  
A: After upload, blueprints start in `pending_review`. An OEM or admin must approve it before it becomes available for orders. You can track approval status in Blueprint Library.

**Q: How do I reset my tutorial guides?**  
A: Settings → Tutorial & Help → Restart Tutorial. This resets all 19 section tutorials and the onboarding tour. Your data is not affected.

**Q: How do I export audit logs for a regulatory submission?**  
A: Audit Logs → apply the relevant date range and category filters → click **Export CSV** (top-right). The export includes all visible columns and is formatted for standard compliance reporting.

**Q: What is the AI Risk Score?**  
A: Each order receives an AI Risk Score (0–100) based on: material criticality, print center compliance history, blueprint certification level, and lead time pressure. Higher scores mean more risk. Orders above 75 are flagged for manual review.

**Q: Can the AI Assistant access my real data?**  
A: The AI Assistant is trained on platform knowledge (procedures, workflows, definitions) but does **not** have access to your specific order, customer, or financial data. It answers procedural and explanatory questions only.

---

*For additional support, contact the AddManuChain team or use the AI Assistant on any page.*
