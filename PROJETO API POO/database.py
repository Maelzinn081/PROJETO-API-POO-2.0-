import sqlite3

def get_connection():
    # Esta linha cria o arquivo 'database.db' se ele não existir
    return sqlite3.connect("database.db")

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    # Criação da tabela de Sensores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY, 
            tipo TEXT, 
            local TEXT
        )
    """)

    # Criação da tabela de Leituras
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY, 
            sensor_id INTEGER, 
            valor REAL
        )
    """)

    conn.commit()
    conn.close()


# ⚠️ NOVA FUNÇÃO CRÍTICA PARA O FASTAPI (Dependency Injection) ⚠️
def get_db():
    # 1. Abre a conexão
    conn = get_connection() 
    try:
        # 2. 'yield' entrega a conexão ao FastAPI
        yield conn 
    finally:
        # 3. 'finally' garante que a conexão será FECHADA após o uso
        conn.close() 
