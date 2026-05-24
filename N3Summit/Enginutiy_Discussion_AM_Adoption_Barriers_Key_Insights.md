# Enginutiy Discussion: AM Adoption Barriers — Key Insights

**Metadata**: Date Context: 2026 | Context: N3 Summit conversation | Participants: Engineering representatives from industry/academia

## EXECUTIVE SUMMARY

Brief conversation highlighting the fundamental tension between defense sector's desire for on-site additive manufacturing capability and the significant regulatory, certification, and liability barriers preventing deployment, with reference to aerospace industry caution as leading indicator. The defense sector sees clear value in distributed 3D printing for supply chain resilience and remote operations, yet certification pathways, liability assignment, and cultural conservatism create a nearly prohibitive barrier to entry. Meanwhile, adjacent sectors (mining, oil & gas) present lower-friction opportunities where uptime economics outweigh regulatory complexity.

## ADOPTION BARRIERS IDENTIFIED

- **Certification pathway complexity** — Naval, aerospace, and defense standards (MIL-SPEC, NADCAP, Lloyd’s, DNV) impose multi-year qualification cycles that require exhaustive material characterization, process validation, and post-build inspection protocols that do not map cleanly to distributed manufacturing models.

- **Liability assignment ambiguity** — When a printed part fails in a submarine or aircraft, accountability fractures across the printer OEM, material supplier, platform operator, site maintainer, and the end-user organization. Neither defense buyers nor commercial insurers have mature frameworks for allocating fault when digital files travel across platforms.

- **Material qualification and process validation requirements** — Each alloy–machine–parameter combination must be recertified; site-specific environmental controls (humidity, temperature, cleanliness) introduce variance that invalidates previous qualifications, forcing redundant testing for every new installation.

- **Cultural resistance in conservative defense acquisition** — Legacy procurement cultures prioritize provenance and pedigree over innovation. The phrase “conservative” recurs across aerospace primes and defense primes; organizations such as GKN are described as risk-averse with “lives at stake,” translating into reluctance to adopt distributed AM despite acknowledged strategic value.

- **Trust deficit in new manufacturing technology for mission-critical parts** — Submarines and aircraft cannot tolerate invisible flaws. Without long-field reliability data and accepted inspection standards (CT scanning, phased-array UT), buyers default to “no” even when the economic case is compelling.

- **Training and workforce readiness gaps** — Operators need metallurgy literacy, printer calibration skills, post-processing competence, and NDE interpretation ability. The defense sector lacks pipelines to staff hundreds of remote sites with consistent capability.

- **Quality assurance and inspection capability requirements** — Distributed sites must duplicate sophisticated metrology suites. The cost and complexity of in-situ inspection often erodes the logistics savings that motivate on-site printing in the first place.

## SECTOR COMPARISONS

- **Aerospace (GKN) as cautionary tale** — Highly conservative with lives at stake and long qualification cycles; GKN’s hesitance signals how aerospace primes entering defense will approach AM conservatively, extending timelines and increasing documentation overhead.

- **Mining (Kinross) as more accessible use case** — Remote sites with high downtime costs create economic urgency; regulatory burden is lighter than aerospace/defense, making mining a logical beachhead to prove platform reliability and build trust.

- **Defense: sovereign capability drivers vs risk-averse procurement culture** — Strategic imperative to maintain readiness and reduce long supply chains conflicts with conservative acquisition processes; the result is interest without adoption.

- **Energy/oil & gas: similar reliability requirements, different regulatory regime** — Offshore platforms exhibit failure-cost profiles akin to defense (expensive downtime) but with maritime/class society rules rather than defense specifications, creating a mid-difficulty pathway to scale.

## STRATEGIC IMPLICATIONS for AddManuChain

- **Regulatory mapping** — Different domains (naval, army, air force, class societies) have divergent certification ladders; a platform must surface requirements and evidence templates tailored to each pathway rather than generic “certification-ready” claims.

- **Liability framework design** — The platform cannot assume liability for part performance but must enable immutable traceability and audit trails (digital thread, machine logs, material certs, inspection records) so OEMs and primes can confidently stand behind parts.

- **Pilot strategy** — Prioritize mining and remote industrial sites as lower-barrier entry points to demonstrate uptime impact, accumulate reliability data, and de-risk the technology narrative before attempting defense primes.

- **Education and change management** — Target conservative procurement officers and program managers with case studies, site visits, and transparent data; reduce perceived risk by making qualification steps legible and repeatable.

- **Partnership requirement** — Need established OEMs or primes (e.g., GKN, Raytheon Canada) to vouch for or co-certify platform outputs; their brand becomes the trust anchor that unlocks defense conversations.

## KEY QUOTES

- “They see the opportunity… but the thing that defense wants is to install separate printers on-site. The certification path… there’s an even inspiration… I’m worried… liable someone else.” — Speaker 1/2 on certification and liability as the decisive friction.

- “We have to have the trust. They don’t have the education, and most importantly, they don’t have the skill level. They see that… okay, if I can have the 3D printer on-site, we’re going to certify that.” — Speaker 1 on the trust–education–skill triad.

- “There’s a company in the UK called Greek deep… they’ve been through a small family [foundry?]… now that’s been done.” — Reference (likely Geo Deep) to offshore/maritime qualification precedents.

- “Park off, man… people are at the event… they’re working on aerospace, so they’re using the aerospace sector into defense.” — Commentary on aerospace as the on-ramp to defense AM adoption.

## RECOMMENDATIONS

1. **Target mining and oil & gas as beachhead** — Launch pilots in remote industrial sites where downtime costs justify investment and regulatory friction is lowest. Capture uptime and reliability metrics to build an evidence base.

2. **Develop certification-ready documentation templates** — Align with Lloyd’s, DNV, NADCAP, and defense-specific quality system templates so customers can generate compliant Technical Data Packages and quality records with minimal friction.

3. **Create a liability matrix and digital thread** — Publish a clear responsibility model (OEM, operator, material supplier, platform) and implement immutable machine logs, material traceability, and inspection-record chain-of-custody to allocate risk transparently.

4. **Partner with established aerospace/defense OEMs** — Secure co-development or endorsement agreements with firms such as GKN or Raytheon Canada to vouch for platform outputs and accelerate trust in conservative circles.

5. **Build a regulatory-readiness assessment tool** — Enable customers to self-assess which certification ladder applies, what evidence is required, and what gaps exist before committing capital; turn regulatory opacity into a legible project plan.
