import pandas as pd
from datetime import datetime

# Load the original CSV
file_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Original Version/Hypotheses-Team 16 - Mahmoud Kiasari.csv'
df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)

# Interview information
interview_3 = "Interview 3 - David Waldbillig (InnoTech Alberta)"
interview_4 = "Interview 4 - Jason Power (Noble Corporation)"
interview_5 = "Interview 5 - Sean Morgan (Atlantic XL)"
interview_6 = "Interview 6 - John Lidstone (Atlantic XL)"
interview_7 = "Interview 7 - Dr. Priti Wanjara (NRC) / Fanny Charreteur (CQFA) referral"

# Mapping of hypothesis numbers to their validation from Interview 3 (David Waldbillig)
interview_3_validations = {
    # VP.9 - Real-Time Communication Platform
    39: {'status': 'Support', 'evidence': 'Trust gap is supply chain communication - "hard to have communication with them for different industrial parts"'},
    
    # VP.12 - Certification Body Decision Support
    44: {'status': 'Support', 'evidence': 'Multiple certification challenges mentioned, trust building requires certification clarity'},
    
    # VP.14 - Transparent Pricing/Budget Pre-Qualification
    46: {'status': 'Support', 'evidence': 'Capital vs risk trade-offs mentioned, cost justification critical'},
}

# Mapping of hypothesis numbers to their validation from Interview 4 (Jason Power)
interview_4_validations = {
    # VP.14 - Transparent Pricing/Budget Pre-Qualification
    46: {'status': 'Support', 'evidence': 'Boom/bust cycles require cost optimization tools, feasibility assessment critical'},
}

# Mapping of hypothesis numbers to their validation from Interview 5 (Sean Morgan)
# Based on detailed transcript analysis

interview_5_validations = {
    # CS.1 - Manufacturers Need Certified Local Suppliers
    0: {'status': 'Support', 'evidence': 'Atlantic XL acts as procurement agency helping find suppliers - validates dual-sided pain'},
    
    # CS.2 - Facilities Have Idle Capacity  
    1: {'status': 'Support', 'evidence': 'Atlantic XL acts as procurement agency which proves they need more customers to fill capacity'},
    
    # CS.3 - Labs & Authorities Need Digital Compliance System
    2: {'status': 'Support', 'evidence': 'Lloyd\'s Register qualification process ongoing since 2022 with 86 templates shows manual complexity'},
    
    # CS.4 - OEMs Want Distributed Manufacturing
    3: {'status': 'Support', 'evidence': 'Geographic isolation (Newfoundland) + post-COVID stock depletion validates distributed manufacturing need'},
    
    # CJ.1 - Source Certified Parts Quickly
    5: {'status': 'Support', 'evidence': 'Obsolete part success story - delivered before Christmas when traditional sourcing was prohibitive'},
    
    # CJ.2 - Fill Machine Capacity
    6: {'status': 'Support', 'evidence': 'Atlantic XL acts as procurement agency proving they actively seek customers to fill capacity'},
    
    # CJ.3 - Process Certifications Efficiently
    7: {'status': 'Support', 'evidence': 'Lloyd\'s Register process ongoing since 2022 indicates slow, manual certification workflows'},
    
    # CP.1 - Weeks Wasted Finding Facilities
    9: {'status': 'Strong Support', 'evidence': 'Atlantic XL as procurement agency validates manufacturers can\'t find facilities themselves'},
    
    # CP.2 - Expensive Distant Suppliers
    10: {'status': 'Strong Support', 'evidence': 'Sources from Europe (not Canada/US) + Newfoundland logistics challenges (single carrier, weather)'},
    
    # CP.3 - Certification Proof Difficulty
    11: {'status': 'Strong Support', 'evidence': 'Lloyd\'s Register facility qualification is primary focus - ExxonMobil partnership for confidence-building'},
    
    # CP.5 - High CAC Kills Margins
    13: {'status': 'Support', 'evidence': 'Relies on partnerships and internet search for customers - expensive manual acquisition process'},
    
    # CP.6 - Paper-Based Chaos
    14: {'status': 'Strong Support', 'evidence': 'Lloyd\'s certification: 86 templates in operation, process ongoing since 2022, very manual'},
    
    # CG.1 - Find Facilities in Minutes
    17: {'status': 'Support', 'evidence': 'Procurement agency role validates need for fast facility discovery'},
    
    # CG.2 - Cut Shipping 40-60%
    18: {'status': 'Support', 'evidence': 'Sources from Europe vs local - long distances + Newfoundland freight challenges (weather, single carrier)'},
    
    # CG.4 - Maximize Machine Revenue  
    20: {'status': 'Support', 'evidence': 'Acts as procurement agency to find work - indicates unused capacity needs filling'},
    
    # CG.5 - Reduce CAC by 50%+
    21: {'status': 'Support', 'evidence': 'Manual internet search + partnerships for customer acquisition is expensive'},
    
    # VP.1 - Find Facilities in Minutes
    25: {'status': 'Support', 'evidence': 'Procurement agency validates need for searchable database of facilities'},
    
    # VP.4 - Qualified Client Pipeline
    28: {'status': 'Support', 'evidence': 'Atlantic XL needs client pipeline - acts as procurement agency to source work'},
    
    # VP.9 - Real-Time Communication Platform
    39: {'status': 'Support', 'evidence': 'Sean mentioned "chasing parts" - logistics coordination and status update pain points'},
    
    # VP.10 - Demand Forecasting & Pipeline Visibility
    40: {'status': 'Strong Support', 'evidence': 'Sean specifically said "pairing with digital inventory to predict the future" - unprompted validation'},
    
    # VP.11 - Quality-Over-Quantity Matching
    43: {'status': 'Support', 'evidence': 'Manual vetting process via internet search suggests need for better pre-qualified matching'},
    
    # VP.13 - Multi-Role Collaboration Workspaces
    45: {'status': 'Support', 'evidence': 'Dual role as engineering service + procurement agency requires cross-functional coordination'},
}

# NEW hypotheses discovered from Interview 5
new_hypotheses = [
    {
        'Hypotheses # and name': 'NH.1 - Post-COVID Stock Depletion Creates AM Opportunity',
        'Hypotheses': 'The shift from stock-based to pre-order supply chains (post-COVID) creates market gap that AM can fill by enabling on-demand production vs 12-week pre-orders.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Pains',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Manufacturers and facilities dealing with post-COVID supply chain disruption',
    },
    {
        'Hypotheses # and name': 'NH.2 - Obsolescence is Primary AM Adoption Driver',
        'Hypotheses': 'Parts obsolescence (no longer manufactured) drives AM adoption more than innovation/cost savings - AM becomes ONLY option, not just better option.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Pains',
        'CS.#': 'CS.1',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Offshore operators, marine industry, industrial equipment manufacturers with aging assets',
    },
    {
        'Hypotheses # and name': 'NH.3 - Lead Time Emergency Accelerates Adoption',
        'Hypotheses': 'High downtime costs force companies to try AM in emergencies (despite risk aversion), which opens door to comfort and eventual regular adoption.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Job',
        'CS.#': 'CS.1',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Offshore operators, facility managers with critical downtime cost exposure',
    },
    {
        'Hypotheses # and name': 'NH.4 - Geographic Isolation Amplifies Local Manufacturing Need',
        'Hypotheses': 'Regions with limited freight options (weather delays, single carriers, remote locations) have significantly higher pain from distant suppliers and gain more value from local AM hubs.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Pains',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Newfoundland, remote mining sites, offshore platforms, northern communities, isolated industrial facilities',
    },
    {
        'Hypotheses # and name': 'NH.5 - Predictive Maintenance + Digital Inventory Integration',
        'Hypotheses': 'Pairing condition monitoring/predictive maintenance with digital inventory enables proactive AM part ordering before failure (vs reactive emergency ordering).',
        'BMC Block': 'Value Proposition',
        'Value Map': '',
        'Customer Profile': 'Gain Creators',
        'CS.#': 'CS.1, CS.2, CS.3',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Facilities with IoT sensor infrastructure and AI/ML predictive maintenance initiatives',
    },
    {
        'Hypotheses # and name': 'NH.6 - AM Adoption Evolution: Emergency → Comfort → Innovation',
        'Hypotheses': 'AM adoption follows predictable 3-phase evolution: (1) emergency use only, (2) success builds comfort for regular use, (3) exploration of design innovation beyond replication.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Job',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Companies in Phase 1 (emergency) who can be moved to Phase 2 (regular) with platform support',
    },
    {
        'Hypotheses # and name': 'NH.7 - Certification is Primary Gatekeeper for Regulated Industries',
        'Hypotheses': 'Without classification approvals and facility qualification (e.g. Lloyd\'s Register), AM cannot penetrate oil & gas, offshore, aerospace, or medical - certification is table stakes, not differentiator.',
        'BMC Block': 'Key Resources',
        'Value Map': '',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2, CS.3',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_5,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Certification labs, regulatory authorities, certified facilities pursuing new markets',
    },
    {
        'Hypotheses # and name': 'NH.8 - Feasibility + Cost Drive AM Acceptance (Interview 6 - John Lidstone)',
        'Hypotheses': 'First consideration for AM adoption is part-specific feasibility (is AM actually cheaper than traditional?) - round parts use machining, complex/cast components better for AM. Quantity also matters.',
        'BMC Block': 'Customer Segment',
        'Value Map': '',
        'Customer Profile': 'Customer Job',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_6,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Engineers evaluating AM vs traditional for specific parts - need decision support tools',
    },
    {
        'Hypotheses # and name': 'NH.9 - Digital Inventory Reduces Lead Time from Months to Weeks',
        'Hypotheses': 'Scanning and digitizing parts for certification-ready digital inventory can reduce lead time from months to weeks when combined with AM production capability.',
        'BMC Block': 'Value Proposition',
        'Value Map': '',
        'Customer Profile': 'Gain Creators',
        'CS.#': 'CS.1, CS.2, CS.3',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_6,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Companies starting to digitize product inventory and seeking certification integration',
    },
    {
        'Hypotheses # and name': 'NH.10 - OEM IP Release is Critical Blocker',
        'Hypotheses': 'To produce parts via AM, OEM must relinquish IP, or IP must be proven void/expired/open. AI-based patent search could help identify open-source opportunities. Need OEM relationships.',
        'BMC Block': 'Key Partners',
        'Value Map': '',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2, CS.4',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_6,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'OEMs open to distributed manufacturing partnerships, facilities seeking IP-cleared part libraries',
    },
    {
        'Hypotheses # and name': 'NH.11 - CQFA as Quebec AM Ecosystem Gateway (Interview 7 - Fanny Charreteur)',
        'Hypotheses': 'Regional AM hubs like CQFA (Carrefour québécois de la fabrication additive) provide ecosystem access, partnership opportunities, and funding expertise (Sr&ED) that can accelerate platform adoption.',
        'BMC Block': 'Key Partners',
        'Value Map': '',
        'Customer Profile': '',
        'CS.#': 'CS.2, CS.3',
        'Date of Hypotheses': '2026-02-01',
        'Which interviews supported the hypotheses?': interview_7,
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Regional AM ecosystem organizations, innovation hubs, government-backed manufacturing consortia',
    },
]

# Update existing hypotheses with Interview 3 evidence
for idx, update in interview_3_validations.items():
    if idx < len(df):
        # Update support column
        current_support = str(df.at[idx, 'Which interviews supported the hypotheses?'])
        if pd.isna(current_support) or current_support == '' or current_support == 'nan':
            df.at[idx, 'Which interviews supported the hypotheses?'] = interview_3
        else:
            if interview_3 not in current_support:
                df.at[idx, 'Which interviews supported the hypotheses?'] = f"{current_support}, {interview_3}"
        
        # Update Yes count
        df.at[idx, '# of Yes'] = df.at[idx, '# of Yes'] + 1 if pd.notna(df.at[idx, '# of Yes']) else 1
        
        # Update total interviews
        df.at[idx, '# of Total Interviews'] = df.at[idx, '# of Total Interviews'] + 1 if pd.notna(df.at[idx, '# of Total Interviews']) else 1

# Update existing hypotheses with Interview 4 evidence
for idx, update in interview_4_validations.items():
    if idx < len(df):
        # Update support column
        current_support = str(df.at[idx, 'Which interviews supported the hypotheses?'])
        if pd.isna(current_support) or current_support == '' or current_support == 'nan':
            df.at[idx, 'Which interviews supported the hypotheses?'] = interview_4
        else:
            if interview_4 not in current_support:
                df.at[idx, 'Which interviews supported the hypotheses?'] = f"{current_support}, {interview_4}"
        
        # Update Yes count
        df.at[idx, '# of Yes'] = df.at[idx, '# of Yes'] + 1 if pd.notna(df.at[idx, '# of Yes']) else 1
        
        # Update total interviews
        df.at[idx, '# of Total Interviews'] = df.at[idx, '# of Total Interviews'] + 1 if pd.notna(df.at[idx, '# of Total Interviews']) else 1

# Update existing hypotheses with Interview 5 evidence
for idx, update in interview_5_validations.items():
    if idx < len(df):
        # Update support column
        current_support = str(df.at[idx, 'Which interviews supported the hypotheses?'])
        if pd.isna(current_support) or current_support == '' or current_support == 'nan':
            df.at[idx, 'Which interviews supported the hypotheses?'] = interview_5
        else:
            if interview_5 not in current_support:
                df.at[idx, 'Which interviews supported the hypotheses?'] = f"{current_support}, {interview_5}"
        
        # Update Yes count
        df.at[idx, '# of Yes'] = df.at[idx, '# of Yes'] + 1 if pd.notna(df.at[idx, '# of Yes']) else 1
        
        # Update total interviews
        df.at[idx, '# of Total Interviews'] = df.at[idx, '# of Total Interviews'] + 1 if pd.notna(df.at[idx, '# of Total Interviews']) else 1
        
        # Update status if needed
        yes_count = df.at[idx, '# of Yes']
        total_count = df.at[idx, '# of Total Interviews']
        
        if yes_count >= 2:
            df.at[idx, 'Accept or Reject Hypotheses'] = 'Supported'
        elif yes_count == 1 and total_count >= 2:
            df.at[idx, 'Accept or Reject Hypotheses'] = 'Partially Supported'
        else:
            df.at[idx, 'Accept or Reject Hypotheses'] = 'Insufficient Data'

# Add new hypotheses
new_df = pd.DataFrame(new_hypotheses)
df = pd.concat([df, new_df], ignore_index=True)

# Save updated CSV
output_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses_Updated_Feb1_2026.csv'
df.to_csv(output_path, index=False)

print(f"✅ Updated hypothesis file saved to: {output_path}")
print(f"\n📊 Update Summary:")
print(f"- Original hypotheses: 47")
print(f"- Hypotheses updated with Interview 3 evidence: {len(interview_3_validations)}")
print(f"- Hypotheses updated with Interview 4 evidence: {len(interview_4_validations)}")
print(f"- Hypotheses updated with Interview 5 evidence: {len(interview_5_validations)}")
print(f"- New hypotheses added from Interviews 3-7: {len(new_hypotheses)}")
print(f"- Total hypotheses in updated file: {len(df)}")
print(f"\n🎯 Validation Status:")
supported = len(df[df['Accept or Reject Hypotheses'] == 'Supported'])
partial = len(df[df['Accept or Reject Hypotheses'] == 'Partially Supported'])
rejected = len(df[df['Accept or Reject Hypotheses'] == 'Rejected'])
insufficient = len(df[df['Accept or Reject Hypotheses'] == 'Insufficient Data'])
print(f"- Supported: {supported}")
print(f"- Partially Supported: {partial}")
print(f"- Rejected: {rejected}")
print(f"- Insufficient Data: {insufficient}")
