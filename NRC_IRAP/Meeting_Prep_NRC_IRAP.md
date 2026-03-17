# NRC IRAP Meeting Preparation — AddManuChain

**Purpose:** Present AddManuChain to NRC IRAP Industrial Technology Advisor (ITA)
**Dashboard Demo:** https://addmanuchain-dashboard.vercel.app/
**Public Website:** https://addmanuchain.vercel.app/
**Goal:** Secure ITA buy-in to advance toward a formal funding proposal

---

## MEETING OBJECTIVE

Walk the ITA through AddManuChain's:
1. Problem and market validation (90+ customer discovery interviews)
2. Platform demo — full working dashboard with 20+ modules
3. Technical development roadmap (what IRAP funding would enable)
4. Ask: ITA advocacy + next steps toward a proposal

---

## WHAT TO PRESENT

### 1. The Problem (2 min)
- Industrial operators in mining, marine, offshore energy, and defence face critical spare parts crises: long lead times (60–90 days typical), obsolete OEM parts, sole-source foreign dependencies
- When a critical machine goes down, the inability to source a part costs tens of thousands of dollars per day — sometimes production stops entirely
- Current supply chains are fragile, globalized, and entirely unfit for low-volume, high-criticality parts
- **Defence specifically (Interview 71 — DRDC Atlantic):** procurement bottlenecks in the Canadian Armed Forces are severe; no established ISO/qualification standards for AM parts exist in the defence context — AddManuChain's certification layer is the missing infrastructure
- Canada has a national sovereignty exposure: 27% of critical industrial parts sourced from foreign suppliers, with China-sourced components carrying an 87/100 geopolitical risk score in our platform's live analysis

### 2. The Solution — AddManuChain (3 min)
- A full-stack digital platform connecting industrial operators with certified additive manufacturing (AM/3D printing) service providers
- Enables on-demand production of certified spare parts — locally, quickly, traceably, and with full IP protection
- Digital thread: OEM blueprint → DRM-encrypted token → qualified facility → certified printed part → delivery → audit log
- Key platform modules (all live in demo):
  - **Emergency Response** — fast-path from breakdown to replacement, typically 4–11 hrs vs 60-day traditional procurement
  - **AM Feasibility Triage** — 30-second AI verdict on whether a part is suitable for AM, with cost comparison ($4,200 AM vs $18,400 traditional in validated examples)
  - **Supply Chain Intelligence** — sovereignty dashboard, LEAN inventory conversion analysis ($1.1M projected savings), Pareto working capital optimiser
  - **Material Properties Library** — tested AM mechanical data (the MMPDS equivalent for additive manufacturing); 12 validated alloys, 339 test coupons
  - **Digital Cooperative** — shared certified blueprint pool across member operators; 847 digital assets, 98.2% replenishment rate
  - **OEM Portal** — OEMs earn passive royalty revenue from controlled digital licensing ($284K demonstrated earnings)

**Live Demo of https://addmanuchain-dashboard.vercel.app/**
- Switch to "End User" role → Emergency Response → submit a breakdown request → show Instant Response Panel
- Switch to "Admin" role → Supply Chain Intelligence → walk the sovereignty pie chart and LEAN table
- AM Feasibility Triage → run an assessment → show cost comparison result
- Keep demo to 4–5 minutes max; know exactly which flows to show

### 3. Market Validation (2 min)
- **90+ customer discovery interviews** completed through the Lab2Market/Mitacs program
- Key segments with confirmed pain:
  - **Mining / Heavy Industry** — downtime costs $15K–$80K/day; AM lead time advantage confirmed as primary purchase driver
  - **Offshore O&G (Hibernia, Suncor, Terra Nova FPSOs)** — production-stopped emergencies, no local certified AM facility; willing to pilot
  - **Defence / Naval (DRDC Atlantic — Interview 71)** — no AM qualification standards in the DND ecosystem; new submarine procurement program (Summer 2026) is a direct opportunity; referrals provided to Cameron Monroe (Defence Construction Canada) and Allan Williams (Perseus Design)
  - **Marine / Shipping** — class society certification (DNV GL, Lloyd's Register) is the unlock; platform already integrates both
- Pain confirmed across all segments: parts obsolescence, lead time, supply chain fragility, no digital file management
- Early traction: operators signalling willingness to pilot; OEM partners interested in royalty licensing model

### 4. Technical Roadmap (2 min) — What IRAP Funds
IRAP funds **technical innovation and R&D**, not marketing. Frame the ask around:
- [ ] **Secure digital part file management** — DRM encryption, IP-protected print tokens, time-limited access control (core novel software challenge)
- [ ] **AM qualification and matching engine** — algorithm mapping part geometry + material + regulatory context to qualified facility; integrates with DNV GL, Lloyd's Register, ABS, Bureau Veritas certification frameworks
- [ ] **AI-assisted feasibility scoring** — training and validating the suitability model (geometry, material printability, regulatory burden, volume economics sub-scores)
- [ ] **Material Properties Database** — building the industry's first open AM mechanical property dataset for offshore/defence alloys; currently 12 alloys / 339 coupons; target 50+ alloys to reach class-society acceptance
- [ ] **Supply chain sovereignty analytics** — LEAN digital-conversion confidence modelling and geopolitical risk scoring engine
- [ ] **Integration with industry standards** — AS9100, ISO 9001, ASTM AM standards (F3122, F2924), DNV GL RP-0394 (AM for offshore)
- [ ] **Pilot deployment** with 1–2 industrial clients (mining or offshore O&G in Atlantic Canada preferred)

### 5. The Ask (1 min)
> "We're looking for an ITA who sees the potential here to work with us on structuring a project proposal. We want to understand what IRAP can fund in our next phase and how to align our technical milestones with IRAP's requirements. We have a working platform, 90+ validated customer interviews, and a clear R&D roadmap — we're ready to move fast."

---

## KEY MESSAGES TO HIT

| Theme | Message |
|---|---|
| Market Pull | "90+ interviews confirm real, urgent pain in mining, offshore O&G, and defence — operators are waiting for this" |
| Technical Innovation | "Novel work required in secure DRM, AM qualification algorithms, AI feasibility scoring, and a first-of-kind material properties database" |
| Canadian Sovereignty | "27% of critical industrial parts come from foreign sources — our platform directly reduces that exposure; this is a national resilience story" |
| Defence Opportunity | "DRDC Atlantic (Interview 71) confirmed no qualification standards exist for AM parts in the DND ecosystem — we are building that infrastructure" |
| Readiness | "We have a full working platform at addmanuchain-dashboard.vercel.app — 20+ modules, not just a deck" |
| Atlantic Canada Impact | "Platform designed around Atlantic Canada's offshore and defence industrial base — NRC Halifax, Dalhousie, local print centres already in the data" |

---

## ANTICIPATED IRAP QUESTIONS & YOUR ANSWERS

**Q: Is AddManuChain incorporated in Canada?**
A: [Insert current incorporation status]

**Q: What is the core technical challenge you need R&D funding for?**
A: Three interconnected challenges: (1) secure digital rights management for encrypted AM part files — a novel software engineering problem; (2) building and validating the first AM material mechanical property database for offshore/defence alloys at the scale required for class-society acceptance; and (3) developing the AI-assisted feasibility and qualification matching engine that maps part requirements to the right certified facility.

**Q: Do you have letters of support or LOIs from potential customers?**
A: We have strong verbal validation from 90+ discovery interviews. We are actively pursuing LOIs from pilot customers. From our most recent interview, DRDC Atlantic (Brian May) expressed clear interest and provided referrals to procurement decision-makers at Defence Construction Canada and Perseus Design. [Add any others you have.]

**Q: Who is on your team?**
A: [Insert team / advisors / Lab2Market mentors / NRC contacts]

**Q: What is your funding ask?**
A: We're looking to understand what's eligible first — we estimate our next phase of technical development (AM matching engine, material database, secure DRM, pilot deployment) will require approximately $[X] over [Y] months. We want the ITA's guidance on structuring the proposal to maximize eligible R&D scope.

**Q: Why is IRAP the right fit vs. other programs?**
A: IRAP's focus on technical innovation aligns perfectly with our core challenges — these are genuine R&D problems, not commercialization. The material properties database alone is a multi-year data collection and validation effort that requires structured R&D investment.

**Q: What is your revenue model?**
A: Three streams: (1) transaction fee per print order (2–5% of order value); (2) OEM royalty licensing — OEMs earn from IP they upload, AddManuChain takes a platform fee; (3) SaaS subscription for operators accessing the platform's intelligence tools (Supply Chain Intelligence, AM Feasibility, Digital Cooperative).

---

## WEBSITE DEMO CHECKLIST — Before the Meeting

- [ ] Dashboard loads cleanly on the device you're presenting from: https://addmanuchain-dashboard.vercel.app/
- [ ] Test on the network you'll be using (no VPN issues)
- [ ] Pre-load the Emergency Response page (role: End User) — know the form flow
- [ ] Pre-load the Supply Chain Intelligence page (role: Admin) — know the pie chart and LEAN table
- [ ] Pre-load AM Feasibility Triage — run through one assessment beforehand so timing feels smooth
- [ ] Have a backup: screen recording of the key flows in case of connectivity issues
- [ ] Know the 3 features to highlight — don't demo everything

---

## DOCUMENTS TO BRING / SEND IN ADVANCE

- [ ] One-page AddManuChain overview (problem, solution, market, team)
- [ ] Customer discovery summary (90+ interviews, key segments, top pain quotes)
- [ ] Technical roadmap / development milestones aligned to IRAP-eligible R&D
- [ ] Dashboard link: https://addmanuchain-dashboard.vercel.app/

---

## POST-MEETING FOLLOW-UP

Within 24 hours:
- Send thank-you email with dashboard link and one-pager attached
- Confirm next steps: proposal timeline, ITA contact for ongoing relationship
- Note any specific guidance the ITA gave on what IRAP can/cannot fund
- If ITA is interested in the defence angle, follow up with the DRDC Atlantic connection (Brian May) — he offered to vouch for the problem validation
