import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA']


    def parse(self, response):
        for business_page in response.css('h3>a'):
            yield {
                'title': response.css('h3 a::text').get().strip()
                # 'link':  response.css('h3 a::href').get().strip()
            }
            # yield response.follow(business_page,  callback=self.parse_info)
            
            
        
    def parse_info(self, response):
        yield {
            'address':  response.css('.street-address address::text').get(),
            'phone':  response.css('.biz-phone::text').get().strip(),
            'website':  response.css('.biz-website a::text').get().strip()
        }





        # for next_page in response.css('a.pages_arrow'):
        #     yield response.follow(next_page, self.parse)

        # scrapy runspider myspider.py -o test.csv

        