import scrapy
import time
class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    # CONFIGURE HERE
    start_urls = ['https://www.localsaver.com/10001']
    allResult = False # True or False
    waitTime = 1 #seconds
    # CONFIGURE HERE

    #RUN 
    # scrapy runspider /root/docker-LEMP/public/DataScraper/PY/localsaver.py -o /root/docker-LEMP/public/DataScraper/PY/reports/localsaver.csv
    # runLOCALSAVER

    #DOWNLOAD
    # Close VPN connection
    # Visit http://68.183.131.151:85?report=localsaver



    def parse(self, response):
        for business_page in response.css('.items>.result-wrapper'):
            if  business_page.css('.bizname>h2::text').get():
                yield response.follow('https://www.localsaver.com' + business_page.css('.bizname::attr(href)').get(),  callback=self.parse_info)
                time.sleep(BlogSpider.waitTime)

        if BlogSpider.allResult is True:      
            time.sleep(BlogSpider.waitTime)
            for next_page in response.css('.show-more-results'):
                yield response.follow(next_page, self.parse)  

    def parse_info(self, response):
        yield {
            'website':  response.css('.openwebsite::attr(href)').extract(),
            'phone':  response.css('.showphone::attr(data-phone)').extract(),
            'street address':  response.css('.street-address::text').extract(),
            'location': response.css('.locality::text').extract(),
            'link': response.url,
            'title': response.css("h1::text").extract()
        }



        