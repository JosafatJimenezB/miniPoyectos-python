import requests
from bs4 import BeautifulSoup

genero = "fiction"
palabras_clave = "matrix"

url = f"https://www.imdb.com/search/title?genres={genero}&keywords={palabras_clave}"

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    lista_peliculas = soup.select(".lister-item.mode-advanced")

    for pelicula in lista_peliculas:

        titulo = pelicula.h3.a.text

        elemento_calificacion = pelicula.select_one(".ratings-imdb-rating")
        calificacion = elemento_calificacion.text.strip() if elemento_calificacion else "N/A"

        anio = pelicula.select_one(".lister-item-year").text.strip("()")

        print("Título:", titulo)
        print("Calificación:", calificacion)
        print("Año:", anio)
        print("---")
else:
    print("No se pudo obtener los datos de IMDb.")
