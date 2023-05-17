from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    amenities = Field()


class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    start_urls = 'https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html'
    download_delay = 2
    # Con esta reglas lo que le indicamos, es primero el comienzo de los links que queremos encontrar
    # luego le indicamos que funcion vamos a utilizar dentro de estos links que encontremos.
    rules = (
        Rule(
            LinkExtractor(
                    # con una expresion regular le indicamos la regla allow
                    allow=r'/Hotel_Review-'
            ), follow= True, callback="parse_hotel"
        )
    )

    def parse_hotel(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)
        item.add_xpath('nombre', '')
        item.add_xpath('precio', '')
        item.add_xpath('descripcion', '')
        item.add_xpath('amenities', '')






