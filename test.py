# importing the scrapy module
from os import link
import scrapy

class ExtractUrls(scrapy.Spider):
	name = "extract"

	# request function
	def start_requests(self):
		urls = [ 'https://www.midsouthshooterssupply.com/dept/reloading/primers', ]
		
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	# Parse function
	def parse(self, response):
		
		# Extra feature to get title
		product = response.css('product::text').extract_first()
		
		# Get anchor tags
		links = response.css('product::attr(href)').extract()
    
        for product in response.css("div.product"):
            price = product.css("div.catalog-item-price::price").get()
            title = product.css("div.catalog-item-brand::title").get()
            status = product.css("div.out-of-stock::status").getall()
            brand = product.css("div.manufacturer::brand").getall()
            result = product.css("div.review-product::result").getall()
            description = product.css("div.catlog.item-name::description").getall()
            delievery = product.div(delivery_info.script).getall()
                
            print(dict(price=price, title=title, status=status, brand=brand, result=result, description=description, delivery=delivery))
		}
			
		if 'midsouthshooterssupply' in product:

		    yield scrapy.Request(url = link, callback = self.parse)
                
                
                