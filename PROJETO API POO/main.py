# A N O T A Ç Õ E S:
# -----------------------------------------------------------------------------
# uvicorn main:app  --reload // para executar a API
# cd app // para acessar a pasta app

# Caso o VSCODE não reconheça as funções (reinstalação):
# pip instal uvicorn;
# pip instal uvicorn;
# ------------------------------------------------------------------------------

# AONDE O CÓDIGO DE FATO ESTÁ INICIANDO O BANCO? (BANCO DE DADOS)
# A inicialização e criação das tabelas do banco de dados (database.db) acontece aqui,
# chamando a função 'criar_tabelas()' que está definida em database.py.
# -------------------------------------------------------------------------------


from fastapi import FastAPI
from database import criar_tabelas
from app.controllers.sensor_controller import router


app = FastAPI()
criar_tabelas() 
app.include_router(router)


