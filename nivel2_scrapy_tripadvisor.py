from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose


class Hotel(Item):
    nombre = Field()
    precio_booking = Field()
    precio_expedia = Field()
    precio_hilton = Field()
    descripcion = Field()
    amenities = Field()


class TripAdvisor(CrawlSpider):
    name = "hotels_tripadvisor"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html']
    download_delay = 2
    # Tupla de reglas para direccionar el movimiento de nuestro Crawler a traves de las paginas
    rules = (
        Rule(  # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/Hotel_Review-'  # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_hotel"),
    # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )

    def limpiar_item_extraido(self, texto):
        nuevo_texto = texto.replace(" ", " ")
        nuevo_texto + nuevo_texto.replace('\n', '')
        return nuevo_texto

    def parse_hotel(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)
        item.add_xpath('nombre', "//h1[@id='HEADING']/text()")
        item.add_xpath('precio_booking', "(//div[contains(text(), 'ARS')])[2]/text()",
                       # Con el MapCOmpose limpiamos el dato extraido.
                       MapCompose(self.limpiar_item_extraido))
        item.add_xpath('precio_expedia', "(//div[contains(text(), 'ARS')])[3]/text()",
                       MapCompose(self.limpiar_item_extraido))
        item.add_xpath('precio_hilton', "(//div[contains(text(), 'ARS')])[5]/text()",
                       MapCompose(self.limpiar_item_extraido))
        # XPATH, obtenemos el texto de dos elementos <p> que estan dentro de un <div>.
        item.add_xpath('descripcion', "(//div//p/text())[position()<=2]")
        # XPATH obtenemos el texto de 8 elementos que son los 8 primeros de 20 elementos con el mismo XPATH padre.
        item.add_xpath('amenities', "(//div[@class='yplav f ME H3 _c'])[position()<=8]/text()")
        # devolvemos el objeto
        yield item.load_item()









