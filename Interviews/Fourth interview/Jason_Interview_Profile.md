# Jason Power - Interview Profile

**Interviewee:** Jason Power  
**Organization:** Noble Corporation (moving to Valaris Limited as VP Business Development)  
**Current Role:** Senior leadership at Noble Corporation (Offshore Drilling)  
**Interview Date:** January 28, 2026  
**Interview Type:** In-person  
**Segment:** CS.1 - Clients (Offshore Energy Operators)

---

## Professional Background

**Current Position (as of interview):**
- Senior leadership role at Noble Corporation
- Transitioning to **Vice President of Business Development at Valaris Limited**
- Deep expertise in offshore drilling operations, supply chain, and technology adoption

**Company Context - Noble Corporation:**
- Fleet: High-specification drillships and semisubmersibles
- Operations: Ultra-deepwater and high-specification jackup drilling globally
- **Fleet Value:** $500M - $1B per vessel
- **Spare Parts Inventory Per Vessel:** $30M - $50M in physical inventory on board
- **Technology:** Uses IFS Cloud ERP with IFS.ai for maintenance and inventory optimization

**Experience:**
- Offshore drilling operations
- Supply chain management (spare parts, logistics)
- Business development
- Technology evaluation and adoption
- Relationship with major suppliers (HMH, BOP manufacturers)

---

## Critical Findings from Interview

### 🔴 FINDING #1: Risk Categorization is THE Primary Decision Factor

**Direct Quote Context:**
> "The very first thing that they would consider to work with any product or AM is that they would consider the risks like to safety or environment or other things and with that categorization they can work on spare parts that they need are associate for the critical equipment."

**Risk-Based Decision Framework:**

1. **Safety Risk Assessment**
   - Is part safety-critical? (life/death implications)
   - Environmental risk? (spill, explosion, regulatory violation)
   - Regulatory compliance? (design verification, manufacturing verification)

2. **Equipment Criticality Assessment**
   - Is equipment critical to operations?
   - What's the shutdown cost if it fails?
   - What's the lead time for replacement?

3. **Part Categorization**
   - **High-risk/critical:** Physical inventory on board (always available)
   - **Medium-risk:** Regional warehouses (fast delivery)
   - **Low-risk:** Just-in-time delivery acceptable

**Implication for AddManuChain:**
- Cannot sell AM platform without RIGOROUS risk classification system
- Must integrate with regulatory verification processes
- Risk assessment must be AUTOMATED (not manual)
- Platform must support different workflows for different risk levels

---

### 🔴 FINDING #2: Downtime Costs Justify Massive Inventory Investment

**Direct Quote Context:**
> "Because of the cost of those events makes it easy to justify to have numbers of equipments at the vessel on board just in case if they shut down. Because of the shut down could cause 500 K or 1 million dollars of cost each day."

**Economic Reality:**

| Metric | Value |
|--------|-------|
| **Vessel Value** | $500M - $1B |
| **Spare Parts Inventory (on board)** | $30M - $50M per vessel |
| **Shutdown Cost** | **$500K - $1M PER DAY** |
| **Risk Tolerance** | ZERO for high-risk parts |

**Decision Logic:**
- If shutdown risk exists → keep physical inventory (regardless of cost)
- Physical inventory is "insurance" against catastrophic downtime
- **$50M inventory cost << potential shutdown losses**

**Why This is Critical:**
- AddManuChain value prop CANNOT be "reduce inventory costs" (they won't optimize high-risk parts)
- Must focus on **low-risk parts** where inventory is burdensome but not critical
- Must reduce **lead time** for bust cycles (when budgets tighten)

---

### 🔴 FINDING #3: Predictive Maintenance is Major Focus (Lots of Effort on Repair)

**Direct Quote Context:**
> "A lot of effort would go to the predictable maintenance. They work on too much on repair."

**Current State:**
- Heavy investment in predictive maintenance systems
- Significant operational effort spent on repairs
- IoT sensors, FMECA (Failure Modes, Effects and Criticality Analysis)
- IFS.ai platform for automated work orders

**Pain Point:**
- Predictive maintenance identifies WHEN failure will occur
- But spare parts ordering is still MANUAL process
- Gap between prediction and action

**Opportunity:**
This validates **H53 (Predictive Maintenance API Integration)** from David Waldbillig interview!

Jason explicitly confirmed: **"No one in the business has accomplished that yet"** (integrating predictive maintenance + supply chain automation)

---

### 🔴 FINDING #4: Supply Chain is Complex Multi-Tier Integrator Model

**Direct Quote Context:**
> "They know manufacturers from main suppliers and vendors. They are integrators they buy from other sub vendors and put it in a package and will sell them the package. Something as simple as pump they will sell they the spare parts related to package. Even the suppliers don't manufacture them either they are gathering them from another sectors."

**Supply Chain Structure:**

```
Noble (Operator)
    ↓ buys packages from
OEMs/Integrators (HMH, NOV, Baker Hughes, Weatherford, etc.)
    ↓ assemble parts from
Sub-Vendors / Component Manufacturers
    ↓ source from
Raw Material Suppliers / Specialty Manufacturers
```

**Key Insight:**
- **Integrators (like HMH) don't manufacture** - they ASSEMBLE packages
- Even "simple" pumps are sold as complete packages with spare parts
- Components sourced from different sectors entirely

**Critical Strategic Implication:**
> "The idea of using AM goes back to the place that whether individual supplier vendors would like to use that or not so in the concept of the big industries like oil and gas and the companies work with them is not that meaningful."

**WHAT THIS MEANS:**
- Noble (end user) does NOT decide whether to use AM
- Decision is made by **INTEGRATORS** (HMH, NOV, Weatherford, etc.)
- AddManuChain must target **INTEGRATORS**, not end users!

**This is a FUNDAMENTAL PIVOT of target customer!**

---

### 🟡 FINDING #5: Boom and Bust Cycles Drive Technology Adoption

**Direct Quote Context:**
> "Options for using it is there the oil field in general goes into boom and bust cycle. In the boom cycle it doesn't matter how much the spare part cost just get them come. In the bust would be so advantageous to optimize the cost and time. By minimizing also inventory or manufacture some parts for themselves."

**Boom vs. Bust Dynamics:**

| Cycle Phase | Characteristics | Technology Interest |
|-------------|----------------|-------------------|
| **BOOM** | High oil prices, full production | "Cost doesn't matter, just get parts fast" |
| **BUST** | Low oil prices, tight budgets | "Optimize costs, reduce inventory, manufacture in-house" |

**Current Operational Philosophy:**
> "They haven't chased them very much because they tend to operate everything lean based on the boom and bust and optimizing."

**Implication:**
- Technology adoption happens in BUST cycles (when cost optimization matters)
- But purchasing power is LOW in bust cycles
- Must have value prop that works in BOTH cycles:
  - **Boom:** Speed (reduce lead time)
  - **Bust:** Cost (reduce inventory)

---

### 🔴 FINDING #6: Technology Companies Must Come to Them (Not Vice Versa)

**Direct Quote Context:**
> "Having the equipment on the board to produce those parts could take a significant effort from their side and the way the technology works is that the company should go to them and should sell them capabilities. They don't normally go for that company."

**Decision-Making Culture:**

1. **Operators (Noble) are REACTIVE, not proactive on technology**
   - Focus on core business (drilling, production)
   - Don't have capacity to evaluate new technologies
   - Don't have confidence to implement themselves

2. **Technology adoption process:**
   - Technology company approaches operator
   - Demonstrates capabilities (proof of concept)
   - Sells turnkey solution (not just concept)
   - Provides implementation support

3. **Sales Strategy:**
   > "Some idea like mine should look for them and help them to develop and implement the technology there. They don't have the capacity or confidence to do that."

**Implication for AddManuChain:**
- Must have PROACTIVE sales approach
- Must provide turnkey solutions (not just platform access)
- Must offer implementation support
- Cannot expect operators to seek you out

---

### 🔴 FINDING #7: Environmental Challenges Make On-Board AM Difficult

**Direct Quote Context:**
> "Because of very safety critical equipment mostly are regulated and they have lots of standards they have design verifications. They have manufacture verifications by the some sort of regulatory. That would be a challenge to start a 3d printing or those types of AM on board. You also have to consider the environment that you are working with considering the HVAC control and internal issues. You can easily just print out sth you have to consider environment."

**Environmental Constraints:**

**Offshore Vessel Challenges:**
1. **HVAC Control Issues**
   - Temperature fluctuations
   - Humidity (salt air)
   - Vibration from vessel movement
   - Space constraints

2. **Material Sensitivity:**
   - Plastic AM: Sensitive to temperature, humidity
   - Metal AM: Even more sensitive (powder handling, inert atmosphere)
   - Environmental control expensive on vessels

3. **Regulatory Requirements:**
   - Design verification required for safety-critical parts
   - Manufacturing verification by regulatory bodies
   - Cannot simply "print something" and use it

**Real-World Example:**
> "They do have some drill pipes that have laser cladding. They have to be considered or safe against the corrosion. Also have to have pressure control for the steams and stainless still they should also last for at least for 5 years or more."

**Implication:**
- On-board AM is NOT viable for most applications
- Regional hub model better (controlled environment)
- Must account for corrosion, pressure, longevity in part design
- Laser cladding (repair) more viable than full AM production

---

### 🟢 FINDING #8: Best Target is INTEGRATORS (Not End Users)

**Direct Quote Context:**
> "The best target for this work would be integrator the main suppliers that they have that manufacturers some parts where big industries would come back to them for the spare parts to provide. If they have the capability to reduce the lead time that is where more cost effective solution for them and then big companies."

**CRITICAL STRATEGIC PIVOT:**

**Wrong Target:** Noble Corporation (operator)  
**Right Target:** HMH, NOV, Baker Hughes, Weatherford (integrators)

**Why Integrators are Better:**

1. **Decision-Makers**
   - They decide which manufacturing methods to use
   - Operators buy packages (don't specify manufacturing method)

2. **Volume**
   - Integrators serve MANY operators (Noble + competitors)
   - One integrator partnership = access to entire industry

3. **Cost Pressure**
   - Operators press integrators for lower costs + faster lead times
   - Integrators need solutions to stay competitive

4. **Technical Capability**
   - Integrators have engineering teams (can evaluate AM)
   - Operators don't have capacity to evaluate new technologies

**Specific Company Examples Jason Mentioned:**

- **HMH** (https://www.linkedin.com/company/hmhw/)
  - Premier drilling solutions provider
  - Delivers full-service offshore and onshore drilling equipment
  - 29,379 employees, global presence (5 continents, 16 countries)
  - OEM spare parts provider (35,000+ parts catalog)
  - 24-hour delivery guarantee

- **BOP Manufacturers**
  - Companies making well controllers, blowout preventers
  - Examples: Cameron, Hydril, Shaffer, NOV, Weatherford
  - "Could be not as big as drilling side but useful"

**Jason's Exact Words:**
> "Targeting OEMs or intermediate layer would be a better option now to find market. They could be more cost effective usage rather than back to the ventures section."

**This validates David Waldbillig's insight:** Operators outsource AM to integrators/universities (don't build in-house)

---

### 🔴 FINDING #9: AI for Inventory Optimization is BIGGER Opportunity Than AM (Initially)

**Direct Quote Context:**
> "Another important thing that he mentioned is that it would be better to shift the usage of AI into this matter more like optimizing the inventory level based on the consumption and find what spare parts you need based on different factors like the delivery time. Rely on just in time delivery. Identifying the parts that could be better serve by the process. It's a separated concept and would be supporting to build a technology around of it would be way better. AI can do that better than supply chain people."

**Jason's Hierarchy of Value:**

**TIER 1 (Highest Value): AI for Inventory Optimization**
- Analyze consumption patterns
- Optimize stock levels based on:
  - Historical usage
  - Delivery times
  - Criticality
  - Boom/bust cycle phase
- Identify which parts should be:
  - On-board inventory
  - Regional warehouse
  - Just-in-time delivery
  - AM-suitable

**TIER 2: AI + AM Integration**
> "It also could be integrated with the idea of using AM by itself to make it more feasible."

- AI identifies parts suitable for AM
- AM provides fast delivery for those parts
- Combined solution stronger than either alone

**Why AI Alone is Valuable:**
- "AI can do that better than supply chain people"
- Supply chain optimization is PAIN right now
- AM adoption takes time (trust, regulatory)
- AI can show value immediately

**Strategic Implication:**
- **Don't lead with AM** → Lead with AI inventory optimization
- AM becomes a feature (not the product)
- AI proves value → opens door for AM adoption

---

### 🔴 FINDING #10: Predictive Maintenance + Supply Chain Integration = HUGE UNMET NEED

**Direct Quote Context:**
> "Other use cases is using AI ML to predict failures and very well established but needs space. Integrating that failure prediction into repairing, supply chain management and planning would be logical next step. **No one in the business has accomplished that yet** (which is a great market for me focus on this !). Everybody is looking for reducing the down time cost and AI tool for the predictive part for the maintenance and optimize the spare parts in hand an plan making not for reactive and failure could be beneficial."

**Current State:**
- **Predictive Maintenance:** ✅ Well-established (Schlumberger, C3.ai, IFS.ai)
  - Sensors predict when equipment will fail
  - "This pump will fail in 14 days"

- **Supply Chain:** ❌ Still manual
  - Human sees prediction
  - Manually orders part
  - Hopes part arrives before failure

**The Gap:**
> "Integrating that failure prediction into repairing, supply chain management and planning would be logical next step."

**What "Integrated" Means:**
1. Predictive maintenance system predicts failure
2. **Automatically** triggers spare parts order
3. **Automatically** optimizes:
   - When to order (considering lead time)
   - Where to source (on-board, warehouse, AM)
   - Who should install (schedule maintenance crew)
4. **Automatically** converts reactive repair → proactive maintenance

**Jason's Validation:**
> "No one in the business has accomplished that yet"

**THIS IS THE BIGGEST OPPORTUNITY!**

---

### 🟡 FINDING #11: AI Standalone Not Useful (Must Be Layer on Top)

**Direct Quote Context:**
> "AI stand alone could not be useful but it could be useful as the layer on the top of the AM section of supply chain or any other aspect of AddManuChain."

**Architecture Insight:**

**WRONG:**
- AI inventory optimization tool (standalone SaaS)

**RIGHT:**
- AddManuChain platform
  - AI layer (inventory optimization, predictive ordering)
  - AM layer (digital inventory, on-demand production)
  - Supply chain layer (integrators, logistics)
  - Integration layer (predictive maintenance APIs)

**Why Layered Approach:**
- AI needs data (supply chain generates data)
- AI needs action (AM provides fulfillment)
- Standalone AI = insights with no execution path
- Integrated AI = insights → automatic action

---

### 🟢 FINDING #12: Feasibility Assessment AI Most Valuable Feature

**Direct Quote Context:**
> "Feasibility matters in the AI usage for finding the threshold very quickly. Use AI to make it feasible or not?"

**Use Case:**
Customer uploads part specification → AI instantly answers:

1. **Is this part suitable for AM?**
   - Geometry complexity
   - Material requirements
   - Tolerance specifications
   - Certification requirements

2. **What's the fastest/cheapest option?**
   - Physical inventory (on-board)
   - Regional warehouse
   - Traditional manufacturing
   - AM production

3. **What's the risk level?**
   - Safety-critical?
   - Environmentally regulated?
   - Pressure-bearing?

**Value:**
- Instant decision support (vs. manual engineering analysis)
- Removes guesswork from AM adoption
- Builds confidence through transparency

---

### 🔴 FINDING #13: Regulatory Challenges Are MAJOR Barrier

**Direct Quote Context:**
> "Because of very safety critical equipment mostly are regulated and they have lots of standards they have design verifications. They have manufacture verifications by the some sort of regulatory."

**Regulatory Requirements:**

1. **Design Verification**
   - Part design must meet industry standards (API, ASME, ISO)
   - Engineering review required
   - Cannot change design without re-certification

2. **Manufacturing Verification**
   - Manufacturing process must be certified
   - Quality control at each step
   - Traceability (who made it, when, with what materials)

3. **Material Certification**
   - AM materials must meet same specs as traditional
   - Batch testing required
   - Long-term reliability data needed

4. **Equipment Exposure Regulations:**
   > "The equipment that are exposed with the environment also should be categorized inside the critical ones and they are very regulated ones and goes for the regulatory programs which is a challenge."

**Examples:**
- Drill pipes with laser cladding (corrosion protection)
- Pressure control equipment (must last 5+ years)
- Steam systems (stainless steel, high pressure)

**Implication:**
- Platform must integrate with certification bodies
- Must track regulatory compliance for each part
- Cannot bypass regulations (unlike consumer products)

---

### 🟢 FINDING #14: Jason Willing to Provide Referrals + Follow Up

**Direct Quote Context:**
> "He can connect me with some one who is managing the type of technology who can answer with. He is interested to see what I will come at the end and find if it is feasible or not and identified and my idea is worth or not."

**Relationship:**
- Jason is supportive of the research
- Willing to connect to technology managers (at Valaris? at integrators?)
- Open to future discussions as concept develops
- Wants to see feasibility results

**Next Steps:**
- Follow up after developing AI feasibility assessment tool
- Ask for introduction to:
  - HMH contacts
  - BOP manufacturer contacts
  - Other integrator contacts
- Show prototype and get feedback

---

## Summary of Key Strategic Pivots

### PIVOT #1: Target Customer

**Before:** Oil & gas operators (Noble, Shell, BP, etc.)  
**After:** Integrators/OEMs (HMH, NOV, Baker Hughes, Weatherford)

**Why:**
- Operators don't decide manufacturing methods
- Integrators are decision-makers
- One integrator = access to many operators

---

### PIVOT #2: Value Proposition

**Before:** "Reduce inventory costs with digital warehouse"  
**After:** "AI-driven inventory optimization + integrated AM for non-critical parts"

**Why:**
- Operators won't reduce inventory for critical parts (shutdown risk too high)
- AI for optimization is more valuable than AM alone
- Must prove value with AI before AM adoption

---

### PIVOT #3: Product Architecture

**Before:** AM marketplace platform  
**After:** AI-powered supply chain optimization with integrated AM layer

**Why:**
- AI standalone not useful (needs execution path)
- Predictive maintenance integration is unmet need (#1 opportunity)
- AM is enabler (not the core product)

---

### PIVOT #4: Go-To-Market Strategy

**Before:** Wait for operators to discover platform  
**After:** Proactive sales to integrators with turnkey solutions

**Why:**
- Operators are reactive (don't seek technology)
- Must approach them with proven solutions
- Must provide implementation support

---

## Hypothesis Validation

### ✅ STRONGLY SUPPORTED

**H50:** Low-Risk Part Categorization System (CRITICAL)
- Jason: "The very first thing... consider the risks"
- MUST HAVE feature for market entry

**H53:** Predictive Maintenance API Integration (TIER 1 OPPORTUNITY)
- Jason: "No one in the business has accomplished that yet"
- Biggest unmet need identified

**H46:** Transparent Pricing/Budget Pre-Qualification
- Boom/bust cycles require cost optimization tools
- Feasibility assessment AI validates this

---

### ❌ REJECTED

**H25:** Find Certified Facilities Within 48 Hours
- Wrong target (not operators)
- Operators buy from integrators (don't search for manufacturers)

**H27:** Track Every Part (QR Codes/Blockchain)
- Not mentioned as priority
- Regulatory tracking is important, but QR/blockchain not the solution

---

### 🆕 NEW HYPOTHESES GENERATED

See separate document: `New_Hypotheses_from_Jason.md`

---

## Target Company List (From Interview)

### Tier 1: Major Integrators

| Company | Product/Service | Why Target |
|---------|----------------|------------|
| **HMH** | Full-service drilling equipment, 35K+ parts catalog | Premier integrator, global presence |
| **NOV** (National Oilwell Varco) | Drilling equipment, BOP systems | Major OEM, global after-sales |
| **Baker Hughes** | Oilfield services, AM capabilities | Already doing AM (partner opportunity) |
| **Weatherford** | Pressure control, BOP systems | Key supplier to offshore operators |
| **Schlumberger** | Integrated drilling solutions, DELFI platform | Technology leader, predictive maintenance |
| **Halliburton** | Drilling services, pressure control | Major supplier |

### Tier 2: Specialized Manufacturers

| Company | Product/Service | Why Target |
|---------|----------------|------------|
| **Cameron** | BOP systems | Market leader in BOPs |
| **Hydril** | BOP equipment | Specialized supplier |
| **Shaffer** | Ram-type BOPs | Component manufacturer |

### Tier 3: Operators (Secondary Market)

| Company | Fleet Size | Why Engage |
|---------|-----------|------------|
| **Noble Corporation** | Corporate contact (Jason) | Case study, feedback |
| **Valaris Limited** | Jason moving here as VP BD | New contact |

---

## Interview Quality Assessment

**Rating:** ⭐⭐⭐⭐⭐ (EXCELLENT - Strategic Game-Changer)

**Strengths:**
- ✅ Identified correct target customer (integrators vs. operators)
- ✅ Revealed #1 unmet need (predictive maintenance + supply chain integration)
- ✅ Validated AI-first, AM-second approach
- ✅ Provided specific company targets (HMH, NOV, BOP manufacturers)
- ✅ Explained boom/bust cycle dynamics
- ✅ Clarified regulatory challenges
- ✅ Willing to provide referrals and follow-up

**Impact:**
- 🔴 **FUNDAMENTAL PIVOT of target customer** (operators → integrators)
- 🔴 **FUNDAMENTAL PIVOT of value prop** (AM marketplace → AI optimization + AM)
- 🔴 **FUNDAMENTAL PIVOT of product** (platform → AI layer + AM layer)

**Key Takeaway:**
This interview **completely changed the business model**. The insights from Jason are MORE STRATEGIC than any previous interview because they revealed:
1. WHO to sell to (integrators)
2. WHAT to sell (AI inventory optimization + AM integration)
3. WHEN to sell (proactively, with turnkey solutions)
4. HOW to differentiate (predictive maintenance integration - no one has done it)

---

**Interview Completed:** January 28, 2026  
**Analyzed By:** Mahmoud Kiasari  
**Status:** Documented ✅  
**Next Steps:** Follow up for integrator introductions, develop AI feasibility tool
