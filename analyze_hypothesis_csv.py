import pandas as pd

# Read the CSV file
csv_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses_Updated_Feb1_2026.csv'
df = pd.read_csv(csv_path)

print("=" * 80)
print("HYPOTHESIS TABLE ANALYSIS")
print("=" * 80)

# Basic statistics
total_hypotheses = len(df)
print(f"\nTotal Hypotheses: {total_hypotheses}")

# Status breakdown
status_counts = df['Accept or Reject Hypotheses'].value_counts()
print("\nValidation Status Breakdown:")
for status, count in status_counts.items():
    print(f"  {status}: {count}")

# Interview validation counts
print("\n" + "=" * 80)
print("HYPOTHESES VALIDATED BY EACH INTERVIEW")
print("=" * 80)

interviews = {
    'Interview 3 - David Waldbillig': [],
    'Interview 4 - Jason Power': [],
    'Interview 5 - Sean Morgan': [],
    'Interview 6 - John Lidstone': [],
    'Interview 7 - Dr. Priti Wanjara': []
}

for idx, row in df.iterrows():
    hyp_id = row['Hypotheses # and name']
    supported = str(row['Which interviews supported the hypotheses?'])
    
    if 'David Waldbillig' in supported or 'Interview 3' in supported:
        interviews['Interview 3 - David Waldbillig'].append(hyp_id)
    if 'Jason Power' in supported or 'Interview 4' in supported:
        interviews['Interview 4 - Jason Power'].append(hyp_id)
    if 'Sean Morgan' in supported or 'Interview 5' in supported:
        interviews['Interview 5 - Sean Morgan'].append(hyp_id)
    if 'John Lidstone' in supported or 'Interview 6' in supported:
        interviews['Interview 6 - John Lidstone'].append(hyp_id)
    if 'Interview 7' in supported or 'Priti Wanjara' in supported or 'Fanny' in supported:
        interviews['Interview 7 - Dr. Priti Wanjara'].append(hyp_id)

for interview, hypotheses in interviews.items():
    print(f"\n{interview}: {len(hypotheses)} hypotheses")
    for h in hypotheses:
        print(f"  - {h}")

# New hypotheses (NH.) status
print("\n" + "=" * 80)
print("NEW HYPOTHESES (NH.1-NH.11) STATUS")
print("=" * 80)

new_hyp = df[df['Hypotheses # and name'].str.contains('NH.', na=False)]
print(f"\nTotal New Hypotheses: {len(new_hyp)}")

for idx, row in new_hyp.iterrows():
    hyp_id = row['Hypotheses # and name']
    status = row['Accept or Reject Hypotheses']
    supported = row['Which interviews supported the hypotheses?']
    print(f"\n{hyp_id}")
    print(f"  Status: {status}")
    print(f"  Supported by: {supported}")

# Strongest validated hypotheses (multiple interviews)
print("\n" + "=" * 80)
print("HYPOTHESES WITH STRONGEST VALIDATION (2+ interviews)")
print("=" * 80)

strong_validation = df[df['# of Yes'] >= 2].sort_values('# of Yes', ascending=False)
for idx, row in strong_validation.iterrows():
    hyp_id = row['Hypotheses # and name']
    yes_count = int(row['# of Yes'])
    supported = row['Which interviews supported the hypotheses?']
    print(f"\n{hyp_id} - {yes_count} interviews")
    print(f"  Supported by: {supported}")

print("\n" + "=" * 80)
