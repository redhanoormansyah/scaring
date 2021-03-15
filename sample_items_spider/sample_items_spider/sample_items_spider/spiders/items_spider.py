import scrapy
from sample_items_spider.items import SampleItemsSpiderItem


class ItemsSpiderSpider(scrapy.Spider):
    name = 'items_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath('//*[@itemprop="author"]/text()').extract()
        tags = response.xpath('//*[@class="tag-item"]/text()').extract()
        # yield {'authors': authors}
        item = SampleItemsSpiderItem()
        item['authors'] = authors
        item['tags'] = tags
        return item
