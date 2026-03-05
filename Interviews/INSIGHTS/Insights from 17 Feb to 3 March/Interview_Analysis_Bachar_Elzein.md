# Interview #50 — Analysis (Part 1 of 2)
## Bachar Elzein — CEO & CTO, Reaction Dynamics
**Date:** February 20, 2026
**Duration:** ~15 minutes (reschedule planned for full conversation)
**Conducted by:** Mahmoud (Michael) Kiasari
**Referral Source:** Mr. Gwanim (mentioned in transcript)

---

## INTERVIEWEE PROFILE

| Field | Detail |
|-------|--------|
| **Name** | Bachar Elzein |
| **Role** | CEO & CTO |
| **Company** | Reaction Dynamics (Montreal) |
| **Sector** | Commercial Space Launch — Hybrid Rocket Propulsion |
| **AM Use** | Very extensive in-house use of metal 3D printing for rocket engines |
| **Speaker** | Speaker 1 |

---

## CONTEXT

This was a brief 15-minute call because Bachar had a hiring interview pop up. He agreed to a reschedule in ~2 weeks for a fuller conversation. Despite the short duration, the insights are **exceptional** — Bachar is one of the most experienced AM practitioners interviewed so far, running a real rocket company using AM for its core product.

---

## KEY INSIGHTS

### 🔑 Insight #1 — Space/Rockets and Aviation Are Completely Different Markets
This is the most important market-calibration insight from this interview:

> *"An airplane has to live 40 years. A rocket has to live 4 minutes. An airplane will be carrying people. A rocket is carrying satellites or trash."*

**Implication for AddManuChain:**
- **Aviation (GKN, Boeing, Airbus):** They said they don't trust AM for critical parts. Correct — because FAA certification for 40-year life cycles is extraordinarily difficult. This is NOT our market for critical structural parts.
- **Space/Rockets:** AM is already standard, trusted, and table stakes. One rocket every 2 weeks = "mass production" in their world. This IS a viable market.
- **Offshore/Naval:** Sits between these two extremes — more like rockets (short-lifespan, lower volume, critical parts need replacement) than like commercial aviation.

---

### 🔑 Insight #2 — AM Collapsed a 30–40-Part Engine to 3 Parts
This is one of the most powerful AM value propositions ever stated in our interviews:

> *"My rocket engine with conventional methods would have maybe 30–40 parts. Because we leverage additive manufacturing a lot, and because we're using a propulsion technology conducive to AM — we only have 3 parts. A typical rocket engine has 500 to 5,000 parts. Ours has 3."*

**Why this matters for AddManuChain:**
The AM consolidation effect (merging multiple parts into one print) is an argument for WHY operators and designers would want to put their designs onto our platform. An OEM that designs an AM-native version of a complex sub-assembly creates a defensible, platform-exclusive digital asset. This is a new product line for them, not just a digital copy of an existing part.

---

### 🔑 Insight #3 — "Trust Nobody, Test Everything" Is the AM Certification Philosophy
Bachar articulated the ONLY defensible way to use AM in safety-critical applications:

> *"We buy valves from suppliers. They tell us it's rated to 1,000 psi. We say 'thank you, f*** off' and we rate it ourselves to 2,000–3,000 psi."*

> *"We found mistakes in the data sheet provided by the printer manufacturer — mistakes shared with 60 other companies. We had to correct their data sheet because we tested it ourselves."*

**Implication for AddManuChain:** Our certification layer = this. Our platform doesn't just rely on OEM specs. The pre-certification process (working with Lloyd's Register, running test coupons alongside every part) is exactly the "trust nobody, test everything" philosophy — but done once, stored in the library, and available to every buyer.

This is actually a **credibility argument**: *"We built the test regime into the platform so you never have to trust the spec sheet again."*

---

### 🔑 Insight #4 — Outsourcing AM Is a Dangerous Business Risk (6 Weeks → 6 Months)
Bachar shared a critical war story about outsourcing their AM to someone else:

> *"We made the very first engine with a supplier using an EOS machine. It was supposed to take 6 weeks. We ended up needing 6 months because they had a hard time printing the parts — they dropped it, had to redo it again, it was complex for them."*

> *"6 months when you're a startup is very, very precious time. You can kill the company with this."*

**Solution:** They bought their own printer with government funding, gaining control over the scheduling.

**What this means for AddManuChain:** This story is actually a strong argument FOR our platform's value to startups and scale-ups who can't afford to own a printer. The alternative is outsourcing and getting burned. AddManuChain offers **vetted, LR-pre-certified facilities** where the printer operator already knows what they're doing — reducing the risk of the 6-week-to-6-month failure mode.

**BUT** — for Reaction Dynamics specifically, they no longer need us. They own their printer, have mastered it, and operate it better than the manufacturer documented. They are the "Builder node," not a "Buyer node."

---

### 🔑 Insight #5 — Government AM Funding Works (They Got It, You Should Too)
Bachar mentioned that they received government funding to buy their own printer:

> *"We applied for funding with the government and we were successful in securing it and we bought our printer."*

**Implication:** Canadian government AM funding (IRAP, NRC-IRAP, NSERC, ISED) is accessible and real. Bachar's experience de-risks the path for AddManuChain to help customers acquire their first on-site 3D printer as part of a pilot program.

---

### 🔑 Insight #6 — AM for Repair (Deposition) Is a Separate Question
Near the end, Michael asked about using printers for repair, not just producing new parts. Bachar started to answer but they ran out of time. This is a key question to **reserve for Part 2**:

- Directed Energy Deposition (DED) printers can add material to worn parts, effectively "reprinting" worn surfaces
- This could be incredibly valuable for aging offshore and naval equipment
- Bachar has direct experience with this use case — follow up in Part 2

---

## HYPOTHESIS TESTING RESULTS

| Hypothesis | Result | Evidence |
|-----------|--------|----------|
| AM is trusted in aerospace | ⚠️ DEPENDS — Yes in space/rockets, No in commercial aviation | Bachar's explicit breakdown |
| Volume constraint makes AM viable | ✅ CONFIRMED — "1 rocket every 2 weeks is mass production" | Direct quote |
| Certification is handled by testing, not trust | ✅ CONFIRMED — "Trust nobody, test everything" | EOS data sheet correction story |
| Outsourcing AM without pre-qualification is risky | ✅ CONFIRMED — 6 weeks → 6 months failure | War story |
| Government funding for AM is accessible | ✅ CONFIRMED | Bachar's printer purchase |
| AM reduces part count (consolidation) | ✅ CONFIRMED — 30-40 parts → 3 parts | Rocket engine case study |

---

## BACHAR'S POSITION IN THE THREE-NODE MODEL

| Node | Bachar's Role |
|------|--------------|
| **Designer** | ✅ Yes — designs proprietary AM-native rocket components |
| **Builder** | ✅ Yes — owns and operates their own AM printer (EOS + unique printer) |
| **Buyer** | ❌ No — they don't need the platform for their current use case |

**Conclusion:** Bachar is a **potential ecosystem partner** (their AM expertise could make them a certified Builder node for other customers on the platform) but NOT a direct Buyer. The question for Part 2: *"Would Reaction Dynamics ever consider offering their AM facility capacity to other sectors between rocket builds?"*

---

## QUESTIONS TO ASK IN PART 2

1. **Repair by AM deposition:** *"Do you use your printer not just to make new parts but to repair existing worn parts? How does that work in practice?"*

2. **Spare parts for rockets:** *"When Reaction Dynamics needs a replacement component for your own rocket (ground handling, launch infrastructure, test stand) — what does that sourcing process look like? Do you ever print your own replacements?"*

3. **Platform curiosity:** *"We're building a platform where certified AM facilities can offer their capacity to other industries. Would Reaction Dynamics ever consider offering your printer time to other Canadian industries between your own production runs?"*

4. **Defense angle:** *"You mentioned Canada's Defence Industrial Strategy. How do you see Reaction Dynamics fitting into that? And where does AM fit into Canada's sovereignty argument for space launch?"*

5. **The DND document Dwayne Hopkins shared:** *"The DND released a document this week calling for 'Advanced sovereign and scalable production methods to optimize system performance through supply chain resilience.' Does that language match what you're hearing in your defense conversations?"*

---

## ACTION ITEMS

| # | Action | Priority |
|---|--------|----------|
| 1 | **Schedule Part 2 call with Bachar** (~2 weeks, per his offer) | 🔴 URGENT |
| 2 | Prepare the 5 Part 2 questions above | 🟡 Before the call |
| 3 | Send a thank-you email referencing his "3-part engine" insight — this shows you were listening | 🟡 This week |
| 4 | Research Reaction Dynamics' funding history (IRAP/NRC) to understand which program worked for them | 🟢 Background |
| 5 | Add Bachar Elzein to CRM; tag as: Designer, Builder, Aerospace, Defense, Space, Montreal | 🟡 This week |

---

## BEST QUOTES FROM THIS INTERVIEW

> *"A rocket has to live 4 minutes. An airplane has to live 40 years."*

> *"A typical rocket engine has 500 to 5,000 parts. Ours has 3."*

> *"We say 'thank you, f*** off' and we test it ourselves to 3,000 psi."*

> *"We found mistakes in the data sheet that was shared with 60 companies — and they had to correct it."*

> *"6 months when you're a startup can kill the company."*

---

*Interview #50 (Part 1 of 2) | AddManuChain | Lab2Market Oceans Program 2026*
*Transcript: `transcript_part1.md`*
