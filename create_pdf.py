from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Manual da Marca - SOU Portal', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Content
content = [
    ("SOU Portal", "Sistema de Organização Unificada"),
    ("Conceito", "Central unificada de documentação, contratos e acompanhamento técnico do desenvolvimento do CRM da Administradora Mutual."),
    ("Logo Principal", "O logotipo é composto por quadrados concêntricos em azul institucional (#0056B3) e branco."),
    ("Valores", "1. Unificação\n2. Organização\n3. Transparência\n4. Segurança Jurídica\n5. Acompanhamento Técnico"),
    ("Cores", "Azul Institucional: #0056B3\nAzul Escuro: #004494\nBranco: #FFFFFF"),
    ("Tipografia", "Fonte principal: Inter (Bold, SemiBold, Regular, Light)"),
    ("Contato", "Gestão do Projeto SOU: projeto@administradoramutual.com.br")
]

for title, text in content:
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, title, 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, text)
    pdf.ln(5)

pdf.output('downloads/manual_sou_portal.pdf', 'F')
print("PDF manual created successfully.")
