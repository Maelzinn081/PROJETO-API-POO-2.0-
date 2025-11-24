# Link da API: http://127.0.0.1:8000/docs#/default/registrar_leitura_sensores__id__registrar_post
# Estou trabalhando para solucionar este erro.
# API REST COM ARQUITETURA 3 CAMADAS.

# ..> Controllers
# ..> Service
# ..> Models
# uvicorn main:app  --reload//para executar a API
# cd app // para acessar a pasta app
# -------------------------------------------------------

# AONDE O CÓDIGO DE FATO ESTÁ INICIANDO O BANCO? (BANCO DE DADOS)
# A inicialização e criação das tabelas do banco de dados (database.db) acontece aqui,
# chamando a função 'criar_tabelas()' que está definida em database.py.
criar_tabelas() # <-- Este comentário e chamada servem como lembrete

# -------------------------------------------------------------

from fastapi import FastAPI
from database import criar_tabelas # 1. NOVIDADE: Importa a função do DB
from app.controllers.sensor_controller import router # Usei 'router' conforme sua imagem mais recente

# Cria a sua Loja Online (FastAPI)
app = FastAPI()

# 2. NOVIDADE: Diz ao Arquiteto para construir as salas do banco!
# Esta linha executa a criação do DB e das tabelas (se elas não existirem).
criar_tabelas() 

# Inclui as Rotas da Loja
app.include_router(router)


