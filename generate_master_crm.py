import csv
import datetime

input_file = "Company,Persona,Full Name,Exact Job.txt"
output_file = "Master_Customer_Discovery_Database.md"

def clean_text(text):
    return text.strip() if text else ""

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        contacts = list(reader)

    # Group by Industry (infer from Company)
    industries = {
        "Offshore Energy (Oil & Gas)": ["Suncor", "CNRL", "Cenovus", "Imperial", "Enbridge", "TC Energy", "Irving Oil", "Saudi Aramco", "ADNOC", "QatarEnergy", "Kuwait", "Petrobras", "ExxonMobil", "Chevron", "Shell", "BP", "TotalEnergies", "Equinor", "Eni", "ConocoPhillips", "Occidental", "Repsol", "OMV", "Galp", "Petronas", "Pertamina", "PetroChina", "Sinopec", "CNPC", "Gazprom", "Woodside", "Santos"],
        "Mining & Metals": ["Teck", "Barrick", "Agnico", "Kinross", "First Quantum", "Lundin", "Hudbay", "B2Gold", "Nutrien", "Vale", "Glencore", "Anglo American", "Freeport", "Newmont", "Fortescue", "Antofagasta", "Southern Copper", "Zijin", "CMOC", "Coal India", "KGHM", "Rio Tinto", "BHP"],
        "Maritime & Shipbuilding": ["Irving Shipbuilding", "Seaspan", "Babcock", "Canadian Coast Guard", "Maersk", "MSC", "CMA CGM", "COSCO", "Hapag-Lloyd", "Ocean Network", "Evergreen", "ZIM", "PIL", "X-Press", "Matson", "Hafnia", "HII", "GD Electric", "Bath Iron", "Fincantieri", "Naval Group", "BAE", "Damen", "Austal"],
        "Drilling Contractors": ["Transocean", "Valaris", "Noble", "Seadrill", "Diamond", "Stena", "Shelf", "Odfjell", "COSL", "Saipem"]
    }

    markdown_content = f"""# Master Customer Discovery Database
## Lab2Market Ocean Technology Project

*Generated: {datetime.datetime.now().strftime("%B %d, %Y")}*

---

## 🧠 Strategic Context: The Two Personas

### **Persona A: The Asset/Operations Owner**
*   **Focus:** "Cost of Downtime", "Schedule Attainment", "Profit".
*   **Role:** General Manager, VP Operations, President.
*   **Pitch:** "We ensure your assets actally run 99.8% of the time by eliminating supply chain delays."

### **Persona B: The Technical Gatekeeper**
*   **Focus:** "Mechanical Integrity", "Reliability", "Spare Parts Strategy".
*   **Role:** Maintenance Manager, Technical Director, Reliability Engineer.
*   **Pitch:** "We automate the DNV certification trail so you never fail an audit."

---

"""

    # Process and organize contacts
    unknown_industry = []
    
    for industry, companies in industries.items():
        industry_contacts = []
        for contact in contacts:
            company = contact.get("Company", "")
            # Check if company starts with any of the known company keys
            if any(key in company for key in companies):
                industry_contacts.append(contact)
        
        if not industry_contacts:
            continue
            
        markdown_content += f"## 🏭 {industry}\n\n"
        markdown_content += "| Company | Persona | Name | Job Title | Location | Contact |\n"
        markdown_content += "| :--- | :---: | :--- | :--- | :--- | :--- |\n"
        
        for c in industry_contacts:
            name = f"**{clean_text(c.get('Full Name'))}**"
            title = clean_text(c.get('Exact Job Title'))
            persona = clean_text(c.get('Persona')).replace("Persona ", "")
            company = f"**{clean_text(c.get('Company'))}**"
            location = clean_text(c.get('Primary Physical Work Location'))
            
            # Format Contact Info
            email = clean_text(c.get('Work Email Address'))
            phone = clean_text(c.get('Office Phone'))
            linkedin = clean_text(c.get('LinkedIn Profile URL'))
            
            contact_str = ""
            if email: contact_str += f"📧 [{email}](mailto:{email})<br>"
            if phone: contact_str += f"📞 {phone}<br>"
            if linkedin: contact_str += f"🔗 [LinkedIn]({linkedin})"
            
            markdown_content += f"| {company} | {persona} | {name} | {title} | {location} | {contact_str} |\n"
        
        markdown_content += "\n---\n\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully generated {output_file}")

except Exception as e:
    print(f"Error: {e}")
