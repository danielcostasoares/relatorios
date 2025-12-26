import fitz

MESES = {
    9: 20,   # Setembro
    10: 21,  # Outubro
    11: 22,  # Novembro
    12: 23,  # Dezembro
    1: 24,   # Janeiro
    2: 25,   # Fevereiro
    3: 26,   # Março
    4: 27,   # Abril
    5: 28,   # Maio
    6: 29,   # Junho
    7: 30,   # Julho
    8: 31    # Agosto
}

def preencher_mes(
    pdf_entrada,
    pdf_saida,
    mes_numero,
    participou,
    estudos,
    horas,
    observacoes,
    pioneiro_aux=False
):
    indice = MESES[mes_numero]

    doc = fitz.open(pdf_entrada)

    for page in doc:
        for w in page.widgets():
            if not w.field_name:
                continue

            if w.field_name == f"901_{indice}_CheckBox":
                w.field_value = participou
            elif w.field_name == f"902_{indice}_Text_C_SanSerif":
                w.field_value = str(estudos)
            elif w.field_name == f"903_{indice}_CheckBox":
                w.field_value = pioneiro_aux
            elif w.field_name == f"904_{indice}_S21_Value":
                w.field_value = str(horas)
            elif w.field_name == f"905_{indice}_Text_SanSerif":
                w.field_value = observacoes

            w.update()

    doc.save(pdf_saida, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)

import fitz
from pathlib import Path
import shutil

def criar_cartao_ano_servico(
    modelo_pdf,
    pasta_cartoes,
    nome_completo,
    data_nascimento,
    data_batismo,
    sexo,                # "M" ou "F"
    designacoes=None,    # lista: ["Anciao", "Servo"]
    privilegios=None,    # lista: ["Pioneiro Regular", ...]
    esperanca=None,      # "Outras" ou "Ungido"
    ano_servico=2026
):
    designacoes = designacoes or []
    privilegios = privilegios or []

    # ── Preparar caminhos ─────────────────────────────
    pasta_ano = Path(pasta_cartoes) / str(ano_servico)
    pasta_ano.mkdir(parents=True, exist_ok=True)

    nome_arquivo = nome_completo.replace(" ", "_")
    pdf_destino = pasta_ano / f"{nome_arquivo}_{ano_servico}.pdf"

    # ── Copiar modelo ─────────────────────────────────
    shutil.copy(modelo_pdf, pdf_destino)

    # ── Abrir PDF ─────────────────────────────────────
    doc = fitz.open(pdf_destino)

    for page in doc:
        widgets = page.widgets()
        if not widgets:
            continue

        for w in widgets:
            if not w.field_name:
                continue

            # ── Dados pessoais ─────────────────────────
            if w.field_name == "900_1_Text_SanSerif":
                w.field_value = nome_completo

            elif w.field_name == "900_2_Text_SanSerif":
                w.field_value = data_nascimento

            elif w.field_name == "900_5_Text_SanSerif":
                w.field_value = data_batismo

            elif w.field_name == "900_13_Text_C_SanSerif":
                w.field_value = str(ano_servico)

            # ── Sexo ───────────────────────────────────
            elif w.field_name == "900_3_CheckBox":  # Masculino
                w.field_value = (sexo.upper() == "M")

            elif w.field_name == "900_4_CheckBox":  # Feminino
                w.field_value = (sexo.upper() == "F")

            # ── Esperança ──────────────────────────────
            elif w.field_name == "900_6_CheckBox":  # Outras ovelhas
                w.field_value = (esperanca == "Outras")

            elif w.field_name == "900_7_CheckBox":  # Ungido
                w.field_value = (esperanca == "Ungido")

            # ── Designações ────────────────────────────
            elif w.field_name == "900_8_CheckBox":  # Ancião
                w.field_value = ("Anciao" in designacoes)

            elif w.field_name == "900_9_CheckBox":  # Servo ministerial
                w.field_value = ("Servo" in designacoes)

            # ── Privilégios ────────────────────────────
            elif w.field_name == "900_10_CheckBox":  # Pioneiro regular
                w.field_value = ("Pioneiro Regular" in privilegios)

            elif w.field_name == "900_11_CheckBox":  # Pioneiro especial
                w.field_value = ("Pioneiro Especial" in privilegios)

            elif w.field_name == "900_12_CheckBox":  # Missionário
                w.field_value = ("Missionario" in privilegios)

            w.update()

    # ── Salvar incrementalmente ───────────────────────
    doc.save(pdf_destino, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()

    return pdf_destino

