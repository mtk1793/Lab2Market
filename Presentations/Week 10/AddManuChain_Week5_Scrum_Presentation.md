# AddManuChain — Lab2Market Week 5 Scrum Presentation
**Sprint #2 Review & Sprint #3 Plan**
*12653681 Canada Inc. (ALMA TECH) | Dalhousie University | March 2026*

---

---

## SLIDE 1: COVER SLIDE

### AddManuChain
**Replacing Physical Spare Parts Stockpiles with On-Demand, Certified Digital Manufacturing**

---

**Team Members:**

| Name | Title | Role |
|---|---|---|
| Mahmoud Kiasari | CEO & Lead Researcher | PhD Candidate, Electrical Engineering, Dalhousie University — Customer Discovery, Platform Strategy, Outreach |
| Dr. Alireza Vahedi Nemani | Co-Founder & Technical Lead | AM Engineering, Platform Architecture, Industry Partnership |
| Mahya Ghaffari | Co-Founder & Operations Lead | Business Operations, Platform Development, Market Research |

**Program:** Lab2Market (Mitacs) — Dalhousie University
**Company:** 12653681 Canada Inc. (ALMA TECH) — Halifax, Nova Scotia

---

---

## SLIDE 2: BUSINESS THESIS

### Value Proposition Statement

> Mid-size industrial operators in oil & gas, maritime, naval, and utilities — organizations that cannot absorb the capital burden of massive physical spare parts inventories, yet cannot afford days of equipment downtime — face a broken, slow, and opaque spare parts procurement process. **AddManuChain** replaces physical spare parts stockpiles with a certified digital inventory platform that connects operators to qualified additive manufacturing (AM) facilities on demand, backed by a Digital Birth Certificate that provides full traceability from design file to manufactured part.

**Target Customer:** Mid-size industrial operators (oil & gas, maritime, naval, utilities, Arctic mining) — procurement managers and maintenance engineers at asset-intensive organizations where downtime costs exceed $100K/day.

**Their Problem:** Physical spare parts inventories are enormously expensive to hold, go obsolete, and still fail to prevent downtime because the right part isn't always in stock. The alternative — emergency sourcing from traditional suppliers — takes weeks and costs even more.

**Our Solution:** A digital platform that converts certified part designs into a searchable, on-demand manufacturing network. Operators find a qualified local AM facility, trigger a certified print, and receive a part in hours or days — not weeks.

**Benefit:** Eliminate the capital cost of physical inventory. Eliminate the downtime risk of slow procurement. Get a certified part, faster, cheaper, with full traceability.

---

### 🔶 How Sprint #2 Changed Our Value Proposition:

**BEFORE Sprint #2:**
We positioned AddManuChain broadly to all operators — including Tier-1 majors like ExxonMobil, CNRL, and Equinor — as the primary target customers.

**AFTER Sprint #2 (Key Pivot):**
- **Tier-1 majors have largely solved the spare parts problem** (Joy Romero/CNRL, Craig Dicken/ExxonMobil, Tyler Beatty/ExxonMobil). They carry massive inventories, have global supplier networks, and rely on helicopter logistics. They are **reference partners and credibility sources — not primary customers.**
- **Mid-size operators feel the pain acutely** and lack the infrastructure to absorb it. This is the true beachhead.
- **The pitch reframe (Cynthia Clark, Interview #66):** Stop leading with platform features and certification challenges. Lead with the question: *"If this platform existed and met all regulatory requirements — would you use it?"* Get the yes-in-principle first. Turn prospects into design partners.
- **Downtime cost — not parts cost — is the correct value framing.** Procurement managers respond to the avoided-downtime dollar figure, not the per-part savings.
- **Cross-organizational inventory duplication** (Dean Dalpe/Enbridge, Interview #64) is a major underutilized cost lever — operators are carrying duplicate inventory for identical equipment that sits across organizational boundaries and could be pooled.

---

---

## SLIDE 3: ECOSYSTEM MAP

### AddManuChain Ecosystem

> Instructions for the AI rendering this slide: Create a structured node-and-relationship diagram. Use three concentric layers: CENTER (AddManuChain Platform), MIDDLE RING (Direct Participants), OUTER RING (Enablers & Influencers). Show directional arrows between nodes to indicate information/value flow.

---

### Ecosystem Nodes & Relationships:

**CENTER — AddManuChain Platform**
- Digital part file repository
- Facility matching engine
- Digital Birth Certificate (traceability layer)
- Certification status API

---

**MIDDLE RING — Direct Participants (3 Primary Parties)**

**1. Operators (Customers)**
- Mid-size oil & gas operators
- Maritime / shipping operators (MSC, Maersk)
- Naval / defense contractors (Irving Shipbuilding, Horizon Naval Engineering)
- Utilities (Enbridge, Nova Scotia Power)
- Arctic mining operators
- *Pain:* Spare parts downtime, inventory capital cost, obsolete part availability

**2. AM Facilities (Suppliers)**
- Qualified additive manufacturing providers
- Machine shops with AM capability (e.g., Precise Design, Dartmouth NS)
- Specialist DED providers (e.g., InnsTek — Korean DED specialist, motion-compensated for shipboard use)
- Atlantic XL (Halifax)
- Assembly PEI
- *Pain:* Customer acquisition, capacity underutilization, reaching certified markets

**3. Certification Bodies (Trust Layer)**
- DNV (Det Norske Veritas)
- Lloyd's Register
- CSA Group
- *Role:* Validate part files and facilities; issue traceability documentation; their endorsement is the "permission layer" for regulated industry adoption

---

**OUTER RING — Enablers & Influencers**

- **OEMs** (provide original IP / design files; define certification requirements; key IP licensing question)
- **ERP / Supply Chain Systems** (SAP, Oracle — integration point for existing operator infrastructure)
- **Digital Inventory Platforms** (FieldNode — complementary, not competitive; potential integration)
- **Industry Associations** (Women in Supply Chain / WISC, Canada Makes, NextGen Manufacturing Canada, CME — channel and network access)
- **Government / Regulatory Bodies** (NRC-IRAP, C-NLOPB, Transport Canada, DND — funding and regulatory access)
- **Research Institutions** (Dalhousie University, NRC, AMII — AI architecture, materials R&D)
- **Procurement Professionals** (individual buyers and procurement managers — end users within operator organizations)

---

**Key Relationships (Arrows):**
- Operator → Platform: submits part request (digital file or part number lookup)
- Platform → AM Facility: sends certified job order
- AM Facility → Platform: returns completed part + quality data
- Certification Body → Platform: issues Digital Birth Certificate / validates facility credentials
- OEM → Platform: licenses digital design files (IP framework TBD)
- Platform → Operator: delivers certified part + full traceability record
- Industry Associations → Operators: channel for awareness and introductions
- Government Bodies → AM Facilities: fund certification costs (ERINL, NRC-IRAP)

---

---

## SLIDE 4: OBJECTIVES FOR SPRINT #2 | WHAT I DID TO ACHIEVE THEM

| **Objectives for Sprint #2** | **What I Did to Achieve Them** |
|---|---|
| **Hypothesis:** Tier-1 majors vs. mid-size operators — who feels the pain most acutely? | Conducted interviews with ExxonMobil (Craig Dicken, Tyler Beatty), CNRL (Joy Romero), and Enbridge (Dean Dalpe). Confirmed Tier-1 majors have solved availability; pivoted beachhead to mid-size operators. |
| **Hypothesis:** Certification is the primary adoption barrier — not technical capability | Interviewed Lloyd's Register (Adam Saxty, Dave Whitehouse), DNV, GE Aerospace/APNC (Jens Kroeger). All confirmed regulatory permission — not technical readiness — is the gating factor. Tyler Beatty's Value-Capability-Permission framework coined this pivot definitively. |
| **Hypothesis:** Supply chain associations (WISC, Canada Makes) are viable go-to-market channels | Interviewed Cynthia (Cindy) Clark (Women in Supply Chain Association, Interview #66). Confirmed WISC actively bridges industries that don't talk to each other; Cindy personally committed to making aerospace introductions (WestJet, Havelin, Lufthansa Technik Calgary). |
| **Hypothesis:** Maritime / shipping sector faces the same downtime-vs.-inventory tradeoff as oil & gas | Interviewed Andre Simha (MSC, global Chief Digital Officer). Confirmed shipboard spare parts procurement is a major pain; Pelagus 3D (on-vessel AM) already emerging as a response. |
| **Outreach plan:** Expand into new sectors beyond oil & gas | Used LinkedIn + warm referral chains. New sectors engaged: naval (Jared Newcombe / Horizon Naval Engineering), supply chain associations (Cindy Clark / WISC), commercial vehicles and manufacturing (Cindy Clark / Western Star / Daimler background). |
| **Outreach plan:** Improve response rate through referral-led introductions | Applied structured referral ask at the close of each interview. Dean Dalpe (Enbridge) referred Eashwar (IT lead). Joy Romero referred Cindy Clark. Tyler Beatty has 5 warm intros pending (including Greda Aleirum at Equinor's global AM team). |
| **Interview script update:** Reframe pitch to reduce friction with senior executives | Updated cold outreach to position as academic validation research ("100-interview discovery study, no sales intent"). Cindy Clark confirmed: lead with *"If this existed and met all requirements — would you use it?"* rather than describing current platform limitations. |

---

---

## SLIDE 5: NUMBER OF INTERVIEWS

| | **Contacted** | **Responded** | **Response Rate** | **Interviews Completed** | **Scheduled / Pending** | **Referrals Obtained** |
|---|---|---|---|---|---|---|
| **New in Sprint #2** | ~30 | ~18 | ~60% | 10 | 4 | 12 |
| **TOTAL (Cumulative)** | 250+ | 130+ | ~52% | **66** | 4 | 40+ |

**Sectors Covered (Cumulative):**
Oil & Gas · Maritime / Shipping · Naval / Defense · Aerospace · Additive Manufacturing Specialists · Certification Bodies (DNV, Lloyd's Register, CSA) · ERP / Supply Chain Systems · Government / Policy · Industry Associations · Commercial Vehicles / Heavy Equipment

**Sprint #2 New Interviews (10 completed):**
- #57 — Aker Solutions (Scott Humber + Heather Davis) — Offshore O&G, AM workflow + certification
- #58 — Fanny Charreteur — AM/aerospace supply chain
- #59 — André Simha (MSC, Chief Digital Officer) — Maritime shipping, digital supply chain
- #60 — Mikhail Gladkikh — AM specialist
- #61 — Nichelle (Assembly Studio / Assembly PEI) — AM facility operator
- #62 — [Confidential interviewee] — Supply chain systems
- #63 — Craig Dicken (ExxonMobil) — O&G procurement & AM
- #64 — Dean Dalpe (Enbridge) — O&G operations, AI in supply chain
- #65 — Jared Newcombe (Horizon Naval Engineering) — Naval shipbuilding & repair
- #66 — Cynthia (Cindy) Clark (Women in Supply Chain Association) — Cross-sector supply chain, procurement, AM adoption

---

---

## SLIDE 6: HYPOTHESIS TEST — SLIDE A

### Hypothesis: Certification Is the "Permission Layer" — Not Technology — Blocking AM Adoption in Regulated Industries

| Field | Content |
|---|---|
| **Customer Segment** | Mid-size operators and procurement managers in oil & gas, maritime, and naval industries |
| **Industry** | Oil & Gas, Maritime Shipping, Naval/Defense |
| **# of Interviews (Sprint #2)** | 8 |
| **Hypothesis** | We believe that the primary barrier to additive manufacturing adoption in regulated industrial sectors is not technical capability (AM can already produce parts at required specifications) — it is regulatory permission: the absence of a certified, traceable pathway from digital file to inspected, approved part. |
| **Status** | ✅ **VALIDATED** |

**Learnings & Insights:**

1. **Tyler Beatty (ExxonMobil, Interview #33) — "Value-Capability-Permission" Framework:** Tyler articulated the clearest synthesis of the entire 66-interview series: the industry already sees the value (downtime avoided), the technical capability already exists, but regulatory *permission* — a certified, auditable process — is the missing link. This became the organizing framework for our entire value proposition.

2. **Dave Whitehouse & Adam Saxty (Lloyd's Register, Interviews #45–46):** Confirmed that Lloyd's Register certifies *facilities and processes*, not individual parts. This means the platform's role is to connect operators to pre-certified facilities — not to certify each print job independently. A major workflow simplification vs. our original model.

3. **Scott Humber & Heather Davis (Aker Solutions, Interview #57):** Aker has a documented global AM workflow. The Canada gap: no domestic platform connects the Aker procurement decision → qualified Canadian AM facility → Lloyd's Register certification milestone. The domestic supply chain is broken specifically at the discovery + certification integration step.

4. **Cynthia Clark (WISC, Interview #66):** Validated that certification must be "designed in from day one" — operators and procurement managers in regulated industries will not adopt any tool that retrospectively tries to layer compliance on top. The Digital Birth Certificate concept resonated immediately.

5. **Jens Kroeger (GE Aerospace/APNC):** Confirmed IP protection as a parallel blocker — OEMs won't release digital files without ironclad licensing frameworks. This is now a platform-level design requirement, not an afterthought.

**Representative Quote:**
> *"The cost to add that digital application into a 3D printer would actually pay for itself quite quickly because of the value-add to the client base and the turnaround."* — Cynthia Clark (Cindy), WISC, Interview #66

> *"Design the certification in from day one."* — Cynthia Clark, paraphrasing the requirement from regulated industry procurement managers.

**Next Steps (Impact on Sprint #3):**
- Formalize the certification partner model with Lloyd's Register and DNV — move from validation conversations to partnership MOU discussions.
- Build the Digital Birth Certificate spec into the platform MVP as a non-negotiable core feature, not a Phase 2 add-on.
- Test: Would operators pay a premium for a part that comes with a pre-certified facility Digital Birth Certificate vs. a standard supplier quote?

---

---

## SLIDE 7: HYPOTHESIS TEST — SLIDE B

### Hypothesis: Mid-Size Operators — Not Tier-1 Majors — Are the True Beachhead Customer

| Field | Content |
|---|---|
| **Customer Segment** | Mid-size industrial operators in oil & gas, maritime, utilities, and naval |
| **Industry** | Oil & Gas, Utilities, Maritime, Naval/Defense |
| **# of Interviews (Sprint #2)** | 6 |
| **Hypothesis** | We believe that mid-size operators — not Tier-1 majors like ExxonMobil and CNRL — experience the most acute pain from spare parts downtime and inventory cost, because they lack the capital reserves to hold large physical stockpiles and the global supplier network to source emergency parts quickly. |
| **Status** | ✅ **VALIDATED** |

**Learnings & Insights:**

1. **Joy Romero (CNRL) — Strategic Pivot:** Joy was explicit: CNRL's scale means spare parts availability is rarely an operational crisis. They maintain massive inventories, run helicopter logistics, and have established global OEM relationships. She reframed Tier-1 majors as **reference customers and credibility anchors**, not primary buyers. The real pain is downstream, at mid-size operators.

2. **Dean Dalpe (Enbridge, Interview #64):** Enbridge operates at the boundary — large enough to have some infrastructure, but acutely aware of cross-organizational inventory duplication costs. Dean identified a specific unexplored cost lever: multiple organizations operating identical assets each carry redundant physical spare parts inventories. A supplier partnership model — shared digital inventory across organizational boundaries — could eliminate this duplication without anyone holding more physical stock.

3. **Jared Newcombe (Horizon Naval Engineering, Interview #65):** Naval repair organizations are a strong mid-size analog. Horizon works on ship repair with tight timelines, limited inventory, and high-stakes downtime costs. Jared identified *specification ambiguity* — not vendor response time — as the root cause of procurement bottlenecks in his context, pointing to a platform feature opportunity: structured part specification at the point of request, not after.

4. **Cynthia Clark (WISC, Interview #66) — Commercial Vehicle Sector Validation:** Cindy drew directly from her Daimler/Western Star dealership experience. Mid-size dealerships servicing commercial fleets faced the exact same problem: a truck down is a revenue emergency, and the response was to cannibalize other vehicles for parts. She framed it precisely: *"Their downtime was worth more than the part — so the math was easy."* This is the identical cost-of-ownership logic that drives our value proposition.

5. **Andre Simha (MSC, Interview #59):** Maritime shipping confirms the pattern at the sector level. Pelagus 3D's rise (on-vessel AM for ships) is a direct market signal that the maritime sector is actively trying to solve the at-sea/remote spare parts problem — exactly the mid-size operator pain point in a different sector context.

**Representative Quote:**
> *"If that truck was down, it couldn't do the job — that's critical. We'd always strip parts from other vehicles just to have something available to keep clients on the road."* — Cynthia Clark, WISC, Interview #66

> *"Cross-organizational inventory duplication is a major cost lever. Supplier partnership models preferred over carrying physical inventory."* — Dean Dalpe, Enbridge, Interview #64

**Next Steps (Impact on Sprint #3):**
- Develop a targeted mid-size operator persona: 500–5,000 employee organizations in O&G, maritime, naval, or utilities with field operations more than 200km from a major industrial center.
- Pilot conversation with Jared Newcombe at Horizon Naval Engineering — most immediate pilot candidate.
- Explore cross-organizational digital inventory pooling as a platform feature with Enbridge's Eashwar (IT lead, referred by Dean Dalpe).

---

---

## SLIDE 8: HYPOTHESIS TEST — SLIDE C

### Hypothesis: Industry Associations (WISC, Canada Makes) Are a Viable Go-To-Market Channel

| Field | Content |
|---|---|
| **Customer Segment** | Procurement professionals, supply chain managers, AM facilities |
| **Industry** | Cross-sector (oil & gas, aerospace, maritime, manufacturing, utilities) |
| **# of Interviews (Sprint #2)** | 2 |
| **Hypothesis** | We believe that industry associations — particularly those focused on supply chain and manufacturing (WISC, Canada Makes / Polyunity) — are an effective go-to-market channel because they bridge sectors that don't talk to each other and can generate warm introductions to procurement decision-makers at a rate that cold LinkedIn outreach cannot achieve. |
| **Status** | ✅ **VALIDATED — and upgraded to active channel** |

**Learnings & Insights:**

1. **Cynthia Clark (Women in Supply Chain / WISC, Interview #66):** Cindy validated WISC as a high-leverage channel immediately. WISC actively bridges aerospace, oil & gas, agriculture, and manufacturing — sectors that, in Cindy's own words, *"hate each other at different points"* and do not naturally share intelligence. WISC creates structured cross-sector dialogue. Critically, Cindy committed to **personally making warm introductions** to WestJet, Havelin, and Lufthansa Technik Calgary — three aerospace contacts that would have been impossible to cold-reach.

2. **Sector Siloing Confirmed as a Structural Problem:** Cindy identified that oil & gas associations in Alberta are deeply siloed — *"they only talk to themselves."* This means that sector-specific associations (O&G focused) will route you back into known contacts and close off new segments. Cross-sector associations like WISC bypass this silo.

3. **Channel Pitch Reframe (Cindy's Recommendation):** For association-sourced introductions, the most effective first question is: *"If this platform existed and met all regulatory and safety requirements — would you use it?"* This removes the objection about current limitations, gets a yes-in-principle, and converts a prospective interviewee into a co-developer with skin in the game.

4. **Mark Kirby (Canada Makes / Polyunity):** Previously validated Canada Makes as a network gateway to qualified AM facilities and government manufacturing programs. The combination of WISC (demand-side, operator and procurement contacts) and Canada Makes (supply-side, AM facility contacts) creates a two-sided channel strategy aligned with the platform's two-sided marketplace model.

**Representative Quote:**
> *"The thing is, aerospace doesn't talk to oil and gas, and oil and gas doesn't talk to agriculture. They don't know what each one is doing. WISC fixes that."* — Cynthia Clark, WISC, Interview #66

> *"When I approach these people, the ask I'm going to use is: 'If this was available and all the issues were met — would you be interested in using it?' That's the first question."* — Cynthia Clark, WISC, Interview #66

**Next Steps (Impact on Sprint #3):**
- Follow up with Cindy Clark to confirm aerospace introductions (WestJet, Havelin, Lufthansa Technik Calgary).
- Explore formal partnership or co-marketing arrangement with WISC — speaking slot at a chapter event, or platform listing with WISC network.
- Engage NextGen Manufacturing Canada (recommended by Cindy) as a third association channel.
- Test whether WISC channel generates higher-quality interviews than cold LinkedIn outreach (track: response rate, referral rate, conversion to pilot interest).

---

---

## SLIDE 9: UPDATED BUSINESS MODEL CANVAS
**Name:** AddManuChain | **Iteration #:** 3

---

| **KEY PARTNERS** | **KEY ACTIVITIES** | **VALUE PROPOSITION** | **CUSTOMER RELATIONSHIPS** | **CUSTOMER SEGMENTS** |
|---|---|---|---|---|
| • Lloyd's Register, DNV, CSA (certification bodies) | • Platform development & maintenance | **For Operators:** Eliminate the capital cost of physical spare parts inventory. Get certified parts on demand, faster and cheaper than emergency sourcing, with full traceability. | • Self-serve digital platform (part search + order) | • **PRIMARY:** Mid-size industrial operators — oil & gas, maritime, naval, utilities, Arctic mining |
| • AM facilities (Atlantic XL, Assembly PEI, Precise Design, InnsTek) | • Customer discovery & market development | **For AM Facilities:** Get pre-qualified, certified client jobs without spending on customer acquisition. Fill idle capacity with high-margin certified work. | • Dedicated onboarding for AM facilities | • **SECONDARY (reference):** Tier-1 majors (ExxonMobil, CNRL, Enbridge) — for credibility and introductions |
| • InnsTek (DED specialist, motion-compensation for shipboard AM) | • Certification pathway integration (facility pre-qualification) | **🔶 UPDATED (Sprint #2):** Platform value is *downtime avoided*, not parts cost saved. Mid-size operators, not Tier-1 majors, are the primary buyers. | • Account management for key operator accounts | • Procurement managers & maintenance engineers within operator organizations |
| • OEMs (IP licensing framework — in development) | • Outreach & interview-driven iteration | | • Association channel (WISC, Canada Makes, NextGen Manufacturing Canada) | • Naval & defense repair organizations (Horizon Naval Engineering, Irving Shipbuilding) |
| • WISC, Canada Makes, NextGen Manufacturing Canada (channels) | • Digital Birth Certificate issuance & traceability | | | • Commercial vehicle dealer networks (validated by Cindy Clark / Western Star analogy) |
| • NRC-IRAP (funding) | | | | |

---

| **KEY RESOURCES** | | | **CHANNELS** | |
|---|---|---|---|---|
| • Digital part file repository (certified design files) | | | • Direct outreach (LinkedIn + warm referral chains) | |
| • Certification body partnerships (DNV, LR) | | | • Industry associations: WISC, Canada Makes, NextGen Manufacturing Canada | |
| • AM facility network (qualified, pre-certified providers) | | | • Conference & event presence (Canada Makes Summit, offshore energy events) | |
| • Additive manufacturing technical expertise (Dr. Nemani) | | | • **🔶 UPDATED (Sprint #2):** Cross-sector associations (WISC) proven more effective than sector-specific O&G associations | |
| • Platform software (hosted on Vercel — addmanuchain.vercel.app) | | | • Warm referrals from senior executive interviews (Tyler Beatty → 5 intros; Cindy Clark → 3 aerospace intros) | |

---

| **COST STRUCTURE** | | **REVENUE STREAMS** | |
|---|---|---|---|
| Platform development & hosting | | Transaction fee (% of part order value) — per certified print job | |
| Certification partnership integration | | Subscription (AM facilities) — monthly access to certified client jobs | |
| Customer discovery (ongoing) | | SaaS (operators) — digital inventory management + on-demand sourcing | |
| Sales & business development | | **🔶 UPDATED (Sprint #2):** Potential new revenue stream — AI-powered parts normalization / inventory deduplication (validated by Cindy Clark as an unmet high-value use case) | |
| IP licensing framework development | | Compliance-as-a-Service (supply chain traceability legislation — emerging regulatory tailwind identified by Cindy Clark) | |

---

---

## SLIDE 10: PLAN FOR SPRINT #3

| **Hypothesis** | **Stakeholder to Interview** | **Key Questions to Ask** |
|---|---|---|
| Mid-size operators will pay a platform fee (SaaS or transaction) for on-demand certified parts — pricing model validation | 3–4 procurement managers or maintenance leads at mid-size operators (500–5,000 employees) in O&G, utilities, maritime | "What is the daily downtime cost for your most critical equipment?" / "What do you currently spend on emergency spare parts sourcing?" / "Would you pay [X] per month for a verified certified supplier directory?" / "Would you pay a transaction fee per certified print job?" |
| Jared Newcombe (Horizon Naval Engineering) is a viable pilot partner — pilot feasibility test | Jared Newcombe + Horizon Naval Engineering team | "What would a 3-month pilot look like in your organization?" / "Which part types would you want to test first?" / "Who needs to approve a pilot internally?" / "What does success look like in 90 days?" |
| Aerospace procurement managers (WestJet, Havelin, Lufthansa Technik Calgary) face the same spare parts downtime pain as oil & gas | WestJet procurement, Havelin, Lufthansa Technik Calgary (via Cindy Clark warm introductions) | "What is your current process for sourcing hard-to-find or obsolete aircraft parts?" / "What is the average lead time?" / "What would certified on-demand AM manufacturing mean for your MRO operation?" |
| AI-powered parts normalization (the "Tomato Problem" — deduplicating multi-source inventory records) is an unmet, high-value use case | ERP/Supply chain leads at mid-size operators (Eashwar at Enbridge, referred by Dean Dalpe, is first target) | "How many different part descriptions do you have for the same physical component across your systems?" / "What does it cost you to rationalize your parts database?" / "Would you pay for an AI tool that normalized your inventory records?" |
| Supply chain traceability legislation (Canada's forced/child labor supply chain laws) creates a compliance tailwind for AddManuChain's Digital Birth Certificate | Policy / compliance leads at manufacturing-sector companies; government trade compliance contacts | "Are you currently tracking your supply chain for forced labor / child labor compliance?" / "What documentation do you need to demonstrate supply chain transparency?" / "Would a Digital Birth Certificate that traces a part from file to certified manufacturer satisfy your compliance requirement?" |
| WISC and NextGen Manufacturing Canada can generate higher-quality introductions than cold LinkedIn outreach (channel comparison hypothesis) | NextGen Manufacturing Canada contacts (per Cindy Clark recommendation) | "Who in your network is responsible for spare parts procurement or maintenance engineering?" / "Would you be open to introducing us to [specific role]?" — Track: response rate vs. cold outreach response rate |

---

### Sprint #3 Outreach Priority Queue:

**Immediate (this week):**
1. Cindy Clark follow-up — confirm aerospace introductions (WestJet, Havelin, Lufthansa Technik Calgary)
2. Tyler Beatty (ExxonMobil) — 5 pending warm introductions overdue, including Greda Aleirum (Equinor global AM team)
3. Eashwar (Enbridge IT lead — referred by Dean Dalpe) — AI/data integration angle
4. Jared Newcombe (Horizon Naval Engineering) — pilot conversation

**Short-term (next 2 weeks):**
5. NextGen Manufacturing Canada — intro via Cindy Clark
6. Aaron Plamondon (Irving Shipbuilding) — Navy AM decision timeline is time-sensitive
7. Haakon Ellekjaer (Pelagus 3D) — maritime on-vessel AM; validate overlap/partnership
8. Lee Vessey (Thales/AOPS) — re-engage; Precise Design intro pathway

**Ongoing:**
9. NRC-IRAP conversation (Gina Funicelli) — funding pathway for certification costs
10. Research forced labor / supply chain traceability legislation → develop compliance VP addition

---

*Presentation prepared for Lab2Market (Mitacs) Week 5 Scrum | March 2026*
*AddManuChain | 12653681 Canada Inc. (ALMA TECH) | Halifax, Nova Scotia*
