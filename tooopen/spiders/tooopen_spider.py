#coding:utf-8	
import scrapy
from tooopen.items import TooopenItem
site="http://www.tooopen.com"

class tooopenspider(scrapy.Spider):
	name = "tooopenspider"
	start_urls = ["http://www.tooopen.com/img/"]

	def parse(self, response):
		global site
		imageclassurls=response.xpath('//div[contains(@class,"cell type-list")]/ul/li/a[(contains(@href,"img/97"))]/@href').extract()
		for imageclassurl in imageclassurls:
			print "imageclassurls=",imageclassurl
			yield scrapy.Request(site+imageclassurl.encode("utf-8"),callback=self.parse_dir_contents)
		#yield scrapy.Request(site+imageclassurls[0].encode("utf-8"),callback=self.parse_dir_contents)

	def	parse_dir_contents(self, response):
		imageurls=response.xpath('//a[@target="_blank" and contains(@href,"http://www.tooopen.com/v")]/@href').extract()
		for imageurl in imageurls:
			print "imageurl=",imageurl
			yield scrapy.Request(imageurl.encode("utf-8"),callback=self.parse_image)		
		nextpage=response.xpath('//span[contains(@class,"page-nav")]/a/@href').extract()
		print "nextpage[-1]=",type(nextpage[-1])
		yield scrapy.Request(site+nextpage[-1].encode("utf-8"),callback=self.parse_dir_contents)
	
	def	parse_image(self,response):
		image=response.xpath('//div[contains(@class,"pic-box")]/img[contains(@id,"imgView")]/@src').extract()
		print "image=",image
		item = TooopenItem()
		item['image_urls']=image
		yield item
		
#response.xpath('//a[@target="_blank" and contains(@href,"http://www.tooopen.com/v")]/@href').extract() //页面图片

#response.xpath('//div[contains(@class,"cell type-list")]/ul/li/a[contains(@href,"img/88")]/@href').extract()
#response.xpath('//div[contains(@class,"cell type-list")]/ul/li/a[not(contains(@href,"img/88"))]/@href').extract())／／页面地址
#response.xpath('//span[contains(@class,"page-nav")]/a/@href')[-1].extract()／／下一页
