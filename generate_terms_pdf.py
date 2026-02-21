"""
AddManuChain / Lab2Market
Key Terms & Industry Vocabulary Guide
Generated from 44+ customer discovery interviews

Author: Generated for Mahmoud (Michael) Kiasari
Date: February 21, 2026
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import datetime

OUTPUT_PATH = r"C:\Users\mtk17\OneDrive\Desktop\L2M\Lab2Market\AddManuChain_Industry_Terms_Guide.pdf"

# ─────────────────────────────────────────────────────────────
# COLOUR PALETTE
# ─────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0A1628")
STEEL_BLUE = colors.HexColor("#1B4F72")
ACCENT     = colors.HexColor("#2980B9")
GOLD       = colors.HexColor("#D4AC0D")
LIGHT_BG   = colors.HexColor("#EBF5FB")
PALE_BG    = colors.HexColor("#F8F9FA")
WHITE      = colors.white
MID_GRAY   = colors.HexColor("#7F8C8D")
DARK_GRAY  = colors.HexColor("#2C3E50")
RED_ALERT  = colors.HexColor("#C0392B")
GREEN_OK   = colors.HexColor("#1E8449")

# ─────────────────────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

COVER_TITLE = ParagraphStyle("CoverTitle", fontSize=32, leading=40,
    textColor=WHITE, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=10)

COVER_SUB = ParagraphStyle("CoverSub", fontSize=16, leading=22,
    textColor=GOLD, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=6)

COVER_BODY = ParagraphStyle("CoverBody", fontSize=11, leading=15,
    textColor=colors.HexColor("#BDC3C7"), alignment=TA_CENTER, fontName="Helvetica")

SECTION_HDR = ParagraphStyle("SectionHdr", fontSize=18, leading=24,
    textColor=WHITE, fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=4)

CAT_TITLE = ParagraphStyle("CatTitle", fontSize=13, leading=17,
    textColor=STEEL_BLUE, fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=4)

TERM_NAME = ParagraphStyle("TermName", fontSize=11, leading=14,
    textColor=NAVY, fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=2)

TERM_ABBREV = ParagraphStyle("TermAbbrev", fontSize=9, leading=12,
    textColor=ACCENT, fontName="Helvetica-Oblique", spaceBefore=0, spaceAfter=2)

BODY_STYLE = ParagraphStyle("Body", fontSize=9.5, leading=14,
    textColor=DARK_GRAY, fontName="Helvetica", spaceBefore=2, spaceAfter=2,
    alignment=TA_JUSTIFY, leftIndent=12)

QUOTE_STYLE = ParagraphStyle("Quote", fontSize=9, leading=13,
    textColor=STEEL_BLUE, fontName="Helvetica-Oblique", spaceBefore=4, spaceAfter=4,
    leftIndent=20, rightIndent=20)

REF_STYLE = ParagraphStyle("Ref", fontSize=8.5, leading=12,
    textColor=MID_GRAY, fontName="Helvetica", spaceBefore=2, spaceAfter=0,
    leftIndent=12)

PITCH_STYLE = ParagraphStyle("Pitch", fontSize=9, leading=13,
    textColor=GREEN_OK, fontName="Helvetica-Bold", spaceBefore=3, spaceAfter=3,
    leftIndent=12)

WARN_STYLE = ParagraphStyle("Warn", fontSize=9, leading=13,
    textColor=RED_ALERT, fontName="Helvetica-Bold", spaceBefore=3, spaceAfter=3,
    leftIndent=12)

TOC_STYLE = ParagraphStyle("TOC", fontSize=10, leading=16,
    textColor=DARK_GRAY, fontName="Helvetica", leftIndent=20)

TOC_CAT = ParagraphStyle("TOCCat", fontSize=11, leading=16,
    textColor=STEEL_BLUE, fontName="Helvetica-Bold", leftIndent=0, spaceBefore=6)

# ─────────────────────────────────────────────────────────────
# TERM DATABASE
# Each entry: (term, abbreviation_or_None, definition, why_matters, quote_or_None, pitch_tip_or_None, ref)
# ─────────────────────────────────────────────────────────────

CATEGORIES = [

  ("1. Additive Manufacturing (AM) Process Technologies",
   [
    ("Additive Manufacturing", "AM",
     "The industrial process of building objects layer-by-layer from digital files, "
     "using materials such as metal powder, polymer filament, or wire. In industrial "
     "contexts, AM enables on-demand production of complex geometries that would be "
     "impossible or cost-prohibitive with conventional subtractive machining.",
     "This is the core technology underpinning AddManuChain. Every conversation about "
     "digital inventory, certification, or supply chain disruption ultimately traces back "
     "to what AM can and cannot print, and how fast.",
     None,
     "Lead with outcomes, not the technology. Say 'certified parts in 48 hours' not 'we use AM'.",
     "All 44+ interviews; insights.md, Shawn Sooley, Mark Kirby"),

    ("Laser Powder Bed Fusion", "LPBF",
     "An AM process in which a high-powered laser selectively fuses layers of "
     "metal powder spread across a build platform. Common machine brands: EOS M290/M280/M270, "
     "Renishaw RenAM, GE Additive Concept Laser. Produces high-density metal parts with "
     "complex internal geometries. Requires inert atmosphere (argon/nitrogen) and careful "
     "powder management.",
     "LPBF is the dominant metal AM process for aerospace, marine, and offshore parts. "
     "Any certified AM facility you partner with likely uses LPBF. Understanding its "
     "constraints (machine-specific qualification, powder reuse cycles) is essential.",
     None,
     "When prospects ask 'what process?', say LPBF for metals. Be ready to name EOS M290 as the industry standard.",
     "insights.md §1; Adam Saxty (LR) Interview #45; GKN Aerospace Interview #43"),

    ("Direct Energy Deposition", "DED",
     "An AM process that deposits material (blown powder or wire) directly onto a "
     "substrate while simultaneously melting it with a laser, electron beam, or plasma arc. "
     "Sub-types: Blown Powder DED, Laser Wire DED. Used for large structural repairs and "
     "near-net-shape production. GKN Aerospace's Matthew Erning is a DED technical authority.",
     "DED is used for repair and large-scale parts — relevant for offshore platform component "
     "restoration where replacement parts are unavailable. Laser Wire DED is emerging for "
     "naval/defense because it uses wire (simpler logistics than powder).",
     None,
     "For repair use cases, mention DED. For entirely new parts, default to LPBF or polymer AM.",
     "GKN Aerospace Interview #43; insights.md §1"),

    ("Hot Isostatic Pressing", "HIP",
     "A post-processing technique in which AM metal parts are subjected to high temperature "
     "AND high pressure simultaneously (using inert gas in a sealed chamber). HIP eliminates "
     "internal porosity and micro-cracks that form during printing, significantly improving "
     "fatigue life and mechanical properties. Adds cost and 1-3 weeks to lead time.",
     "HIP is often REQUIRED for safety-critical AM parts in marine, aerospace, and defense. "
     "It is a major cost adder that can erode the price advantage of AM over conventional "
     "manufacturing. Always factor HIP into your cost estimates.",
     None,
     "When asked about part quality: 'Our process includes HIP post-processing to meet DNV/LR fatigue requirements.'",
     "insights.md §3; Adam Saxty LR Interview #45"),

    ("Non-Destructive Testing", "NDT",
     "Inspection methods that evaluate material integrity without permanently altering the "
     "part. Traditional NDT includes: X-ray radiography, ultrasonic testing (UT), dye "
     "penetrant inspection (DPI), magnetic particle inspection (MPI). For AM parts, "
     "traditional 2D NDT is insufficient because AM-specific defects (micro-porosity, "
     "delamination, subsurface cracks) require 3D inspection.",
     "Class societies (DNV, LR) require NDT as part of part certification. AM parts are "
     "harder to NDT than conventional parts because their microstructure is anisotropic "
     "and defects are often subsurface. Micro-CT is the gold standard but is expensive.",
     None,
     "When discussing quality: 'Our certified facilities use Micro-CT and traditional NDT per DNV/LR requirements.'",
     "insights.md §3; Adam Saxty Interview #45"),

    ("Micro-CT Scanning", "Micro-CT",
     "Micro-Computed Tomography — a 3D X-ray scanning technique that creates detailed "
     "internal cross-sectional images of AM parts, revealing porosity, cracks, inclusions, "
     "and other subsurface defects. The gold standard for AM quality inspection. "
     "Limitations: expensive (~$500-$2,000 per scan), slow data processing, high false-positive "
     "rates for AM-specific defect types.",
     "Micro-CT is the technical proof point for 'we verify quality.' When asking about your "
     "quality assurance process, a sophisticated buyer (Lloyd's Register, Navy, ExxonMobil) "
     "will expect Micro-CT to be part of the answer.",
     None,
     "Drop 'Micro-CT' naturally when discussing QA. It signals you understand the technical depth.",
     "insights.md §3"),

    ("Anisotropy", None,
     "The property of being directionally dependent — AM parts have different mechanical "
     "properties depending on the orientation in which they were printed (XY plane vs. "
     "Z-axis build direction). Parts printed vertically are typically weaker in tension "
     "than horizontally printed equivalents. Fatigue testing confirmed: horizontal orientation "
     "outperforms vertical/diagonal in cyclic loading.",
     "Anisotropy is why regulators and class societies require extensive testing of AM parts "
     "before certification. When a client asks 'is the printed part as strong as the original?', "
     "the correct answer is: 'Yes, IF we control build orientation, which our certified process does.'",
     "Same material printed in 3 directions showed different failure profiles. — insights.md",
     None,
     "insights.md §3"),

    ("Porosity", None,
     "Micro-scale voids (holes) that form within AM parts during the printing process due to "
     "gas entrapment, incomplete powder fusion, or spattering. Porosity weakens parts under "
     "cyclic loading (fatigue), particularly dangerous in high-pressure applications. "
     "Mitigation strategies: process parameter optimization, HIP post-processing.",
     "Porosity is the primary reason AM parts historically failed FAT (Factory Acceptance Testing) "
     "for marine and naval applications. Class societies test for it. Always mention HIP as the "
     "mitigation when porosity concerns come up.",
     None,
     None,
     "insights.md §3"),

    ("Feedstock Qualification", None,
     "The process of certifying the specific metal powder (or wire) used in AM production. "
     "Includes: chemical composition verification, particle size distribution, flowability, "
     "contamination testing, and reuse cycle limits. A given AM facility must requalify "
     "feedstock if they change powder suppliers or exceed reuse cycles.",
     "Feedstock qualification is one of Lloyd's Register's 7 certification steps. If an AM "
     "facility changes its powder supplier, the part certification may become invalid and "
     "re-qualification is required — a major delay and cost driver.",
     "With powder-based processes — how is the feedstock going to change over time with every reuse? — Adam Saxty, LR",
     None,
     "Adam Saxty LR Interview #45"),

    ("Test Coupon", None,
     "A standardized sample printed simultaneously alongside each production batch using "
     "identical parameters. Test coupons are destructively tested (tensile, fatigue, hardness) "
     "to verify that the material properties of the batch meet specification — without "
     "destroying the actual part.",
     "Test coupons are Lloyd's Register's mandated per-order verification step. This is the "
     "lightweight recurring cost in the pre-certified parts library model — not a full "
     "re-certification, just a batch coupon test. Critical to understand for your business model.",
     "Once facility and part are qualified, the only thing then would be printing + a test coupon. — Trevor Butler, LR",
     None,
     "Trevor Butler LR Interview #42; Adam Saxty Interview #45"),

    ("Factory Acceptance Testing", "FAT",
     "The final validation step before a customer accepts a manufactured system or component. "
     "Performed by the customer/end-user under realistic operating conditions. For AM parts "
     "in marine/naval: includes corrosion testing (saltwater exposure), fatigue testing "
     "(million-cycle loading), multi-directional stress analysis. Can take months to complete.",
     "FAT has historically been where AM parts fail for Navy and marine applications — "
     "fatigue performance under the FAT protocol falls short of conventional equivalents. "
     "This is the root cause of the certification barrier that Tyler Beatty (ExxonMobil) "
     "called 'certifying authorities haven't led the charge.'",
     None,
     None,
     "insights.md §4"),
   ]
  ),

  ("2. Certification, Classification & Regulatory Bodies",
   [
    ("Lloyd's Register", "LR",
     "One of the world's oldest and largest classification societies (founded 1760, London). "
     "Provides technical standards, certification, and inspection services for marine vessels, "
     "offshore installations, and AM facilities. LR's AM certification follows a 7-step process "
     "(Design Review → Material Spec → Facility Qualification → Feedstock Qual → Part Qual → "
     "Production Cert → Installation). Atlantic XL in St. John's recently became the FIRST "
     "LR-qualified AM facility in all of the Americas (North and South).",
     "Your anchor partner (Atlantic XL) holds LR facility qualification. This is a major "
     "competitive differentiator. LR also employs Adam Saxty (Lead AM Technologist, UK), "
     "Trevor Butler (Offshore BD, St. John's), and Dave Whitehouse (Naval/Defense, Dartmouth) "
     "— all confirmed warm contacts.",
     "It's the first AM facility we've qualified in North America — well, North and South America actually. — Trevor Butler, LR",
     "Drop 'Lloyd's Register' early. Say: 'We work within LR's certification framework — Atlantic XL just received LR's first AM facility cert in the Americas.'",
     "Trevor Butler Interview #42; Adam Saxty Interview #45; Dave Whitehouse Interview #46"),

    ("DNV (Det Norske Veritas)", "DNV",
     "Norwegian classification society and leading global certification body for maritime, "
     "oil & gas, and energy sectors. Equinor, Shell, and major offshore operators operate "
     "under DNV rules. DNV is the dominant classification society in Norway and is increasingly "
     "active in Canadian offshore. For AM: DNV has published Technology Qualification (TQ) "
     "framework guidelines for additive-manufactured components.",
     "When speaking to Equinor contacts, DNV is likely their default classification society. "
     "For offshore oil & gas in Atlantic Canada, DNV and LR are both relevant. Understanding "
     "that they are SERVICE PROVIDERS (they work for the operator, not the regulator) is critical.",
     "DNV and Lloyd's technically work for ExxonMobil, Suncor, Equinor — their job is to ensure compliance. — Shawn Sooley",
     None,
     "Shawn Sooley Interview #32; insights.md §3; Jim Granger Interview #23"),

    ("ABS (American Bureau of Shipping)", "ABS",
     "US-based classification society. Major player in offshore oil & gas, particularly "
     "Gulf of Mexico and US-flagged vessels. For AM certification, ABS requires white papers "
     "and iterative approval (minimum 2-year timeline per Jim Granger, MAN Energy). "
     "Less relevant for Canadian/Atlantic context but essential for any US market expansion.",
     "If you ever target US-flagged vessels or Gulf of Mexico operations, ABS becomes the "
     "relevant body. For Canadian offshore (Hibernia, Hebron, Bay du Nord), LR and DNV dominate.",
     None,
     None,
     "Jim Granger Interview #23"),

    ("TÜV Nord / TÜV Rheinland", "TÜV",
     "German technical inspection associations. Dominant certification bodies in European "
     "industrial and AM sectors. Less relevant for Canadian market but important to know when "
     "discussing European competitors (FieldNode, Pelagus 3D) or European supply chains.",
     None,
     None,
     None,
     "insights.md §3"),

    ("Facility Qualification", None,
     "The one-time process by which a classification society (LR, DNV) audits and certifies "
     "an AM facility's quality management system, personnel training, machine maintenance, "
     "post-processing procedures, and CAD-to-machine translation processes. Once a facility "
     "is qualified, all subsequent parts produced there benefit from this foundation.",
     "Facility qualification is the MOAT. Atlantic XL already has LR facility qualification "
     "(first in the Americas). This means the expensive, time-consuming part of the "
     "certification process is DONE for Atlantic XL. Every part AddManuChain routes through "
     "Atlantic XL leverages this pre-built certification foundation.",
     "You don't have to go through all that qualification process every single time. That should be a prerequisite to being included in a digital inventory. — Trevor Butler, LR",
     "Use this line: 'Facility qualification is done once. We've already done the hard work through Atlantic XL — the first LR-certified AM facility in the Americas.'",
     "Trevor Butler Interview #42; Adam Saxty Interview #45"),

    ("Part Qualification", None,
     "The one-time process of certifying a specific part design for AM production. Steps: "
     "Design review, custom material specification, prototype build, destructive mechanical "
     "testing, performance validation vs. conventional equivalent. Once a part design is "
     "qualified for a specific facility, it can be re-ordered with only test-coupon verification.",
     "Part qualification is the core value of the pre-certified parts library. Each part "
     "goes through this expensive process ONCE. Subsequent orders are lightweight (print + "
     "test coupon). This is how AddManuChain amortizes certification costs across many orders.",
     None,
     None,
     "Adam Saxty Interview #45"),

    ("MMPDS (Metallic Materials Properties Development and Standardization)", "MMPDS",
     "The aerospace industry's definitive handbook of certified material properties for "
     "metals (titanium, aluminum, steel, etc.). When designing aerospace components with "
     "conventional manufacturing, engineers reference MMPDS to validate material performance. "
     "MMPDS does NOT yet contain data for additively manufactured materials — designers must "
     "generate their own material data, which is expensive and time-consuming.",
     "The MMPDS gap is the real certification barrier in aerospace (not regulatory complexity). "
     "This framing from Matthew Erning (GKN Aerospace) corrects a common misconception. "
     "When talking to aerospace contacts, use 'MMPDS gap' instead of 'certification black box.'",
     "The problem with additive right now is those material databases don't exist. — Matthew Erning, GKN Aerospace",
     "In aerospace conversations: 'We're building the AM equivalent of the MMPDS — a material database for certified additive parts.'",
     "GKN Aerospace Interview #43"),

    ("FAA PMA (Part Manufacturing Approval)", "FAA PMA",
     "The Federal Aviation Administration's approval pathway for replacement/aftermarket "
     "aviation parts that are not produced by the original equipment manufacturer. Matthew Erning "
     "at Tronosjet (PEI) achieved FAA PMA for a metal AM part — making it one of the earliest "
     "examples of a certified metal AM replacement part for aviation. Canadian equivalent: "
     "TCCA STC (Supplemental Type Certificate) or TCCA PMA.",
     "FAA PMA is the aerospace equivalent of the pre-certified parts library concept. "
     "Once a replacement part has PMA approval, it can be reproduced without full re-certification. "
     "This is the model AddManuChain should follow for marine/offshore (LR equivalent of PMA).",
     None,
     "When asked about precedents: 'This model already exists in aerospace as FAA PMA — we're applying the same logic to marine/offshore through Lloyd's Register.'",
     "GKN Aerospace Interview #43; Mark Kirby Interview #9"),

    ("C-NLOPB (Canada-Newfoundland & Labrador Offshore Petroleum Board)", "C-NLOPB",
     "The federal-provincial regulatory body governing offshore oil & gas activities in the "
     "Canada-Newfoundland and Labrador offshore area (including Hibernia, Hebron, Terra Nova, "
     "Bay du Nord). Any technology deployed offshore in Newfoundland waters must have "
     "C-NLOPB regulatory acceptance. C-NLOPB's limited technical staff means new technology "
     "review can take 1-1.5 years if the regulator is not engaged early.",
     "C-NLOPB is the gatekeeper for ALL offshore deployments in Atlantic Canada. "
     "Keith Healey's advice: engage them during R&D (not after), present quarterly milestone "
     "updates, get DNV/LR sign-off first to give C-NLOPB confidence.",
     "The biggest hurdle is the regulator itself — their limited knowledge on technology. That unfortunately makes the path longer. — Keith Healey, ERINL",
     "Never pitch an offshore deployment without mentioning C-NLOPB compliance. Say: 'We engage C-NLOPB throughout our development process, not just at the end.'",
     "Keith Healey Interview #27"),

    ("CSA (Canadian Standards Association)", "CSA",
     "Canada's primary standards development organization. Issues product safety standards "
     "(CSA sticker) for electrical equipment, pressure vessels, and other industrial components. "
     "In offshore/utility contexts, self-regulating organizations (Newfoundland utilities, "
     "offshore platforms) often write their own internal specs rather than requiring the "
     "CSA sticker — because operations are non-public and personnel are qualified.",
     "Understanding when CSA IS required (public-facing distribution equipment) vs. when it "
     "is NOT (offshore platforms, utility substations) helps you scope certification requirements "
     "correctly. Adam Chubbs (Frobisher Energy) confirmed utilities self-certify.",
     "We don't look for that sticker on the equipment. We're in a substation — not exposed to the public. — Adam Chubbs, Frobisher Energy",
     None,
     "Adam Chubbs Interview #30; Keith Healey Interview #27"),

    ("Classification Society", None,
     "Private technical organizations that set standards for the design, construction, and "
     "maintenance of ships, offshore structures, and industrial facilities. The major ones: "
     "Lloyd's Register (UK), DNV (Norway), ABS (USA), Bureau Veritas (France), ClassNK (Japan). "
     "They issue certificates of compliance and conduct surveys/audits. Important: they are "
     "NOT government regulators — they work for the operators and asset owners.",
     "Every sophisticated buyer in marine/offshore will ask 'which classification society?' "
     "Knowing that LR certified Atlantic XL (first in Americas) is your strongest credential.",
     None,
     None,
     "All LR interviews; Jim Granger Interview #23"),

    ("TRL (Technology Readiness Level)", "TRL",
     "A 1-9 scale used by NASA (and adopted by defense and industry) to measure the maturity "
     "of a technology. TRL 1 = basic research. TRL 7 = prototype in operational environment. "
     "TRL 8 = system qualified in test environment (analogous to offshore). TRL 9 = full "
     "commercial deployment. Tyler Beatty (ExxonMobil) explicitly used this framework: you "
     "must de-risk at TRL 8 (onshore analogous environment) before jumping to TRL 9 (platform).",
     "Using TRL language with technical buyers (ExxonMobil, Navy) immediately signals maturity. "
     "Position AddManuChain as TRL 8 (validated at Atlantic XL onshore) with a pathway to TRL 9.",
     "You may be trying to sell this commercial right now. We don't have a management of change order to change what's going on on the platform. — Tyler Beatty, ExxonMobil",
     "Say: 'We're currently at TRL 8 — validated at an LR-certified onshore facility. Our TRL 9 pathway is through Equinor's Bay du Nord program.'",
     "Tyler Beatty Interview #33"),
   ]
  ),

  ("3. Oil & Gas Operations Terminology",
   [
    ("FPSO (Floating Production Storage and Offloading)", "FPSO",
     "A floating vessel used to process and store crude oil or gas from nearby wells. "
     "FPSOs are moored in deep water and offload product to tankers. They are essentially "
     "floating factories — containing processing equipment, living quarters, power generation, "
     "and storage. Hibernia and Hebron (Newfoundland) are examples. FPSOs require extensive "
     "spare parts management due to remoteness and the criticality of uninterrupted production.",
     "FPSOs are the primary target customer for AddManuChain's digital inventory. Downtime "
     "on an FPSO means production stops, wells may be damaged, and costs cascade. "
     "Douglas Garcia-Golindano (Equinor) quantified this: spare parts = 1-2% of capex "
     "but protect 98% of production value.",
     "My cost is 1 to 2% of the total capex. If you don't have it, you can lose 98% of your production. — Douglas Garcia-Golindano, Equinor",
     "In pitches to O&G: 'Your 1-2% spare parts investment protects 98% of your production stream. We make that insurance policy faster and smarter.'",
     "Equinor Interview #44 (insight.md); insights.md"),

    ("Bay du Nord", None,
     "Equinor's $14 billion CAD deepwater oil development project offshore Newfoundland, "
     "approximately 500 km from shore. Conditions are harsher than the Norwegian Sea. "
     "Final Investment Decision (FID) expected 2027. First production: 2030-2033. "
     "Equinor describes it as unprecedented in terms of harsh environment and technical challenge. "
     "Local content requirements in Newfoundland may favor Canadian-based solutions.",
     "Bay du Nord is the SINGLE most compelling target project for AddManuChain in Canada. "
     "Spare parts strategy decisions are being made NOW (pre-FID). A greenfield project means "
     "no legacy systems to retrofit. Distance (500 km offshore) makes digital inventory "
     "a perfect fit — physical logistics would be prohibitively expensive.",
     "It's about 500 km from shore. Estimated $14 billion Canadian. Decision expected next year with horizon to start producing in 2030-2033. — Douglas Garcia-Golindano, Equinor",
     "Name-drop Bay du Nord specifically in every Equinor conversation and every investor pitch. It is your $14B proof-of-concept target.",
     "insight.md (Equinor Interview #44); Keith Healey Interview #27"),

    ("Cascading Shutdown", None,
     "The chain-reaction cost impact when a single component failure propagates through the "
     "entire oil & gas value chain. Example: Midstream shutoff valve fails → pipeline shuts "
     "→ upstream wells must stop → wells may be permanently damaged (re-drill costs millions) "
     "→ downstream refinery fills storage → upstream must also shut. A single part failure "
     "triggers losses far exceeding the part's value.",
     "This framing is the most powerful ROI argument for AddManuChain. Douglas (Equinor): "
     "'My midstream cost is minimal compared to what I'm causing to the whole system.' "
     "The cascading effect is multiplicative — not just the downtime cost but well damage, "
     "re-drill costs, lost refinery throughput.",
     "Upstream will not happen if midstream has a situation. — Douglas Garcia-Golindano, Equinor",
     "Start pitches with the cascade story: 'One $5,000 valve failed. Total cascading cost: $40 million. We solve that.'",
     "insight.md (Equinor Interview #44)"),

    ("Capital Maintenance", None,
     "Equinor's internal term for the strategic inventory of critical spare parts that must "
     "be maintained at all times to prevent production loss. These parts have lead times of "
     "10-18 months and their absence can trigger cascading shutdowns. Capital maintenance "
     "inventory represents 1-2% of total capex.",
     "Use 'capital maintenance' when speaking to Equinor personnel — it's their language. "
     "Frame digital inventory as the evolution of capital maintenance: from physical stock "
     "to on-demand digital production.",
     "We do what we call capital maintenance — critical spare parts that need to be maintained at all time. — Douglas Garcia-Golindano, Equinor",
     None,
     "insight.md (Equinor Interview #44)"),

    ("Long Lead Items", None,
     "Parts or equipment that require exceptionally long procurement lead times — typically "
     "10-18 months for critical O&G components such as valves, pumps, and custom completion "
     "equipment. The combination of JIT (just-in-time) inventory philosophy and long lead "
     "items creates dangerous gaps when unplanned failures occur.",
     "Long lead items are AddManuChain's primary target. Not every part — just the ones that "
     "take 10-18 months. Tyler Beatty explicitly named well casing and completion equipment "
     "as long lead items at ExxonMobil/Hibernia.",
     "Parts sometimes take 10 months, 12 months, 18 months — those are what we call critical — must be held at all time. — Douglas Garcia-Golindano, Equinor",
     "Specify: 'We target long lead items — the 10-18 month parts that cause catastrophic downtime when they fail unexpectedly.'",
     "Tyler Beatty Interview #33; insight.md"),

    ("War on Inventory", None,
     "ExxonMobil's internal term for the ongoing tension between: (1) the visible, recurring "
     "cost of holding physical spare parts inventory (warehousing, insurance, maintenance, "
     "preservation), and (2) the hidden but acute cost of hot-shotting (chartering aircraft "
     "for emergency parts delivery). Budget processes tend to cut visible inventory costs, "
     "unknowingly increasing the risk of catastrophic hot-shot expenses.",
     "This phrase was voluntarily disclosed by Tyler Beatty (ExxonMobil, 18 years). "
     "Using it in a room with ExxonMobil executives will immediately signal that you "
     "understand their world. Digital inventory resolves BOTH sides of the war simultaneously.",
     "The 'War on Inventory.' No, I'm not kidding. That's a term that I use. — Tyler Beatty, ExxonMobil",
     "Open ExxonMobil pitches with: 'You've described it internally as the War on Inventory. We end that war.'",
     "Tyler Beatty Interview #33"),

    ("Hot-Shotting", None,
     "Industry slang for emergency high-cost courier service — chartering a dedicated "
     "aircraft, helicopter, or vehicle to deliver a single critical spare part to a remote "
     "location (offshore platform, Arctic mine, remote pipeline station). Costs can reach "
     "tens of thousands of dollars per event. Tyler Beatty described chartering an aircraft "
     "'for a doorknob' as a real example.",
     "Hot-shotting is the emotional counterargument to 'we should cut inventory.' "
     "When challenging customers who say 'we've reduced our inventories to save money,' "
     "ask: 'What's your hot-shot bill?' This reframes the conversation from visible "
     "inventory costs to hidden emergency logistics costs.",
     "A super intense, high-cost courier job... you've probably heard examples of needing to charter an aircraft for a doorknob. — Tyler Beatty, ExxonMobil",
     None,
     "Tyler Beatty Interview #33"),

    ("LEAN / 5S Methodology", "LEAN",
     "A manufacturing philosophy originating at Toyota that aims to eliminate waste in "
     "all its forms (overproduction, inventory, waiting, transport, defects, motion, "
     "over-processing). 5S is a LEAN workplace organization method: Sort, Set in order, "
     "Shine, Standardize, Sustain. Douglas Garcia-Golindano (Equinor) is a LEAN Instructor "
     "and uses full value-chain process mapping + 5S for spare parts criticality analysis.",
     "LEAN practitioners are a natural audience for digital inventory BECAUSE digital inventory "
     "is the ultimate LEAN solution for spare parts: it eliminates physical waste (no stock "
     "sitting unused) while maintaining availability (JIT manufacturing). Key pitch: "
     "'Digital inventory is LEAN-compatible — eliminate waste WITHOUT the atomic bomb risk.'",
     "I have heard producers that have been hurt. Because they try to minimize cost of stores... and then you have an atomic bomb of a string die. — Douglas Garcia-Golindano, Equinor",
     "For LEAN-certified buyers: 'Digital inventory applies JIT principles to spare parts without the atomic bomb risk of inventory stockouts.'",
     "insight.md (Equinor Interview #44)"),

    ("FMEA (Failure Mode and Effects Analysis)", "FMEA",
     "A systematic engineering methodology for identifying all potential failure modes of a "
     "system, their causes, effects, and criticality. Used to prioritize maintenance, "
     "spare parts selection, and risk management. FMEA-style criticality prioritization "
     "is standard practice at Equinor for spare parts classification across full value chains.",
     "When speaking to engineers about how we identify which parts to put in the digital "
     "inventory: reference FMEA. Our parts selection process should be FMEA-driven — "
     "prioritize parts with high severity + high occurrence + low detectability.",
     None,
     None,
     "insight.md (Equinor Interview #44)"),

    ("JIT (Just-in-Time)", "JIT",
     "An inventory management philosophy that aims to reduce carrying costs by only "
     "ordering/producing parts immediately before they are needed, rather than maintaining "
     "large safety stocks. JIT reduces working capital but creates vulnerability to supply "
     "disruptions — the 'atomic bomb' risk when critical parts fail and none are on hand.",
     "Digital inventory IS the resolution to the JIT paradox for spare parts: you maintain "
     "zero physical inventory (JIT principle) but CAN produce any certified part within "
     "hours (availability guarantee). This framing resonates strongly with CFOs and "
     "LEAN practitioners.",
     "Just in time inventory is nice, but then you gotta balance that with reliability — you gotta have it. — Adam Chubbs, Frobisher Energy",
     None,
     "Adam Chubbs Interview #30; insight.md"),

    ("N+1 / N+2 Redundancy", None,
     "Equipment redundancy standards used in critical operations. N+1 means one backup "
     "unit is available if the primary fails. N+2 means two backup units are available "
     "(used in extremely critical operations like Arctic diamond mines). Beyond redundant "
     "equipment, spare parts inventory is managed at 5% of fleet size for transformers "
     "and standardized critical spares across multiple sites.",
     "N+1/N+2 redundancy is expensive infrastructure. Digital inventory is an alternative: "
     "instead of buying a $2M spare turbine, a certified digital file enables on-demand "
     "production when needed. Adam Chubbs quantified spare parts at 8-10% of total asset value "
     "for a $50M utility — a large working capital burden that digital inventory can reduce.",
     None,
     None,
     "Adam Chubbs Interview #30"),

    ("Sealift", None,
     "Seasonal resupply by ship to Arctic and remote northern communities — typically only "
     "available 2-3 months per year during summer when waters are navigable. Sealift is "
     "heavily cost-advantaged vs. year-round air freight for large/heavy items. Winter "
     "failures must use air freight at dramatically higher cost — and winter coincides with "
     "peak energy demand (worst timing for failures).",
     "Sealift logistics validates the Arctic use case for AddManuChain. On-site AM at "
     "Arctic communities eliminates both sealift waiting (months) and emergency air "
     "freight (extremely expensive) for critical parts.",
     "Most capital work is planned for summer months for sea lifts. Winter failures — the only option is flight in, which increases costs big time. — Adam Chubbs, Frobisher Energy",
     None,
     "Adam Chubbs Interview #30"),

    ("POB (Personnel on Board)", "POB",
     "The number of people on an offshore platform at any given time. Reducing POB is a "
     "key safety and operational goal — fewer people offshore means lower liability, "
     "lower helicopter costs, and reduced housing/catering requirements. Technology "
     "adoption (robotics, AI, remote operations) is primarily evaluated by its ability "
     "to reduce POB. ExxonMobil has reduced crew by 40-45% on Guyana FPSOs using AI.",
     "POB reduction is Tyler Beatty's #1 technology driver at ExxonMobil — more important "
     "than cost savings alone. Frame digital inventory as a POB-reduction tool: fewer "
     "people need to be offshore to manage, track, and deploy spare parts.",
     "Personnel onboard in the offshore is one of the main metrics in terms of value driver — we're always trying to reduce that. — Tyler Beatty, ExxonMobil",
     "Add a POB slide to your deck: 'Digital inventory reduces the need for onshore-to-offshore parts logistics personnel.'",
     "Tyler Beatty Interview #33; insight.md"),

    ("Management of Change", "MOC",
     "A formal documented process required to modify any equipment, procedure, or system "
     "on an offshore platform. MOC ensures changes are reviewed for safety, operability, "
     "and regulatory compliance before implementation. Even a seemingly minor equipment "
     "change (new part supplier, new manufacturing process) triggers an MOC review, "
     "which can take months.",
     "MOC is the procedural gatekeeping mechanism that slows AM adoption on existing platforms. "
     "Tyler Beatty used this to explain why you can't sell AddManuChain as 'install it on your "
     "platform today.' The path: pilot onshore (no MOC), generate data, then sponsor MOC approval "
     "for platform deployment.",
     "You may be trying to sell this commercial right now. We don't have a management of change order to go and change what's going on on the platform. — Tyler Beatty, ExxonMobil",
     "Acknowledge MOC proactively: 'We understand MOC requirements — that's why we start with shore-based pilot, then support your MOC process for platform deployment.'",
     "Tyler Beatty Interview #33; Kwadwo Ampofo Interview #25"),
   ]
  ),

  ("4. Supply Chain & Procurement Terms",
   [
    ("Digital Inventory", None,
     "The concept of storing parts as certified digital files (CAD + material specs + "
     "process parameters + certification documentation) rather than — or in addition to — "
     "physical spare parts. When a part is needed, it is printed on-demand at a certified "
     "facility using the pre-validated digital file, eliminating the need to hold costly "
     "physical inventory of low-frequency, high-value spare parts.",
     "Digital inventory is the core product concept of AddManuChain. Multiple industry "
     "leaders (Trevor Butler at LR, Tyler Beatty at ExxonMobil, Douglas Garcia-Golindano "
     "at Equinor) all independently validated the concept. FieldNode is the primary "
     "competitor attempting to build this, but has not yet achieved commercial traction "
     "in North America.",
     "Digital inventory and on-demand processing — it's natural table stakes. — Tyler Beatty, ExxonMobil",
     None,
     "Trevor Butler Interview #42; Tyler Beatty Interview #33; insight.md"),

    ("Pre-Certified Parts Library", None,
     "A structured digital catalog of AM-producible parts for which all upfront certification "
     "work (design review, material spec, facility qualification, part qualification) has "
     "already been completed. Subsequent orders from the library require only: printing + "
     "test coupon verification + installation survey. Eliminates the per-order certification "
     "burden, making AM economically competitive with conventional manufacturing.",
     "The pre-certified parts library is AddManuChain's core differentiator from FieldNode "
     "and other digital inventory platforms. FieldNode connects buyers to facilities; "
     "AddManuChain owns the TRUST LAYER — the certification that makes each part "
     "in the catalog safe to use and install without re-work.",
     "You don't have to go through all that qualification process every single time. That should be a prerequisite to being included in a digital inventory. — Trevor Butler, LR",
     "Pitch: 'We don't just connect you to a printer. We've already done the LR certification work so your team doesn't have to.'",
     "Trevor Butler Interview #42"),

    ("Working Capital", None,
     "The money locked up in a company's current assets (including spare parts inventory) "
     "that cannot be invested elsewhere. Kwadwo Ampofo (Deloitte SAP) identified working "
     "capital as THE primary financial pain of physical spare parts inventory — not warehouse "
     "rent or depreciation, but the opportunity cost of money tied up in sitting parts.",
     "Working capital framing elevates the conversation from Supply Chain Manager level "
     "to CFO level. CFOs own working capital decisions. Adam Chubbs quantified: "
     "$4-5M inventory for a $50M utility (8-10% ratio). Kwadwo confirmed: if it becomes "
     "a CFO problem, 'that's when decision makers do anything about this.'",
     "If it becomes a CFO problem, that's when decision makers do anything about this. — Kwadwo Ampofo, Deloitte",
     "When presenting ROI: lead with 'free up $X million in working capital' — not 'save on warehouse costs.'",
     "Kwadwo Ampofo Interview #25"),

    ("Insurance Stock", None,
     "Mandatory spare parts held 'just in case' — parts so critical that their absence "
     "could cripple the entire operation. Insurance stock is kept even if failure probability "
     "is very low. It represents the most expensive category of physical spare parts inventory "
     "because it may never be used, yet must be maintained and preserved indefinitely.",
     "Insurance stock is the highest-value target for digital inventory conversion. "
     "If AM can reliably reproduce insurance stock parts on-demand, companies can eliminate "
     "millions in tied-up working capital while maintaining (or improving) availability guarantees.",
     None,
     "Specific pitch: 'Convert your insurance stock to digital. Same availability guarantee, zero working capital trapped.'",
     "Kwadwo Ampofo Interview #25"),

    ("Obsolescence", None,
     "The stage reached when a manufacturer stops producing a specific part entirely (beyond "
     "'legacy' — the interim stage when support is reduced but parts are still available). "
     "Darren Wood (Proax): 'Legacy → Obsolescence is the progression. I deal with that all "
     "the time.' Obsolescence forces companies to choose between: full equipment replacement "
     "(very expensive), engineering retrofit with non-spec parts (MOC required), or "
     "custom AM reproduction (AddManuChain's answer).",
     "Obsolescence is the #1 adoption driver for AM in industrial settings — confirmed by "
     "Sean Morgan (Atlantic XL), Darren Wood (Proax), Kwadwo Ampofo (Deloitte), and the "
     "Executive Summary. Target companies with 15-20 year old install bases where parts "
     "are entering obsolescence.",
     "You're dealing with people who have an install base from 15, 20 years ago... at one point those parts went into legacy, and then obsolescence. I deal with that all the time. — Darren Wood, Proax",
     "Ask prospects: 'What's your oldest installed equipment? What happens when those parts enter obsolescence?' Then show them AddManuChain.",
     "Darren Wood Interview #29; Sean Morgan Executive Summary"),

    ("ERP / SAP S/4HANA", "ERP",
     "Enterprise Resource Planning — integrated software that manages business processes "
     "including procurement, inventory, production planning, and maintenance. SAP S/4HANA "
     "is the dominant ERP platform in large industrial companies. Within SAP: MM (Materials "
     "Management), PM (Plant Maintenance), QM (Quality Management) are the relevant modules "
     "for digital inventory integration.",
     "ERP integration is technically feasible per Kwadwo Ampofo (Deloitte SAP Architect): "
     "defining AM parts as 'make in-house' in the material master allows the MRP engine "
     "to compare lead times and costs for physical vs. digital production. No company has "
     "done this yet — first-mover opportunity.",
     "I know the system well enough to know it can happen. I've never seen any company do it. — Kwadwo Ampofo, Deloitte",
     "For enterprise customers: 'We integrate natively with SAP — your MRP engine automatically compares supplier lead times vs. our print times.'",
     "Kwadwo Ampofo Interview #25"),

    ("MRP (Material Requirements Planning)", "MRP",
     "The planning engine within ERP systems (SAP MRP, Oracle, etc.) that calculates what "
     "materials are needed, when they are needed, and whether to buy or make them. MRP "
     "compares reorder points, lead times, and safety stock levels to generate purchase "
     "orders or production orders automatically. Kwadwo Ampofo explained how MRP could "
     "be configured to include digital AM production as a 'make' option alongside traditional "
     "procurement.",
     None,
     None,
     None,
     "Kwadwo Ampofo Interview #25"),

    ("EDI (Electronic Data Interchange)", "EDI",
     "A standardized electronic format for business-to-business data exchange — purchase "
     "orders, invoices, inventory updates — transmitted directly between ERP systems "
     "without human intervention. Darren Wood (Proax) confirmed large customers use EDI "
     "to order directly from Proax's ERP system. AddManuChain should offer EDI integration "
     "as part of enterprise offerings.",
     None,
     None,
     None,
     "Darren Wood Interview #29"),

    ("Vendor Diversification", None,
     "The procurement strategy of qualifying multiple suppliers for critical parts to "
     "reduce dependency on any single vendor. At Equinor, when a critical part fails "
     "and the primary vendor cannot supply quickly, procurement teams check alternative "
     "vendors — but proprietary/IP agreements often limit which vendors can legally "
     "supply certain parts.",
     "IP constraints in conventional procurement validate that IP protection is already "
     "a known challenge — not unique to digital inventory. Frame AddManuChain as a "
     "SOLUTION to the vendor diversification problem: 'We add certified AM as an "
     "additional qualified vendor for your critical parts.'",
     "You have to have diversification. Sometimes among those vendors there's proprietary information that needs to be in agreement. — Douglas Garcia-Golindano, Equinor",
     None,
     "insight.md (Equinor Interview #44)"),

    ("Consignment Model", None,
     "A supply arrangement where an OEM or distributor stocks parts at the customer's "
     "facility, with the customer paying only when parts are actually consumed (monthly "
     "audit). Kwadwo Ampofo noted Equinor and other major operators use consignment "
     "arrangements with OEMs. This eliminates working capital for the customer while "
     "maintaining availability.",
     "The consignment model is relevant to AddManuChain's revenue model: instead of "
     "customers paying for physical inventory upfront, they pay a subscription/access "
     "fee for digital file availability, then pay per-print when parts are needed.",
     None,
     None,
     "Kwadwo Ampofo Interview #25"),
   ]
  ),

  ("5. Navy, Defense & Marine Terms",
   [
    ("ILS (Integrated Logistics Support)", "ILS",
     "A military lifecycle management discipline that encompasses all logistics elements "
     "required to support a defense system throughout its operational life: maintenance "
     "manuals, spare parts lists, technical publications, training, test equipment, "
     "and facilities. Every component on a Canadian Navy ship has an ILS plan linked to "
     "its preventive maintenance schedule.",
     "ILS is the direct framing for AddManuChain in defense contexts. Aaron Plamondon "
     "(Irving Shipbuilding) introduced this term. Digital inventory = ILS modernization. "
     "Frame platform as 'ILS digitization tool' when talking to DND, Irving, or Thales.",
     "The data goes back 20 years... digitizing it, that's a great idea. — Aaron Plamondon, Irving Shipbuilding",
     "For defense: 'AddManuChain modernizes your ILS — converting physical spare parts lists into certified digital inventory.'",
     "Aaron Plamondon Interview #34"),

    ("IPMS (Integrated Platform Management System)", "IPMS",
     "The computerized system used aboard naval vessels to monitor and control ship systems "
     "(propulsion, damage control, power management, machinery). L3 Harris (L3 MAPPS, "
     "Montreal) provides IPMS for both Halifax-class frigates and the future CSC (Canadian "
     "Surface Combatant). L3 Harris is the incumbent on Navy predictive maintenance; "
     "they seized data from National Defence faster than Irving/Dalhousie.",
     "L3 Harris is an incumbent in the Navy space. AddManuChain should seek to partner "
     "with or integrate alongside L3 Harris IPMS — not compete with them. The angle: "
     "IPMS tells you a part is degrading; AddManuChain delivers the replacement part.",
     None,
     "Position alongside IPMS: 'IPMS predicts what will fail next. AddManuChain makes sure the replacement part is ready when you need it.'",
     "Aaron Plamondon Interview #34"),

    ("AOPS (Arctic and Offshore Patrol Ship)", "AOPS",
     "Canada's fleet of Arctic patrol vessels — 6 Navy ships all complete, 2 Coast Guard "
     "ships in production. In-service support managed by Thales (not Irving). "
     "Lee Vessey at Thales is confirmed as the correct contact for AOPS spare parts strategy.",
     "AOPS is a near-term target because: (1) fleet recently deployed, long service life "
     "ahead, (2) Thales manages spares strategy (Lee Vessey is your contact), (3) Arctic "
     "operations = extreme logistics challenges = high value for AM/digital inventory.",
     None,
     None,
     "Aaron Plamondon Interview #34"),

    ("CSC (Canadian Surface Combatant)", "CSC",
     "Canada's largest-ever defense procurement — the replacement program for the Halifax- "
     "class frigates. Massive multi-decade investment. Irving Shipbuilding builds the ships; "
     "L3 Harris is supplying IPMS. The CSC program is actively designing maintenance and "
     "logistics strategies — a potential 20-year opportunity for digital inventory integration "
     "if AddManuChain is embedded in the program early.",
     "CSC is a greenfield opportunity (being designed now) — analogous to Bay du Nord "
     "for the Navy. Getting into CSC's spare parts architecture at the design stage is "
     "far easier than retrofitting later. Aaron Plamondon (Irving) is the entry point.",
     None,
     None,
     "Aaron Plamondon Interview #34"),

    ("AOR / JSS (Auxiliary Oiler Replenishment / Joint Support Ship)", "AOR/JSS",
     "Naval support/replenishment vessels designed to resupply combat ships at sea with "
     "fuel, ammunition, food, and spare parts. Dave Whitehouse (LR Naval) identified AOR/JSS "
     "as the correct platform for ship-based AM (not combat ships) because: they are designed "
     "for containerized modules, have more space, and are not subject to the same shock/vibration "
     "requirements as frigates.",
     "AOR/JSS is the right naval architecture for embedded AM capability — frame it as a "
     "'forward-deployed AM node' that travels with the fleet. This preserves combat ship "
     "readiness while bringing fabrication capability forward.",
     "I would think rather than on a combat vessel, it's more likely you put them on an AOR or JSS — they're already designed to have containerized modules. — Dave Whitehouse, LR",
     "Naval pitch: 'We propose containerized AM modules for AOR/JSS vessels — a floating digital inventory hub for fleet maintenance.'",
     "Dave Whitehouse Interview #46"),

    ("River-Class Destroyers", None,
     "Canada's planned next-generation destroyer program — the successors to the Halifax- "
     "class frigates (which succeed the CSC). Still conceptual but raised by both Trevor "
     "Butler and Dave Whitehouse (LR) as a potential future AddManuChain opportunity, "
     "particularly with on-vessel printing and Canadian-sovereign data protection requirements.",
     None,
     "Maybe in some not-so-wild future, those destroyers would have a printer onboard. The Canadian Navy would want some level of protection — you guys being Canadian-based — that could be a differentiator. — Trevor Butler, LR",
     None,
     "Trevor Butler Interview #42; Dave Whitehouse Interview #46"),

    ("Victoria-Class Submarines", None,
     "Canada's current fleet of 4 decommissioned British Upholder-class submarines "
     "(purchased 1998). Key characteristic: all 4 are custom-built slightly differently, "
     "with no original spare parts remaining in inventory. 'As-built' certification "
     "requires replacement parts to exactly replicate the original install condition — "
     "even for ships 20-30 years old with only 5-10 years of service life remaining.",
     "Dave Whitehouse's submarine case study is your most powerful Navy pitch. The absurdity "
     "of applying full as-built certification to a 30-year-old submarine with 10 years left "
     "perfectly crystallizes the AM value proposition: scan the original part, certify the "
     "digital file, print on demand.",
     "Why are you putting an as-built part in when you may only need it for 10 years? The philosophy around using AM parts in a maintenance program hasn't really been thought through. — Dave Whitehouse, LR",
     "Open Navy pitches with the submarine story: '4 submarines, each custom-built, no original parts left. Every repair requires custom as-built manufacturing. We digitize the as-built record and print on demand.'",
     "Dave Whitehouse Interview #46"),

    ("ITB (Industrial and Technological Benefits)", "ITB",
     "A Canadian defence procurement policy requiring companies that win defence contracts "
     "to generate offsetting economic benefits in Canada equal to the value of the contract. "
     "ITB benefits are generated in specific categories including R&D (with university "
     "multipliers), manufacturing, and SME engagement. Aaron Plamondon (Irving ITB Director) "
     "confirmed: if AddManuChain generates value for Irving AND the Navy, Irving can fund it "
     "through ITB credits.",
     "ITB is the funding unlock for Navy/defence engagement. Irving Shipbuilding has an "
     "ITB obligation on the CSC program — AddManuChain can generate ITB credits for Irving "
     "through Dalhousie university R&D collaboration. This is a non-dilutive funding pathway.",
     "The real thing you want to zone in on is: why would Irving do it? What's in it for Irving? — Aaron Plamondon, Irving Shipbuilding",
     "For Irving pitch: 'We generate ITB credit for you through Dalhousie R&D AND solve your Halifax-class maintenance problem.'",
     "Aaron Plamondon Interview #34"),

    ("DeepSense (Dalhousie)", None,
     "An ocean data innovation environment at Dalhousie University, Halifax, using AI/ML "
     "for ocean sector challenges. Partnered with IBM high-performance computing. Focus: "
     "fisheries, shipping, offshore energy, environmental monitoring. Attempted a Halifax- "
     "class predictive maintenance project with Irving (failed — estimated 3 years, Irving "
     "said too slow; L3 Harris then took over).",
     "DeepSense could be a research collaboration partner for the AI/data analytics layer "
     "of AddManuChain. The failed Irving-DeepSense project created a warm introduction "
     "opportunity — Aaron Plamondon offered to connect.",
     None,
     None,
     "Aaron Plamondon Interview #34"),
   ]
  ),

  ("6. Industry Organizations & Key Programs",
   [
    ("FieldNode", None,
     "A digital inventory and AM marketplace platform backed by oil & gas majors "
     "(Shell, BP, ExxonMobil, TotalEnergies, Equinor). Positioned as the industry "
     "standard for digital AM inventory in oil & gas. European-centric, enterprise-only, "
     "complex implementation. Trevor Butler (LR) named it as AddManuChain's primary "
     "competitor. Sean Morgan (Atlantic XL): 'None of them seem to have taken up yet.'",
     "FieldNode is your primary competitor — know it inside and out. Your differentiation: "
     "(1) Canada-first, sovereign supply chain; (2) we HANDLE certification end-to-end "
     "(FieldNode is software only); (3) we sell TRUST (LR-backed certified parts), "
     "not just connectivity; (4) we serve mid-market, not just Majors.",
     "Not to be a bit of a downer, but FieldNode already has this. — Trevor Butler, LR  |  Differentiation accepted: 'That's interesting. I would agree.' — Trevor Butler",
     "Always pre-empt by naming FieldNode: 'You may be aware of FieldNode — we differ in three ways: [cert layer, Canada-first, trust-selling].'",
     "Trevor Butler Interview #42; Tyler Beatty Interview #33; Sean Morgan Executive Summary"),

    ("Pelagus 3D", None,
     "A marine AM digital inventory platform — a joint venture between thyssenkrupp "
     "and Wilhelmsen, launched September 2023. Headquartered in Singapore. Marine-only focus, "
     "Asia-Pacific centric. Sean Morgan (Atlantic XL) confirmed: 'None of them seem to have "
     "taken up yet' — not yet commercially successful.",
     "Pelagus 3D validates the market (two industry giants bet on it) but confirms the "
     "opportunity is still open. Your advantage: faster, North American focus, multi-industry "
     "(not marine-only), and you actually manage the certification layer.",
     "None of them seem to have taken up yet. There is definitely a solid opportunity there. — Sean Morgan, Atlantic XL",
     "Mention Pelagus 3D to show market validation: 'thyssenkrupp and Wilhelmsen launched Pelagus 3D in 2023 — proof that major players see this market. They haven't yet won it.'",
     "Sean Morgan Executive Summary"),

    ("NGen (Next Generation Manufacturing Canada)", "NGen",
     "Canada's Advanced Manufacturing supercluster — a pan-Canadian industry-government "
     "consortium that funds manufacturing innovation projects and provides market access. "
     "Frank DeFalco (Director of Member Engagement, NGen) is a warm contact. NGen member "
     "companies represent hundreds of Canadian manufacturers across all sectors.",
     "NGen is a potential funding pathway AND market access channel. Frank DeFalco validated "
     "that large OEMs (100,000+ part inventories) are actively looking for digital inventory "
     "solutions. NGen's AM Demo Program could be a validation vehicle for AddManuChain.",
     "We've been engaging with some of the larger companies... they have inventories of hundreds of thousands of parts... and they're looking for solutions of 'is digital inventory even a possibility?' — Frank DeFalco, NGen",
     None,
     "Frank DeFalco Interview #8"),

    ("Canada Makes", None,
     "Canada's national AM industry network — facilitates connections between companies, "
     "labs, and service providers in the AM sector. Developed the 'Select AM' tool: "
     "an AI system that helps companies with 100,000+ part inventories identify which "
     "~10% are AM candidates. Mark Kirby (Tronosjet, former Renishaw) is the Select AM "
     "developer and a direct contact.",
     "Canada Makes is a potential PARTNER, not a competitor. Their Select AM tool identifies "
     "AM candidates; AddManuChain provides the business case, certification, facility matching, "
     "and digital inventory management. Strategy: 'Select AM identifies → AddManuChain executes.'",
     None,
     "Suggested pitch positioning: 'Canada Makes identifies the parts. We certify them, manage the digital file, and print on demand.'",
     "Frank DeFalco Interview #8; Mark Kirby Interview #9"),

    ("ERINL (Energy Research Initiative — Newfoundland & Labrador)", "ERINL",
     "A Newfoundland provincial R&D funding organization focused on energy innovation. "
     "Keith Healey (former Suncor/ExxonMobil R&D) is an R&D Project Manager there. "
     "ERINL funds technology demonstration projects in collaboration with offshore operators. "
     "Critically: they will fund certification studies (CSA, DNV, LR), not just R&D — "
     "confirmed by Keith Healey ('We provided funding to help a startup get CSA certification done').",
     "ERINL is a non-dilutive funding source specifically for offshore innovation in "
     "Newfoundland. Apply for 'regulatory de-risking funding' (LR/DNV certification costs) "
     "rather than just pilot project funding. Keith Healey is your direct contact.",
     "What we did then was provide funding to help this startup get that CSA certification done. — Keith Healey, ERINL",
     "Frame ERINL application as 'regulatory de-risking' not 'product development.' Ask for LR certification cost coverage.",
     "Keith Healey Interview #27"),

    ("MAMCE (Maritime Additive Manufacturing Centre of Excellence)", "MAMCE",
     "A Halifax-based initiative bringing together Irving Shipbuilding, Dalhousie University, "
     "and the Federal Government to advance AM for Canadian naval applications. Dr. Mohsen "
     "Mohammadi (Dalhousie) leads material certification research. Aaron Plamondon (Irving) "
     "confirms MAMCE is currently stalled — unable to get Navy sign-off despite years of effort.",
     "MAMCE stalling validates the 'governance, not technology' barrier framework. "
     "It also means Dr. Mohammadi's material certification expertise is potentially "
     "available for partnership if the Feb 18 Fleet Admiral visit to Dalhousie reignites "
     "interest.",
     None,
     None,
     "Aaron Plamondon Interview #34"),

    ("SMART Lab (Memorial University)", "SMART Lab",
     "ExxonMobil's $17.5M investment in Memorial University of Newfoundland — a full metals "
     "additive manufacturing lab covering the complete supply chain: materials, printing, "
     "certification, and testing. Led by Dr. Ahmed Arubi. Tyler Beatty (ExxonMobil) personally "
     "directed this investment. Researchers are being brought to CanMap Materials Lab in "
     "Ontario in March 2026.",
     "SMART Lab is a potential testing/certification partner for AddManuChain. Tyler Beatty "
     "offered to introduce Dr. Arubi. A partnership here gives AddManuChain access to "
     "$17.5M in infrastructure without owning it — and connects ExxonMobil's AM commitment "
     "to your platform.",
     "The cost to me was $17.5 million. I guess that should tell you the level of commitment. — Tyler Beatty, ExxonMobil",
     "Mention SMART Lab as your research partner: 'We're working with ExxonMobil's $17.5M AM lab at Memorial University to validate our certification process.'",
     "Tyler Beatty Interview #33"),

    ("C-CORE", None,
     "A Canadian-based research centre specializing in offshore technology validation, "
     "ice engineering, and remote sensing. Used by C-NLOPB and operators for technology "
     "validation studies (impact studies, model validation) before regulatory approval. "
     "Keith Healey (ERINL) mentioned C-CORE as the organization to conduct offshore "
     "technology validation studies required by C-NLOPB.",
     "C-CORE is required for C-NLOPB regulatory pathway. Include C-CORE validation studies "
     "in any budget for offshore deployment. Engage C-CORE during R&D phase (not after) "
     "per Keith Healey's advice.",
     None,
     None,
     "Keith Healey Interview #27"),
   ]
  ),

  ("7. Aerospace-Specific Terms",
   [
    ("Platform Certification (Aerospace)", None,
     "In civil aviation, regulators (FAA, EASA, TCCA) certify entire aircraft platforms "
     "(e.g., Boeing 737) — not individual parts. Parts are qualified to support platform "
     "certification, but the regulatory approval is at the aircraft level. This is "
     "fundamentally different from marine/offshore where parts and facilities are individually "
     "certified.",
     "Understanding this distinction prevents a common mistake in pitch: conflating aerospace "
     "certification with marine/offshore. In aerospace, the platform owner (Boeing) manages "
     "certification; in marine/offshore, the operator (Equinor, Navy) manages it through "
     "class societies. Different buyers, different processes.",
     "Typically, you don't have individual parts that are certified. Platforms are certified. — Matthew Erning, GKN Aerospace",
     "When an aerospace contact asks about certification: 'We operate in the marine/offshore space where LR certifies parts and facilities — similar to PMA but for maritime.'",
     "GKN Aerospace Interview #43"),

    ("PEEK (Polyether ether ketone)", "PEEK",
     "A high-performance engineering polymer with exceptional mechanical properties, chemical "
     "resistance, and thermal stability (continuous use up to 260°C). Considered the gold "
     "standard for polymer AM in aerospace — aerospace manufacturers evaluate AM suppliers "
     "primarily on PEEK print capability. Vertical burn test (flame retardancy) is the critical "
     "PEEK certification hurdle.",
     "Shawn Sooley identified PEEK as the gating material for aerospace credibility: "
     "'Aerospace won't talk to you unless you can print PEEK.' Achieving PEEK capability "
     "is a prerequisite for the aerospace-first credentialing strategy.",
     "Aerospace won't talk to you unless you can print PEEK. — Shawn Sooley, Shield Group",
     "If asked about polymer AM capability: 'We support PEEK printing for aerospace-grade applications, with vertical burn test compliance.'",
     "Shawn Sooley Interview #32"),

    ("Value–Capability–Permission Venn", None,
     "Tyler Beatty's (ExxonMobil) framework for diagnosing why AM adoption in offshore "
     "O&G is stalled despite proven technology. Three overlapping circles: (1) Value — "
     "supply chain elimination, POB reduction, carbon reduction (PROVEN). (2) Capability — "
     "can you print a part that does the job? (PROVEN). (3) Permission — certification/regulatory "
     "approval (BLOCKED — 'certifying authorities haven't led the charge').",
     "This framework is the most credible, operator-level diagnosis of the AM adoption "
     "problem. Use it in every pitch to sophisticated audiences. Position AddManuChain "
     "as the 'Permission solver' — the entity that closes the gap between proven capability "
     "and regulatory acceptance.",
     "Certifying authorities haven't led the charge towards 3D printing and additive manufacturing application in the offshore. — Tyler Beatty, ExxonMobil",
     "Draw this Venn diagram in pitches: 'Value? Proven. Capability? Proven. Permission? That's our product.'",
     "Tyler Beatty Interview #33"),

    ("In-Process Monitoring", None,
     "The emerging approach of certifying AM parts through real-time sensor monitoring "
     "during the print process (layer-by-layer thermal imaging, melt-pool analysis, "
     "acoustic emission detection) rather than through post-print destructive testing. "
     "Adam Saxty (LR) identified this as LR's long-term R&D direction — it would eventually "
     "replace test coupons and solve the machine variability problem.",
     "In-process monitoring is the future technical roadmap for AM certification. A research "
     "partnership with LR on in-process monitoring (aligned with Dr. Ali Nasiri's work at "
     "Dalhousie) could give AddManuChain early access to next-generation certification "
     "technology and a long-term technical moat.",
     "That is our future end goal. I can't say we would do it commercially tomorrow — we don't know yet. — Adam Saxty, LR",
     None,
     "Adam Saxty Interview #45"),

    ("Machine Variability", None,
     "The challenge that AM parts qualified on one specific machine may not produce "
     "identical results on a different machine — even from the same manufacturer. "
     "No universal cross-machine parameter equivalency standards exist. This is the "
     "primary technical barrier to on-site and on-vessel AM printing, because it is "
     "difficult to guarantee that a remote machine will produce a part equivalent to the "
     "qualified benchmark.",
     "Machine variability explains why shore-based certified facilities (Atlantic XL model) "
     "are the correct short-term strategy — not on-vessel printing. Understanding this "
     "limitation signals technical maturity to class societies and sophisticated operators.",
     "What if you qualified a part on one machine, but then you wanted to print it on a machine in the middle of the Atlantic Ocean on an offshore rig? — Adam Saxty, LR",
     "When asked about on-vessel printing: 'Machine variability is the unsolved technical challenge for on-vessel AM. Our short-term model uses shore-based LR-certified facilities while LR R&D solves machine variability.'",
     "Adam Saxty Interview #45"),
   ]
  ),

  ("8. Business & Market Frameworks",
   [
    ("Post-COVID Supply Chain Reset", None,
     "The fundamental restructuring of global supply chains following COVID-19, wherein "
     "manufacturers eliminated buffer stocks in favor of pre-ordered inventory (12+ week "
     "lead times). Sean Morgan (Atlantic XL): 'Nobody carries stock. Everything should be "
     "pre-ordered. It fundamentally changed the supply chain.' The result: a permanent gap "
     "between 'need now' (emergency breakdowns) and 'can get in 3 months' (pre-order lead time).",
     "Post-COVID supply chain disruption is the macro tailwind for AddManuChain. "
     "The traditional 'order from stock' model is dead. AM fills the gap between emergency "
     "need and 12-week pre-order lead times. This framing resonates with procurement "
     "leaders and CFOs who lived through COVID supply constraints.",
     "Nobody carries stock. Everything should be pre-ordered... it fundamentally changed the supply chain. — Sean Morgan, Atlantic XL",
     "Open market context slides with: 'Post-COVID, nobody carries stock. Everything requires 12-week pre-orders. We bridge that gap.'",
     "Sean Morgan Executive Summary"),

    ("AM Adoption Phases", None,
     "Sean Morgan (Atlantic XL) identified the three phases of AM adoption in industry: "
     "Phase 1 — Emergency use only (downtime cost justifies risk); Phase 2 — Success builds "
     "comfort (regular use begins); Phase 3 — Design innovation (beyond replication, new "
     "geometries). Most offshore/marine companies are at Phase 1 or transitioning to Phase 2.",
     "Understanding adoption phases helps target the right message: Phase 1 companies need "
     "'emergency downtime solution'; Phase 2 companies need 'reliability and scale'; "
     "Phase 3 companies need 'design optimization tools.' Tailor pitch to phase.",
     None,
     "Segment your pitch by adoption phase. Ask: 'Have you used AM for an emergency repair yet?' — that places them in Phase 1 or 2.",
     "Sean Morgan Executive Summary"),

    ("Aerospace-First Strategy", None,
     "Shawn Sooley's (Shield Group) contrarian recommendation: pursue aerospace AM "
     "certification FIRST (the hardest), then approach oil & gas. Logic: aerospace "
     "certification is more stringent than O&G class society requirements. When approaching "
     "ExxonMobil/Equinor after achieving aerospace certification: 'You think your Lloyd's "
     "requirements are more stringent than aerospace? No.' The invisible certification "
     "barrier dissolves instantly.",
     "This strategy has high upfront cost and time (aerospace cert is expensive) but "
     "eliminates the #1 objection in O&G forever. Aligns with ITB program (government "
     "aerospace contracts can fund certification). Consider as 2026-2027 roadmap item.",
     "You break through to the aerospace world and approach Exxon — you really think your rules are going to be more stringent than aerospace? No. That invisible barrier goes away. It's gone. — Shawn Sooley, Shield Group",
     None,
     "Shawn Sooley Interview #32"),

    ("Don't Sell AI — Sell the Solution", None,
     "Shawn Sooley's critical advice against leading with AI as a feature. Reasons: "
     "(1) Predictive maintenance software already exists as commodities; (2) Buyers "
     "perceive AI-generated work as 'too easy' → feel overcharged; (3) Rapid AI evolution "
     "creates perpetual deferral ('I'll wait for the better version next month'). "
     "Correct approach: lead with the PROBLEM ('unplanned downtime in remote operations') "
     "and OUTCOME ('certified parts in 48 hours'). AI is a backend feature.",
     "This advice came independently from multiple interviewees (Shawn Sooley, GKN Aerospace, "
     "Kwadwo Ampofo). Consistent pattern: AI pitches trigger skepticism; outcome pitches "
     "trigger interest. Remove 'AI-powered' from all headline slides.",
     "I think you're going to have a really hard sell with selling AI. You need to give a solution. — Shawn Sooley, Shield Group",
     "Replace: 'AI-powered digital inventory platform' → 'Certified spare parts delivered in 48 hours — guaranteed.' AI is described in the 'how we do it' section, not the headline.",
     "Shawn Sooley Interview #32"),

    ("Greenfield vs. Retrofit Strategy", None,
     "The business development principle of targeting new projects (greenfield) where "
     "systems are being designed from scratch, rather than trying to retrofit into "
     "established operations. Keith Healey: 'The key to breaking into industries is with "
     "a new project.' Bay du Nord (FID 2027) and CSC (design phase) are both greenfield "
     "targets where digital inventory can be embedded from day one.",
     "Both Bay du Nord (O&G) and CSC (Navy) are currently in design phases — the ideal "
     "time to influence spare parts architecture decisions. Once operational, MOC "
     "requirements make changes extremely expensive.",
     "I think the key to breaking into industries is with a new project. — Keith Healey, ERINL",
     "Always frame Bay du Nord and CSC as greenfield opportunities: 'The spare parts architecture is being designed right now — before operations begin.'",
     "Keith Healey Interview #27; Tyler Beatty Interview #33"),

    ("Sovereign Supply Chain", None,
     "The principle of maintaining domestic (within-Canada) production capability for "
     "critical parts to avoid dependency on foreign suppliers, esp. in defense, energy, "
     "and critical infrastructure. Trevor Butler, Dave Whitehouse, and Aaron Plamondon "
     "all referenced Canadian domestic sourcing mandates (DND, defense procurement) "
     "as a driver for Canadian-based AM platforms.",
     "Sovereign supply chain is the geopolitical tailwind for AddManuChain. Use it in "
     "DND, PSPC (Public Services and Procurement Canada), and political pitches. "
     "The River-class destroyer example: Navy wants a Canadian-based platform for IP "
     "protection on printed parts.",
     "You guys being Canadian-based — that could definitely be something to look towards as a differentiator. — Trevor Butler, LR",
     None,
     "Trevor Butler Interview #42; Dave Whitehouse Interview #46; Aaron Plamondon Interview #34"),

    ("1% Capex Protects 99% Production (ROI Frame)", None,
     "Douglas Garcia-Golindano's (Equinor) most powerful articulation of the spare parts "
     "value proposition: spare parts inventory is typically 1-2% of total capex, but its "
     "absence can halt 98-99% of production value through cascading shutdowns. This reframes "
     "digital inventory from a cost reduction play to a PRODUCTION ASSURANCE play.",
     "This is the single most powerful ROI framing in 44+ interviews. Use it as the "
     "opening hook for any CFO or VP Operations audience. More impactful than any cost "
     "comparison because it speaks in terms of production value, not warehouse savings.",
     "My cost is 1 to 2% of the total capex. If you don't have it, you can lose 98% of your production. — Douglas Garcia-Golindano, Equinor",
     "Open financial pitch with: 'Your spare parts investment is 1-2% of total capex. It protects 98% of your production value. What if you could guarantee availability of those parts in hours instead of 10-18 months?'",
     "insight.md (Equinor Interview #44)"),
   ]
  ),
]

# ─────────────────────────────────────────────────────────────
# PDF BUILDER
# ─────────────────────────────────────────────────────────────

def build_colored_header(text, bg_color, text_style):
    """Return a Table with a colored background for section headers."""
    data = [[Paragraph(text, text_style)]]
    t = Table(data, colWidths=[7.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t


def build_term_block(term, abbrev, definition, why_matters, quote, pitch_tip, ref, idx):
    """Build a single term entry as a list of flowables."""
    parts = []
    bg = PALE_BG if idx % 2 == 0 else WHITE

    # Term name line
    abbrev_str = f"  [{abbrev}]" if abbrev else ""
    parts.append(Paragraph(f"{term}{abbrev_str}", TERM_NAME))

    # Definition
    parts.append(Paragraph(definition, BODY_STYLE))

    # Why it matters
    if why_matters:
        parts.append(Paragraph(f"<b>Why it matters:</b> {why_matters}", BODY_STYLE))

    # Quote
    if quote:
        parts.append(Paragraph(f"❝ {quote}", QUOTE_STYLE))

    # Pitch tip
    if pitch_tip:
        parts.append(Paragraph(f"✅ Pitch tip: {pitch_tip}", PITCH_STYLE))

    # Source reference
    if ref:
        parts.append(Paragraph(f"Source: {ref}", REF_STYLE))

    parts.append(HRFlowable(width="100%", thickness=0.5,
                             color=colors.HexColor("#D5D8DC"), spaceAfter=4))
    return parts


def on_page(canvas, doc):
    """Header and footer on every page."""
    canvas.saveState()
    W, H = letter

    # Top stripe
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - 28, W, 28, fill=1, stroke=0)

    # Header text
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(36, H - 18, "AddManuChain  |  Industry Terms & Vocabulary Guide")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(W - 36, H - 18, "CONFIDENTIAL  —  February 2026")

    # Footer
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, W, 22, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#BDC3C7"))
    canvas.drawString(36, 7, "Prepared for Mahmoud (Michael) Kiasari  |  Lab2Market / AddManuChain")
    canvas.setFillColor(GOLD)
    canvas.drawRightString(W - 36, 7, f"Page {doc.page}")

    canvas.restoreState()


def build_cover():
    """Cover page."""
    W, H = letter
    elements = []

    # Big colored cover background — use a big table spanning full page
    cover_data = [[""]]
    cover_table = Table(cover_data, colWidths=[7.5 * inch], rowHeights=[9.8 * inch])
    cover_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
    ]))
    # We'll just add paragraphs with custom styles
    elements.append(Spacer(1, 1.2 * inch))

    # Gold rule
    elements.append(HRFlowable(width="100%", thickness=3,
                                 color=GOLD, spaceAfter=24, spaceBefore=0))

    elements.append(Paragraph("ADDMANUCHAIN", COVER_TITLE))
    elements.append(Spacer(1, 0.1 * inch))
    elements.append(Paragraph("Industry Terms & Vocabulary Master Guide", COVER_SUB))
    elements.append(Spacer(1, 0.15 * inch))
    elements.append(Paragraph(
        "Essential language for executive conversations in Additive Manufacturing,\n"
        "Offshore Oil & Gas, Naval Defense, and Supply Chain Innovation",
        COVER_BODY))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(HRFlowable(width="60%", thickness=1,
                                 color=GOLD, spaceAfter=20))

    elements.append(Paragraph(
        f"Distilled from 44+ customer discovery interviews\n"
        f"with executives at ExxonMobil, Equinor, Lloyd's Register,\n"
        f"GKN Aerospace, Irving Shipbuilding, MAN Energy, NGen, Deloitte & more.",
        COVER_BODY))

    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(
        f"Prepared for: Mahmoud (Michael) Kiasari\n"
        f"Lab2Market Cohort — February 21, 2026\n"
        f"CONFIDENTIAL",
        COVER_BODY))

    elements.append(HRFlowable(width="100%", thickness=3,
                                 color=GOLD, spaceBefore=30, spaceAfter=0))

    elements.append(PageBreak())
    return elements


def build_toc():
    """Table of contents."""
    elements = []
    elements.append(build_colored_header("TABLE OF CONTENTS", NAVY, SECTION_HDR))
    elements.append(Spacer(1, 0.2 * inch))

    for i, (cat_name, terms) in enumerate(CATEGORIES, 1):
        elements.append(Paragraph(f"{cat_name}", TOC_CAT))
        for term, abbrev, *_ in terms:
            abbrev_str = f"  [{abbrev}]" if abbrev else ""
            elements.append(Paragraph(f"   • {term}{abbrev_str}", TOC_STYLE))
        elements.append(Spacer(1, 0.05 * inch))

    elements.append(PageBreak())
    return elements


def build_how_to_use():
    """How to use this guide page."""
    elements = []
    elements.append(build_colored_header("HOW TO USE THIS GUIDE", STEEL_BLUE, SECTION_HDR))
    elements.append(Spacer(1, 0.15 * inch))

    intro = (
        "This guide compiles every critical term, framework, and piece of industry vocabulary "
        "extracted from 44+ customer discovery interviews conducted between January–February 2026. "
        "It is designed to prepare you for high-stakes conversations with executives at "
        "oil & gas majors, classification societies, naval defense organizations, and "
        "advanced manufacturing bodies.\n\n"
        "Each entry includes:\n"
        "• <b>Definition</b> — precise, industry-accurate explanation\n"
        "• <b>Why it matters</b> — strategic importance for AddManuChain\n"
        "• <b>Key quote</b> — direct words from industry leaders who validated this term\n"
        "• <b>Pitch tip</b> — how to use this term in conversations\n"
        "• <b>Source</b> — which interview(s) surfaced this insight\n\n"
        "Terms marked ✅ Pitch tip should be actively woven into your language. "
        "Quotes in blue are real words from executives you may encounter — "
        "using their vocabulary signals that you understand their world."
    )
    elements.append(Paragraph(intro, BODY_STYLE))
    elements.append(Spacer(1, 0.2 * inch))

    # Quick reference table of who said what
    elements.append(Paragraph("<b>Key Sources by Organization:</b>", TERM_NAME))
    elements.append(Spacer(1, 0.1 * inch))

    table_data = [
        ["Organization", "Contact", "Role", "Key Contribution"],
        ["ExxonMobil", "Tyler Beatty", "R&D Advisor", "'War on Inventory'; Venn diagram; $17.5M SMART Lab"],
        ["Equinor", "Douglas Garcia-Golindano", "Midstream Asset Mgr", "1-2% capex/98% production; Bay du Nord; cascade economics"],
        ["Lloyd's Register", "Trevor Butler / Adam Saxty / Dave Whitehouse", "BD / AM Tech / Naval", "7-step cert; Atlantic XL first in Americas; submarine case study"],
        ["Irving Shipbuilding", "Aaron Plamondon", "Director of ITB", "Navy AM failure root causes; ITB funding; Feb 18 Admiral visit"],
        ["GKN Aerospace", "Matthew Erning", "Technical Authority — DED", "MMPDS gap; platform vs. part cert; IP barriers"],
        ["Atlantic XL", "Sean Morgan", "Director of Operations", "Post-COVID supply chain; FieldNode/Pelagus landscape; first LR cert in Americas"],
        ["NGen / Canada Makes", "Frank DeFalco / Mark Kirby", "Director / AM Manager", "100K+ part inventories; Select AM tool; business case barrier"],
        ["Shield Group", "Shawn Sooley", "CEO", "Don't sell AI; aerospace-first strategy; certification reframe"],
        ["Deloitte / SAP", "Kwadwo Ampofo", "SAP Architect", "Working capital framing; insurance stock; ERP integration potential"],
        ["ERINL", "Keith Healey", "R&D Project Manager", "C-NLOPB pathway; Equinor Bay du Nord; ERINL cert funding"],
        ["Frobisher Energy", "Adam Chubbs", "AM/Asset Intelligence", "N+1/N+2 redundancy; 8-10% inventory ratio; self-certifying utilities"],
        ["Proax Technologies", "Darren Wood", "VP", "Obsolescence; hot-shot logistics; AM for custom fabricated parts"],
    ]
    col_widths = [1.3*inch, 1.7*inch, 1.5*inch, 2.5*inch]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",   (0, 0), (-1, 0), WHITE),
        ("FONTNAME",    (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, -1), 7.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PALE_BG, WHITE]),
        ("GRID",        (0, 0), (-1, -1), 0.3, colors.HexColor("#D0D3D4")),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",  (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0,0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    elements.append(t)
    elements.append(PageBreak())
    return elements


def build_terms_sections():
    """All terms organized by category."""
    elements = []
    for cat_name, terms in CATEGORIES:
        # Category header
        elements.append(build_colored_header(cat_name.upper(), STEEL_BLUE, SECTION_HDR))
        elements.append(Spacer(1, 0.1 * inch))

        for idx, entry in enumerate(terms):
            term, abbrev, definition, why_matters, quote, pitch_tip, ref = entry
            block = build_term_block(term, abbrev, definition, why_matters,
                                     quote, pitch_tip, ref, idx)
            elements.append(KeepTogether(block))

        elements.append(PageBreak())
    return elements


def build_quick_cheat_sheet():
    """Last page: 1-page cheat sheet of the most important phrases."""
    elements = []
    elements.append(build_colored_header(
        "QUICK CHEAT SHEET — 12 PHRASES TO MASTER BEFORE YOUR NEXT BIG MEETING",
        RED_ALERT, SECTION_HDR))
    elements.append(Spacer(1, 0.15 * inch))

    phrases = [
        ("1. The ROI opener",
         '"Your spare parts budget is 1-2% of total capex. It protects 98% of your production value. What if those parts were available in 48 hours instead of 18 months?"',
         "Douglas Garcia-Golindano, Equinor"),
        ("2. The War on Inventory",
         '"We end the War on Inventory — you don\'t carry physical stock, and you never pay for a hot-shot charter again."',
         "Tyler Beatty, ExxonMobil"),
        ("3. The Permission solver",
         '"Value is proven. Capability is proven. The only thing blocking you is Permission — certification. That\'s our entire product."',
         "Tyler Beatty\'s Venn framework"),
        ("4. Atlantic XL credential",
         '"Our anchor production partner, Atlantic XL, is the first Lloyd\'s Register-certified AM facility in all of the Americas."',
         "Trevor Butler, Lloyd\'s Register"),
        ("5. FieldNode differentiation",
         '"FieldNode connects buyers to printers. We sell trust — certified parts with LR documentation. You\'re not buying connectivity, you\'re buying compliance."',
         "AddManuChain positioning"),
        ("6. The LEAN pitch",
         '"Digital inventory is the ultimate LEAN solution for spare parts: zero physical waste, full JIT availability — without the atomic bomb risk."',
         "Douglas Garcia-Golindano, Equinor"),
        ("7. Bay du Nord specific target",
         '"Bay du Nord — $14B, 500 km offshore, harsher than Norway. Spare parts strategy is being designed right now, before FID. We want to be embedded from day one."',
         "Douglas Garcia-Golindano + Keith Healey"),
        ("8. The certification is not a wall",
         '"Certification is a one-time investment per facility and per part. Atlantic XL already has the facility qualification done. Every part is a one-time check — then it\'s on-demand forever."',
         "Trevor Butler + Adam Saxty, LR"),
        ("9. The submarine story (Navy)",
         '"30-year-old submarines. 10 years of life left. No original parts in inventory. As-built certification required for every repair. We digitize the as-built record and print on demand."',
         "Dave Whitehouse, LR Naval"),
        ("10. Ship availability metric (Navy)",
         '"Canadian Navy ships are available 30-50% of the time. The target is 70-80%. Spare parts delay is a primary driver. We solve spare parts delay."',
         "Dave Whitehouse, LR Naval"),
        ("11. Don\'t sell AI",
         '"We\'re not selling AI. We\'re selling certified spare parts available in 48 hours. The AI is how we do it — not what we do."',
         "Shawn Sooley, Shield Group"),
        ("12. Post-COVID gap positioning",
         '"Post-COVID, nobody carries stock. Everything requires 12-week pre-orders. We bridge that gap — the space between need NOW and can get in 3 months."',
         "Sean Morgan, Atlantic XL"),
    ]

    for label, phrase, credit in phrases:
        elements.append(Paragraph(f"<b>{label}</b>", TERM_NAME))
        elements.append(Paragraph(phrase, QUOTE_STYLE))
        elements.append(Paragraph(f"[Validated by: {credit}]", REF_STYLE))
        elements.append(HRFlowable(width="100%", thickness=0.4,
                                     color=colors.HexColor("#D5D8DC"), spaceAfter=4))

    return elements


def generate_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.45 * inch,
    )

    all_elements = []
    all_elements += build_cover()
    all_elements += build_how_to_use()
    all_elements += build_toc()
    all_elements += build_terms_sections()
    all_elements += build_quick_cheat_sheet()

    doc.build(all_elements, onFirstPage=on_page, onLaterPages=on_page)
    print(f"\n✅  PDF successfully generated:\n   {OUTPUT_PATH}\n")


if __name__ == "__main__":
    generate_pdf()
