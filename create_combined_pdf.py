import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
import unicodedata

# Paths to the markdown files
brain_path = r"C:\Users\mtk17\.gemini\antigravity\brain\1e0b7907-a400-46bb-ba66-c4ebe5cfeb5f"

files = [
    ("1. Business Thesis & Value Proposition", "Business_Thesis_ValueProposition.md"),
    ("2. CRM & Interview Targets", "CRM_Interview_Targets.md"),
    ("3. Business Model Canvas", "Business_Model_Canvas_Draft.md"),
    ("4. AirTable Setup Guide", "AirTable_Setup_Guide.md")
]

# Output path
output_path = r"c:\Users\mtk17\OneDrive - Dalhousie University\Google Drive\PhD\Lab2Market\L2M_Week1_Assignments_Combined.pdf"

def clean_text(text):
    """Remove or replace problematic Unicode characters"""
    # Replace common Unicode characters
    replacements = {
        '✅': '[X]', '✓': '[OK]', '⭐': '*', '→': '->', '←': '<-', '↔': '<->',
        ''': "'", ''': "'", '"': '"', '"': '"', '…': '...',
        '–': '-', '—': '--', '•': '-', '▪': '-', '◦': 'o',
        '①': '1', '②': '2', '③': '3', '④': '4', '⑤': '5',
        '⑥': '6', '⑦': '7', '⑧': '8', '⑨': '9'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Remove any remaining non-ASCII characters
    text = ''.join(char if ord(char) < 128 else '?' for char in text)
    
    return text

# Create PDF using low-level canvas
c = canvas.Canvas(output_path, pagesize=A4)
width, height = A4

# Title page
c.setFont("Helvetica-Bold", 24)
c.drawString(inch, height - inch, "Lab2Market Week 1 Assignments")
c.setFont("Helvetica-Bold", 14)
c.drawString(inch, height - 1.5*inch, "Ocean Technology Project")
c.setFont("Helvetica", 12)
c.drawString(inch, height - 1.8*inch, f"Generated: {datetime.now().strftime('%B %d, %Y')}")

c.showPage()

# Process each file
y_position = height - inch
line_height = 14

for title_text, filename in files:
    filepath = os.path.join(brain_path, filename)
    print(f"Processing {filename}...")
    
    # Section header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(inch, y_position, clean_text(title_text))
    y_position -= 30
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        content = clean_text(content)
        
        lines = content.split('\n')
        
        c.setFont("Helvetica", 10)
        
        for line in lines:
            line = line.strip()
            if not line:
                y_position -= line_height / 2
                continue
            
            # Simple word wrapping
            words = line.split()
            current_line = ""
            
            for word in words:
                test_line = current_line + " " + word if current_line else word
                if c.stringWidth(test_line, "Helvetica", 10) < width - 2*inch:
                    current_line = test_line
                else:
                    if current_line:
                        c.drawString(inch, y_position, current_line)
                        y_position -= line_height
                        current_line = word
                    
                    if y_position < inch:
                        c.showPage()
                        y_position = height - inch
            
            if current_line:
                c.drawString(inch, y_position, current_line)
                y_position -= line_height
            
            if y_position < inch:
                c.showPage()
                y_position = height - inch
    
    # New page for next section
    c.showPage()
    y_position = height - inch

c.save()

print(f"\n[OK] PDF created successfully!")
print(f"Location: {output_path}")
