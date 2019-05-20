import scrapy
import time

class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    # CONFIGURE HERE
    start_urls = ['https://www.groupon.com/browse/los-angeles']
    allResult = False # True or False
    waitTime = 1 #seconds
    # CONFIGURE HERE

    #RUN 
    # scrapy runspider /root/docker-LEMP/public/DataScraper/PY/groupon.py -o /root/docker-LEMP/public/DataScraper/PY/reports/groupon.csv
    # runGROUPON

    #DOWNLOAD
    # Close VPN connection
    # Visit http://68.183.131.151:85?report=groupon
   

    def parse(self, response):
        for business_page in response.css('#pull-cards>figure'):
            yield {
                'test':question.xpath('a/figcaption/div/p[contains(@class,"deal-title")]/text()').extract()
            }  
        #     if  business_page.css('.bizname>h2::text').get():
        #         yield response.follow('https://www.localsaver.com' + business_page.css('.bizname::attr(href)').get(),  callback=self.parse_info)
        #         time.sleep(BlogSpider.waitTime)

        # if BlogSpider.allResult is True:      
        #     time.sleep(BlogSpider.waitTime)
        #     for next_page in response.css('.show-more-results'):
        #         yield response.follow(next_page, self.parse)  
    SPLASH_URL = 'http://127.0.0.1:6023'
    def parse_info(self, response):
        yield {
            'website':  response.css('.openwebsite::attr(href)').extract(),
            'phone':  response.css('.showphone::attr(data-phone)').extract(),
            'street address':  response.css('.street-address::text').extract(),
            'location': response.css('.locality::text').extract(),
            'link': response.url,
            'title': response.css("h1::text").extract()
        }



        