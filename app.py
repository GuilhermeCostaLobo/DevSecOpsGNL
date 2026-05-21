import requests

def buscar_dados():
    print("Buscando dados da API...")
    response = requests.get("https://example.com")
    print(f"Status da resposta: {response.status_code}")
    return response.status_code

if __name__ == "__main__":
    buscar_dados()
