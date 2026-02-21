import pandas as pd

# Read the CRM data
df = pd.read_csv('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Stakeholder CRM-Kanban.csv')

# Calculate metrics
total_contacts = len(df)
completed_interviews = len(df[df['Interview Status'] == 'Interview Completed'])
scheduled_interviews = len(df[df['Interview Status'] == 'Scheduled'])
first_request = len(df[df['Interview Status'] == '1st Request'])
company_email = len(df[df['Interview Status'] == 'Comapny Email'])
connection = len(df[df['Interview Status'] == 'Connection'])

# Calculate conversion rates
outreaches_this_week = total_contacts  # All contacts ever made
completed_this_week = 2  # Bassey + Khashayar
scheduled_upcoming = scheduled_interviews

conversion_rate_completed = (completed_interviews / total_contacts) * 100 if total_contacts > 0 else 0
conversion_rate_all = ((completed_interviews + scheduled_interviews) / total_contacts) * 100 if total_contacts > 0 else 0

# Create summary report
report = f"""
# CUSTOMER DISCOVERY METRICS - WEEK 3
Generated: January 27, 2026

## PIPELINE OVERVIEW

Total Contacts in Database: {total_contacts}
├─ Completed Interviews: {completed_interviews} ({(completed_interviews/total_contacts)*100:.1f}%)
├─ Scheduled Interviews: {scheduled_interviews} ({(scheduled_interviews/total_contacts)*100:.1f}%)
├─ 1st Request Sent: {first_request} ({(first_request/total_contacts)*100:.1f}%)
├─ Company Email Only: {company_email} ({(company_email/total_contacts)*100:.1f})
└─ LinkedIn Connection: {connection} ({(connection/total_contacts)*100:.1f}%)

## CONVERSION METRICS

Conversion Rate (to Completed): {conversion_rate_completed:.2f}%
Conversion Rate (to Scheduled+Completed): {conversion_rate_all:.2f}%

## STATUS BREAKDOWN
"""

status_counts = df['Interview Status'].value_counts()
for status, count in status_counts.items():
    report += f"\n{status}: {count} ({(count/total_contacts)*100:.1f}%)"

report += f"""

## TOP ORGANIZATIONS TARGETED
"""
org_counts = df['Organization'].value_counts().head(10)
for org, count in org_counts.items():
    report += f"\n{org}: {count}"

report += f"""

## TOP DEPARTMENTS TARGETED
"""
dept_counts = df['Department'].value_counts().head(10)
for dept, count in dept_counts.items():
    report += f"\n{dept}: {count}"

report += f"""

## CAROL'S WEEKLY METRICS

**Outreaches this week:** {total_contacts}
**Interviews completed this week:** {completed_this_week}
**Conversion rate:** {(completed_this_week/total_contacts)*100:.2f}%

**Performance Level:** {"Failing" if total_contacts < 75 else "At Risk" if total_contacts < 100 else "Meeting the Bar" if total_contacts < 200 else "Strong" if total_contacts < 300 else "Excellent"}
"""

# Save report
with open('/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Presentations/Week 3/CRM_Metrics_Report.md', 'w') as f:
    f.write(report)

print("✅ Metrics report created successfully!")
print(report)
