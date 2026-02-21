import pandas as pd
import numpy as np

# Load the CSV file
file_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses-Team 16 - Mahmoud Kiasari(1).csv'
df = pd.read_csv(file_path)

# Interview labels
interview_3 = "Interview 3 - David Waldbillig"
interview_4 = "Interview 4 - Jason Power"
interview_5 = "Interview 5 - Sean Morgan"
interview_6 = "Interview 6 - John Lidstone"
interview_7 = "Interview 7 - Dr. Wanjara/Fanny"

# Function to update a hypothesis row
def update_hypothesis(df, hyp_id, supporting_interviews=None, rejecting_interviews=None):
    """Update hypothesis with interview evidence"""
    # Find the row by hypothesis ID
    mask = df['Hypotheses # and name'].str.contains(hyp_id, na=False)
    if not mask.any():
        print(f"Warning: Could not find hypothesis {hyp_id}")
        return
    
    idx = df[mask].index[0]
    
    # Get current values
    current_support = str(df.at[idx, 'Which interviews supported the hypotheses?'])
    current_reject = str(df.at[idx, 'Which interviews rejected the hypotheses?'])
    
    # Update supporting interviews
    if supporting_interviews:
        if pd.isna(current_support) or current_support == '' or current_support == 'nan':
            df.at[idx, 'Which interviews supported the hypotheses?'] = ','.join(supporting_interviews)
        else:
            # Add new interviews if not already present
            existing = [s.strip() for s in current_support.split(',')]
            for interview in supporting_interviews:
                if interview not in existing:
                    existing.append(interview)
            df.at[idx, 'Which interviews supported the hypotheses?'] = ','.join(existing)
        
        # Update yes count
        yes_interviews = df.at[idx, 'Which interviews supported the hypotheses?'].split(',')
        df.at[idx, '# of Yes'] = len([i for i in yes_interviews if i.strip()])
    
    # Update rejecting interviews
    if rejecting_interviews:
        if pd.isna(current_reject) or current_reject == '' or current_reject == 'nan':
            df.at[idx, 'Which interviews rejected the hypotheses?'] = ','.join(rejecting_interviews)
        else:
            existing = [s.strip() for s in current_reject.split(',')]
            for interview in rejecting_interviews:
                if interview not in existing:
                    existing.append(interview)
            df.at[idx, 'Which interviews rejected the hypotheses?'] = ','.join(existing)
        
        # Update no count
        no_interviews = df.at[idx, 'Which interviews rejected the hypotheses?'].split(',')
        df.at[idx, '# of No'] = len([i for i in no_interviews if i.strip()])
    
    # Update total interviews and status
    yes_count = df.at[idx, '# of Yes'] if pd.notna(df.at[idx, '# of Yes']) else 0
    no_count = df.at[idx, '# of No'] if pd.notna(df.at[idx, '# of No']) else 0
    total = yes_count + no_count
    df.at[idx, '# of Total Interviews'] = total
    
    # Update acceptance status
    if yes_count >= 2:
        df.at[idx, 'Accept or Reject Hypotheses'] = 'Supported'
    elif yes_count == 1 and total >= 2:
        df.at[idx, 'Accept or Reject Hypotheses'] = 'Partially Supported'
    elif no_count >= 2:
        df.at[idx, 'Accept or Reject Hypotheses'] = 'Rejected'
    else:
        df.at[idx, 'Accept or Reject Hypotheses'] = 'Insufficient Data'

# Interview 3 - David Waldbillig validations
update_hypothesis(df, 'VP.9', supporting_interviews=[interview_3])
update_hypothesis(df, 'VP.12', supporting_interviews=[interview_3])
update_hypothesis(df, 'VP.14', supporting_interviews=[interview_3])

# Interview 4 - Jason Power validations
update_hypothesis(df, 'VP.14', supporting_interviews=[interview_4])

# Interview 5 - Sean Morgan validations (22 hypotheses)
update_hypothesis(df, 'CS.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'CS.2', supporting_interviews=[interview_5])
update_hypothesis(df, 'CS.3', supporting_interviews=[interview_5])
update_hypothesis(df, 'CS.4', supporting_interviews=[interview_5])
update_hypothesis(df, 'CJ.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'CJ.2', supporting_interviews=[interview_5])
update_hypothesis(df, 'CJ.3', supporting_interviews=[interview_5])
update_hypothesis(df, 'CP.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'CP.2', supporting_interviews=[interview_5])
update_hypothesis(df, 'CP.3', supporting_interviews=[interview_5])
update_hypothesis(df, 'CP.5', supporting_interviews=[interview_5])
update_hypothesis(df, 'CP.6', supporting_interviews=[interview_5])
update_hypothesis(df, 'CG.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'CG.2', supporting_interviews=[interview_5])
update_hypothesis(df, 'CG.4', supporting_interviews=[interview_5])
update_hypothesis(df, 'CG.5', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.4', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.9', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.10', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.11', supporting_interviews=[interview_5])
update_hypothesis(df, 'VP.13', supporting_interviews=[interview_5])

# Update new hypotheses NH.1-NH.11 with interview evidence
update_hypothesis(df, 'NH.1', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.2', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.3', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.4', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.5', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.6', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.7', supporting_interviews=[interview_5])
update_hypothesis(df, 'NH.8', supporting_interviews=[interview_6])
update_hypothesis(df, 'NH.9', supporting_interviews=[interview_6])
update_hypothesis(df, 'NH.10', supporting_interviews=[interview_6])
update_hypothesis(df, 'NH.11', supporting_interviews=[interview_7])

# Save the updated file
df.to_csv(file_path, index=False)

print(f"✅ Updated main hypothesis file: {file_path}")
print(f"\n📊 Update Summary:")
print(f"- Total hypotheses: {len(df)}")
print(f"- Hypotheses updated with Interview 3: 3")
print(f"- Hypotheses updated with Interview 4: 1")
print(f"- Hypotheses updated with Interview 5: 22")
print(f"- New hypotheses updated (NH.1-NH.11): 11")

# Count validation status
supported = len(df[df['Accept or Reject Hypotheses'] == 'Supported'])
partial = len(df[df['Accept or Reject Hypotheses'] == 'Partially Supported'])
rejected = len(df[df['Accept or Reject Hypotheses'] == 'Rejected'])
insufficient = len(df[df['Accept or Reject Hypotheses'] == 'Insufficient Data'])

print(f"\n🎯 Validation Status:")
print(f"- Supported: {supported}")
print(f"- Partially Supported: {partial}")
print(f"- Rejected: {rejected}")
print(f"- Insufficient Data: {insufficient}")
