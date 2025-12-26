from database.db import conectar

def listar_publicadores(grupo=None, ordem_alfabetica=True):
    conn = conectar()
    cur = conn.cursor()

    query = "SELECT id, nome_completo, grupo FROM publicadores WHERE ativo = 1"
    params = []

    if grupo:
        query += " AND grupo = ?"
        params.append(grupo)

    if ordem_alfabetica:
        query += " ORDER BY nome_completo COLLATE NOCASE"

    cur.execute(query, params)
    dados = cur.fetchall()
    conn.close()
    return dados


def status_relatorio(publicador_id, ano_servico, mes):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT participou FROM relatorios_mensais
        WHERE publicador_id=? AND ano_servico=? AND mes=?
    """, (publicador_id, ano_servico, mes))

    r = cur.fetchone()
    conn.close()

    return "Relatou" if r else "Não relatou"
