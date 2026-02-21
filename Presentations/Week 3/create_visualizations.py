import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the CRM data
df = pd.read_csv('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Stakeholder CRM-Kanban.csv')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 1. Interview Status Distribution
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Status counts
status_counts = df['Interview Status'].value_counts()
axes[0, 0].pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
axes[0, 0].set_title('Interview Status Distribution', fontsize=14, fontweight='bold')

# Department distribution (top 15)
dept_counts = df['Department'].value_counts().head(15)
axes[0, 1].barh(dept_counts.index, dept_counts.values, color='skyblue')
axes[0, 1].set_xlabel('Count')
axes[0, 1].set_title('Top 15 Departments Targeted', fontsize=14, fontweight='bold')
axes[0, 1].invert_yaxis()

# Organization distribution (top 15)
org_counts = df['Organization'].value_counts().head(15)
axes[1, 0].barh(org_counts.index, org_counts.values, color='lightcoral')
axes[1, 0].set_xlabel('Count')
axes[1, 0].set_title('Top 15 Organizations Targeted', fontsize=14, fontweight='bold')
axes[1, 0].invert_yaxis()

# Job Title categories
job_title_counts = df['Job Title/Position'].value_counts().head(15)
axes[1, 1].barh(job_title_counts.index, job_title_counts.values, color='lightgreen')
axes[1, 1].set_xlabel('Count')
axes[1, 1].set_title('Top 15 Job Titles Targeted', fontsize=14, fontweight='bold')
axes[1, 1].invert_yaxis()

plt.tight_layout()
plt.savefig('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Presentations/Week 3/CRM_Overview_Visualization.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Detailed metrics
total_contacts = len(df)
completed_interviews = len(df[df['Interview Status'] == 'Interview Completed'])
scheduled_interviews = len(df[df['Interview Status'] == 'Scheduled'])
first_request = len(df[df['Interview Status'] == '1st Request'])
company_email = len(df[df['Interview Status'] == 'Comapny Email'])
connection = len(df[df['Interview Status'] == 'Connection'])

# Create metrics visualization
fig, ax = plt.subplots(figsize=(12, 6))
categories = ['Total\nContacts', 'Completed\nInterviews', 'Scheduled\nInterviews', 
              '1st Request\nSent', 'Company\nEmail Only', 'LinkedIn\nConnection']
values = [total_contacts, completed_interviews, scheduled_interviews, first_request, company_email, connection]
colors = ['#2E86AB', '#06A77D', '#F18F01', '#C73E1D', '#A4036F', '#6A4C93']

bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Count', fontsize=12, fontweight='bold')
ax.set_title('Customer Discovery Pipeline Metrics', fontsize=16, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Presentations/Week 3/CRM_Metrics_Visualization.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Conversion funnel
fig, ax = plt.subplots(figsize=(10, 8))
funnel_stages = ['Total Outreach', '1st Request', 'Scheduled', 'Completed']
funnel_values = [total_contacts, first_request, scheduled_interviews, completed_interviews]
funnel_percentages = [100, (first_request/total_contacts)*100, 
                      (scheduled_interviews/total_contacts)*100, 
                      (completed_interviews/total_contacts)*100]

y_pos = range(len(funnel_stages))
bars = ax.barh(y_pos, funnel_values, color=['#003f5c', '#58508d', '#bc5090', '#ff6361'])

for i, (stage, value, pct) in enumerate(zip(funnel_stages, funnel_values, funnel_percentages)):
    ax.text(value + 5, i, f'{value} ({pct:.1f}%)', va='center', fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(funnel_stages)
ax.set_xlabel('Number of Contacts', fontsize=12, fontweight='bold')
ax.set_title('Customer Discovery Conversion Funnel', fontsize=16, fontweight='bold')
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Presentations/Week 3/CRM_Funnel_Visualization.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Visualizations created successfully!")
print(f"\nMetrics Summary:")
print(f"Total Contacts: {total_contacts}")
print(f"Completed Interviews: {completed_interviews}")
print(f"Scheduled Interviews: {scheduled_interviews}")
print(f"1st Request Sent: {first_request}")
print(f"Conversion Rate (Completed/Total): {(completed_interviews/total_contacts)*100:.2f}%")
print(f"Conversion Rate (Scheduled+Completed/Total): {((completed_interviews+scheduled_interviews)/total_contacts)*100:.2f}%")
