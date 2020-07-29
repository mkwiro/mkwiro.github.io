import scrapy
import datetime
from ..items import AdminareaItem


class AdminSpider(scrapy.Spider):
    name ="admins"
    page_number = 2
    date = datetime.datetime.now()
    b2 = ["00", "01", "03", "08", "09", "10", "14"]
    # start_urls = [
    #     'http://103.27.36.114/sipandu2/ID_barang_perbandingan.php?date2='+ str(date.strftime("%d-%m-%Y")) +'&katakunci=&b1=kosong&b2='+ str(b2[1]) +'&b3=kosong&b11=kosong&b10=kosong&b4=kosong&b5=kosong&b6=kosong&b7=kosong&b8=kosong&txt_design=Semua+Design&b9=kosong&b12=kosong&PageSize=20&cHidden=1&cSubmit=Cari&PageNo=1'
    #     ]
    start_urls = [
       'http://103.27.36.114/sipandu2/ID_barang_perbandingan.php?date2='+ str(date.strftime("%d-%m-%Y")) +'&katakunci=&b1=kosong&b2=kosong&b3=kosong&b11=kosong&b10=kosong&b4=kosong&b5=kosong&b6=kosong&b7=kosong&b8=kosong&txt_design=Semua+Design&b9=kosong&b12=kosong&PageSize=20&cHidden=1&cSubmit=Cari'
   ]

    def parse(self, response):

        items = AdminareaItem()

        all_div_product = response.xpath('/html/body/div[1]/div[2]/div[2]/table[2]/tr')

        for product in all_div_product:

            barcode = product.xpath('td[2]/text()').extract()
            produk =product.xpath('normalize-space(td[3]/text())').extract()
            design = product.xpath('td[4]/text()').extract()
            ukuran = product.xpath('td[5]/text()').extract()
            warna = product.xpath('td[6]/text()').extract()
            sonosewu = product.xpath('td[7]/text()').extract()
            ytr = product.xpath('td[8]/text()').extract()
            posyandu = product.xpath('td[9]/text()').extract()
            sobo = product.xpath('td[10]/text()').extract()
            dgd_store = product.xpath('td[11]/text()').extract()
            jcm = product.xpath('td[12]/text()').extract()
            tugu = product.xpath('td[13]/text()').extract()
            total = product.xpath('td[14]/text()').extract()
            terjual = product.xpath('td[15]/text()').extract()

            items['barcode']= barcode
            items['produk'] = produk
            items['design'] = design
            items['ukuran'] = ukuran
            items['warna'] = warna
            items['sonosewu'] = sonosewu
            items['ytr'] = ytr
            items['posyandu'] = posyandu
            items['sobo'] = sobo
            items['dgd_store'] = dgd_store
            items['jcm'] = jcm
            items['tugu'] = tugu
            items['total'] = total
            items['terjual'] = terjual



            yield items

            next_page = response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]//li[12]/a/@href').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)


            # next_page = 'http://103.27.36.114/sipandu2/ID_barang_perbandingan.php?date2='+ str(AdminSpider.date.strftime("%d-%m-%Y")) +'&katakunci=&b1=kosong&b2='+ str(AdminSpider.b2[1]) +'&b3=kosong&b11=kosong&b10=kosong&b4=kosong&b5=kosong&b6=kosong&b7=kosong&b8=kosong&txt_design=Semua+Design&b9=kosong&b12=kosong&PageSize=20&cHidden=1&cSubmit=Cari&PageNo='+ str(AdminSpider.page_number) +''
            # if AdminSpider.page_number < 5:
            #    AdminSpider.page_number += 1
            #    yield response.follow(next_page, callback=self.parse)
