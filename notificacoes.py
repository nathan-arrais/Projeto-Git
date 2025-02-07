import requests
import json

DOG_API_URL = "https://api.thedogapi.com/v1/images/search"
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

WEBHOOK_URL = "https://webhook.site/6904f9d5-7ddd-4eb2-8178-3ccfe9944d36" 

def buscar_pet(tipo: str):
    """Consulta a API de pets e retorna um nome e imagem."""
    url = DOG_API_URL if tipo == "cachorro" else CAT_API_URL
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()[0]  
        return f"Novo {tipo} disponivel para adocao!", dados.get("url", "Imagem nao encontrada")
    else:
        return f"Erro ao buscar {tipo}", None

def enviar_notificacao(mensagem: str, imagem_url: str):
    """Simula o envio de uma notificaçao via webhook e exibe no terminal."""
    payload = {
        "mensagem": mensagem,
        "imagem": imagem_url
    }

    print("🔔 Notificação enviada!")
    print(json.dumps(payload, indent=4))

if __name__ == "__main__":
    for pet in ["cachorro", "gato"]:
        mensagem, imagem = buscar_pet(pet)
        enviar_notificacao(mensagem, imagem)
