import docx
import os

docx_path = r"c:/Users/mtk17/OneDrive - Dalhousie University/Google Drive/PhD/Lab2Market/Contact List/B2B Lead Generation_ Oil & Gas Research.docx"

try:
    doc = docx.Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    with open("docx_content.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(full_text))
        
    print("Extraction successful.")
except Exception as e:
    print(f"Error: {e}")
