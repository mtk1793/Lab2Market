# AddManuChain Dashboard — Complete Tutorial Guide

> **Version:** 2.0 | **Last Updated:** February 2026
> 
> This document provides a full walkthrough of every section in the AddManuChain dashboard — what it does, how to use it, and tips to get the most value from each feature.

---

## How the In-App Tutorial Works

The dashboard includes a **built-in step-by-step tutorial system**:

| Trigger | What happens |
|---|---|
| **First visit to any section** | A tutorial card automatically slides in from the bottom-right corner |
| **`?` button in the header** | Manually re-launch the tutorial for the current section at any time |
| **Settings → Restart Tutorial** | Resets ALL section tutorials so they auto-show again on next visit |

### Navigating the tutorial card
- **Next** → advance to the next step
- **Back** → go to the previous step
- **Click any dot** → jump directly to that step
- **Done / ×** → dismiss the tutorial for this section (won't auto-show again until you reset)
- **Click backdrop** → also dismisses the tutorial

---

## Section-by-Section Guide

---

### 1. Dashboard Overview (`overview`)

**Purpose:** Command centre — a live snapshot of all platform activity.

| Element | What it shows |
|---|---|
| **KPI Stat Cards** | Active orders, blueprints, print centers, pending certifications, cost savings, lead time reduction |
| **Recent Orders** | Latest 5 orders with colour-coded status badges |
| **Print Center Status** | Live capacity tiles (green = available, yellow = busy, red = full) |
| **Activity Feed** | Real-time event log — orders, approvals, uploads, DRM token issuances |

**Tips:**
- Click any stat card to jump directly to that section.
- Filter the Activity Feed by type or date range using the filter icon.

---

### 2. Orders (`orders`)

**Purpose:** Create, track, and manage all spare-part print requests end-to-end.

**Order lifecycle:** `Draft → Approved → Printing → QC → Shipped → Delivered`

| Feature | How to use it |
|---|---|
| **Status tabs** | Filter by All / Active / Pending / Completed |
| **Priority filter** | Critical / High / Medium / Low — colour-coded |
| **Order cards** | Shows part name, blueprint ID, print center, ETA, status — expand for full detail |
| **Progress bar** | Inside each card — shows % of print job complete |
| **+ New Order** | Wizard: select certified blueprint → choose print center → set priority → confirm materials |
| **Order detail** | Real-time tracking timeline, DRM token status, cert sign-off log, message thread |

**Tips:**
- Only **certified blueprints** can be selected for new orders.
- All communications are hash-logged for compliance traceability.

---

### 3. Print Queue / DRM Approval (`print_queue`)

**Purpose:** Multi-party Digital Rights Management (DRM) approval pipeline.

Every print job requires sign-off from three parties before printing begins:

```
Customer Submitted → OEM Review → Cert Authority Review → Token Issued → Print Authorized
```

| Feature | Detail |
|---|---|
| **Approval stages** | Hover any badge to see timestamp and approver name |
| **DRM Token** | Cryptographic token defines exact quantity, material, and print parameters |
| **Single-use tokens** | Re-printing requires a new approval cycle by default |
| **Approve / Reject** | Available to users with the Approver role |
| **Rejection notes** | Required — explains the correction needed for resubmission |
| **Bulk approval** | Tick checkboxes to approve multiple low-risk items at once |

---

### 4. Physical Inventory (`physical_inventory`)

**Purpose:** Real-time stock levels for physical spare parts across all rigs and warehouses.

| Feature | Detail |
|---|---|
| **Site Selector** | Filter inventory to a specific rig or warehouse |
| **All Sites view** | Aggregate stock — spot cross-site imbalances |
| **Status badges** | In Stock (green) / Low Stock (yellow) / Out of Stock (red) |
| **Blueprint link** | Shows if a certified digital blueprint exists for on-demand re-printing |
| **Reorder point** | Set per-part in the part detail view |

**Tips:**
- Parts without a certified blueprint are flagged for AM digitisation review.
- Sort by Status to prioritise urgent replenishments.

---

### 5. Digital Inventory (`digital_inventory`)

**Purpose:** AI-powered forecasting of which parts are most likely to cause a stockout.

| Feature | Detail |
|---|---|
| **AI Risk Score** | 0–100 — higher = more urgent. Parts > 70 auto-escalate to the Orders queue |
| **Recommended action** | "Print Now" / "Upload Blueprint" / "Monitor" |
| **Onsite Readiness** | Green = certified blueprint + nearby print center + materials available |
| **Readiness refresh** | Recalculated every hour from live print center data |
| **+ Upload Blueprint** | Uploads go through geometry validation → OEM review → certification |
| **Consumption history** | 12-month chart, predicted failure curve, comparable parts |

**Supported file formats:** `.STL`, `.STEP`, `.STP`, `.OBJ`, `.3MF`

---

### 6. Blueprint Library (`blueprints`)

**Purpose:** Central repository of all certified CAD files for printable spare parts.

| Feature | Detail |
|---|---|
| **Blueprint cards** | Part name, blueprint ID, revision, OEM owner, materials, certification status |
| **Certified badge** | Only certified blueprints can be used to create orders |
| **Search** | By name, part number, or OEM reference |
| **Filter** | By material type or certification status |
| **3D preview** | Interactive — rotate and zoom with mouse drag |
| **Spec sheet** | Download certified spec sheet as PDF |
| **Version management** | Old revisions archived; in-progress orders keep their locked version |

---

### 7. Print Centers (`centers`)

**Purpose:** Monitor certified AM facilities and their live capacity.

| Feature | Detail |
|---|---|
| **Capacity bar** | Live utilisation — updates every 15 minutes via API |
| **Queue count** | Number of jobs waiting |
| **"Available Now"** | Center can start a new job within 4 hours |
| **Capability matrix** | Which material types and part categories each center is certified for |
| **Request Print** | Pre-assign an order to a specific facility (goes through DRM pipeline) |
| **Preferred center** | Set per blueprint in the Blueprint Library |

---

### 8. Peer Printers (`peer_printers`)

**Purpose:** Airbnb-style marketplace for sharing idle certified 3D printer capacity.

| Feature | Detail |
|---|---|
| **Printer listings** | Type, build volume, materials, certification level, hourly rate, rating |
| **Book Slot** | Reserve a window — requires DRM-approved token; payment on job completion |
| **Quality guarantee** | Failed prints are reprinted at no cost under the AddManuChain guarantee |
| **List My Printer** | Add your own certified printer — set availability, materials, pricing |
| **Certification audit** | Printers must pass before appearing in search results |
| **Earnings** | Transferred weekly to printer owner |

---

### 9. Shipments (`shipments`)

**Purpose:** End-to-end tracking of all outbound and inbound printed-part deliveries.

| Feature | Detail |
|---|---|
| **Shipment timeline** | Packaged → Collected → In Transit → Customs → On Board → Delivered |
| **Live tracking map** | Vessel/aircraft positions; helicopter transfer status for offshore deliveries |
| **List / Map toggle** | Switch views in the top right |
| **Customs docs** | Auto-generated from blueprint + certification data — download as single PDF |
| **Push notifications** | Alerts at each milestone (enable in Settings) |

---

### 10. Materials Inventory (`materials`)

**Purpose:** Track raw material stocks (powders, polymers, wire) at each print center.

| Feature | Detail |
|---|---|
| **Material list** | Type, grade, lot certificate, mill certificate traceability |
| **Stock gauge** | kg or liters remaining vs. reorder point |
| **Auto-procurement** | System raises procurement request when stock drops below threshold |
| **Dual-source flag** | Mark critical materials for dual-source procurement |
| **30/60/90-day forecast** | Based on current order pipeline — alerts for predicted shortages |
| **Lead time link** | Add procurement lead times so forecasts include replenishment horizons |

---

### 11. OEM Partners (`partners`)

**Purpose:** Manage relationships with Original Equipment Manufacturers.

| Feature | Detail |
|---|---|
| **Partner cards** | Certifications, active blueprints, pending approvals, SLA performance |
| **SLA flag** | Red badge = SLA breach — follow up directly from this page |
| **Blueprint submissions** | View all OEM-owned blueprints and their certification status |
| **Approval nudge** | Ping partner for overdue approvals with one click |
| **Automated reminders** | Set for approvals pending > 48 hours |
| **+ New Partner** | Full onboarding workflow: details → portal user → approval rights → royalty terms |

---

### 12. Analytics (`analytics`)

**Purpose:** Deep-dive into operational performance, cost savings, and environmental impact.

| Feature | Detail |
|---|---|
| **KPI summary** | Total cost savings, average lead time reduction, CO₂ saved, print success rate |
| **Date picker** | All figures calculated over selected range (top right) |
| **Order volume chart** | Monthly bar chart — toggle absolute vs. % split |
| **Cost comparison** | Waterfall chart: AddManuChain vs. traditional procurement |
| **Export** | Any chart as PNG or CSV (hover → download icon) |
| **Generate Report** | Full PDF analytics report for any date range |
| **Scheduled reports** | Auto-email to stakeholders monthly |

---

### 13. Audit Logs (`audit`)

**Purpose:** Immutable, hash-chained log of every action for regulatory compliance.

**Standards covered:** DNV GL, Lloyd's Register, ASTM, NORSOK

| Feature | Detail |
|---|---|
| **Hash chain** | Each entry includes previous entry's hash — tamper-evident |
| **"Chain OK" badge** | Confirms entire log is unmodified |
| **Verify Chain** | Manual integrity check at any time |
| **Filters** | By User, Action Type, Date Range, or Severity |
| **Search** | Find specific event IDs |
| **Export** | Signed PDF or JSON with platform-level digital signature |

**Tip:** Routine quarterly exports are recommended as part of your compliance programme.

---

### 14. Certifications (`certifications`)

**Purpose:** Track and renew certifications for your org, print centers, and blueprints.

**Issuing bodies:** DNV GL, Lloyd's Register, Bureau Veritas, ABS, TÜV SÜD

| Feature | Detail |
|---|---|
| **Status dashboard** | Green = active, amber = expiring in 90 days, red = expired |
| **Renewal reminders** | Automated at 90, 30, and 7 days before expiry |
| **Blueprint certifications** | Standard, issue date, revision covered, expiry |
| **Expired blueprints** | Cannot be used in production — system blocks selection |
| **Auto-renewal workflow** | Submit recertification request 60 days before expiry |
| **+ Add Certification** | Upload document, link to blueprint/center, set expiry |
| **Bulk import** | CSV import for initial platform setup |

---

### 15. Certification Authorities (`authorities`)

**Purpose:** Manage relationships with the bodies that certify blueprints, centers, and materials.

| Feature | Detail |
|---|---|
| **Authority cards** | Standards covered, active reviews, approval history, your account contact |
| **Approval workflows** | Auto-routed by required standard; tracked against SLA |
| **Custom workflows** | Configurable per authority in Settings |
| **Document portal** | Securely share files with authority reviewers — logged, version-controlled |
| **Large file handling** | Files > 100 MB automatically chunked and encrypted |

---

### 16. Customer Success (`services`)

**Purpose:** End-to-end service management — training, support, and account health.

| Feature | Detail |
|---|---|
| **Training modules** | Interactive library for operators, engineers, managers |
| **Completion tracking** | Per user — feeds into account health score |
| **Mandatory modules** | Assign to new users from team management panel |
| **Support tickets** | Technical / Billing / Compliance / Training — 2-hour SLA for Priority |
| **Attach files** | Screenshots and log exports attachable directly to a ticket |
| **Account health score** | 0–100 based on adoption, training, open tickets, SLA compliance |

---

### 17. IP Library (`ip_library`)

**Purpose:** Secure vault for OEM intellectual property — licensed blueprints, formulations, and processes.

| Feature | Detail |
|---|---|
| **Licence types** | Per-print / perpetual / subscription |
| **Royalty metering** | Auto-calculated from actual prints; monthly statements to OEM |
| **File encryption** | Raw design file never accessible outside certified print environment |
| **Access request** | Workflow for requesting expanded access (e.g. re-engineering studies) |
| **Usage analytics** | Prints made, print centers used, royalties generated |
| **+ Add IP Asset** | OEM uploads, sets access tiers, pricing, print center restrictions |

---

### 18. Lab & Testing Portal (`lab_portal`)

**Purpose:** AM testing requests, equipment scheduling, and certification test reports.

**Standards supported:** NORSOK M-630, DNV SE-0472, and custom test bundles

| Feature | Detail |
|---|---|
| **Test requests** | Select print job → specify tests → auto-routed to accredited lab |
| **Test bundles** | Pre-configured offshore standard packages (one-click submission) |
| **Equipment scheduling** | Book CT scanners, tensile machines, CMMs in 4-hour blocks (up to 30 days ahead) |
| **Urgent flagging** | Jump the queue with manager approval |
| **Test reports** | Uploaded directly by lab — linked to print job and blueprint |
| **Pass result** | Auto-triggers certification update |
| **Fail result** | Auto-opens Non-Conformance Report (NCR) |
| **NCR workflow** | Root cause → corrective action → re-test → closure sign-off |
| **AI feedback** | NCR trends feed back into AI model to improve print parameters |

---

### 19. Settings (`settings`)

**Purpose:** Account, team, notifications, and platform configurations.

| Section | What you can configure |
|---|---|
| **Profile & Account** | Name, email, role, photo, password, 2FA (mandatory for Approvers) |
| **Notifications** | Email / SMS / in-app alerts by event type (orders, approvals, certifications, system) |
| **Critical Alerts** | SMS for any red-status event — overrides other notification settings |
| **Team Management** | Add/remove users, assign roles, set mandatory training modules |
| **Integrations** | Connect ERP, procurement, and logistics systems via API |
| **Restart Tutorial** | Resets ALL section tutorials — they re-appear on next visit to each section |

---

## User Roles

| Role | Access Level |
|---|---|
| **Admin** | Full access to all sections and settings |
| **Customer Admin** | All sections except system-level admin settings |
| **OEM Partner** | Blueprint Library, IP Library, Certifications, Analytics (own data) |
| **Print Center** | Print Queue, Orders (assigned), Materials, Lab Portal |
| **Cert Authority** | Print Queue (approval), Certifications, Audit Logs |
| **Operator** | Overview, Orders (read), Physical Inventory, Shipments |

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `/` | Focus the search bar |
| `Esc` | Close any open modal or tutorial |
| `?` | (same as pressing the `?` button) — open current section tutorial |

---

## Frequently Asked Questions

**Q: Why can't I select a blueprint when creating an order?**  
A: Only blueprints with **Certified** status are selectable. Check the Blueprint Library for the certification status and contact the OEM if it's expired.

**Q: The DRM token was issued but the print center can't start printing — why?**  
A: Confirm that (a) the token is **Active** (not revoked), (b) the print center's assigned materials match the token spec, and (c) the center has sufficient capacity.

**Q: How do I onboard a new team member?**  
A: Go to **Settings → Team Management → + Add User**, assign their role, then send them to **Settings → Restart Tutorial** so all section guides appear fresh for them.

**Q: Can I reset a specific section tutorial without resetting all of them?**  
A: Currently, **Settings → Restart Tutorial** resets all sections at once. This will be enhanced to per-section reset in a future release.

**Q: How long are audit logs retained?**  
A: Logs are retained indefinitely and are cryptographically sealed. There is no automatic deletion.

---

*For technical support, raise a ticket in the **Customer Success** section of the dashboard.*
