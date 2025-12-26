import fitz  # PyMuPDF

pdf_path = "/home/user/relatorios/pdf/S-21_T.pdf"
doc = fitz.open(pdf_path)

with open("campos_s21.txt", "w", encoding="utf-8") as f:
    for page_num in range(len(doc)):
        page = doc[page_num]
        widgets = page.widgets()

        if widgets:
            f.write(f"\n--- Página {page_num + 1} ---\n")
            for w in widgets:
                f.write(f"{w.field_name} | {w.field_type}\n")

print("✅ Campos exportados para campos_s21.txt")








