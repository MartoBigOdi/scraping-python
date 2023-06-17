'''
Como ya sabemos siempre conviene utilizar para encontrar el elemento dentro del arbol el
xpath antes que cualquier otro atributo. Mismo conviene en cualquier marco de atributos dinamicos.
@method: parse()
@:parameter primer para metro, Pregunta() --> Clase Pregunta
            Segundo parametro, Selector --> html que contiene el elemento.

#### Comando para correr el archivo:  scrapy runspider nivel1_scrapy_stackoverflow.py -O stackoverflow_questions.csv:csv
Capturamos data pero sin limpieza de datos
'''
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# esta clase hereda de la Clase Item
class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()
    # este atributo es para que tengamos un orden en los
    # elementos que vamos instanciando.
    # Buena practica para luego poder identificarlo mejor
    id = Field()


# esta clase hereda de la Clase Spider
class StackOverFlowSpider(Spider):
    name = "MiPrimerSpider"
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    start_urls = ['https://stackoverflow.com/questions']

    def parse(self, response, **kwargs):
        i = 0
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]')
        for pregunta in preguntas:
            # la clase Pregunta previamante creada la necesitamos para instanciar
            # el objeto, y con el contenido del scrap (que lo pasamos como segundo parametro)
            # seteamos los atributos del objeto de la clase Pregunta
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta', "//h3[@class='s-post-summary--content-title']/a")
            item.add_xpath("descripcion", "//div[@class='s-post-summary--content-excerpt']")
            item.add_value('id', i)
            i += 1
            yield item.load_item()


