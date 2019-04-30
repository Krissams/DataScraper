import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.businesslist.ph/location/manila']

    def parse(self, response):
        for business_page in response.css('h4>a'):
            yield response.follow(business_page,  callback=self.parse_info)
            
            
        
    def parse_info(self, response):
        yield {
            'title': response.css('#company_name::text').get(),
            'address':  response.css('.location::text').get()
        }



        # for next_page in response.css('a.pages_arrow'):
        #     yield response.follow(next_page, self.parse)

        # scrapy runspider myspider.py -o test.csv

        