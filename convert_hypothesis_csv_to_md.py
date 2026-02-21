import pandas as pd

# Read the CSV file
csv_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses_Updated_Feb1_2026.csv'
df = pd.read_csv(csv_path)

# Start building the markdown content
md_content = """# Hypothesis Tracking Table - February 1, 2026

**Last Updated:** February 1, 2026, 10:58 AM AST  
**Total Hypotheses:** {}  
**Source:** `Hypotheses_Updated_Feb1_2026.csv`

---

## 📊 Executive Summary

| Status | Count | Percentage |
|--------|-------|------------|
| **Supported** | {} | {:.1f}% |
| **Partially Supported** | {} | {:.1f}% |
| **Insufficient Data** | {} | {:.1f}% |
| **Rejected** | {} | {:.1f}% |

---

## 📋 Hypotheses by Category

""".format(
    len(df),
    len(df[df['Accept or Reject Hypotheses'] == 'Supported']),
    100 * len(df[df['Accept or Reject Hypotheses'] == 'Supported']) / len(df),
    len(df[df['Accept or Reject Hypotheses'] == 'Partially Supported']),
    100 * len(df[df['Accept or Reject Hypotheses'] == 'Partially Supported']) / len(df),
    len(df[df['Accept or Reject Hypotheses'] == 'Insufficient Data']),
    100 * len(df[df['Accept or Reject Hypotheses'] == 'Insufficient Data']) / len(df),
    len(df[df['Accept or Reject Hypotheses'] == 'Rejected']),
    100 * len(df[df['Accept or Reject Hypotheses'] == 'Rejected']) / len(df) if len(df[df['Accept or Reject Hypotheses'] == 'Rejected']) > 0 else 0
)

# Group hypotheses by BMC Block
categories = df['BMC Block'].unique()

for category in categories:
    if pd.isna(category):
        continue
    
    category_df = df[df['BMC Block'] == category]
    md_content += f"\n### {category} ({len(category_df)} hypotheses)\n\n"
    
    for idx, row in category_df.iterrows():
        hyp_id = row['Hypotheses # and name']
        hyp_text = row['Hypotheses']
        status = row['Accept or Reject Hypotheses']
        yes_count = int(row['# of Yes']) if pd.notna(row['# of Yes']) else 0
        supported_by = str(row['Which interviews supported the hypotheses?'])
        
        # Status emoji
        if status == 'Supported':
            status_emoji = '✅'
        elif status == 'Partially Supported':
            status_emoji = '⚠️'
        elif status == 'Rejected':
            status_emoji = '❌'
        else:
            status_emoji = '⏸️'
        
        md_content += f"#### {status_emoji} {hyp_id}\n\n"
        md_content += f"**Hypothesis:** {hyp_text}\n\n"
        md_content += f"- **Status:** {status}\n"
        md_content += f"- **Validations:** {yes_count}\n"
        
        if supported_by and supported_by != 'nan' and supported_by != '':
            md_content += f"- **Supported by:** {supported_by}\n"
        
        # Add Early Adopter profile
        early_adopter = str(row['Early Adopter'])
        if early_adopter and early_adopter != 'nan' and early_adopter != '':
            md_content += f"- **Early Adopter Profile:** {early_adopter}\n"
        
        md_content += "\n---\n\n"

# Add a section for strongest validated hypotheses
md_content += "\n## 🏆 Strongest Validated Hypotheses (2+ Interviews)\n\n"

strong_df = df[df['# of Yes'] >= 2].sort_values('# of Yes', ascending=False)

if len(strong_df) > 0:
    md_content += "| Hypothesis | Validations | Supported By |\n"
    md_content += "|-----------|-------------|---------------|\n"
    
    for idx, row in strong_df.iterrows():
        hyp_id = row['Hypotheses # and name']
        yes_count = int(row['# of Yes'])
        supported_by = str(row['Which interviews supported the hypotheses?'])
        md_content += f"| **{hyp_id}** | {yes_count} | {supported_by} |\n"
else:
    md_content += "*No hypotheses have been validated by 2+ interviews yet.*\n"

# Add a section for new hypotheses
md_content += "\n\n## 🆕 New Hypotheses (NH.1-NH.11 + H50-H53)\n\n"

new_hyp_df = df[df['Hypotheses # and name'].str.contains('NH.|H5', na=False, regex=True)]

if len(new_hyp_df) > 0:
    for idx, row in new_hyp_df.iterrows():
        hyp_id = row['Hypotheses # and name']
        hyp_text = row['Hypotheses']
        status = row['Accept or Reject Hypotheses']
        supported_by = str(row['Which interviews supported the hypotheses?'])
        
        status_emoji = '✅' if status == 'Supported' else '⏸️'
        
        md_content += f"### {status_emoji} {hyp_id}\n\n"
        md_content += f"{hyp_text}\n\n"
        md_content += f"- **Status:** {status}\n"
        md_content += f"- **Source:** {supported_by}\n\n"

# Save to markdown file
output_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Hypothesis/Hypotheses_Updated_Feb1_2026.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"✅ Created markdown file: {output_path}")
print(f"\nTotal hypotheses: {len(df)}")
print(f"Supported: {len(df[df['Accept or Reject Hypotheses'] == 'Supported'])}")
print(f"Categories covered: {len([c for c in categories if pd.notna(c)])}")
