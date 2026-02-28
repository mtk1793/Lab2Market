import csv

csv_file = r'Airtable\Interviews-Master List of Interviews (1).csv'

# Read existing data
rows = []
headers = []
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    rows = list(reader)

print(f"Current records: {len(rows)}")
print(f"Columns: {headers}")
if len(rows) >= 3:
    print("\nLast 3 interviews:")
    for row in rows[-3:]:
        print(f"  {row.get('Interview Count', 'N/A')}: {row.get('Stakeholder being interviewed', 'N/A')}")

# New data
new_data = [
    {
        "Interview Count": "21",
        "Stakeholder being interviewed": "Arad Gharagozli (Galaxia Mission Systems)",
        "Interview Date + Time": "2/6/2026",
        "Note-taker": "Mahmoud Kiasari",
        "Key Insights": "Galaxia actively uses AM in production (space/rocket propulsion). Two-sided marketplace model immediately understood. IP security & controlled goods = #1 aerospace barrier. Audit trail addresses concern but need certified vetting layer. 30-40 part consolidation validates AM-native design.",
        "Which hypotheses were supported by this interview?": "CS.2,CJ.2,CS.4,NH.10,H85,H86",
        "Which hypotheses were rejected by this interview?": "",
        "PARTIALLY SUPPORTED": "NH.16",
        "Notes": "Interviews/21/insights.md"
    },
    {
        "Interview Count": "52",
        "Stakeholder being interviewed": "Scott Humber & Heather Davis (Aker Solutions)",
        "Interview Date + Time": "2/2/2026",
        "Note-taker": "Mahmoud Kiasari",
        "Key Insights": "Real end-to-end AM workflow exists globally. Formal AM screening with 6 criteria. Lloyd's qualifies facility for ALL criticality levels. Certification follows standard manufacturing process. Aker exploring formal NL workflow integration.",
        "Which hypotheses were supported by this interview?": "CS.4,NH.7,H83,H98,VP.8",
        "Which hypotheses were rejected by this interview?": "",
        "PARTIALLY SUPPORTED": "",
        "Notes": "Interviews/52/insights.md"
    },
    {
        "Interview Count": "53",
        "Stakeholder being interviewed": "Stephen Ryan (PolyUnity Tech - Co-Founder & CMO)",
        "Interview Date + Time": "2/25/2026",
        "Note-taker": "Mahmoud Kiasari",
        "Key Insights": "PolyUnity doing in healthcare exactly what AddManuChain doing in O&G/defense. 3-TIER PLATFORM MODEL. Multi-stage approval pipeline IS the product. Approval cascade eliminates 50% sales friction. Partnership explicit: We can't afford to compete. We need to raise all ships.",
        "Which hypotheses were supported by this interview?": "H60,H74,H75,VP.3,NH.10,RS.2",
        "Which hypotheses were rejected by this interview?": "",
        "PARTIALLY SUPPORTED": "",
        "Notes": "Interviews/53/insights.md - PARTNERSHIP OPPORTUNITY"
    },
    {
        "Interview Count": "55",
        "Stakeholder being interviewed": "André Simha (Mediterranean Shipping Company - CDIO)",
        "Interview Date + Time": "2/26/2026",
        "Note-taker": "Mahmoud Kiasari",
        "Key Insights": "Spare part supply centralized but distributed pragmatically. DATA QUALITY is real blocker - NOT technology. IoT deployed but under-utilized. Blockchain hype ended - APIs won. TRUST is #1 ecosystem killer.",
        "Which hypotheses were supported by this interview?": "VP.10,NH.9,NH.1,H62,H88",
        "Which hypotheses were rejected by this interview?": "",
        "PARTIALLY SUPPORTED": "",
        "Notes": "Interviews/55/insights.md - C-LEVEL VALIDATION"
    },
    {
        "Interview Count": "56",
        "Stakeholder being interviewed": "Sheila Paterson (NS Dept. Energy & Natural Resources - Former COVE COO)",
        "Interview Date + Time": "2/27/2026",
        "Note-taker": "Mahmoud Kiasari",
        "Key Insights": "COVID supply chain fragility CONFIRMED. OEMs may PREFER licensing model. IP security + quality assurance = top two barriers. Government is NOT buyer but direction-setter + accelerator. Canadian Navy availability gap: 30-50% actual vs 70-80% target.",
        "Which hypotheses were supported by this interview?": "CS.4,NH.22,H82,H101,NH.1,H75",
        "Which hypotheses were rejected by this interview?": "",
        "PARTIALLY SUPPORTED": "",
        "Notes": "Interviews/56/insights.md - POLICY ECOSYSTEM + 8 PROGRAMS"
    }
]

# Append new rows
rows.extend(new_data)

# Write back
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"\n✅ Updated Successfully")
print(f"📊 Added 5 new interviews (21, 52, 53, 55, 56)")
print(f"📁 Total interviews now: {len(rows)}")
