# New Hypotheses from David Waldbillig Interview

**Interview Date:** January 28, 2026  
**Interviewee:** David Waldbillig, Principal Engineer, InnoTech Alberta  
**Total New Hypotheses:** 4

---

## H50: VP.18 - Low-Risk Part Categorization System

### Hypothesis Statement

**Hypotheses:** Energy companies will only adopt digital inventory for additive manufacturing if the platform provides a clear **risk categorization system** (low/medium/high risk) that automatically classifies parts based on safety-criticality, pressure ratings, and regulatory requirements, starting with low-risk parts to build trust before expanding to high-risk applications.

### Evidence from Interview

> "Another part that he mentioned was about the usage of AM and digital inventory for low risk parts rather than high risk ones."

**Context:**
- Current industry approach: start with non-critical, low-risk parts
- Build confidence gradually before moving to high-risk parts
- High-risk parts require extensive validation (safety-critical, pressure-bearing)

**Examples of Low-Risk Parts:**
- Non-structural brackets
- Housings and enclosures
- Tooling and fixtures  
- Non-pressure-bearing ducts

**Examples of High-Risk Parts (NOT ready for digital inventory yet):**
- Pressure vessels
- Safety-critical valves
- Load-bearing structural components
- Certified flight hardware

---

### Proposed Value Proposition

**Feature:** **Automated Risk Assessment Engine**

**How It Works:**
1. User uploads part CAD file or specification
2. AI analyzes:
   - Pressure ratings
   - Load-bearing requirements
   - Safety-critical designations
   - Regulatory classifications (ASME, API, etc.)
   - Material specifications
   - Operating environment (temperature, corrosion, etc.)
3. System assigns risk level: 🟢 LOW | 🟡 MEDIUM | 🔴 HIGH
4. Platform applies different workflows based on risk:
   - **Low-risk:** Simplified approval, wider supplier network
   - **Medium-risk:** Enhanced testing requirements, certified suppliers only
   - **High-risk:** Full qualification path, OEM involvement required

**User Benefit:**
- Clear guidance on which parts are "safe" to start with
- Gradual expansion as confidence builds
- Compliance assurance (right process for right risk level)

---

### Validation Plan

**Target Interviewees:**
- 5 plant managers (oil & gas, power generation)
- 3 procurement directors
- 2 quality assurance managers

**Questions:**
1. "How do you currently decide which parts are safe to source from non-OEM suppliers?"
2. "Would an automated risk classification system give you confidence to try digital inventory?"
3. "What specific criteria make a part 'high-risk' vs. 'low-risk' in your operations?"

**Success Criteria:**
- 8/10 interviewees confirm risk classification as critical decision factor
- 8/10 would start with low-risk parts if system clearly identified them
- Clear definition of risk criteria emerges from interviews

---

### Business Model Implications

**Revenue Impact:**
- Enables **tiered pricing** (low-risk = lower fees, high-risk = premium fees)
- Faster adoption (low-risk parts have shorter sales cycle)
- Upsell path (expand from low → medium → high risk over time)

**Cost Structure:**
- **Development:** AI model training for risk classification (moderate cost)
- **Regulatory:** Consult with certification bodies to define criteria (one-time)
- **Maintenance:** Update risk criteria as standards evolve (ongoing)

**Partnerships:**
- Certification bodies (DNV, ABS) to validate risk framework
- Insurance companies (underwrite high-risk parts)
- Legal firms (liability frameworks for risk levels)

---

### Market Size Estimation

**Serviceable Market (Low-Risk Parts Initially):**

| Sector | Total Spare Parts Market | Low-Risk % | Low-Risk Market Size |
|--------|--------------------------|------------|----------------------|
| Oil & Gas | $8B/year | 40% | **$3.2B** |
| Power Generation | $5B/year | 50% | **$2.5B** |
| **TOTAL** | **$13B/year** | **44% avg** | **$5.7B** |

**Expansion Potential (Medium + High Risk):**
- Year 2-3: Add medium-risk parts (+$4B)
- Year 4-5: Add high-risk parts (+$3.3B)
- **Total Addressable Market: $13B**

---

### Priority Assessment

**Priority:** 🔴 **CRITICAL - MVP Feature**

**Rationale:**
- Without risk classification, platform cannot launch safely
- Liability concern (if customer uses AM for wrong parts)
- Enables market entry (start with low-risk, proven approach)
- Competitive differentiation (Fieldnode doesn't emphasize this)

**Estimated Effort:**
- **High (6-9 months development)**
- Requires AI model training
- Regulatory consultation
- Extensive testing/validation

---

## H51: VP.19 - Post-Processing Service Network

### Hypothesis Statement

**Hypotheses:** Digital inventory for additive manufacturing will fail in energy sector applications unless the platform includes **integrated post-processing services** (coating, surface finishing, heat treatment) with certified service providers in the network, because most AM parts require extensive post-processing before they meet industry specifications for corrosion resistance, wear protection, and surface quality.

### Evidence from Interview

> "Another aspect he mentioned was about the coating side which is quite important for different industries related to that."

**Context:**
- Coatings are CRITICAL for energy sector applications:
  - Corrosion protection (offshore, oil sands)
  - Wear resistance (high-friction applications)
  - Heat resistance (power generation turbines)
  - Surface finish (regulatory compliance)

**David's Expertise:**
- 20+ years in materials and coatings
- Leads materials portfolio at InnoTech Alberta
- Specializes in harsh environment applications

---

### Proposed Value Proposition

**Feature:** **End-to-End Supply Chain Orchestration**

**How It Works:**
1. Customer requests part with specifications:
   - Base material (AM)
   - Coating requirements (e.g., corrosion-resistant nickel coating)
   - Surface finish (Ra value, etc.)
   - Heat treatment (stress relief, hardening)
2. Platform automatically:
   - Matches with certified AM printer
   - Matches with certified coating service provider
   - Matches with testing lab (coating adhesion, thickness testing)
   - Coordinates logistics between suppliers
   - Provides single quote for entire workflow
3. Customer gets finished part (not just raw AM component)

**Post-Processing Services Included:**
- **Coatings:** Nickel, chrome, ceramic, thermal barrier
- **Surface Finishing:** Machining, polishing, shot peening
- **Heat Treatment:** Annealing, stress relief, hardening
- **Testing:** Non-destructive testing (NDT), dimensional inspection

---

### Validation Plan

**Target Interviewees:**
- 5 maintenance managers (energy sector)
- 3 coating service providers
- 2 quality engineers

**Questions:**
1. "What percentage of your AM parts require post-processing before use?"
2. "How do you currently coordinate between AM supplier and coating supplier?"
3. "Would you pay a premium for a platform that handles end-to-end orchestration?"

**Success Criteria:**
- 8/10 confirm most AM parts need post-processing
- 7/10 find current coordination painful (multiple vendors)
- 6/10 willing to pay 10-15% premium for integrated solution

---

### Business Model Implications

**Revenue Impact:**
- **Transaction fees on post-processing** (10-15% of coating service value)
- Higher average order value (AM + coating vs. AM only)
- Stickier customers (end-to-end solution harder to replace)

**Cost Structure:**
- **Network development:** Recruit certified coating providers (moderate effort)
- **Logistics integration:** Coordinate shipping between suppliers (software development)
- **Quality assurance:** Inspect coating quality (partnership with testing labs)

**Partnerships:**
- Coating service providers (regional networks needed)
- Logistics companies (multi-leg shipping)
- Testing labs (quality verification)

---

### Market Size Estimation

**Post-Processing Market in Energy Sector:**

| Service Type | % of AM Parts Requiring | Avg. Cost per Part | Annual Market Size |
|--------------|-------------------------|--------------------|--------------------|
| Coatings | 70% | $500 | **$2.8B** |
| Surface Finishing | 50% | $200 | **$800M** |
| Heat Treatment | 30% | $150 | **$360M** |
| **TOTAL POST-PROCESSING** | **-** | **-** | **$3.96B** |

**AddManuChain Revenue Potential (15% take rate):**
- **$594M annual revenue potential** (at full market penetration)

---

### Priority Assessment

**Priority:** 🟡 **HIGH - Phase 2 Feature**

**Rationale:**
- Not MVP (can launch with AM-only, add post-processing later)
- But critical for energy sector adoption (most parts need coatings)
- Competitive differentiation (Fieldnode doesn't offer this)

**Estimated Effort:**
- **Medium (3-6 months development)**
- Requires network development (coating providers)
- Logistics coordination software
- Quality assurance protocols

---

## H52: VP.20 - Reverse Engineering Integration

### Hypothesis Statement

**Hypotheses:** Energy companies will pay a premium for a digital inventory platform that integrates with **reverse engineering service providers** to scan obsolete parts on-site, create CAD files, store them in a searchable repository, and enable on-demand reproduction, because the current process is manual, project-based, and results are not reusable across the industry.

### Evidence from Interview

> "For the reverse engineering part he mentioned that there are some companies that regularly go on site for the equipment that are not built anymore to scan them and make blueprints by using the reverse engineering."

**Context:**
- Reverse engineering firms exist (validated market)
- Current process:
  - Company A calls reverse engineering firm
  - Firm scans part on-site
  - Creates CAD file
  - Delivers file to Company A
  - **File is NOT shared** (Company B needs same part, starts from scratch)
- Massive inefficiency (duplicate scanning for identical obsolete parts)

---

### Proposed Value Proposition

**Feature:** **Reverse Engineering Marketplace + Reusable Scans**

**How It Works:**

**Scenario 1: First Company Needs Obsolete Part**
1. Company A searches platform for obsolete part
2. Part not found (never scanned before)
3. Platform connects Company A with certified reverse engineering provider
4. Provider scans part on-site, creates CAD file
5. CAD file uploaded to platform (Company A owns IP, but makes shareable)
6. Company A gets part reproduced via AM
7. **CAD file now available for future requests**

**Scenario 2: Second Company Needs Same Part**
1. Company B searches platform for same obsolete part
2. Part FOUND (Company A already paid for scan)
3. Company B pays licensing fee to Company A (or platform) for CAD file
4. Instantly gets part reproduced (no need to re-scan)
5. **Massive time/cost savings**

**Revenue Model:**
- **Transaction fee** on initial reverse engineering service (15%)
- **Licensing fee** on CAD file reuse (30% to platform, 50% to original scanner, 20% to reverse eng firm)
- **Subscription fee** for companies that want priority access to scanned library

---

### Validation Plan

**Target Interviewees:**
- 5 plant managers (with obsolete equipment)
- 3 reverse engineering service providers
- 2 procurement managers

**Questions:**
1. "How often do you need parts that are no longer manufactured?"
2. "Have you ever paid to reverse engineer a part that someone else already scanned?"
3. "Would you be willing to share your scanned CAD files for a licensing fee?"

**Success Criteria:**
- 8/10 have needed obsolete parts (high frequency)
- 5/10 suspect they've duplicated reverse engineering efforts
- 6/10 willing to share scans for passive income

---

### Business Model Implications

**Revenue Impact:**
- **Network effects** (more scans = more value)
- **Passive income** for early adopters (licensing fees)
- **Lower cost** for late adopters (reuse existing scans)

**Cost Structure:**
- **Technology:** Search/match algorithms for part identification (AI-driven)
- **Legal:** IP licensing frameworks (one-time setup)
- **Network:** Recruit reverse engineering providers (moderate effort)

**Partnerships:**
- Reverse engineering firms (don't compete, integrate)
- IP law firms (licensing agreements)
- Equipment OEMs (historical part databases)

---

### Market Size Estimation

**Obsolete Parts Market:**

| Industry | Annual Obsolete Part Demand | Avg. Reverse Eng Cost | Annual Market Size |
|----------|----------------------------|----------------------|---------------------|
| Oil & Gas | 50,000 unique parts | $5,000 | **$250M** |
| Power Generation | 30,000 unique parts | $6,000 | **$180M** |
| **TOTAL** | **80,000 unique parts** | **$5,375 avg** | **$430M** |

**AddManuChain Revenue Potential:**
- **Year 1:** 5% market share → $21.5M revenue
- **Year 3:** 20% market share → $86M revenue
- **Year 5:** 35% market share → $150M revenue (as library grows, value compounds)

---

### Priority Assessment

**Priority:** 🟡 **MEDIUM - Phase 2-3 Feature**

**Rationale:**
- Strong network effect potential (valuable long-term)
- But complex (IP licensing, search algorithms, provider network)
- Not needed for MVP (start with new parts, add obsolete parts later)

**Estimated Effort:**
- **High (9-12 months development)**
- AI-powered part matching
- Legal framework for IP licensing
- Provider network development

---

## H53: VP.21 - Predictive Maintenance API Integration

### Hypothesis Statement

**Hypotheses:** Energy companies will pay a 25% premium for digital inventory platforms that integrate with **predictive maintenance IoT systems** (vibration sensors, thermal imaging, oil analysis) to automatically trigger spare parts orders BEFORE failures occur, reducing downtime by 40% compared to reactive replacement after failures.

### Evidence from Interview

> "And also they focused over the automated repair and approaches that would be beneficial for them."

**Context:**
- Automated repair is emerging trend in energy sector
- Predictive maintenance systems already exist (IoT sensors)
- Current gap: **Sensors detect issues, but humans still manually order parts**
- Opportunity: **API integration to automate spare parts ordering**

---

### Proposed Value Proposition

**Feature:** **IoT-Triggered Automatic Ordering**

**How It Works:**

1. **Integration Setup:**
   - AddManuChain API connects to customer's predictive maintenance system
   - Map equipment IDs to spare parts catalog
   - Define failure thresholds (e.g., vibration > X, temperature > Y)

2. **Monitoring:**
   - IoT sensors continuously monitor equipment health
   - Predictive algorithms forecast time-to-failure (e.g., "Pump #7 will fail in 14 days")

3. **Automated Ordering:**
   - When failure predicted, API automatically:
     - Searches AddManuChain for required spare part
     - Checks lead time (ensure part arrives before failure)
     - Places order without human intervention
     - Notifies maintenance team: "Part ordered, arrives in 10 days, schedule replacement on Day 13"

4. **Execution:**
   - Part delivered just-in-time
   - Planned maintenance (not emergency downtime)
   - **40% downtime reduction** (proactive vs. reactive)

---

### Validation Plan

**Target Interviewees:**
- 5 maintenance managers (with predictive maintenance systems)
- 3 IoT/sensor platform providers (GE Predix, Siemens MindSphere, etc.)
- 2 reliability engineers

**Questions:**
1. "Do you use predictive maintenance systems today? Which platform?"
2. "When a failure is predicted, what's the current process for ordering spare parts?"
3. "Would automated ordering reduce your downtime? By how much?"

**Success Criteria:**
- 6/10 already use predictive maintenance (market exists)
- 8/10 manually order parts after prediction (pain point confirmed)
- 7/10 estimate 30-50% downtime reduction from automated ordering

---

### Business Model Implications

**Revenue Impact:**
- **Premium pricing** (25% higher subscription for API integration)
- **Higher retention** (integrated into critical workflows, sticky)
- **Larger contract sizes** (enterprise IoT deals are large)

**Cost Structure:**
- **Development:** API connections to major IoT platforms (high initial cost)
- **Maintenance:** Ongoing API updates as platforms evolve (moderate)
- **Partnerships:** Certification from IoT vendors (GE, Siemens)

**Partnerships:**
- GE Predix
- Siemens MindSphere
- IBM Maximo
- SAP Predictive Maintenance
- Emerson

---

### Market Size Estimation

**Predictive Maintenance Market (Energy Sector):**

| Segment | Companies Using Predictive Maintenance | Avg. Annual Spend on Spare Parts | Premium Fee (25%) | Market Size |
|---------|---------------------------------------|----------------------------------|-------------------|-------------|
| Oil & Gas Majors | 200 | $5M | $1.25M | **$250M** |
| Power Plants | 500 | $2M | $500K | **$250M** |
| **TOTAL** | **700** | **-** | **-** | **$500M** |

**AddManuChain Revenue Potential:**
- **Year 3:** 10% penetration → $50M annual revenue
- **Year 5:** 25% penetration → $125M annual revenue

---

### Priority Assessment

**Priority:** 🔵 **LOW - Phase 3-4 Feature**

**Rationale:**
- Very valuable LONG-TERM (high revenue potential)
- But requires mature platform first (need large parts catalog)
- Complex integrations (multiple IoT vendors)
- Target customers are advanced users (not early adopters)

**Estimated Effort:**
- **High (12-18 months development)**
- API integrations with 5+ IoT platforms
- Partnership negotiations
- Security/compliance (enterprise-grade)

---

## Summary Table: New Hypotheses

| ID | Hypothesis | Priority | Effort | Estimated Revenue Impact |
|----|------------|----------|--------|--------------------------|
| **H50** | Low-Risk Part Categorization | 🔴 CRITICAL (MVP) | High (6-9 mo) | Enables market entry |
| **H51** | Post-Processing Service Network | 🟡 HIGH (Phase 2) | Medium (3-6 mo) | $594M potential |
| **H52** | Reverse Engineering Integration | 🟡 MEDIUM (Phase 2-3) | High (9-12 mo) | $150M (Year 5) |
| **H53** | Predictive Maintenance API | 🔵 LOW (Phase 3-4) | High (12-18 mo) | $125M (Year 5) |

---

## Strategic Implications

### Immediate Actions:

1. **H50 (Risk Categorization) - START NOW**
   - Critical for safe market entry
   - Liability protection
   - Enables low-risk parts MVP

2. **Validate H51 (Post-Processing) in Next 5 Interviews**
   - Ask every interviewee about coating/finishing needs
   - Identify potential coating service partners
   - May be more critical than anticipated

3. **Deprioritize H52 & H53 for Now**
   - Valuable but not MVP
   - Revisit in Year 2-3

---

**Document Created:** January 28, 2026  
**Status:** New Hypotheses Documented ✅  
**Next Step:** Add to Hypothesis Tracking Sheet
