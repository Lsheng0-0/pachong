import scrapy

from blood.items import BloodItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxxxx.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        # 解析片名+上映时间+演员+评分+链接
        div_list = response.xpath('//*[@id="content"]/div/div[1]/div/div/table')
        # print(div_list)
        for div in div_list:
            # xpath 返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中的data参数储存的字符串提取出来,调列表data
            name = div.xpath('//*[@class="pl2"]/a/text()')[0].extract()
            name = name.split()[0]
            scr = div.xpath('//*[@class="pl2"]/a/@href')[0].extract()
            # print(scr, name)
            item = BloodItem()
            item['name'] = name
            yield scrapy.Request(url=scr, callback=self.parse_two, meta={'name': item['name']})

    def parse_two(self, response):

        item = BloodItem()
        for i in item:
            item['name'] = response.meta['name']
            item['type'] = i.xpath('//*[@id="info"]/span[4]/text()')[0].extract()
            item['publish_time'] = i.xpath('//*[@id="info"]/span[11]/text()')[0].extract()
            # 主演
            item['Starring'] = i.xpath('//*[@id="info"]/span[3]/span[2]/span[1]/a/text()')[0].extract()
            # 评分
            item['Score'] = i.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0].extract()
            yield item

