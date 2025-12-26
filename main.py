
from pathlib import Path
from pdf.s21 import criar_cartao_ano_servico, preencher_mes

BASE_DIR = Path(__file__).resolve().parent

# ── Criar cartão do ano de serviço ───────────────────
pdf = criar_cartao_ano_servico(
    modelo_pdf=BASE_DIR / "/home/user/relatorios/dados/cartoes/S-21_T.pdf",
    pasta_cartoes=BASE_DIR / "dados/cartoes",
    nome_completo="João da Silva",
    data_nascimento="10/05/1985",
    data_batismo="12/08/2005",
    sexo="M",
    designacoes=["Anciao"],
    privilegios=["Pioneiro Regular"],
    esperanca="Outras",
    ano_servico=2026
)

print("Cartão criado em:", pdf)

# ── Preencher um mês (teste) ─────────────────────────
preencher_mes(
    pdf_entrada=str(pdf),
    pdf_saida=str(pdf),
    mes_numero=11,  # Novembro
    participou=True,
    estudos=2,
    horas=35,
    observacoes="Boas visitas"
)










