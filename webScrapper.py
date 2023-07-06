import requests
from bs4 import BeautifulSoup

url = input('Ingrese la URL del sitio: ')

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    print('Enlaces encontrados \n')

    for link in links:
        href = link.get('href')
        text = link.text.strip()
        print(f'Enlace: {href}')
        print(f'Texto: {text}')
        # Imprime otros atributos relevantes si es necesario

except requests.HTTPError as e:
    print('Error al acceder al sitio web:', e)
except requests.RequestException as e:
    print('Error de solicitud:', e)
except Exception as e:
    print('Error inesperado:', e)