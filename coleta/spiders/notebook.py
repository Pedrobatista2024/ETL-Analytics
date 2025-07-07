import scrapy

class NotebookSpider(scrapy.Spider):
    name = 'notebook'
    allowed_domains = ['lista.mercadolivre.com.br']
    start_urls = ['https://lista.mercadolivre.com.br/notebooks']

    def parse(self, response):
        for produto in response.css('li.ui-search-layout__item'):
            nome = produto.css('a.poly-component__title::text').get(default='').strip()
            marca = nome.split()[0] if nome else ''

            old_cur = produto.css(
                's.andes-money-amount--previous .andes-money-amount__currency-symbol::text'
            ).get()
            old_val = produto.css(
                's.andes-money-amount--previous .andes-money-amount__fraction::text'
            ).get()
            preco_antigo = f'{old_cur}{old_val}' if old_val else None

            new_cur = produto.css(
                'div.poly-price__current .andes-money-amount__currency-symbol::text'
            ).get()
            new_val = produto.css(
                'div.poly-price__current .andes-money-amount__fraction::text'
            ).get()
            preco_atual = f'{new_cur}{new_val}' if new_val else None

            yield {
                'nome': nome,
                'marca': marca,
                'preco_antigo': preco_antigo,
                'preco_atual': preco_atual,
            }

        next_page = response.css('a.andes-pagination__link--next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)