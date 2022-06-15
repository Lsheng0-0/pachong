# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BloodItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    type = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 主演
    Starring = scrapy.Field()
    # 评分
    Score = scrapy.Field()
