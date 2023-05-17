'''
Ejemplo de como definir las clases de abstraccion
'''
from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Dato(Item):
    texto = Field()

class SpiderDeDatos(Spider):
    name = "MiPrimerSpider"
    start_url = ['https://paginaParaExtraerDatos.com/']

    def parse(self, response):
        sel = Selector(response)
        titulo_de_pagina = sel.xpath('//h1/text()').get()

        lista = sel.xpath('//div[@id="datos"]')
        for elemento in lista:
            item = ItemLoader( Dato(), elemento)
            item.add_xpath('texto', '//h3/a/text()')
            yield item.load_item()