from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class first(BaseSpider):
    name = "mywebsite"
    allowed_domains = "bewithaman.wordpress.com"
    start_urls = ["https://bewithaman.wordpress.com"]
    def parse (self, response):
        '''filename = 'aman'
        open(filename, 'wb').write(response.body)'''
        hxs = HtmlXPathSelector(response)
        list = hxs.select("//html/body[@class='home blog custom-background mp6 highlander-enabled highlander-light infinite-scroll neverending']/div[@id='page']/div[@id='content']/div[@id='primary']/main[@id='main']/article[@id='post-5']/div[@class='entry-content']/p")
	p=[]
        for iter in list:
            myres = iter.select('text()').extract()
	    p.append(myres)
            print myres
            filename = 'amannnn'
            open(filename, 'a').write(str(myres))
	open('list', 'a').write(str(myres))
	
            
