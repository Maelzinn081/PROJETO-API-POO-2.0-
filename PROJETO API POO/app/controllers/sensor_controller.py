import sqlite3 # Adicionado para tipagem
from fastapi import APIRouter, Depends # 'Depends' é a chave!
from ..services.sensor_service import ( 
    service_criar_sensor,
    service_registrar_leitura,
    service_listar_sensores,
    service_relatorio
)
# IMPORTANTE: Você precisa garantir que esta função exista no seu database.py
# Ela deve usar 'yield' e 'finally' para abrir e fechar a conexão.
from database import get_db 

router = APIRouter()

@router.get("/")
def inicio():
    return {"Mensagem": "API FUNCIONANDO! Use /docs para testar."}


@router.post("/sensores")
# O Service agora precisa receber a conexão para criar o sensor no DB
def criar_sensor(tipo: str, local: str, conn: sqlite3.Connection = Depends(get_db)):
    sensor_id = service_criar_sensor(conn, tipo, local) # Conexão passada ao service
    return {"mensagem": "Sensor criado!", "id": sensor_id}


@router.post("/sensores/{id}/registrar")
# 1. Correção: Injeção de Dependência usando 'Depends(get_db)'
def registrar(id: int, valor: float, conn: sqlite3.Connection = Depends(get_db)):
    # 2. Correção: A conexão 'conn' deve ser passada para o Service
    alerta, erro = service_registrar_leitura(conn, id, valor)

    if erro:
        return {"erro": erro}

    return {"mensagem": "Leitura registrada!", "valor": valor, "alerta": alerta}


@router.get("/sensores")
# O Service agora precisa receber a conexão para listar no DB
def listar(conn: sqlite3.Connection = Depends(get_db)):
    return service_listar_sensores(conn)


@router.get("/relatorio")
# O Service agora precisa receber a conexão para gerar o relatório
def relatorio(conn: sqlite3.Connection = Depends(get_db)):
    return service_relatorio(conn)


@router.get("/relatorio")
def relatorio():
    return service_relatorio()

