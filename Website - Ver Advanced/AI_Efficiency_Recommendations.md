# AI Efficiency Recommendations — AddManuChain Platform
**Date:** April 3, 2026  
**Scope:** All 21 dashboard modules + supporting infrastructure  
**Goal:** Identify where AI can reduce manual effort, speed up decisions, and create compounding value across the platform

---

## How to Read This Document

Each section maps to a dashboard module. For each one you'll find:
- **Current state** — what the module does today
- **AI opportunity** — specific, actionable integrations
- **Model/tool to use** — concrete Claude/AI tooling recommendation
- **Impact** — time saved or risk reduced

---

## 1. Orders (`/orders`)

**Current state:** Manual order creation, status updates tracked by hand, DRM approval flow requires human polling.

**AI Opportunities:**

### 1.1 Smart Order Drafting
When a user starts an order, AI pre-fills `partName`, `quantity`, `priority`, and `printCenterId` based on:
- Historical order patterns for that operator
- Current digital inventory risk scores
- Nearest available print centre with matching certification

**How:** Add a "Smart Fill" button that calls Claude with the operator's order history + current inventory snapshot. Returns a pre-filled form the user can review and confirm.

### 1.2 Anomaly Detection on New Orders
Before submitting, AI flags orders that look unusual:
- Quantity far above historical average
- Part ordered recently (possible duplicate)
- Print centre selected has a low capacity or offline status
- No matching certified blueprint exists

**How:** A lightweight validation pass via Claude before the `POST /api/orders` call. Show a warning banner, not a hard block.

### 1.3 Priority Recommendation
AI reads the operational context (vessel location, part criticality rating, last replacement date) and recommends `CRITICAL / HIGH / NORMAL` with a one-line justification shown inline.

**Impact:** Reduces incorrect priority assignment, which currently causes SLA mismatches and delays in the DRM queue.

---

## 2. Print Approval / DRM Queue (`/print_queue`)

**Current state:** OEM approvals and Cert Authority approvals happen manually, in sequence, with no time estimates or bottleneck visibility.

**AI Opportunities:**

### 2.1 Auto-Draft OEM Approval Decisions
For repeat orders of already-approved blueprints, AI can pre-populate the OEM approval with:
- Prior approval rationale
- Suggested licence terms (same as last approved)
- Risk summary (print centre certification match, quantity check)

OEM only needs to click "Confirm" rather than reviewing from scratch.

### 2.2 Cert Authority Matching Intelligence
When a print job enters the queue, AI checks:
- Blueprint's required certification standard (DNV, ABS, Lloyd's, etc.)
- Print centre's active certifications + expiry dates
- Current queue depth at that centre

If the assigned centre is a mismatch or near expiry, AI surfaces a re-routing suggestion before the request reaches the Cert Authority.

### 2.3 Queue ETA Prediction
AI predicts how long each pending approval will take based on:
- Cert Authority's historical average approval time
- Current queue depth
- Time of day / day of week patterns

Surfaces this as a live countdown on each queue card so operators can plan.

**Impact:** Cuts average DRM approval time from current baseline. Eliminates the most common cause of delays — wrong centre assignment caught too late.

---

## 3. Digital Inventory (`/digital_inventory`)

**Current state:** Risk scores (0–100) are already computed. But there is no automated action triggered when risk crosses a threshold.

**AI Opportunities:**

### 3.1 Risk Score Narrative Generation
For any part with a risk score above 70, AI generates a plain-English explanation:
> "Bearing assembly #BR-441 has a risk score of 84 because lead time is 18 days (above 14-day threshold) and stock is at 1 unit (below 3-unit minimum for this vessel class). Recommend immediate reorder."

Users currently have to interpret raw numbers. The narrative removes cognitive load.

### 3.2 Proactive Reorder Recommendations
AI monitors all risk scores daily and generates a prioritized reorder list each morning. Shows:
- Part name + risk score
- Recommended order quantity
- Suggested print centre
- Estimated time to restock

Delivered as a digest inside the platform (no email needed — just a banner on login).

### 3.3 What-If Simulation
Operator inputs a scenario: "What if Bay du Nord goes into unplanned downtime for 72 hours?" AI runs through the digital inventory and flags which parts would hit critical stock levels and when, giving procurement a head start.

**Impact:** Transforms the Digital Inventory from a read-only dashboard into an active decision-support tool.

---

## 4. Physical Inventory (`/physical_inventory`)

**Current state:** Site-based stock tracking (rigs, vessels, yards) with manual condition ratings (New/Serviceable/Used/Condemned) and manual transfer requests.

**AI Opportunities:**

### 4.1 Condition Degradation Prediction
AI tracks condition changes over time per part per location. If a part is moving from Serviceable → Used faster than the historical norm for that part type, AI flags it for inspection before it becomes Condemned.

### 4.2 Cross-Site Transfer Optimization
When site A is low on a part and site B has surplus, AI automatically surfaces a transfer recommendation with:
- Logistics cost estimate
- Transit time estimate
- Net savings vs. printing a new part

User confirms or dismisses with one click.

### 4.3 Condemned Parts Digitization Pipeline
When a part is marked Condemned, AI prompts: "Would you like to initiate a digitization request?" and pre-fills the blueprint upload form with known metadata (part name, OEM, material, last known certification). Turns a write-off into an AM opportunity.

**Impact:** Reduces redundant inventory purchases and accelerates the digitization pipeline.

---

## 5. Materials (`/materials`)

**Current state:** Stock status alerts (Adequate/Low/Critical) per material per centre. Reorder is manual.

**AI Opportunities:**

### 5.1 Consumption Rate Forecasting
AI analyzes order history to predict how fast each material (Ti-6Al-4V, Inconel 625, 316L SS, etc.) will be consumed over the next 30/60/90 days at each print centre. Computes a projected stockout date per material per location.

### 5.2 Bulk Purchase Optimization
When multiple centres are running low on the same material, AI bundles the reorder into a single consolidated purchase recommendation with:
- Combined quantity
- Estimated bulk discount
- Split delivery plan per centre

### 5.3 Material Substitution Suggestions
If a required material is Critical and lead time is long, AI checks the blueprint's mechanical requirements and suggests compatible substitute materials with a confidence score and a note on any certification implications.

**Impact:** Prevents print job stoppages due to material stockouts. Reduces material carrying cost through smarter ordering.

---

## 6. Blueprint Library (`/blueprints`)

**Current state:** Manual upload, manual categorization, manual status management (Active/Pending/Archived). 3D viewer exists but is passive.

**AI Opportunities:**

### 6.1 Auto-Classification on Upload
When a new blueprint is uploaded (STL/STEP/3MF), AI:
- Classifies it by category (bearing, bracket, fitting, sensor mount, valve, etc.)
- Extracts metadata (bounding box, estimated weight, complexity score)
- Suggests compatible materials based on geometry
- Flags if a similar blueprint already exists in the library (deduplication)

### 6.2 AM Feasibility Pre-Check
Before a blueprint enters the approval queue, AI runs a quick feasibility screen:
- Wall thickness check (minimum printable threshold)
- Overhangs requiring support structures
- Surface finish requirements vs. AM capability
- Estimated print time and material usage

Saves Cert Authorities from reviewing blueprints that are not yet AM-ready.

### 6.3 Version Diff Summaries
When a new blueprint version is uploaded, AI compares it to the previous version and generates a change summary:
> "Version 3.1 modifies the inner bore diameter by +0.2mm and increases wall thickness in the flange area by 15%. These changes may affect the DNV cert issued under v3.0 — re-certification recommended."

**Impact:** Dramatically speeds up the blueprint onboarding and review process. Reduces re-work from uploading non-printable files.

---

## 7. Print Centers (`/centers`)

**Current state:** Live status grid (Online/Busy/Offline), capacity bars, printer counts. Entirely read-only — no recommendations.

**AI Opportunities:**

### 7.1 Intelligent Job Routing
When an order is created, AI selects the optimal print centre (not just the nearest) based on:
- Current capacity and queue depth
- Certification match for the blueprint
- Material availability
- Historical quality score (defect rate per centre)
- Estimated delivery time to the vessel/rig

Displayed as "Recommended Centre" with reasoning, operator can override.

### 7.2 Predictive Maintenance Flagging
AI tracks printer uptime patterns per centre. If Centre X typically goes offline every 3 weeks for 2 days, AI pre-warns the scheduler so jobs are re-routed before the downtime hits.

### 7.3 Capacity Planning
AI forecasts which centres will be over-capacity in the next 7/14 days based on current order pipeline. Suggests pre-positioning jobs or onboarding a new peer printer before the crunch.

**Impact:** Increases network utilization efficiency. Reduces job failures caused by last-minute centre unavailability.

---

## 8. Peer Printers (`/peer_printers`)

**Current state:** Airbnb-style idle printer marketplace. Listing and booking is manual.

**AI Opportunities:**

### 8.1 Demand-Supply Matching
AI matches urgent orders to available peer printers based on:
- Printer capability (material, bed size, tolerance)
- Operator rating
- Location relative to delivery point
- Price

Surfaces as "Best Match" at the top of the listing, not just alphabetical/chronological.

### 8.2 Dynamic Pricing Suggestions
When a peer printer owner lists capacity, AI suggests a price range based on:
- Current platform-wide demand for that printer type
- Time of day/week
- Job complexity

### 8.3 Peer Printer Vetting Assistance
AI reviews a new peer printer's listed specs against the blueprint requirements for the job being assigned and flags any incompatibilities before the booking is confirmed.

**Impact:** Turns an unstructured marketplace into an intelligent matching engine.

---

## 9. Shipments (`/shipments`)

**Current state:** 5-stage progress tracking (Preparing → In Transit → Out for Delivery → Delivered). Manual status updates, no predictions.

**AI Opportunities:**

### 9.1 Delay Prediction
AI monitors shipment progress in real time and computes an updated ETA. If a shipment is likely to miss the original ETA (based on carrier patterns, weather, port congestion), it alerts the operator proactively — not after the miss.

### 9.2 Vessel Arrival Synchronization
AI cross-references shipment ETA with the vessel's port schedule. If the part will arrive 2 days after the vessel has already left port, it flags this and suggests expedited shipping or a closer print centre for re-routing.

### 9.3 Auto-Status Narration
For each shipment, AI generates a one-line human update:
> "Your VITON seal (Order #ORD-2847) departed Halifax at 06:00 and is on track to arrive at Bay du Nord Platform by Friday 14:00. No delays detected."

Replaces the raw status codes with operator-friendly language.

**Impact:** Prevents costly vessel holds caused by shipment visibility gaps.

---

## 10. OEM Partners (`/partners`)

**Current state:** OEM partner directory with status management, blueprint contribution count, and royalty analytics.

**AI Opportunities:**

### 10.1 Partner Health Scoring
AI computes a partner health score per OEM based on:
- Blueprint approval response time (avg days)
- Blueprint rejection rate (too many low-quality submissions)
- Revenue generated (royalties earned)
- Relationship tenure

Surfaces partners at risk of churn or disengagement before they go quiet.

### 10.2 Royalty Optimization Recommendations
AI analyzes which blueprints generate the most royalties and surfaces underperforming blueprints with recommendations:
> "Part #FLV-009 has been ordered 0 times in 90 days. Consider reducing the licence fee from $45 to $20 to stimulate demand — estimated revenue uplift: $1,200/quarter at projected order volume."

### 10.3 Partner Outreach Draft Generation
When AI detects a partner hasn't logged in or contributed in 60+ days, it generates a draft outreach message tailored to that partner's profile and contribution history. One click to send.

**Impact:** Increases OEM engagement and royalty revenue without requiring manual relationship management overhead.

---

## 11. IP Library (`/ip_library`)

**Current state:** Licence management (Restricted/Open/Pay-Per-Print/Consortium), royalty tracking, usage analytics.

**AI Opportunities:**

### 11.1 Licence Model Recommendation
When an OEM uploads a new blueprint, AI recommends the optimal licence model based on:
- Part criticality and complexity
- Market demand signals (similar parts' order history)
- OEM's stated monetization goals

With projected revenue estimates for each model.

### 11.2 IP Conflict Detection
When a new blueprint is submitted, AI cross-checks it against existing IP in the library for potential conflicts or near-duplicates. Flags before it enters the approval queue, not after.

### 11.3 Usage Pattern Insights
AI generates quarterly narratives for each OEM:
> "Your 12 blueprints generated $14,200 in royalties this quarter. The INCONEL exhaust flange (ID: BP-0042) accounts for 61% of revenue. Consider adding a bulk-print tier to capture latent enterprise demand."

**Impact:** Makes the IP Library a proactive revenue tool, not just a static vault.

---

## 12. Certifications (`/certifications`)

**Current state:** Manual expiry tracking, manual renewal workflow. Filtering by status (Active/Pending/Expiring Soon/Expired).

**AI Opportunities:**

### 12.1 Renewal Forecasting & Prioritization
AI ranks all certifications by urgency (days to expiry × criticality of parts covered × number of active orders dependent on that cert). Operators see a single prioritized renewal queue, not a flat alphabetical list.

### 12.2 Renewal Package Preparation
When a certification is flagged for renewal, AI pre-fills the renewal package:
- Pulls the relevant audit log entries since last certification
- Summarizes print jobs completed under this cert
- Lists any defect/quality events
- Generates a summary document ready to send to the Cert Authority

Turns a multi-hour manual documentation task into a one-click draft.

### 12.3 Certification Gap Analysis
AI checks: given the current order pipeline for the next 90 days, which certifications are required? Then cross-checks against active certs. If a gap exists (e.g. a DNV cert covers only 3 of the 5 required facilities), it surfaces the gap before it blocks an order.

**Impact:** Eliminates certification lapses — one of the highest-risk compliance failures for offshore operators.

---

## 13. Certification Authorities (`/authorities`)

**Current state:** Directory of DNV GL, Lloyd's Register, ABS, Bureau Veritas, CSA/ISO, ASTM. Approval lead times tracked.

**AI Opportunities:**

### 13.1 Authority Selection Optimization
When a new blueprint needs certification, AI recommends the optimal Cert Authority based on:
- Their historical approval time for this part category
- Current queue depth
- Cost
- Geographic jurisdiction of the print centre

### 13.2 Approval Timeline Prediction
AI predicts how long each authority will take to approve a pending submission based on historical patterns and current workload signals.

### 13.3 Relationship Intelligence
AI tracks interaction history with each authority and surfaces:
- Which contacts approve fastest
- What information they consistently request that is not in the standard package
- Upcoming regulatory changes that may affect approval criteria

**Impact:** Reduces certification lead time — currently the longest step in the DRM pipeline.

---

## 14. Audit Logs (`/audit`)

**Current state:** Immutable SHA-256 hash chain. Excellent compliance foundation but entirely reactive — you search, not act.

**AI Opportunities:**

### 14.1 Anomaly Detection on the Audit Stream
AI monitors the audit log in real time for unusual patterns:
- Same user issuing print tokens for unusually large quantities
- Cert approvals happening outside business hours
- Orders created, approved, and executed in under 10 minutes (too fast for genuine review)
- Multiple failed login attempts followed by a successful token issuance

Flags these for the Admin role immediately — not buried in a log search.

### 14.2 Compliance Report Generation
AI generates ready-to-submit compliance reports from the audit log:
- Select date range + regulation (DNV standard / ISO 9001 / ABS rules)
- AI pulls all relevant log entries
- Formats them into the required structure
- Produces a PDF-ready document

Replaces hours of manual log parsing per audit cycle.

### 14.3 Audit Digest for Regulators
AI generates plain-English audit summaries:
> "In Q1 2026, 47 print jobs were executed. All 47 had valid OEM approval and Cert Authority sign-off before token issuance. Zero tamper events detected. Average DRM cycle time: 2.3 days."

Ready to hand to DNV or Lloyd's without manual preparation.

**Impact:** Transforms compliance from a cost centre into a competitive differentiator — "we can produce a full audit trail in 30 seconds" is a genuine differentiator in regulated industries.

---

## 15. Analytics (`/analytics`)

**Current state:** ROI comparison (JIT vs JIC), lead time graphs, environmental impact (CO₂, miles, waste), order trends.

**AI Opportunities:**

### 15.1 Narrative Analytics
Every chart gets an AI-generated insight line:
> "Lead time this month averaged 3.8 days — 0.6 days faster than last month. The improvement is driven by the new Halifax print centre coming online. However, delivery variance increased from ±0.5 to ±1.2 days, suggesting logistics scheduling needs attention."

Turns raw charts into decision-ready insights.

### 15.2 Proactive ROI Storytelling for Sales
AI generates a customer-specific ROI report:
- Input: customer name, fleet size, current inventory spend
- Output: personalized one-pager showing projected savings from AddManuChain
- Includes: lead time reduction, warehouse cost savings, downtime cost avoidance, CO₂ impact

Ready to drop into a sales email or pitch deck in one click.

### 15.3 Trend Prediction
AI extrapolates current order trends to predict:
- Next 30/60/90 day order volume
- Revenue forecast
- Which part categories will grow or decline

Displayed as confidence bands on the existing charts.

**Impact:** Makes the analytics module useful for sales and investor conversations, not just internal ops reviews.

---

## 16. Customer Success (`/services`)

**Current state:** Kanban board tracking 5 phases (Assessment → Adoption → Integration → Training → Maintenance) with health scores.

**AI Opportunities:**

### 16.1 Churn Risk Prediction
AI computes a churn risk score per customer based on:
- Days since last login
- Order volume trend (growing or declining)
- Support ticket frequency
- Training completion rate
- Phase progression velocity (stuck in Adoption for 45 days = high risk)

Surfaces a daily "At Risk" list for the customer success team.

### 16.2 Next Best Action Recommendation
For each customer, AI recommends the single most impactful action the CS team should take this week:
> "Statoil: Still in Integration phase after 38 days. Recommend scheduling a technical deep-dive call focused on their ERP integration blockers. Suggested contact: Bjorn Larsson (last active 12 days ago)."

### 16.3 Training Gap Analysis
AI analyzes which training modules a customer's users have completed vs. which are relevant to their role, and surfaces a personalized training recommendation:
> "3 of Equinor's 7 rig operators have not completed the DRM approval walkthrough. This module is correlated with 40% faster order cycle times."

### 16.4 Automated QBR (Quarterly Business Review) Prep
AI pulls all usage data for a customer and generates a draft QBR deck:
- Orders placed / completed
- Lead time improvements
- Cost savings vs. baseline
- Top parts ordered
- Recommendations for next quarter

**Impact:** Enables one CS manager to manage 3–4× more accounts without quality degradation.

---

## 17. Lab Portal (`/lab_portal`)

**Current state:** Test request management, equipment scheduling, report tracking. Dalhousie AM Lab integration.

**AI Opportunities:**

### 17.1 Test Plan Generation
When a new part enters the lab for certification testing, AI generates a suggested test plan:
- Required tests for the target certification standard (DNV / ABS / Lloyd's)
- Equipment needed
- Estimated test duration
- Sequence optimization (destructive tests last)

Saves the lab engineer from researching standards manually.

### 17.2 Test Result Interpretation
When test results are uploaded (tensile strength, hardness, fatigue data), AI:
- Compares to the required specification limits
- Flags any values outside tolerance
- Generates a pass/fail recommendation with supporting evidence
- Drafts the test report conclusion section

### 17.3 Equipment Scheduling Optimization
AI optimizes the lab equipment schedule across concurrent test requests:
- Minimizes equipment idle time
- Prioritizes tests on the critical path for pending orders
- Surfaces conflicts before they cause delays

**Impact:** Accelerates the certification bottleneck — lab throughput directly determines how fast new blueprints can be activated.

---

## 18. Emergency Response (`/emergency`)

**Current state:** Fast-path ordering for critical downtime. Currently UI-only with a streamlined order form.

**AI Opportunities:**

### 18.1 Emergency Triage Assistant
When an emergency is triggered, AI immediately:
- Identifies the failed part from description (even if the operator doesn't know the exact part number)
- Checks if a certified blueprint exists
- Finds the nearest available print centre with capacity and the right certification
- Estimates time to part delivery
- Surfaces the entire recommended action in under 30 seconds

Replaces a 20-minute phone tree with an instant AI-guided response.

### 18.2 Temporary Fix vs. Full Replace Decision Support
AI assesses the failure description and recommends:
- Full replacement (print new part)
- Repair/refurbishment (65% repair rate for worn parts)
- Temporary workaround (bridge solution while full part is printed)

With estimated downtime impact for each option.

### 18.3 Incident Learning Loop
After each emergency event is resolved, AI generates an incident report:
- Root cause analysis
- Lead time performance vs. benchmark
- Recommended inventory changes to prevent recurrence

Feeds back into the Digital Inventory risk scoring.

**Impact:** Emergency response is the highest-value use case (downtime = $500K–$1M/day). Shaving 2 hours off response time with AI is worth more than almost any other improvement on the platform.

---

## 19. AM Feasibility (`/feasibility`)

**Current state:** 30-second verdict on AM suitability. Material recommendations. Appears to be partly rule-based.

**AI Opportunities:**

### 19.1 Natural Language Part Description Input
Instead of requiring structured form input, let operators describe the part in plain English:
> "It's a bracket about 15cm long, mounts on the pump housing, sees moderate vibration, currently made of stainless steel"

AI extracts the structured parameters and runs the feasibility check.

### 19.2 Multi-Material Comparison Output
Instead of one material recommendation, AI presents 3 options with a trade-off table:
| Material | Cost | Lead Time | Strength | Cert Status |
|----------|------|-----------|----------|-------------|
| 316L SS | Low | 2 days | High | DNV Active |
| Ti-6Al-4V | High | 3 days | Very High | Pending |
| Inconel 625 | Very High | 5 days | Extreme | ABS Active |

### 19.3 Feasibility Report Generation
AI generates a one-page feasibility report the operator can share with their engineering team or OEM, including the rationale, material selection, and any certification implications.

**Impact:** Reduces the biggest friction in onboarding new parts — the uncertainty about whether AM is viable.

---

## 20. Supply Chain Intelligence (`/sc_intelligence`)

**Current state:** Sovereignty dashboard, LEAN analysis, Pareto working capital optimization.

**AI Opportunities:**

### 20.1 Supply Chain Risk Narrative
AI interprets the sovereignty and LEAN data and generates a strategic briefing:
> "Your current supply chain has 73% dependency on European OEM parts with average 18-day lead times. 12 of your top 30 parts (by spend) are AM-feasible and could be sourced locally within 3–5 days. Shifting these 12 parts to AddManuChain would reduce your single-supplier exposure by 41%."

### 20.2 Working Capital Optimization Plan
AI analyzes the Pareto data and generates a phased plan:
- Phase 1 (0–3 months): Digitize the top 5 parts by inventory value
- Phase 2 (3–6 months): Move top 12 parts to on-demand printing
- Phase 3 (6–12 months): Full digital inventory transformation

With projected capital release at each phase.

### 20.3 Geopolitical Risk Monitoring
AI monitors news feeds for geopolitical events (sanctions, trade restrictions, port closures) that could affect parts in the customer's supply chain. Alerts the supply chain manager before the disruption hits their order pipeline.

**Impact:** Elevates AddManuChain from a parts ordering tool to a strategic supply chain advisor — a much stronger value proposition for C-suite conversations.

---

## 21. Digital Cooperative (`/cooperative`)

**Current state:** Shared certified blueprint pool across member facilities.

**AI Opportunities:**

### 21.1 Contribution Matching
AI identifies which parts a new member facility is most likely to need (based on their fleet profile) and surfaces matching blueprints already in the cooperative library. Accelerates time-to-value for new members.

### 21.2 Blueprint Gap Analysis
AI analyzes what the cooperative is missing based on member order history:
> "Members have placed 34 orders for parts with no existing blueprint. The top 5 undigitized parts represent 18% of total order volume. Recommend prioritizing digitization of these parts as a cooperative initiative."

### 21.3 Contribution Incentive Modeling
AI models the optimal royalty-sharing formula for cooperative blueprints to maximize total contributions while keeping access costs low. Surfaces as a recommendation to the cooperative administrator.

**Impact:** Makes the cooperative self-sustaining rather than relying on Alma-Tech to curate the library manually.

---

## 22. AI Assistant (`/ai-chat` — Claude 3.5 Haiku)

**Current state:** Floating chat widget with tool-calling (navigate, get stats, list orders/blueprints, create orders, list materials/certifications). Up to 4 agentic rounds.

**AI Opportunities:**

### 22.1 Expand Tool Coverage
Add tools for every major module:
- `get_risk_scores(threshold?)` — top at-risk parts
- `predict_stockout(material, center_id)` — days until stockout
- `route_order(blueprint_id)` — optimal print centre recommendation
- `get_emergency_options(part_description)` — emergency triage
- `generate_compliance_report(date_range, authority)` — one-click audit report
- `get_cert_renewals(days_ahead?)` — upcoming expiries

### 22.2 Role-Aware Responses
The AI assistant should behave differently based on the logged-in user's role:
- **Operator:** Focus on order status, delivery ETAs, inventory levels
- **OEM Partner:** Focus on blueprint performance, royalty analytics, approval queue
- **Cert Authority:** Focus on pending approvals, compliance status, audit log
- **Admin:** Full access, strategic KPIs, system health

Currently the assistant appears to give the same responses regardless of role.

### 22.3 Proactive Suggestions (Push, Not Just Pull)
On dashboard load, the AI assistant proactively surfaces 2–3 action items based on the user's current context:
> "Good morning. You have 3 certifications expiring in the next 30 days, 2 orders stuck in DRM approval for 5+ days, and 1 material at Critical stock level at Halifax. Want me to handle any of these?"

### 22.4 Memory Across Sessions
Use a lightweight session store to remember context across conversations:
- User's preferred print centres
- Recurring order patterns
- Last discussed issues

Prevents the user from re-explaining context every session.

**Impact:** Makes the AI assistant the primary interface for power users, reducing time spent navigating between 21 pages.

---

## 23. Cross-Cutting AI Infrastructure

These are not tied to a single page but apply across the whole platform:

### 23.1 Global Search with Natural Language
Replace or augment the missing global search with AI-powered search:
> "Show me all orders for Inconel parts at Halifax that are waiting on Cert Authority approval"

AI parses the query, hits the relevant API routes, and returns structured results.

### 23.2 Notification Intelligence
Currently notifications exist as toggles with no delivery. When implemented, AI should:
- Deduplicate related alerts (don't send 5 separate alerts for 5 certs expiring the same week)
- Prioritize by impact (a cert expiry blocking 12 active orders > a cert expiry blocking 0)
- Adapt timing (send renewal reminders 60 days out for high-complexity certs, 14 days for simple ones)

### 23.3 Automated Email Drafts
For every key event (order shipped, approval needed, cert expiring), AI generates a draft email the user can review and send in one click. Dramatically reduces email overhead for customer-facing roles.

### 23.4 Onboarding Personalization
The current `OnboardingTutorial.tsx` is static. AI can personalize it:
- Skip steps for experienced users (detected from usage patterns)
- Focus on modules most relevant to the user's role
- Surface contextual tips at the moment they're relevant (not front-loaded)

### 23.5 Row-Level Security via AI
Currently role enforcement is frontend-only. AI can assist by generating natural language explanations of why a user cannot access something, reducing support tickets:
> "This blueprint is restricted to Cert Authority review. Your current role (Operator) does not have access. Contact your admin to request access."

---

## 24. Priority Matrix

| Module | AI Impact | Implementation Effort | Do First? |
|--------|-----------|----------------------|-----------|
| Emergency Response | Extreme (downtime $500K/day) | Low | YES |
| DRM / Print Approval | High (core bottleneck) | Medium | YES |
| Certifications | High (compliance risk) | Low | YES |
| AI Assistant expansion | High (platform-wide) | Medium | YES |
| Digital Inventory | High (prevents stockouts) | Low | YES |
| Orders (smart drafting) | Medium | Low | Yes |
| Audit Logs | Medium (compliance reports) | Low | Yes |
| Analytics (narratives) | Medium (sales/investor value) | Low | Yes |
| Customer Success | Medium (scalability) | Medium | Yes |
| Blueprint Library | Medium (onboarding speed) | Medium | Later |
| Materials | Medium | Low | Later |
| Shipments | Medium | Medium | Later |
| Print Centers | Medium | Medium | Later |
| AM Feasibility | Medium | Low | Later |
| Supply Chain Intel | High (strategic value) | High | Later |
| All others | Low-Medium | Low-Medium | Later |

---

## 25. Recommended Implementation Sequence

### Phase 1 — Quick Wins (Week 1–2)
1. **Cert expiry AI narratives** — add a one-line AI summary to each expiring cert card
2. **Order anomaly detection** — pre-submission validation via Claude
3. **Audit compliance report** — one-click AI report generation from audit log
4. **AI Assistant: expand tools** — add 6 more tool functions to the existing Claude integration

### Phase 2 — Core Value (Week 3–6)
5. **Emergency triage assistant** — AI-guided response from failure description to delivery ETA
6. **DRM queue ETA prediction** — show approval timeline on each queue card
7. **Digital Inventory proactive digest** — daily risk summary on login
8. **Analytics narratives** — AI insight line per chart
9. **Customer success: churn risk + next best action**

### Phase 3 — Strategic Differentiation (Week 7–12)
10. **Blueprint auto-classification** — on upload
11. **Global natural language search**
12. **Supply chain risk narrative** — strategic advisor positioning
13. **Role-aware AI assistant**
14. **Proactive push notifications from AI assistant**

---

## 26. Notes on Implementation

- All AI features should use the existing **OpenRouter → Claude** integration already wired in `/api/ai-chat`
- For high-frequency tasks (risk score narratives, chart insights), use **Claude Haiku** for cost efficiency
- For complex reasoning (feasibility triage, compliance reports, churn prediction), use **Claude Sonnet**
- Keep humans in the loop for all consequential actions — AI recommends, humans confirm
- Add an "AI generated" label to all AI-produced content so users build appropriate trust calibration
- Log all AI recommendations and user accept/reject rates to tune over time

---

*Generated April 3, 2026 — Based on complete review of AddManuChain Platform ("Website - Ver Advanced" directory)*
