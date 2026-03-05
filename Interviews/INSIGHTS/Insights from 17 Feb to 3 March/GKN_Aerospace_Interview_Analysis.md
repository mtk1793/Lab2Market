# Interview #43 Analysis: GKN Aerospace — Matthew Erning
**Date:** February 18, 2026
**Duration:** ~35 minutes
**Format:** Virtual
**Prepared by:** Mahmoud (Michael) Kiasari

---

## INTERVIEWEE PROFILE

| Field | Detail |
|-------|--------|
| **Name** | Matthew Erning |
| **Organization** | GKN Aerospace, UK |
| **Title** | Technical Authority — Direct Energy Deposition (DED), UK |
| **Education** | BEng Mechanical Engineering, Dalhousie; PhD Materials Engineering, Dalhousie (under Dr. Paul Bishop) |
| **PhD Focus** | Industrial processing of aluminum powder metallurgy alloys |
| **Previous Roles** | Boeing Defense & Space research (blown powder DED, wear-resistant coatings for Ti landing gear); Tronosjet PEI (set up AM facility, achieved FAA PMA certification); GKN Aerospace UK (laser wire DED) |
| **AM Expertise** | Laser powder bed fusion, blown powder DED, laser wire DED |
| **Connection** | Dalhousie alumni; worked with Mark Kirby (sold Tronosjet their LPBF machines) |

---

## EXECUTIVE SUMMARY

⭐⭐⭐ **VALUABLE HONEST SKEPTIC** — Matthew provided a highly technical, candid perspective from the aerospace production side. Key takeaways: aerospace certification is fundamentally different from marine/offshore (products certified, not parts); digital inventory and on-demand AM are largely irrelevant to ongoing civilian aviation production; IP connectivity between organizations is a significant cultural and structural barrier; defense angle is the most promising for AddManuChain. He is a good long-term connection but not a near-term customer or partner.

---

## KEY INSIGHT #1: AEROSPACE CERTIFICATION — FUNDAMENTAL MISCONCEPTION CORRECTED ✅

Matthew provided the clearest aerospace certification explanation received to date. This corrects a major misconception in our pitch.

### What Is Actually Certified in Aerospace:
> **Matthew:** *"Typically, you don't have individual parts that are certified. Platforms are certified... for example, Boeing certifies the 737."*

- **Certified:** Platforms (airframes, engines) — by FAA, EASA, TCCA
- **NOT certified individually:** Parts, brackets, components
- **GKN's role:** Tier-1 supplier — they **support** OEM certification, they do not certify themselves
- **Regulators:** FAA (US), EASA (Europe), TCCA (Canada)

### AM Is NOT Treated Differently by Regulators:
> **Matthew:** *"The regulators by FAA and EASA have made it very clear that the regulations are process and material agnostic largely, and there's no special considerations that should be given to AM."*

- From a **regulatory point of view**: AM bracket = machined bracket (same compliance requirements)
- From a **means of compliance point of view**: AM requires different substantiation (no MMPDS data)
- **The real problem:** No material database equivalent to MMPDS for AM materials

### The MMPDS Gap — The Real Certification Barrier in Aerospace:
> **Matthew:** *"The problem with additive right now is those [material databases] don't exist. Where traditionally, if you were machining a bracket out of Ti-64, you go to the MMPDS, which is essentially the Bible of material performance for aerospace. You pull out Ti-64 data. It doesn't exist for additive manufacturing."*

- **MMPDS** = Metallic Materials Properties Development and Standardization (the aerospace material Bible)
- For conventional manufacturing: Pull data from MMPDS → check compliance → done
- For AM: Must generate your own material data → expensive, time-consuming, one-off
- **This is the real certification barrier in aerospace — not regulatory complexity, but lack of standardized material data**

### Strategic Implication:
- Our pitch that "certification is THE barrier" is correct — but the **mechanism** differs by industry:
  - **Marine/Offshore:** Regulatory framework not yet developed for AM (Adam Saxty confirmed)
  - **Aerospace:** Regulations exist and are AM-agnostic, but **material data doesn't exist** (MMPDS gap)
- **Do not conflate aerospace and marine/offshore certification in the pitch**

---

## KEY INSIGHT #2: DIGITAL INVENTORY / ON-DEMAND AM — NOT RELEVANT TO CIVILIAN AVIATION PRODUCTION ❌

> **Matthew:** *"From a civilian aviation ongoing production point of view, this digital inventory and on-demand processing — it's not quite as important... the production we're looking at is very well-defined. We know how many 737s are being produced a month."*

### Why Civilian Aviation Doesn't Need Digital Inventory:
- Production rates are known far in advance (Airbus A320 rate, Boeing 737 rate)
- Supply chain is planned accordingly — no "just-in-case" inventory problem
- **No emergency/unplanned demand** in the same way as offshore or naval operations
- GKN produces to schedule, not on-demand

### Where It Might Apply (Matthew's View):
- **Repair and replacement** — but this is not Matthew's focus area
- **Defense** — more potential for on-demand/unpredictable demand
- **Not civilian aviation production** — wrong market for AddManuChain's core pitch

### Strategic Implication:
- **Aerospace production ≠ target market** for digital inventory
- **Aerospace MRO (Maintenance, Repair, Overhaul)** might have potential — but different buyer
- Confirm: Is aerospace MRO a better angle than aerospace production?

---

## KEY INSIGHT #3: IP AND DATA CONNECTIVITY — MAJOR CULTURAL BARRIER IN AEROSPACE 🚨

> **Matthew:** *"Connectivity between different organizations... everybody is quite protective of their internal data, internal capability... We would never want our customers to have direct access to our data. We don't want our customers to be able to basically take our knowledge and shift it to another location."*

### The Aerospace Supply Chain Data Problem:
- Large OEMs (Airbus, Boeing) want supply chain visibility
- Tier-1 suppliers (GKN, Safran) resist direct data uplinks — IP protection
- Matthew has heard of OEMs wanting **direct uplinks to powder bed fusion machines** — GKN would resist this
- **Cultural norm:** Each tier protects its own process knowledge aggressively

### Where It Could Work:
> **Matthew:** *"Possibly a defense angle would be more suited in that, you know, if the US DoD says we want full uplink to our suppliers — Lockheed Martin — and then that's flowed down to companies like GKN aerospace... we'll just get onboard at that point."*

- **Defense mandates** can override corporate IP resistance (government customer = compliance required)
- **US DoD model:** Top-down mandate flows through supply chain
- **Canadian equivalent:** DND/PSPC procurement requirements could force connectivity

### Strategic Implication:
- **Don't try to sell AddManuChain to aerospace Tier-1 suppliers** — they will resist data sharing
- **Sell to defense procurement bodies** — they can mandate connectivity down the supply chain
- **Or sell to operators** (end users who own the parts problem) — not to manufacturers

---

## KEY INSIGHT #4: FAA PART MANUFACTURING APPROVAL (PMA) — VALIDATED PATHWAY 🎯

Matthew's Tronosjet experience is directly relevant:

> **Matthew:** *"The biggest highlight was we went through the FAA and certified a metal AM part through the Part Manufacturing Approval process through the FAA."*

- **FAA PMA** = Part Manufacturing Approval — the pathway for certifying replacement/aftermarket parts
- Matthew achieved this at Tronosjet PEI for a metal AM part
- Mark Kirby (Interview #9) also mentioned this achievement
- **This is the most relevant aerospace certification pathway for AddManuChain's use case** (replacement parts, not new production)

### What PMA Means for AddManuChain:
- PMA is for **replacement parts** — exactly what digital inventory enables
- If a part is PMA-approved for AM production, it can be reproduced without full re-certification
- **This is the aerospace equivalent of the "pre-certified parts library" concept**
- **Action:** Research FAA PMA process in detail; explore Canadian equivalent (TCCA STC/PMA)

---

## KEY INSIGHT #5: AI IN AEROSPACE — HIGH BAR, LONG TIMELINE ⚠️

> **Matthew:** *"Anything in civilian aviation — it's a very risk-averse industry. They won't start implementing things until there is a tremendous amount of confidence in what the technology is offering... To build the confidence that your AI or machine learning tool is actually going to pick up the maintenance requirements before they're having an adverse effect on the manufacturing process is a very challenging area."*

### AI Barriers in Aerospace:
- Lives at risk → extremely high confidence threshold required
- Regulatory substantiation needed before AI-driven decisions accepted
- Predictive maintenance for AM machines: "potential, but a long ways off"
- **Not a near-term market for AI-driven AM solutions**

### Strategic Implication:
- **Don't lead with AI when pitching aerospace** — it triggers risk-aversion
- Consistent with Shawn Sooley's advice: *"Don't sell AI. Sell the solution."*
- AI as a backend feature, not a headline

---

## KEY INSIGHT #6: AEROSPACE IS NOT THE BEACHHEAD — CONFIRMS OIL & GAS / DEFENSE FOCUS

Matthew's overall feedback confirms our market prioritization:

| Market | Digital Inventory Relevance | AM Certification Complexity | AI Receptivity |
|--------|---------------------------|----------------------------|----------------|
| **Civilian Aviation (Production)** | ❌ Low (planned production) | 🟡 Medium (MMPDS gap) | ❌ Low (risk-averse) |
| **Aerospace MRO** | 🟡 Medium (repair/replacement) | 🟡 Medium (PMA pathway) | 🟡 Medium |
| **Defense Aerospace** | ✅ High (unpredictable demand) | 🟡 Medium (mandate-driven) | ✅ High (DoD push) |
| **Oil & Gas Offshore** | ✅ High (remote, unplanned) | 🟡 Medium (application standards) | ✅ High |
| **Naval/Marine** | ✅ High (availability-driven) | 🔴 High (LR Rules) | ✅ High |

**Conclusion:** Civilian aviation production is the wrong market. Defense aerospace and naval are right.

---

## CONNECTIONS & REFERRALS

### Existing Connections Confirmed:
- **Dr. Paul Bishop** (Dalhousie) — Matthew's PhD supervisor; Michael has indirect connection
- **Mark Kirby** (Tronosjet/former Renishaw) — Both know Mark; Matthew sold him LPBF machines

### Referral Request Made:
- Michael asked Matthew for introductions to relevant contacts
- Matthew agreed to be contacted again for a follow-up (15-20 min) once idea is more refined
- **No specific referrals given in this meeting** — follow up when pitch is tighter

### Action:
- [ ] Follow up with Matthew in 4-6 weeks with refined pitch deck
- [ ] Ask specifically: Who in aerospace MRO or defense aerospace should I speak to?
- [ ] Ask: Any contacts at TCCA (Transport Canada) for Canadian AM certification?

---

## HYPOTHESIS VALIDATION SCORECARD

| Hypothesis | Status | Evidence |
|------------|--------|----------|
| **H1: Certification is THE barrier** | ✅ CONFIRMED (nuanced) | In aerospace: MMPDS gap, not regulatory complexity |
| **H2: AM regulations are unclear** | ❌ CHALLENGED for aerospace | FAA/EASA are process-agnostic; regulations exist, material data doesn't |
| **H3: Digital inventory relevant to aerospace** | ❌ NOT for production | Civilian aviation production is planned; MRO/defense may apply |
| **H4: AI has near-term aerospace potential** | ❌ CHALLENGED | Very risk-averse; long substantiation required |
| **H5: Defense = better market than civilian aviation** | ✅ CONFIRMED | Matthew explicitly suggested defense angle |
| **H6: IP connectivity is a barrier** | ✅ CONFIRMED | GKN would resist direct OEM data uplinks |
| **H7: FAA PMA = relevant certification pathway** | ✅ NEW INSIGHT | Matthew achieved this at Tronosjet — replacement parts pathway |

---

## STRATEGIC LESSONS LEARNED

### 1. SEPARATE AEROSPACE PRODUCTION FROM AEROSPACE MRO IN THE PITCH
- Aerospace **production** = wrong market (planned, not on-demand)
- Aerospace **MRO** = potentially right market (repair, replacement, unplanned)
- Aerospace **defense** = right market (unpredictable demand, mandate-driven connectivity)

### 2. THE MMPDS GAP IS THE REAL AEROSPACE CERTIFICATION BARRIER
Not regulatory complexity — the lack of standardized AM material data. A platform that helps build and share AM material databases (with appropriate IP protection) could be a valuable aerospace tool.

### 3. FAA PMA IS THE AEROSPACE EQUIVALENT OF PRE-CERTIFIED PARTS LIBRARY
Research this pathway. If we can help operators get PMA approval for AM replacement parts, that's a reusable certification that dramatically lowers the barrier for subsequent orders.

### 4. DON'T PITCH AI AS A HEADLINE TO AEROSPACE AUDIENCES
Consistent with Shawn Sooley's advice. Matthew confirmed: aerospace is extremely risk-averse about AI. Lead with the solution (parts availability, downtime reduction), not the technology.

### 5. DEFENSE MANDATE = THE KEY TO AEROSPACE CONNECTIVITY
Corporate IP resistance can be overridden by government mandates. If DND/PSPC or US DoD requires supply chain connectivity, Tier-1 suppliers will comply. **Sell to the government buyer, not the manufacturer.**

### 6. MATTHEW IS A LONG-TERM ASSET, NOT A NEAR-TERM LEAD
He is honest, technically deep, and well-connected (Dalhousie, Tronosjet, GKN). Follow up in 4-6 weeks with a refined pitch. He agreed to another conversation.

---

## KEY QUOTES

> *"Typically, you don't have individual parts that are certified. Platforms are certified."* — Matthew Erning

> *"The regulators by FAA and EASA have made it very clear that the regulations are process and material agnostic."* — Matthew Erning

> *"The problem with additive right now is those [material databases] don't exist."* — Matthew Erning, on the MMPDS gap

> *"We would never want our customers to have direct access to our data... that's an IP aspect."* — Matthew Erning, on supply chain connectivity

> *"Possibly a defense angle would be more suited... if the US DoD says we want full uplink to our suppliers."* — Matthew Erning

> *"To build the confidence that your AI or machine learning tool is actually going to pick up the maintenance requirements... is a very challenging area."* — Matthew Erning, on AI in aerospace

---

## ACTION ITEMS

### Immediate:
- [ ] Research **FAA PMA process** in detail — Canadian equivalent (TCCA)?
- [ ] Research **MMPDS gap** — is there an AM equivalent being developed? (AMPOWER, NIST, etc.)
- [ ] Update pitch: Separate "aerospace production" from "aerospace MRO/defense" in market slides

### Short-term (4-6 weeks):
- [ ] Follow up with Matthew Erning — refined pitch, ask for specific referrals
- [ ] Ask Matthew: Contacts at TCCA? Aerospace MRO companies? Defense aerospace buyers?
- [ ] Explore: Is aerospace MRO a viable secondary market for AddManuChain?

### Strategic:
- [ ] Develop defense mandate strategy — how to get DND/PSPC to require supply chain connectivity
- [ ] Investigate AM material database initiatives — could AddManuChain contribute to / leverage these?

---

**Rating: 7/10 — Valuable honest skeptic**

Matthew confirmed that civilian aviation production is the wrong market, clarified the real aerospace certification barrier (MMPDS gap, not regulatory complexity), validated the defense angle, and provided the FAA PMA pathway as a relevant certification model. He is a strong long-term connection and agreed to a follow-up conversation.

---
**Interview conducted by:** Mahmoud (Michael) Kiasari
**Analysis prepared:** February 18, 2026
