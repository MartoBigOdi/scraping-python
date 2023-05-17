from lxml import html
import requests

encabezados = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url_semilla = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

respuesta = requests.get(url_semilla, headers=encabezados)
print(respuesta.text)

parser = html.fromstring(respuesta.text)

print(parser)

h2_span = parser.get_element_by_id("Gwen_Stefani")
h2_span_by_xpath = parser.xpath("//span[@id='Gwen_Stefani']")

print(h2_span.text_content())
print(h2_span_by_xpath)



