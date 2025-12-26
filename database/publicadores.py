from database.db import conectar

def adicionar_publicador(
    nome,
    nascimento,
    batismo,
    sexo,
    designacoes,
    privilegios,
    esperanca,
    grupo
):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO publicadores
    (nome_completo, data_nascimento, data_batismo, sexo,
     designacoes, privilegios, esperanca, grupo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome, nascimento, batismo, sexo,
        designacoes, privilegios, esperanca, grupo
    ))

    conn.commit()
    conn.close()
