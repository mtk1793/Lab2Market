# Segment 3 - Labs & Authorities
## Interview Questions & Responses - Khashayar Morshed Behbahani

**Interviewee:** Khashayar Morshed Behbahani  
**Date:** January 27, 2026  
**Segment:** CS.3 - Labs, Testing Facilities, Certification Authorities  
**Interview Quality:** ⭐⭐⭐ (Good - Limited by NDA restrictions)

---

## CONTEXT QUESTIONS

### Q1: What is your lab's primary focus and who are your main clients?

**Answer:**
> "Their main job at the lab was investigating the behaviour of materials when we talk about corrosion. Their lab is working with the national defense of Canada related to the materials that they used for the ship."

**Analysis:**
- **Client:** National Defense Canada (government/military)
- **Application:** Ship materials
- **Focus:** Material behavior, specifically corrosion resistance
- **Technology:** Comparing AM (Additive Manufacturing) vs. traditional methods

**Key Insight:**  
Government/defense sector is a major client for advanced materials testing labs. High-stakes, high-value applications require rigorous certification.

---

### Q2: What is your role in the testing process?

**Answer:**
> "He is not in the making team. He is testing them with the lab instructors and will compare it with the previous versions as AM is new. They will make report for that they are working at characterization."

**Analysis:**
- **Role:** Testing and characterization (not manufacturing)
- **Team:** Works with lab instructors (academic supervisors)
- **Output:** Reports comparing AM vs. traditional methods
- **Focus:** Characterization (material properties analysis)

**Validation:**
- ✅ Confirms labs are often separate from manufacturing (H3)
- ✅ Reporting is key deliverable (supports digital compliance tool need)

---

## PROCESS & WORKFLOW QUESTIONS

### Q3: Walk me through your testing process from start to finish.

**Answer:**
> "The first they will work on the micro structure of the material that they have received or micro structure and compare it with the traditional methods to compare their changes. Then they do some corrosion test for the alloy based on its previous behaviour and current tests and they will decide about the experiment different alloys have different tests they have different destructive and non destructive."

**Detailed Process:**

**Step 1: Microstructure Analysis**
- Receive material sample
- Analyze microstructure using advanced microscopy
- Compare with traditional manufacturing methods
- Document structural differences

**Step 2: Corrosion Testing Design**
- Review alloy's previous behavior (historical data)
- Design current tests based on material properties
- Select appropriate testing methods:
  - Destructive tests (sample is destroyed)
  - Non-destructive tests (sample remains intact)
- Different alloys require different test protocols

**Step 3: Material Modification & Optimization**
> "They will do some changes to the material to see that if changes could increase or optimize the quality or no. They will do some treatment like heat processing or testing."

- Apply treatments (e.g., heat processing)
- Test if modifications improve quality
- Iterative optimization process

**Step 4: Reporting & Decision**
> "They will make the report. In the meeting supervisors will be decided to the process were good or not or just the alloy can be declined."

- Generate comprehensive report
- Present findings to supervisors
- Decision made: Accept alloy or decline
- Two main decision-makers + other industry representatives

**Analysis:**
- **Multi-stage process** → Each stage has potential for delays (communication pain point)
- **Decision-making hierarchy** → Supervisors + industry partners (multiple stakeholders)
- **Iterative nature** → No "one-size-fits-all" process

**Validation:**
- ✅ H7: Process certifications are time-consuming and require efficiency
- ✅ H14: Paper-based reporting is likely (manual reports mentioned)
- 🟡 H22: Could reduce admin time with digital workflow (partial support)

---

## PAIN POINT QUESTIONS

### Q4: What are the biggest challenges you face in your day-to-day work?

**Answer:**
> "The main challenge related is that AM are immature and main problem is about the customer service related to the devices and lack of human resources for checking the device could increase so much time. Also because of confidentiality and lack of clarity about the devices could cause problems and details are not shared."

**Challenge Breakdown:**

**Challenge #1: AM Technology Immaturity** 🔴
- Additive Manufacturing still developing
- Lack of established standards
- Unpredictable outcomes
- Requires experimental approach

**Challenge #2: Poor Customer Service for Devices** 🔴
- Equipment manufacturers don't provide adequate support
- When devices fail, fixes are slow
- Limited troubleshooting resources

**Challenge #3: Human Resource Shortage** 🔴
> "Lack of human resources for checking the device could increase so much time"

- Not enough qualified personnel to maintain/operate devices
- Device checks take excessive time due to staffing
- Specialized expertise required (hard to find)

**Challenge #4: Confidentiality Restrictions** 🔴
> "Because of confidentiality and lack of clarity about the devices could cause problems and details are not shared"

- NDA restrictions limit information sharing
- Device specifications not fully disclosed
- Harder to troubleshoot without complete documentation
- Creates information silos

**New Pain Points Discovered:**

1. **Equipment Reliability:**
   > "Since the devices are getting down and some problems are new they haven't seen before it would be hard for them to fix the device"
   
   - Devices fail with unfamiliar issues
   - No precedent for troubleshooting
   - Increases downtime

2. **Finding Qualified Personnel:**
   > "AM devices are expensive so finding the right people is hard as the materials are so sensitive"
   
   - Materials require specialized handling
   - Training time is long
   - High-stakes work (expensive materials + defense applications)

**Validation:**
- 🆕 **Equipment Status Tracking** could be valuable feature
- 🆕 **Expertise Marketplace** to find qualified operators
- ✅ H14: Lack of clarity = documentation/compliance pain

---

### Q5: How do you handle situations where you need instruments you don't have?

**Answer:**
> "At some point they will send the products while they are black box to other universities and ask them for just some tests nothing more as everything is confidential finally we do the evaluation by ourselves we only need their instruments."

**Current Workaround:**
1. Identify need for external instrument
2. Package material as "black box" (no context)
3. Send to other university
4. Request specific test only (no explanation why)
5. Receive raw data back
6. Perform evaluation internally using that data

**Analysis:**
- **Inefficient:** Physical shipping, coordination overhead
- **Confidentiality Maintained:** No context shared
- **Trust:** Evaluation done internally (don't trust external interpretation)
- **Resource Access:** Need diverse instrument set

**Potential Platform Feature:**
- **Inter-Lab Instrument Sharing Network**
  - Secure, confidentiality-preserving
  - Request tests without revealing project details
  - Fast turnaround
  - Build trust through track record

**New Hypothesis:**
> **H47 (New): Labs Need Secure Inter-Lab Collaboration Tools**  
> Hypothesis: Labs frequently need access to instruments they don't own but require secure, confidential ways to request tests without revealing proprietary project details.

---

## DECISION-MAKING & ECONOMICS QUESTIONS

### Q6: How do you decide whether to invest in new equipment or processes?

**Answer:**
> "Expensive devices and powder also so expensive as well and you should make it logical to invest on sth that you need. You have to compare it with the industry that you are working."

**Decision Framework:**

**Cost Factors:**
- **Capital:** Devices cost millions (stated earlier)
- **Materials:** AM powder is very expensive
- **Operating Costs:** Maintenance, personnel, utilities

**Decision Criteria:**
> "You should make it logical to invest on something that you need"

- **ROI Justification:** Must prove investment value
- **Industry Comparison:** Compare with what industry uses
- **Need Validation:** Only invest in what's truly necessary

**Analysis:**
- Labs face significant budget constraints
- Each investment requires rigorous justification
- Benchmarking against industry standards important

**Potential Platform Feature:**
- **Cost/ROI Analysis Tool** for AM vs. Traditional
  - Compare project economics
  - Benchmark against industry data
  - Support invest/don't invest decisions

**New Hypothesis:**
> **H48 (New): Labs Need Cost Comparison Tools**  
> Hypothesis: Labs would pay for decision support tools that help justify AM equipment investments by comparing costs, capabilities, and ROI vs. traditional manufacturing methods.

---

## TEAM & COLLABORATION QUESTIONS

### Q7: Who is on your team and how do you collaborate?

**Answer:**
> "The team are from students master phd and professors from mechanical engineering department. also they do everything from the device production and optimization of parts, characterization and everything related to the thing that industrial partner is needed also some time they will test the industrial partner products that have been produced by them in the lab."

**Team Composition:**
- **Students:** Master's and PhD level
- **Faculty:** Professors (Mechanical Engineering)
- **External:** Industrial partners (occasionally)

**Scope of Work:**
- **End-to-End Capabilities:**
  - Device production (in-house AM)
  - Part optimization
  - Characterization (material testing)
  - Testing of industrial partner products

**Collaboration Model:**
- Work with industrial partners
- Sometimes test products made by partners
- Students do hands-on work
- Professors oversee and make decisions

**Analysis:**
- **Multi-stakeholder environment:** Students, professors, industry
- **Communication Complexity:** Hierarchical (students → professors → industry)
- **Reporting Needs:** Multiple audiences with different needs

**Validation:**
- ✅ H45: Multi-Role Collaboration Workspaces would help
  - Students documenting work
  - Professors reviewing
  - Industry partners tracking progress
- ✅ Communication across hierarchy is challenge

---

## PROCESS OPTIMIZATION QUESTIONS

### Q8: Is there an "ideal" process you follow, or is it more experimental?

**Answer:**
> "There is no ideal process we use the instruments to have the best results ever it can be failured or high time scheduled we should see that if we do have feasibility of doing one thing or not but based on the parameters we can decide and we can do efforts."

**Key Insights:**

**No Standard Process:**
- Each material/project is unique
- No "cookbook" formula
- Experimental, parameter-driven approach

**Acceptance of Failure:**
> "It can be failure or high time scheduled"

- Failures expected and accepted
- Time schedules often overrun
- Part of research nature

**Feasibility Assessment Critical:**
> "We should see that if we do have feasibility of doing one thing or not"

- Before starting, assess if project is feasible
- Parameter-based decision making
- "Efforts" (trial and error) required

**Analysis:**
- **Uncertainty is inherent** → Planning tools need to account for variability
- **Time estimation is hard** → Forecasting/pipeline visibility even more valuable
- **Decision support needed** → Feasibility assessment is pain point

**Validation:**
- 🟡 H40: Demand Forecasting & Pipeline Visibility (harder for labs than manufacturing due to uncertainty)
- 🆕 **Feasibility Assessment Tools** could be valuable

**New Hypothesis:**
> **H49 (New): Labs Need Feasibility Assessment Tools**  
> Hypothesis: Labs would value tools that help assess project feasibility based on material parameters, available instruments, and historical success/failure data before committing resources.

---

## MARKET MATURITY & FUTURE OUTLOOK QUESTIONS

### Q9: How do you see AM evolving? Will it replace traditional manufacturing?

**Answer:**
> "AM devices are expensive so finding the right people is hard as the materials are so sensitive till couple of decades AM can't be replaceable that much."

**Key Insights:**

**AM is Complementary, Not Replacement (Near-Term):**
- Won't "replace" traditional for "couple of decades"
- Specialized applications only (currently)
- Not ready for mass adoption

**Barriers to Widespread Adoption:**
1. **Cost:** Devices very expensive
2. **Expertise:** Hard to find qualified operators
3. **Material Sensitivity:** Requires specialized handling
4. **Technology Maturity:** Still "immature" (mentioned earlier)

**Analysis:**
- Platform should NOT position as "AM revolution"
- Better: "Optimize hybrid workflows (AM + Traditional)"
- Target: Specialized, high-value applications first
- Expect coexistence for 20+ years

**Validation:**
- ✅ Aligns with Bassey's view (OEMs using both AM and traditional)
- ✅ Confirms market is in "early majority" for specialized use cases
- ❌ Contradicts assumption that AM will rapidly replace traditional (H8 needs reframing)

---

## FACILITIES & CAPABILITIES QUESTIONS

### Q10: Tell me about your lab's capabilities and facilities.

**Answer:**
> "The process from 0 that uses mostly by powder and they do have high end facilities in their labs worth of millions to do all of the processes there. High investment the devices are the best in the North America."

**Facilities:**
- **Equipment Value:** Millions of dollars
- **Quality:** "Best in North America"
- **Capabilities:** End-to-end (powder → finished part → testing)

**Process:**
- **Material:** Powder-based AM
- **Scope:** "From 0" (start to finish)
- **Complete Workflow:**
  - Powder handling
  - AM device operation
  - Characterization
  - Testing (destructive + non-destructive)

**Analysis:**
- High-investment labs serve as testing partners for industry
- "Best in North America" = competitive advantage
- Full-service capability = can run complete projects

**Strategic Implication:**
- Premium labs can command higher prices
- Platform could have "premium" vs. "standard" lab tiers
- Highlight unique capabilities (e.g., "only lab in North America with X")

---

## CONFIDENTIALITY & NDA QUESTIONS

### Q11: How do NDAs affect your ability to share information?

**Answer:**
> "The very first thing he told me was that because of NDAs and confidentiality he can't share that much of information with me so most of the parts were general."

**Impact of NDAs:**
- **Severely Limited Detail Sharing:**
  - Can only discuss general processes
  - Cannot share specific project details
  - Cannot disclose client information
  - Cannot reveal material specifications

- **Device Information Restricted:**
  > "Because of confidentiality and lack of clarity about the devices could cause problems and details are not shared"
  
  - Equipment specifications confidential
  - Operating parameters not disclosed
  - Makes troubleshooting harder

**Analysis:**
- This is a **structural challenge** for customer discovery in lab segment
- Cannot get specific, quantified pain points
- Limits depth of hypothesis validation
- Must adjust interview approach

**Interview Strategy Adjustment:**
- Focus on **general workflow** (not specific projects)
- Ask about **operational challenges** (not technical details)
- Target **lab managers/administrators** (not project researchers)
- Validate through **public case studies** when possible

**Validation:**
- ✅ Confirms Week 3 finding about NDA restrictions
- ✅ Justifies adjusted interview approach for CS.3

---

## SUMMARY OF KEY INSIGHTS

### Top 3 Pain Points Identified:

1. **Equipment Reliability & Maintenance** 🔴
   - Devices fail with unfamiliar problems
   - Lack of qualified maintenance personnel
   - Downtime causes cascading project delays
   - Customer service from manufacturers inadequate

2. **Confidentiality vs. Collaboration Tension** �
   - Need to protect IP while accessing external resources
   - "Black box" testing workaround is inefficient
   - Information silos make troubleshooting harder

3. **Cost Justification Complexity** 🔴
   - Every investment requires rigorous ROI analysis
   - Expensive equipment + expensive materials
   - Need to benchmark against industry alternatives

---

### New Hypotheses Generated:

**H47: Inter-Lab Secure Collaboration**
- Labs need access to instruments they don't own
- Current workaround: Ship "black box" samples
- Opportunity: Secure testing request network

**H48: Cost/ROI Decision Tools**
- Labs struggle to justify AM investments
- Need: Compare AM vs. traditional economics
- Include: Equipment, materials, time, quality trade-offs

**H49: Feasibility Assessment Tools**
- No "ideal process" exists
- Trial-and-error is costly
- Opportunity: Parameter-based feasibility prediction

---

### Hypotheses Validated:

**Strongly Supported:**
- ✅ H3: Labs Need Digital Compliance System
- ✅ H7: Process Certifications Efficiently
- ✅ H14: Paper-Based Chaos

**Partially Supported:**
- 🟡 H15: Reactive Enforcement Only
- 🟡 H22: Reduce Admin Time 60%
- 🟡 H23: Real-Time Compliance Visibility

---

### Strategic Implications:

1. **Lab Segment Requires Different Approach:**
   - NDA restrictions are real and significant
   - Focus on operational vs. technical pain points
   - Target administrators, not researchers

2. **Equipment Reliability is Underexplored:**
   - Could be major differentiator for platform
   - Status tracking, predictive maintenance features
   - Connect labs with qualified maintenance experts

3. **Inter-Lab Collaboration Opportunity:**
   - Network effect potential
   - Secure, confidential instrument sharing
   - Build trust through transaction history

4. **AM is Complementary (Decades Timeline):**
   - Don't position as "replacement" technology
   - Focus on "hybrid optimization" messaging
   - Target high-value, specialized applications

---

**Interview Date:** January 27, 2026  
**Analyzed By:** Mahmoud Kiasari  
**Segment:** CS.3 - Labs & Authorities  
**Quality:** ⭐⭐⭐ (Good - Limited by NDAs, but valuable operational insights)  
**Status:** Documented ✅
