import pdfplumber

pdf_path = r'c:\Users\mtk17\OneDrive\Desktop\L2M\Lab2Market\Presentations\Week 9 - Mid\AddManuChain_Mid-Program_Report.pdf'

with pdfplumber.open(pdf_path) as pdf:
    print(f'Total Pages: {len(pdf.pages)}\n')
    for i, page in enumerate(pdf.pages):
        print(f'PAGE {i+1}:')
        
        # Extract text
        text = page.extract_text()
        if text.strip():
            print("TEXT:")
            print(text)
        
        # Extract tables
        tables = page.extract_tables()
        if tables:
            print("\nTABLES:")
            for table in tables:
                for row in table:
                    print(row)
        
        print('\n' + '='*80 + '\n')
