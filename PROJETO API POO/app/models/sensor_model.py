import sqlite3 # Adicionado para tipagem
# Removida a importação de get_connection, pois agora ela vem do argumento da função.
# from .database import get_connection 

# =============================
# CRUD — Banco de Dados (DAO)
# =============================

# 1. FUNÇÃO: criar_sensor
def criar_sensor(conn: sqlite3.Connection, tipo: str, local: str):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO sensores (tipo, local) VALUES (?, ?)", (tipo, local))
    conn.commit()

    sensor_id = cursor.lastrowid
    # REMOVIDO: conn.close()
    return sensor_id


# 2. FUNÇÃO: buscar_sensor
def buscar_sensor(conn: sqlite3.Connection, id: int):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT tipo, local FROM sensores WHERE id = ?", (id,))
    row = cursor.fetchone()

    # REMOVIDO: conn.close()
    return row


# 3. FUNÇÃO: registrar_leitura
def registrar_leitura(conn: sqlite3.Connection, sensor_id: int, valor: float):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO leituras (sensor_id, valor) VALUES (?, ?)", (sensor_id, valor))
    conn.commit()
    # REMOVIDO: conn.close()


# 4. FUNÇÃO: listar_sensores
def listar_sensores(conn: sqlite3.Connection):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sensores")
    sensores = cursor.fetchall()
    # REMOVIDO: conn.close()
    return sensores


# 5. FUNÇÃO: listar_leituras
def listar_leituras(conn: sqlite3.Connection, sensor_id: int):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT valor FROM leituras WHERE sensor_id = ?", (sensor_id,))
    dados = cursor.fetchall()

    # REMOVIDO: conn.close()
    return [d[0] for d in dados]


# 6. FUNÇÃO: gerar_relatorio
def gerar_relatorio(conn: sqlite3.Connection):
    # REMOVIDO: conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT local, tipo, COUNT(*), AVG(valor)
        FROM sensores 
        JOIN leituras ON sensores.id = leituras.sensor_id 
        GROUP BY sensores.id
    """)

    dados = cursor.fetchall()
    # REMOVIDO: conn.close()
    return dados
