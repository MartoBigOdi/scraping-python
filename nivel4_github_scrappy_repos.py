"""
OBJETIVO:  
    - Inicio de sesion a partir de formulario con scrapy
"""
import os
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
import scrapy

class LoginSpiderGitHub(Spider):
  name = 'GitHubLogin'
  start_urls = ['https://github.com/login']

  def parse(self, response):
    return scrapy.FormRequest.from_response(
      response,
      formdata={'login': 'MartoBigOdi', 'password': open('./password.txt').readline().strip()},
      callback=self.after_login
    )

  def after_login(self, response):
    request = scrapy.Request(
      'https://github.com/MartoBigOdi?tab=repositories',
      callback=self.parse_repositorios
    )
    yield request

  def parse_repositorios(self, response):
    sel = Selector(response)
    repositorios = sel.xpath('//h3[@class="wb-break-all"]/a/text()')
    output = "Username Github: MartoBigOdi\n"
    for repositorio in repositorios:
      output += "Repo Name: " + repositorio.get() + "\n"

    # Creamos la capeta donde va a estar el txt con los datos
    folder = "resultadoAuthGitHub"
    if not os.path.exists(folder):
      os.makedirs(folder)

    with open(os.path.join(folder, "resultados.txt"), "w") as file:
      file.write(output)


# Para poder ejecutar el archivo como un runner
process = CrawlerProcess()
process.crawl(LoginSpiderGitHub)
process.start()