# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdminareaItem(scrapy.Item):
    # define the fields for your item here like:
    barcode = scrapy.Field()
    produk = scrapy.Field()
    design = scrapy.Field()
    ukuran = scrapy.Field()
    warna = scrapy.Field()
    sonosewu = scrapy.Field()
    ytr = scrapy.Field()
    posyandu = scrapy.Field()
    sobo = scrapy.Field()
    dgd_store = scrapy.Field()
    jcm = scrapy.Field()
    tugu = scrapy.Field()
    total = scrapy.Field()
    terjual = scrapy.Field()
