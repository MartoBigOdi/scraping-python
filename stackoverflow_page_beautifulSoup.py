'''
Scrap a la web stackOverFlow
Consumimos las preguntas y sus descripciones
Utilizamos: requests y BeautifulSoup
'''
import requests
from bs4 import BeautifulSoup

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url, headers=headers)
# print(respuesta.text)

# prestar atencion a colocar "features="lxml"
soup = BeautifulSoup(respuesta.text, features="lxml")

# obtenemos el contenedor de preguntas
contenedor_preguntas = soup.find('div', id="questions")
# guardamos en una lista las preguntas que sacamos de esta pagina
lista_preguntas = contenedor_preguntas.find_all('div', class_="s-post-summary js-post-summary")

# iteramos para conseguir el texto de cada pregunta, buscamos el tag h3 y le pedimos el text
for pregunta in lista_preguntas:
    elemento_pregunta_h3 = pregunta.find("h3")
    txt_h3_pregunta = pregunta.find("h3").text
    # obetenemos el texto de las descriociones
    descripcion_pregunta = elemento_pregunta_h3.find_next_sibling("div").text
    # otra forma de obtener la descripcion
    # descripcion_pregunta = pregunta.find(class_="s-post-summary--content-excerpt").text

    descripcion_pregunta = descripcion_pregunta.replace('\r', '').strip()
    print("Pregunta: " + txt_h3_pregunta)
    print(("Descripcion: " + descripcion_pregunta + "\n"))
    print("*************************************************************************************************************************************************************")


