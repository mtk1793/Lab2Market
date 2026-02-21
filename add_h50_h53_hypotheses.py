import pandas as pd

# Load the main hypothesis file
file_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses-Team 16 - Mahmoud Kiasari(1).csv'
df = pd.read_csv(file_path)

# Define the new hypotheses H50-H53 from Interview 3 (David Waldbillig)
new_hypotheses = [
    {
        'Hypotheses # and name': 'H50 - Low-Risk Part Categorization System',
        'Hypotheses': 'Platform must provide automated risk categorization (critical vs non-critical) to help users identify parts safe for AM adoption. This is THE primary decision factor and should be MVP feature.',
        'BMC Block': 'Value Proposition',
        'Value Map': 'Product/Service',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-01-28',
        'Which interviews supported the hypotheses?': 'Interview 3 - David Waldbillig (InnoTech Alberta)',
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Engineers and procurement managers evaluating AM feasibility who need decision support for risk assessment',
        'Field 15': '',
        'Field 16': '',
        'Which interviews rejected the hypotheses? copy': ''
    },
    {
        'Hypotheses # and name': 'H51 - Post-Processing Service Network Integration',
        'Hypotheses': 'Platform must integrate post-processing services (coatings, surface finishing, heat treatment) as these are critical for energy sector and often blocking factor for AM adoption. Network of qualified service providers needed.',
        'BMC Block': 'Key Partnerships',
        'Value Map': 'Gain Creators',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-01-28',
        'Which interviews supported the hypotheses?': 'Interview 3 - David Waldbillig (InnoTech Alberta)',
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Energy sector manufacturers requiring coatings/finishing, AM facilities seeking to offer complete solutions',
        'Field 15': '',
        'Field 16': '',
        'Which interviews rejected the hypotheses? copy': ''
    },
    {
        'Hypotheses # and name': 'H52 - Reverse Engineering Service Integration',
        'Hypotheses': 'Platform should integrate reverse engineering services to scan obsolete parts and create certification-ready digital library. This transforms one-off emergency solutions into reusable assets.',
        'BMC Block': 'Key Partnerships',
        'Value Map': 'Gain Creators',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2',
        'Date of Hypotheses': '2026-01-28',
        'Which interviews supported the hypotheses?': 'Interview 3 - David Waldbillig (InnoTech Alberta)',
        '# of Yes': 1,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 1,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Companies with aging equipment and obsolete parts, reverse engineering firms seeking platform integration',
        'Field 15': '',
        'Field 16': '',
        'Which interviews rejected the hypotheses? copy': ''
    },
    {
        'Hypotheses # and name': 'H53 - Predictive Maintenance API Integration',
        'Hypotheses': 'Platform should provide API integration with predictive maintenance systems (IoT sensors, CMMS) to enable proactive part ordering before failure. This is ultimate vision combining predictive analytics with digital inventory.',
        'BMC Block': 'Key Resources',
        'Value Map': 'Gain Creators',
        'Customer Profile': '',
        'CS.#': 'CS.1, CS.2, CS.3',
        'Date of Hypotheses': '2026-01-28',
        'Which interviews supported the hypotheses?': 'Interview 3 - David Waldbillig (InnoTech Alberta), Interview 5 - Sean Morgan (Atlantic XL)',
        '# of Yes': 2,
        'Which interviews rejected the hypotheses?': '',
        '# of No': 0,
        '# of Total Interviews': 2,
        'Accept or Reject Hypotheses': 'Supported',
        'Early Adopter': 'Facilities with IoT infrastructure and predictive maintenance programs, Industry 4.0 early adopters',
        'Field 15': '',
        'Field 16': '',
        'Which interviews rejected the hypotheses? copy': ''
    }
]

# Convert to DataFrame and append
new_df = pd.DataFrame(new_hypotheses)
df_updated = pd.concat([df, new_df], ignore_index=True)

# Save the updated file
df_updated.to_csv(file_path, index=False)

print(f"✅ Added H50-H53 to main hypothesis file")
print(f"\nTotal hypotheses now: {len(df_updated)}")
print(f"\nNew hypotheses added:")
for h in new_hypotheses:
    print(f"  - {h['Hypotheses # and name']}")
    print(f"    Status: {h['Accept or Reject Hypotheses']}")
    print(f"    Supported by: {h['Which interviews supported the hypotheses?']}")
    print()
