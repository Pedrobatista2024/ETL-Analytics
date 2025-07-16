import scrapy

class NotebooksSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["mercadolivre.com.br"]
    base_url = "https://lista.mercadolivre.com.br/notebooks"
    max_pages = 10

    def start_requests(self):
        yield scrapy.Request(
            self.base_url,
            callback=self.parse,
            meta={'page': 1}
        )

    def parse(self, response):
        page = response.meta['page']
        self.logger.info(f"⚙ Página {page}: {response.url}")

        produtos = response.css("li.ui-search-layout__item")
        if not produtos:
            self.logger.warning("❌ Nenhum produto encontrado.")
            return 

        for p in produtos:
            # Nome
            nome = p.css("a.poly-component__title::text")\
                    .get(default="").strip()

            # Marca
            marca_raw = p.css("span.poly-component__seller::text")\
                         .get(default="").strip()
            marca = marca_raw.replace("Por ", "") or "—"

            # Vendedor
            vendedor = p.css("span.poly-component__seller::text")\
                        .get(default="").strip()

            # Reviews
            reviews_rating = p.css("span.poly-reviews__rating::text")\
                              .get() or "—"
            reviews_amount = p.css("span.poly-reviews__total::text")\
                              .re_first(r'\d+') or "—"

            # Tentativa de captar preço antigo via <s>
            old_cur = p.css(
                "s.andes-money-amount--previous span.andes-money-amount__currency-symbol::text"
            ).get()
            old_val = p.css(
                "s.andes-money-amount--previous span.andes-money-amount__fraction::text"
            ).get()

            if old_val:
                preco_antigo = f"{old_cur}{old_val}"
                # preço atual no div
                new_cur = p.css(
                    "div.poly-price__current span.andes-money-amount__currency-symbol::text"
                ).get()
                new_val = p.css(
                    "div.poly-price__current span.andes-money-amount__fraction::text"
                ).get()
                preco_atual = f"{new_cur}{new_val}" if new_val else "—"
            else:
                # sem <s>, pega o primeiro fraction como atual
                fractions = p.css("span.andes-money-amount__fraction::text").getall()
                currencies = p.css("span.andes-money-amount__currency-symbol::text").getall()
                preco_antigo = "—"
                if fractions and currencies:
                    preco_atual = f"{currencies[0]}{fractions[0]}"
                else:
                    preco_atual = "—"

            yield {
                "pagina":        page,
                "nome":          f"Nome: {nome}",
                "marca":         f"Marca: {marca}",
                "vendedor":      f"Vendedor: {vendedor}",
                "reviews":       f"Avaliação: {reviews_rating} ({reviews_amount} reviews)",
                "preco_antigo":  f"Preço antigo: {preco_antigo}",
                "preco_atual":   f"Preço atual: {preco_atual}",
            }

        # Paginação manual até max_pages
        if page < self.max_pages:
            next_offset = page * 48 + 1
            next_url = f"{self.base_url}_Desde_{next_offset}_NoIndex_True"
            self.logger.info(f"➡️ Indo para página {page+1}: {next_url}")
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                meta={'page': page + 1}
            )
        else:
            self.logger.info(f"✅ Limite de {self.max_pages} páginas atingido.")