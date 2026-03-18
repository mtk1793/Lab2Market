# Interview 74 — Mohamad NASIRY
**Date:** March 18, 2026
**Interviewee:** Mohamad NASIRY
**Title:** IMC Materials Leader / Materials Team Leader
**Company:** SLB (Schlumberger) — SRPC, Clamart, Paris, France
**Mutual connections:** Ali Nasiri PEng PhD (Interview 11), Mahya Ghaffari

---

## BRIEF CONTEXT

Mohamad is the person inside SLB — the world's largest oilfield services company — who is directly responsible for expanding AM capability at their Surface Production Research Centre in Paris. He has overseen 11,000+ LPBF parts and holds an ASME Design for AM certification. His Master's research at École Polytechnique was on in-situ process monitoring during LMD — meaning he understands not just the output of AM but the physics and quality control *during* the build. He is one of the most technically deep interviewees to date.

---

## THE 5 CORE QUESTIONS

---

### Q1 — The Qualification Bottleneck (Most Important)

You're expanding AM tools at SLB's SRPC and have delivered 11,000+ LPBF parts — that's a serious industrial operation, not a pilot. But scaling past a certain point inevitably runs into the qualification wall: you need certified mechanical property data, you need traceability from powder batch to finished part, and you need sign-off from whoever is responsible for putting that part into a system that matters.

**In your experience at SLB, what is the single most painful step in that qualification chain — and where does it most often break down or slow things down?**

*What I'm listening for:* Is the bottleneck internal (SLB approval process, conservative engineering sign-off)? External (class society / API / ASME certification timelines)? Data-related (insufficient mechanical property evidence for a new alloy or process parameter set)? This tells me where AddManuChain needs to focus — DRM, materials data, or certification workflow.

---

### Q2 — The Digital File & IP Problem at Scale

SLB designs and manufactures proprietary downhole tools and surface equipment — many of those geometries are core IP. When you want to print a part that was originally designed by an OEM partner, or when a field operation in a remote location needs a part that you can only provide from SRPC Paris — there's a fundamental tension: you need the digital file to travel, but the OEM or internal IP owner doesn't want that file to leave a controlled environment unprotected.

**How does SLB handle that today — is there a formal digital rights management or access control process for AM-ready files, or is it mostly handled through contracts and trust? And where has that broken down for you in practice?**

*What I'm listening for:* Whether IP protection around digital files is a live, real problem at SLB or whether it's already solved internally. If it's unsolved, that validates AddManuChain's DRM / secure print token layer directly. If it's solved internally, I want to know how — and whether that solution could scale to an external network.

---

### Q3 — The Materials Data Gap

One of the concepts I'm building is essentially the MMPDS equivalent for additive manufacturing — a validated, shared material properties database for offshore-relevant alloys: yield strength, tensile, fatigue, elongation, density — tested to actual process parameters (LPBF, DED, wire-arc), validated by class societies like DNV GL or Lloyd's Register. Right now that data either lives in proprietary company databases, academic papers that don't reflect production parameters, or simply doesn't exist for many alloys.

**From where you sit at SLB — does that gap actually exist in your work? When you're qualifying a new alloy or justifying a material choice to a certification body, is the data there, or are you building it yourself every time?**

*What I'm listening for:* Validation that SLB generates its own property data from scratch for each alloy/process combination (which is expensive and creates a data silo), OR that they rely on published data that doesn't fully represent their process (which is a risk). Either answer validates the shared database concept. If he says SLB contributes to industry-wide data efforts already, I want to know which ones.

---

### Q4 — When SLB Can't Print In-House

SLB operates on every continent — rigs offshore Brazil, platforms in the North Sea, fields in the Middle East, remote operations in Canada. SRPC Paris is your centre of excellence, but it can't serve a production-stopped emergency in Newfoundland in 4 hours.

**When a field operation needs an AM part urgently and your SRPC facility is geographically out of reach — what actually happens today? Is there a vetted network of external certified AM facilities SLB can direct work to, or is it still "wait for the part to ship from Paris"? And if you do use external printers, how do you handle the IP and certification assurance?**

*What I'm listening for:* Whether there's a structured external AM supply chain at SLB or whether remote emergency AM is still an unsolved problem. This is the core AddManuChain use case — if SLB has no certified external network and no IP-safe way to outsource print jobs, that's a direct gap the platform fills.

---

### Q5 — The Real Barrier to AM Scaling in O&G

You've been inside SLB's AM operation for over 6 years, you've seen it grow from Materials & Process Engineer to IMC Materials Leader. You've watched AM adoption evolve — and also seen where it stalls. You're in a better position than almost anyone to answer this honestly.

**What is the real reason AM adoption in oil & gas is still slower than the technology deserves — and what would it actually take to break through that ceiling? Not the polished conference answer — the honest one from someone who lives it every day.**

*What I'm listening for:* Is it certification and standards? Engineering conservatism? Cost of qualification vs. volume of parts? Lack of trusted suppliers? Supply chain visibility? This is the most open-ended question but often produces the most useful strategic signal. I want to understand what the platform needs to solve to be genuinely adopted at a company like SLB, not just used for a pilot.

---

## 2 BONUS QUESTIONS
*(Show I've read his profile — use if conversation allows)*

---

### BONUS Q1 — His LMD Research & In-Process Quality Monitoring

Your Master's thesis at École Polytechnique was on in-situ measurements during LMD — studying how process parameters affect mechanical properties in real time. That's not just AM knowledge, that's understanding the physics of the build as it happens, which most AM engineers never get into.

**Has that research background actually changed how you think about quality assurance for LPBF at SLB — do you push for any kind of in-process monitoring in production, or does the industrial reality mean you're still relying on post-build inspection? And do you think in-situ monitoring is going to become a certification requirement, or will it stay optional?**

*Why this matters:* It shows genuine respect for his research — and the answer has direct implications for AddManuChain's traceability layer. If in-situ process data becomes part of certification evidence, the platform needs to capture and store it as part of the digital thread.

---

### BONUS Q2 — The Framatome Nuclear AM Centre & What It Signals

You reposted the Framatome announcement about their new AM centre in Romans-sur-Isère — a facility dedicated specifically to nuclear and defence AM, with LPBF and wire-arc, covering everything from production to R&D to qualification and training. That's a massive strategic investment, and the framing was explicitly about *sovereignty* — making France's industrial base self-sufficient for critical components.

**Do you think oil & gas is heading toward that model — dedicated, sector-specific certified AM infrastructure — or is O&G too fragmented and too cost-sensitive to make that kind of commitment? And is SLB positioning itself to be that infrastructure for the sector, or more of a user of it?**

*Why this matters:* The sovereignty framing in the Framatome post directly maps to AddManuChain's Supply Chain Intelligence module. It also signals whether the market wants one company to own the AM infrastructure (SLB / vertical integration) or whether there's room for a neutral platform that connects certified facilities across the sector.

---

## CLOSING ASK

> "One last thing — I'm trying to build a genuinely useful platform for people in your position, not just a concept. Is there anyone else at SLB, or in the AM/certification/oil & gas space, that you'd recommend I speak with? Even a supply chain engineer, a procurement lead, or someone at a class society who deals with AM qualification — a warm intro from you would mean a lot."
