import csv
from collections import Counter

csv_path = r'C:\Users\mtk17\Downloads\Stakeholder CRM-Kanban (6).csv'

status_counts = Counter()

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        status = row.get('Interview Status', '').strip()
        if status:
            status_counts[status] += 1

total = sum(status_counts.values())

print("Status Breakdown:")
print("=" * 60)
print(f"{'Status':<30} {'Count':<15} {'% of Total':<15}")
print("-" * 60)

for status, count in sorted(status_counts.items(), key=lambda x: x[1], reverse=True):
    percentage = (count / total * 100) if total > 0 else 0
    print(f"{status:<30} {count:<15} {percentage:.1f}%")

print("-" * 60)
print(f"{'Total Outreach':<30} {total:<15} {'100.0%':<15}")
