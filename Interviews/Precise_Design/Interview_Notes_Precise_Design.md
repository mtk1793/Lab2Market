# Interview: Precise Design Meeting - Digital Inventory & Additive Manufacturing Solution

**Date:** May 2026 (Approximate)  
**Participants:** 
- Dr. Ali (Dalhousie University - Project Lead, Materials Engineering, PhD Additive Manufacturing)
- Mahmoud (Lab2Market Entrepreneur in Residence)
- Alan Williams (Precise Design - Business Development)
- Brennan (Precise Design - Recent Mechanical Engineering Graduate)
- Technical Facilitator

**Location:** Virtual Meeting (Teams/Video Conference)

**Duration:** ~62 minutes

---

## Executive Summary

This meeting introduced Precise Design, a full-service design engineering, machining, and manufacturing company in the Maritimes, to a digital inventory software platform being developed at Dalhousie University. The software aims to facilitate adoption of additive manufacturing (3D printing) for critical spare parts, with particular focus on supply chain resilience in industries like oil & gas, marine, and defense. The meeting generated strong interest from Precise Design, with explicit discussion of a potential Phase 2 collaboration with Tallis/Canadian Navy to operationalize the solution.

---

## Company Backgrounds

### Precise Design (Canada)
**Key Details:**
- Full-service design engineering, machining, fabrication, and manufacturing company
- Small-to-medium enterprise (SME) with 5 sites throughout the Maritimes
- Founded ~20 years ago
- **Capabilities:**
  - 33-34 CNC machines with robotic 7-axis capabilities
  - Ability to machine parts from titanium, stainless steel, and other materials
  - Prototype design through certified production capability
  - High-volume production capacity
  - Both equipment design and manufacturing execution

**Notable Projects:**
- Universal charging station for soldier system (partnership with US-based company with Department of Defense contract)
- Active participant in Tallis Challenge for additive manufacturing framework development (6-month project, pursuing Phase 2)
- Proposed partnership with Tronos Jet (PEI-based company with significant 3D metal printing capability for aerospace)

**Key Personnel:**
- Alan Williams - Business Development (primary contact)
- Brennan - Recent mechanical engineering graduate, newly hired
- Bruce - President (20+ years with company)

### Dalhousie University - Digital Inventory Software Team
**Project Lead:** Dr. Ali
**Background:** 
- PhD in Additive Manufacturing from Dalhousie
- Completed PhD in 2022
- Background in materials engineering and welding technology

**Technical Advisors:**
- Dr. Laser - PhD Supervisor
- Dr. Roman Ali - Thesis Supervisor
- Other team members: Mahmoud (Electrical Engineering), Mathews (Mechanical Engineering), Pierce (PhD Candidate)

**Support Network:**
- Dalhousie University resources
- Lab2Market program (startup acceleration)
- Dr. Paul Bishop (Mechanical Engineering Department, Dalhousie)
- Academic partnerships with industry

---

## Core Problem Statement

### Supply Chain Resilience Challenges
The software addresses critical supply chain bottlenecks in industries with remote operations, extended lead times, and high downtime costs:

**Specific Examples Cited:**
1. **Oil & Gas (Offshore):** Spare parts access requires either:
   - Helicopter delivery: Fast but expensive, limited cargo capacity
   - Supply vessels: Cheaper but slow delivery (weeks/months)
   - Result: Critical equipment shutdowns due to small part failures

2. **Marine/Navy Operations:** 
   - Parts for aging submarines that are out of production
   - Lead times of months to years for OEM parts
   - Federal procurement constraints and IP security requirements
   - Downtime costs exceeding $1 million+ per vessel

3. **Aviation/Aerospace:** 
   - US and China already implementing on-site 3D printing solutions
   - Europe ahead of curve with additive manufacturing infrastructure
   - Canada lagging significantly behind

**Quantified Impact:**
- Oil & Gas industry: Up to $88 million in annual downtime costs
- Spare parts inventory sitting unused: 80% of physical inventory worth $4.5 billion never used
- Critical downtime example: $500 part caused entire operation shutdown; needed helicopter delivery of safety handle

---

## The Solution: Digital Inventory Platform

### Core Concept
**Shift from "Just-in-Case" to "Just-in-Time" Philosophy**

Replace physical spare parts inventory with:
1. Digital inventory of part designs
2. On-site or nearby 3D printing capability
3. Software platform connecting all ecosystem participants
4. Real-time part requests and production

**Analogy Provided:**
"20 years ago, if you wanted to print a paper page, you went to a printing center. Today, everyone has a printer at home. Eventually, all equipment users will have on-site 3D printers and print their own parts, with some specialty printing handled by external facilities."

### Software Architecture & Ecosystem

**Key Entities Connected by Platform:**
1. **End Users (Equipment Operators)** - Oil & gas, Navy, marine operations
   - Access digital parts library
   - Request parts when needed
   - Submit printing requests
   - Either print on-site or receive from nearest facility

2. **Original Equipment Manufacturers (OEMs)** - Caterpillar, Komatsu, etc.
   - Upload digital part designs to platform
   - Receive revenue from digital part licensing
   - Maintain IP protection through controlled access
   - Keep existing physical spare parts business model

3. **3D Printing Facilities/Job Shops**
   - Identified by software based on proximity
   - Handle overflow parts beyond user's in-house capability
   - Provide fastest delivery option to end users

4. **Certification Authorities** - Standards bodies, regulatory agencies
   - Verify all designs meet safety standards
   - Certify raw materials used
   - Certify machines and technicians
   - Ensure compliance throughout supply chain

5. **Digital Inventory Software (Core Platform)**
   - Manages all ecosystem interactions
   - Enforces IP protection (single-use CAD file release)
   - Coordinates printing requests
   - Tracks certifications and compliance
   - Routes to most efficient printing source

### IP Protection Mechanism
**Unique approach to handle OEM concerns:**
- OEMs maintain control of digital designs
- Software releases CAD files for **single-use printing only**
- After printing, design file disappears
- No permanent IP exposure
- OEMs compensated for each digital part access
- Creates new revenue stream without disrupting existing business

### Benefits Quantified

**For End Users:**
- Reduced downtime from weeks/months to days/hours
- Eliminated massive spare parts warehousing costs
- Flexibility in design changes as needs evolve
- Can repair/modify existing parts rather than replace
- Reduced transportation costs when printing on-site

**For OEMs:**
- New digital licensing revenue stream
- Maintains existing physical parts business
- No threat to vendor relationships
- IP fully protected through platform mechanisms

**For Supply Chain:**
- Reduced transportation and logistics costs
- Eliminated waste from obsolete parts sitting in warehouses
- More agile response to equipment failures

---

## Current Development Stage

### MVP (Minimum Viable Product) Status
- **Development stage:** Proof of concept with MVP prototype
- **Not yet operational:** No real companies currently connected to platform
- **Demo capability:** Local server with sample data to demonstrate functionality
- **Status:** Can show how system works, but not production-ready

### Technology Platform
- Web-based software with user authentication
- Separate portals for different user types (end users, OEMs, printers, certification)
- Cloud/server-based with centralized management
- Single-use CAD file release mechanism (core IP protection)

### Team and Timeline
- Current core team: 2-3 developers
- Development phase requires expansion of team
- Estimated timeline: 6-12 months for production-ready software (dependent on funding)
- Need: Software engineers, cybersecurity specialists, infrastructure support

---

## Precise Design's Interest & Positioning

### Why Precise Design Fits
1. **Existing Tallis collaboration** - Currently in Phase 1 of AM framework development for Navy
2. **No 3D printing in-house** - Complements Tronos Jet partnership (PEI-based company with aerospace-certified metal printing)
3. **Manufacturing expertise** - Can support operationalization and validation
4. **Academic connection** - Established relationship with Dalhousie (Dr. Paul Bishop)
5. **Government contract exposure** - Active in Navy and defense procurement

### Potential Phase 2 Opportunity

**Alan Williams' Vision for Phase 2:**
Precise Design could position this within their Tallis Phase 2 proposal as:
1. **AM Framework operationalization tool** - Use software to implement the AM framework developed in Phase 1
2. **Supply chain optimization** - Tailored specifically for Tallis Navy supply operations
3. **Education component** - Training Tallis personnel, PMs, supply chain staff on identifying parts suitable for AM
4. **Collaborative model:** 
   - Precise Design (manufacturing/design expertise)
   - Tronos Jet (3D printing capability)
   - Dalhousie University (academic partnership, 9x ITB credits multiplier)
   - Lead contractor for Phase 2 proposal to Tallis/Navy

**Proposed Arrangement:**
- Tailored software specifically for Tallis supply chain management
- Tallis warehouse inventory analysis to identify candidates for AM vs. physical stock
- Integration with existing Navy procurement and supply processes
- Potential funding: "6 months and a million bucks" ballpark (Alan's experience reference)

---

## Key Concerns & Barriers Raised

### 1. IP Security & OEM Trust
**Precise Design's Concern:** 
- Industry majors (Caterpillar, Komatsu) make significant margins on spare parts
- They control parts supply to maintain customer lock-in
- Reluctance to share designs with any external software platform
- Previous experience with software like "SelectAM" - OEMs unwilling to participate without absolute certainty of IP protection

**Response from Team:**
- Current focus: Start with Navy and obsolete parts (no OEM IP issues)
- Reverse engineering approach for out-of-production parts
- Build trust with smaller use cases before approaching major OEMs
- Tailor software for specific client needs (build trust through success)

### 2. Certification & Compliance
**Challenge Identified:**
- 3D printed parts must meet same standards as traditional parts
- Heat treatment, metallurgical properties, surface treatments must be verified
- Complex certification chain needed (materials, machines, technicians, processes)
- Regulatory approval from aviation, maritime, defense authorities

**Current Status:** Being addressed but not fully resolved

### 3. Liability & Warranty Chain
**Question Posed:**
- Who bears liability if 3D printed part fails during operation?
- Complex when part goes into OEM-warranted equipment
- Multiple parties involved: OEM, software provider, printing facility, certification body
- Must be legally resolved before implementation

**Current Status:** Framework needed but not yet finalized

### 4. Operational Usability
**Concern:**
- Workforce capability: Are specialized mechanical engineers needed to operate printers?
- Or is it truly plug-and-play simple?
- Total cost of ownership must include training/staffing
- Applies across global operations (South America, Chile, Brazil, Africa, Alaska)

**Response:** Could be customized based on client needs

### 5. OEM Market Resistance
**Challenge:**
- Industry suppliers profit primarily from spare parts, not equipment sales
- On-demand printing threatens their recurring revenue model
- Risk of vendor pushback or refusal to collaborate
- Need to create value proposition that addresses vendor concerns

**Strategy:** Inclusion in ecosystem with new revenue streams rather than disruption

---

## Discussions & Feedback

### Alan's Blue-Sky Vision for Center of Excellence
**Ambitious proposal discussed:**
- Create "Centre of Excellence for Additive Manufacturing" in Halifax, Nova Scotia
- Bringing together:
  - Tronos Jet (aerospace-certified 3D printing)
  - Dalhousie University (academic expertise)
  - Precise Design (manufacturing/design expertise)
  - Support for Canadian Navy supply chain
  - Regional hub for other companies seeking AM solutions
- Model: Tallis has supported similar centers in Morocco and Australia
- Vision: Collaborative rather than competitive approach

### Development Pathway Discussion

**Current Status:**
- Proof of concept complete
- MVP ready for demonstration
- Not yet ready for production deployment
- Technical team needs expansion for next phase

**Timeline & Funding Estimate:**
- Timeframe: 6-12 months (Alan's experience: previous projects took 12 months, $1M, typically within ±10%)
- Budget: Team expansion, cybersecurity, infrastructure, testing
- Not seeking "big money" at this stage - looking for partner to cover operating costs and development
- Flexible on specifics pending actual assessment of requirements

### Tailored vs. General Platform

**Key Discussion Point:**
Alan proposed: "Could software be tailored specifically for Tallis/Navy rather than general-purpose?"

**Response:** 
- Yes, this is preferred approach - build trust through specific use case success
- Learn from actual end-user needs rather than hypothetical scenarios
- Customize based on real pain points
- Scale to other clients after validation

**Advantage:** Reduces OEM/IP concerns if platform is internal to specific organization

---

## Next Steps & Follow-Up Actions

### Immediate (Next Few Weeks)
1. **Access MVP Software:** Mahmoud/Ali to send link to Precise Design team to review platform demo
2. **COVE2026 Conference Meeting:** Ali and Mahmoud attending May 8-9 (or nearby date)
   - Alan plans to attend
   - Mark Coburn from Tronos Jet also attending Thursday
   - Plan to meet in person
3. **Contact Exchange:** Alan to provide contact info; Ali will share email/phone for follow-up

### Medium Term (Summer 2026)
1. **Internal Tallis Discussion:** Alan to position software within Phase 2 proposal context
2. **Lee (Tallis Contact) Meeting:** In-person meeting planned with Alan and Mark Coburn Thursday (from conference)
3. **Phase 2 Proposal Development:** If interest confirmed, begin structuring proposal with:
   - Dedicated software customization for Tallis supply chain
   - AM framework operationalization
   - Education/training curriculum for Tallis personnel
   - Collaborative team structure (Precise Design + Tronos Jet + Dalhousie)

### Required Before Moving Forward
1. **Three Critical Questions to Answer** (from earlier interviews):
   - Technical qualification: Can 3D printed parts meet aerospace/maritime standards?
   - Liability framework: How is responsibility structured?
   - Usability: Training and operational requirements quantified?

2. **Independent Validation:**
   - Lab testing of 3D printed parts under operational conditions
   - Certification pathway analysis
   - Liability legal framework development

3. **OEM Engagement Strategy:**
   - Build case study with Navy (no IP concerns)
   - Demonstrate success before approaching major manufacturers
   - Develop inclusion model for OEM participation

---

## Key Insights & Strategic Observations

### 1. Government Procurement as Gateway
**Insight:** Navy supply chain (federal procurement) is ideal first market because:
- Parts often obsolete (no living OEM)
- No IP ownership issues to navigate
- High financial impact of downtime (>$1M per vessel)
- Security advantage of keeping manufacturing in Canada
- Can serve as proof-of-concept before approaching private sector OEMs

### 2. Collaborative Model is Key
**Observation from Alan's Comments:**
- "We're better working together than working alone"
- ITB (Industrial and Technological Benefits) credits favor collaborative models
- Academic partnership multiplier: 9x vs. 3x for private companies
- Practical need: Precise Design lacks 3D printing → partnership with Tronos Jet required

### 3. Supply Chain Economics Favor Solution
**Critical Factor:**
- Oil & gas and other major industries "don't care" about small costs
- But Navy downtime = equipment going to scrap (existential, not just financial)
- Examples: $500 part causing shutdown, $1M+ downtime per incident
- Economic incentive exists but must be triggered by operational pain

### 4. Technology Adoption Timeline
**Maturity Curve Observed:**
- Aerospace: Already ahead of the curve (US, Europe)
- Defense: Beginning adoption (Canada with Navy interest)
- Oil & Gas: Aware of problem but not yet motivated to change (high current spend)
- Manufacturing: Varies by segment

### 5. Trust and Relationships Matter Most
**Strategic Observation:**
- Referral path: Lab2Market contact → Levis → Precise Design
- Alan explicitly said: "What differentiates the good ones is the advisory they're seeking"
- Academic partnership (Dalhousie) adds legitimacy
- Success requires trusted intermediaries in early stages

---

## Precise Design's Role & Value Proposition

### Why They're Strategic Partner
1. **Manufacturing Credibility:** Real production capability, not just software
2. **Navy Access:** Existing Tallis collaboration creates channel
3. **Problem Understanding:** Deal with supply chain daily (no 3D printing currently limits their offerings)
4. **Partnership Capability:** Proven ability to collaborate (Tronos Jet relationship)
5. **Regional Hub Potential:** Could serve as Center of Excellence location

### Their Needs from Partnership
- Production-ready software for supply chain management
- IP protection mechanism they can trust with OEM customers
- Technology that differentiates their offering to prime contractors
- Collaboration model that works within government procurement rules

---

## Market & Competitive Context

### Why Now? Why Canada?
**Drivers:**
- US Navy already implementing on-site 3D printing on ships
- China and Europe ahead with AM infrastructure
- Canada falling behind in adoption curve
- Canadian submarine fleet needs immediate parts (national security angle)
- Treasury Board and Defense procurement urgency

**Opportunity Window:**
- Phase 2 Navy funding could accelerate development
- Risk: If Canada continues to lag, market opportunity lost to US/international solutions

### Geographic Advantage
- Proximity to Navy headquarters (Halifax)
- Tronos Jet aerospace certification (industrial credibility)
- Dalhousie technical partnership (academic excellence in AM)
- Federal procurement preference for Canadian companies

---

## Critical Success Factors

### For Software Development
1. Cybersecurity robust enough for Navy/Defense use
2. IP protection mechanism legally sound and practically secure
3. Integration with Navy's existing supply chain systems
4. Usability for non-technical operators across multiple sites

### For Market Adoption
1. Successful proof-of-concept with Navy (obsolete parts replacement)
2. Demonstration of significant cost savings/downtime reduction
3. Resolution of certification and liability frameworks
4. OEM partnership model that creates value for suppliers
5. Regulatory approval from relevant authorities

### For Partnership Success
1. Clear division of responsibilities (Precise Design vs. Tronos vs. Dalhousie)
2. Aligned incentives and benefit sharing
3. Government support (National Research Council, defense procurement)
4. Customer co-development (Tallis as first production user)

---

## Relationship Status

🟢 **WARM LEAD - High Quality Collaboration Partner**  
✅ Fit: Perfect technical and organizational fit for Phase 2  
✅ Interest: Explicit interest in tailoring software for Navy supply chain  
✅ Opportunity: Clear path to Phase 2 funding through Tallis collaboration  
📅 Next Touchpoint: COVE2026 conference (May 8-9 in-person meeting)  
🤝 Partnership Potential: High (complementary capabilities, shared vision)

---

## Financial & Resource Implications

### Phase 2 Proposal Estimate
- **Duration:** 6-12 months
- **Budget:** ~$1 million (based on Alan's experience with similar projects)
- **Team Expansion Needed:**
  - Full-stack software developers (2-3)
  - Cybersecurity specialist
  - DevOps/Infrastructure
  - Technical project manager
  - Subject matter experts (Navy procurement, AM certification)

### Funding Sources Discussed
1. Tallis Phase 2 project funding (primary)
2. National Research Council ITB program (academic partnership multiplier)
3. Defense procurement budget (government interest)
4. Potential co-investment from Tronos Jet (complementary to their printing services)

---

## Critical Quotes

> "We're better working together than we are working alone" - Alan Williams, emphasizing collaborative model

> "What differentiates the really good ones is the advisory that they're seeking. You're asking questions, you're being curious." - From earlier referenced interview

> "You've got a $600 million programme worth of Navy. They got a big hawk and warehouse with all these parts... if I can get rid of them, I don't need to spend the money, don't need to buy the warehousing space." - Alan, describing Tallis supply chain opportunity

> "Canada is falling way behind the 8 ball here... The US is head and shoulders above us" - Alan, on AM adoption globally

> "Eventually all equipment users will be having some sort of printers in-house... but there would be some parts that they would still need to rely on printing facilities." - Dr. Ali, on future vision

> "Come back to me with your MVP, your answers, and we can have another meeting. I absolutely want to continue this." - (From earlier interview, applicable here)

---

## Appendix: Attendee Location Notes

- **Dr. Ali:** Ottawa area (1-hour time difference from Maritimes)
- **Mahmoud:** Halifax/Maritimes area
- **Alan Williams:** Maritime location (Precise Design based in Maritime region)
- **Brennan:** Maritime location
- **Meeting Time Preference:** After 3:30 PM accommodates both time zones

