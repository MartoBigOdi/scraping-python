"""
OBJETIVO:  
    - Extraer los datos de repositorios publicos y privados de Github de mi cuenta.
    - Aprender a autenticarnos dentro de Requests utilizando Basic Auth.
    - Aprender a autenticarnos por medio de un API.
    - Contrastar la autenticacion por API y la autenticacion por FORM DATA (LOGIN).
"""
import requests
from termcolor import colored

# Obtener token de acceso personal en la web de github
TOKEN = open('./oauthtoken.txt').readline().strip()
USERNAME = 'MartoBigOdi'
ENDPOINT = 'https://api.github.com/user/repos'
# Documentacion del API: https://api.github.com/


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

response = requests.get(
    ENDPOINT,
    headers=headers,
    auth=(USERNAME, TOKEN)  # TUPLA DE AUTENTICACION POR MEDIO DE BASIC AUTH
)

if response:
    repositorios = response.json()  # RESPUESTA ESTA EN FORMATO JSON
    print(colored("GitHub User: " + USERNAME, 'green', 'on_black', ['bold', 'blink']))
    for repositorio in repositorios:
        print("Repo Name:" + colored(repositorio['name'], 'green', 'on_black', ['bold', 'blink']))
