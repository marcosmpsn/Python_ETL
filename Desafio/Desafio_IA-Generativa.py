# lendo arquivo csv
import pandas as pd

df = pd.read_csv('D:\Cursos\DIO\Python\Desafio\SDW2023.csv')
user_ids = df['UserID'].tolist()
#print(user_ids)

# importando usuários pela API SDW
import json
import requests

def get_user(id):
    response = requests.get(f'https://sdw-2023-prd.up.railway.app/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
#print(json.dumps(users, indent=2))

#Integrando com o ChatGPT

#Documentação API OpenAI: https://platform.openai.com/docs/api-reference/introduction
#Periodo Gratuito: https://help.openai.com/en/articles/4936830

#Para gerar uma API Key: https://platform.openai.com/account/api-keys
# 1. Crie uma conta na OpenAI
# 2. Acesse a seção "API Keys"
# 3. Clique em "Create API Key"


openai_api_key = "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"

import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=[
     {"role": "system", "content": "Você é um especialista em marketing bancário"},
     {"role": "user", 
      "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"}
     ])
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)