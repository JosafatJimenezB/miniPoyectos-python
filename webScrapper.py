import requests
from bs4 import BeautifulSoup

url = 'https://midu.dev/'
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

else:
    print('No se pudo acceder al sitio web:', response.status_code)
