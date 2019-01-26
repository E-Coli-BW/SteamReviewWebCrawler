# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:59:17 2018

@author: Haosong
"""

class ProductSpider(CrawlSpider):

    name = 'products'

    start_urls = ["http://store.steampowered.com/search/?sort_by=Released_DESC"]

    allowed_domains=["steampowered.com"]

    rules = [

        Rule(

            LinkExtractor(

                allow='/app/(.+)/',

                restrict_css='#search_result_container'),

            callback='parse_product'),

        Rule(

            LinkExtractor(

                allow='page=(\d+)',

                restrict_css='.search_pagination_right'))

    ]

    def parse_product(self, response):
    
        return {
    
            'app_name': response.css('.apphub_AppName ::text').extract_first(),
    
            'specs': response.css('.game_area_details_specs a ::text').extract()
    
        }