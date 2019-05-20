import scrapy
import time
class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    # CONFIGURE HERE
    start_urls = ['https://www.yelp.com/search?find_desc=Restaurants&find_loc=Manila%2C+Metro+Manila%2C+Philippines&ns=1']
    allResult = False # True or False
    waitTime = 10 #seconds
    # CONFIGURE HERE

    #RUN 
    # scrapy runspider /root/docker-LEMP/public/DataScraper/PY/yelp.py -o /root/docker-LEMP/public/DataScraper/PY/reports/yelp.csv
    # runYELP

    #DOWNLOAD
    # Close VPN connection
    # Visit http://68.183.131.151:85?report=yelp



    def parse(self, response):
        for business_page in response.css('ul>li'):
            if  business_page.css('h3>a::text').get():
                yield response.follow(business_page.css('h3>a::attr(href)').get().strip(),  callback=self.parse_info)
                time.sleep(BlogSpider.waitTime)

        if BlogSpider.allResult is True:      
            time.sleep(BlogSpider.waitTime)
            for next_page in response.css('a.next-link'):
                yield response.follow(next_page, self.parse)  

    def parse_info(self, response):
        yield {
            'title': response.css(".biz-page-title::text").extract_first(),
            'link': response.url,
            'address':  response.css('.street-address address::text').extract(),
            'phone':  response.css('.biz-phone::text').extract_first().strip(),
            'website':  response.css('.biz-website a::text').extract_first().strip()
        }



        