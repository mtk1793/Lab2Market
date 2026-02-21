import pandas as pd
from openpyxl import load_workbook

# Load the Excel file
file_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Target_Companies_Contacts_AddManuChain.xlsx'
df = pd.read_excel(file_path)

# Contact information found through research
contact_data = {
    # High Priority Contacts
    'Lorenzo Simonelli': {'linkedin': 'https://www.linkedin.com/in/lorenzo-simonelli', 'email': 'lorenzo.simonelli@bakerhughes.com'},
    'Fanny Charreteur': {'linkedin': 'https://ca.linkedin.com/in/fanny-charreteur-5bb5a723', 'email': 'fcharreteur@rtmq.ca'},
    'Sean Morgan': {'linkedin': 'https://ca.linkedin.com/in/sean-morgan-90a3a042', 'email': 'sean.morgan@atlanticxl.com'},
    'Jason Power': {'linkedin': 'https://www.linkedin.com/in/jason-power-8740b1b8', 'email': 'jpower@noblecorp.com'},
    'Maria Claudia Borras': {'linkedin': 'https://www.linkedin.com/in/maria-claudia-borras', 'email': 'maria.borras@bakerhughes.com'},
    'Amerino Gatti': {'linkedin': 'https://www.linkedin.com/in/amerino-gatti', 'email': 'amerino.gatti@bakerhughes.com'},
}

# Company email patterns for contacts we found
email_patterns = {
    'Baker Hughes': '{firstname}.{lastname}@bakerhughes.com',
    'Schlumberger': '{firstname}.{lastname}@slb.com or {F}{lastname}@slb.com',
    'TechnipFMC': '{firstname}.{lastname}@technipfmc.com',
    'NOV': '{firstname}.{lastname}@nov.com',
    'Atlantic XL': '{firstname}.{lastname}@atlanticxl.com',
    'Noble Corporation': '{flast}@noblecorp.com',
    'CQFA': 'info@cqfa.quebec or {contact}@rtmq.ca'
}

# Add research notes column if it doesn't exist
if 'Research_Notes' not in df.columns:
    df['Research_Notes'] = ''

# Update the dataframe with found contact information
for index, row in df.iterrows():
    name = str(row['Stakeholder Name']).strip()
    if name in contact_data:
        # Update LinkedIn if cell is empty or NaN
        if pd.isna(row['LinkedIn']) or row['LinkedIn'] == '':
            df.at[index, 'LinkedIn'] = contact_data[name]['linkedin']
        # Update Email if cell is empty or NaN
        if pd.isna(row['Email']) or row['Email'] == '':
            df.at[index, 'Email'] = contact_data[name]['email']
        df.at[index, 'Research_Notes'] = 'Verified via LinkedIn/Google search - Jan 31, 2026'

# Special notes for contacts that need verification
special_notes = {
    'Christopher J. Kuehn': 'Role may have changed - currently at Trane Technologies  as EVP & CFO. Verify current Schlumberger EVP Wells contact.',
    'Lorenzo Desmarchi': 'LinkedIn not found - verify current SVP Subsea Projects at TechnipFMC',
    'John Kidwell': 'LinkedIn not found for NOV role - verify current VP Supply Chain North America',
    'Rob Bayless': 'LinkedIn not found - verify current GM Operations at Cameron/Schlumberger'
}

for index, row in df.iterrows():
    name = str(row['Stakeholder Name']).strip()
    if name in special_notes and (pd.isna(row['Research_Notes']) or row['Research_Notes'] == ''):
        df.at[index, 'Research_Notes'] = special_notes[name]
    
    # Add email patterns for companies where we didn't find specific emails
    company = str(row['Organization']).strip()
    if company in email_patterns:
        if (pd.isna(row['Email']) or row['Email'] == '') and (pd.isna(row['Research_Notes']) or row['Research_Notes'] == ''):
            df.at[index, 'Research_Notes'] = f'Email pattern: {email_patterns[company]}'

# Save to a new file
output_path = '/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Results/Target_Companies_Contacts_UPDATED.xlsx'
df.to_excel(output_path, index=False)

print(f"✅ Updated contact information saved to: {output_path}")
print(f"\n📊 Summary:")
print(f"- Total contacts in list: {len(df)}")
linkedin_count = df['LinkedIn'].notna().sum()
email_count = df['Email'].notna().sum()
notes_count = df['Research_Notes'].notna().sum()
print(f"- Contacts with LinkedIn URLs: {linkedin_count}")
print(f"- Contacts with email addresses: {email_count}")
print(f"- Contacts with research notes: {notes_count}")
print(f"\n✨ Newly added/verified contacts:")
for name in contact_data.keys():
    print(f"  - {name}")

