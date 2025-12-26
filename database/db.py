import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "dados" / "banco.sqlite"

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_banco():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS publicadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT NULL,
        data_nascimento TEXT,
        data_batismo TEXT,
        sexo TEXT,
        designacoes TEXT,
        privilegios TEXT,
        esperanca TEXT,
        grupo INTEGER,
        ativo INTEGER DEFAULT 1
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS grupos (
        numero INTEGER PRIMARY KEY
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS relatorios_mensais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        publicador_id INTEGER,
        ano_servico INTEGER,
        mes INTEGER,
        participou INTEGER,
        estudos INTEGER,
        horas INTEGER,
        observacoes TEXT,
        FOREIGN KEY (publicador_id) REFERENCES publicadores(id)
    )
    """)

    conn.commit()
    conn.close()
