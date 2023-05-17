'''
Limpieza de datos hecha
Fomatos del archivo con el resultado: JSON y CSV
la "-O" para indicar que sobre escribimos el archivo en cada ejecucion.
la "-o" es para seguir sumando info al archivo que le indicamos con el comando, si no tenemos este archivos lo crea
por nosotros.
comando JSON: "scrapy runspider scrapy_beuatiful_eluniverso.py -O eluniverso_diario.json"
comando CSV: "scrapy runspider scrapy_beuatiful_eluniverso.py -O eluniverso_diario.csv"
Para ejecutar la app con este comando debemos comentar las lineas donde utilizamos la clase "CrawlerProcess"
'''
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

class Noticia(Item):
    id = Field()
    titular = Field()
    descripcion = Field()


class ELUniversoSpider(Spider):
    name = "Mi segunda Spider"
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    start_urls = ["https://www.eluniverso.com/deportes/"]

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.body, features="lxml")
        contenedor_noticias=soup.find_all(class_="feed | divide-y relative")
        id = 0
        for contenedor in contenedor_noticias:
          noticias = contenedor.find_all(class_='relative', recursive = False)
          for noticia in noticias:
            item = ItemLoader(Noticia(), response.body)
            titular = noticia.find('h2').text.replace('\n', '').replace('\r', '')
            descripcion = noticia.find('p')
            if (descripcion):
              item.add_value('descripcion', descripcion.text.replace('\n', '').replace('\r', ''))
            else:
              item.add_value('descripcion', 'N/A')
            item.add_value('titular', titular)
            item.add_value('id', id)
            id += 1
            yield item.load_item()


# Podemos ejecutar nuestra app tambien como una clase runner.
# con la clase CrawlerProcess de Scrapy
process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': './resultados_eluniverso_diario/eluniverso_diario.json'
})

process.crawl(ELUniversoSpider)
process.start()


