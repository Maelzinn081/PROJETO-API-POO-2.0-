from app.models.sensor_model import (
    criar_sensor,
    buscar_sensor,
    registrar_leitura,
    listar_sensores,
    listar_leituras,
    gerar_relatorio
)

from app.models.sensor_classes import (
    Sensor, SensorTemperatura, SensorUmidade, SensorQualidadeAr
)

import sqlite3 

# =============================
# SERVICES
# =============================



def service_criar_sensor(conn: sqlite3.Connection, tipo: str, local: str):
    return criar_sensor(conn, tipo, local)



def service_registrar_leitura(conn: sqlite3.Connection, id: int, valor: float):
    # Passa conn para buscar_sensor
    row = buscar_sensor(conn, id) 

    if row is None:
        return None, "Sensor não encontrado!"

    tipo, local = row

   
    if tipo == "temperatura":
        sensor = SensorTemperatura(tipo, local)
    elif tipo == "umidade":
        sensor = SensorUmidade(tipo, local)
    elif tipo == "ar":
        sensor = SensorQualidadeAr(tipo, local)
    else:
        sensor = Sensor(tipo, local)

    alerta = sensor.analisar_dado(valor)

   
    registrar_leitura(conn, id, valor) 

    return alerta, None



def service_listar_sensores(conn: sqlite3.Connection):
    # Passa conn para listar_sensores
    sensores = listar_sensores(conn)

    resultado = []
    for s in sensores:
        sensor_id, tipo, local = s
        # Passa conn para listar_leituras
        leituras = listar_leituras(conn, sensor_id) 
        media = sum(leituras) / len(leituras) if leituras else 0

        resultado.append({
            "id": sensor_id,
            "tipo": tipo,
            "local": local,
            "leituras": leituras,
            "media": media
        })

    return resultado



def service_relatorio(conn: sqlite3.Connection):
    return gerar_relatorio(conn)


