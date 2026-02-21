import pdfplumber
import os

def extract_text(pdf_path, output_txt_path):
    print(f"Extracting from {pdf_path}...")
    try:
        text_content = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_content += page_text + "\n\n"
        
        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        print(f"Saved to {output_txt_path}")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

base_dir = "/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/Presentations/Week 3"

pdf1 = os.path.join(base_dir, "L2M Oceans 2026 Business Model Design and Customer Discovery FINAL 220126.pdf")
txt1 = os.path.join(base_dir, "business_model_content.txt")

pdf2 = os.path.join(base_dir, "IP & Legal Workshop_L2M_Jan_2026.pdf")
txt2 = os.path.join(base_dir, "ip_legal_content.txt")

extract_text(pdf1, txt1)
extract_text(pdf2, txt2)
