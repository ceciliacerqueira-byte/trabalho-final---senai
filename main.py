import requests
import json
import datetime

# 1. FUNÇÃO PERSONALIZADA & MANIPULAÇÃO DE ARQUIVOS
def salvar_historico(cidade, recomendacao):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Abrindo arquivo em modo de adição ("a")
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{agora}] Cidade: {cidade} | Recomendação: {recomendacao}\n")

def buscar_coordenadas(cidade):
    # CONSUMO DE API PÚBLICA (Open-Meteo Geocoding - Gratuita)
    url_api = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
    resposta = requests.get(url_api)
    dados = resposta.json() # ESTRUTURAS JSON
    
    if "results" in dados:
        lat = dados["results"][0]["latitude"]
        lon = dados["results"][0]["longitude"]
        return lat, lon
    return None, None

def main():
    print("=== Bem-vindo ao Assistente Inteligente de Clima ===")
    url_webhook_n8n = "https://gemeas.app.n8n.cloud/webhook/assistente-clima"

    # 2. ESTRUTURA DE REPETIÇÃO (while)
    while True:
        # 3. ENTRADA DE DADOS (input)
        cidade = input("\nDigite o nome da cidade (ou 'sair' para encerrar): ")
        
        # 4. ESTRUTURAS CONDICIONAIS (if/elif/else)
        if cidade.strip().lower() == 'sair':
            print("Encerrando o assistente. Até logo!")
            break
        elif cidade.strip() == "":
            print("Nome de cidade inválido. Tente novamente.")
            continue
        else:
            print(f"Buscando informações para {cidade}...")
            
            lat, lon = buscar_coordenadas(cidade)
            
            if lat and lon:
                # 5. INTEGRAÇÃO COM N8N (Enviando Webhook)
                payload = {
                    "cidade": cidade,
                    "latitude": lat,
                    "longitude": lon
                }
                
                try:
                    print("Consultando a Inteligência Artificial no n8n...")
                    resposta_n8n = requests.post(url_webhook_n8n, json=payload)
                    
                    if resposta_n8n.status_code == 200:
                        dados_ia = resposta_n8n.json()
                        recomendacao = dados_ia.get("recomendacao", "Nenhuma recomendação recebida.")
                        
                        print("\n🤖 Resposta da IA:")
                        print(f"-> {recomendacao}")
                        
                        salvar_historico(cidade, recomendacao)
                    else:
                        print(f"Erro na integração com o n8n: Status {resposta_n8n.status_code}")
                
                except Exception as e:
                    print(f"Ocorreu um erro ao conectar com o n8n: {e}")
            else:
                print("Cidade não encontrada na API pública. Verifique o nome e tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()

