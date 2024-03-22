import requests

# Endereços das APIs
api_urls = {
    'canais': 'https://iptv-org.github.io/api/channels.json',
    'fluxos': 'https://iptv-org.github.io/api/streams.json',
    'guias': 'https://iptv-org.github.io/api/guides.json',
    'categorias': 'https://iptv-org.github.io/api/categories.json',
    'idiomas': 'https://iptv-org.github.io/api/languages.json',
    'países': 'https://iptv-org.github.io/api/countries.json',
    'subdivisões': 'https://iptv-org.github.io/api/subdivisions.json',
    'regiões': 'https://iptv-org.github.io/api/regions.json',
    'lista_de_bloqueios': 'https://iptv-org.github.io/api/blocklist.json'
}

def obter_dados(api_url):
    """ Função para obter dados da API. """
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Exemplo de uso: Obter e imprimir a lista de canais
dados_canais = obter_dados(api_urls['canais'])
if dados_canais:
    for canal in dados_canais:
        print(f"Canal: {canal['name']} - ID: {canal['id']}")
else:
    print("Não foi possível obter os dados dos canais.")

# Você pode repetir o processo acima para as outras APIs.
