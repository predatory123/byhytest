def crawl_commentInfo(self, response):
    total_product_info = response.css('.gl-item')
    for product_info in total_product_info:
        product_url = 'https:' + product_info.css('.gl-i-wrap .p-img a::attr(href)').extract_first()
        # comment_info crawl firstly
        headers = self.headers.copy()
        headers.update({
            'Referer': 'https://item.jd.com/12330816.html',
            'Host': 'sclub.jd.com',
        })
        match_obj = re.match('.*/(\d+).html', product_url)
        if match_obj:
            product_id = match_obj.group(1)
            yield scrapy.Request(self.start_urls[1].format(product_id), headers=headers,
                                 meta={'product_url': product_url}, callback=self.parse_product)
            print('Now crawl commentInfo url is', self.start_urls[1].format(product_id))
        # break

    match_obj = re.match('.*page=(\d+)$', response.url)
    if match_obj:
        page_num = int(match_obj.group(1)) + 2
    else:
        page_num = 3

    if '下一页' in response.text:
        yield SplashRequest(self.start_urls[0].format(page_num, 'python'), endpoint='execute',
                            callback=self.crawl_commentInfo, splash_headers=self.headers,
                            args={'lua_source': self.lua_script, 'image': 0, 'wait': 1}, cache_args=['lua_source'])
        print('Now page_url is :', self.start_urls[0].format(page_num, 'python'))

    def parse_product(self, response):
        product_url = response.meta.get('product_url')
        praise = 0
        praise_match = re.match('.*"goodRateShow":(\d+),.*', response.text)
        if praise_match:
            praise = praise_match.group(1)
        headers = self.headers.copy()
        headers.update({
            'Upgrade-Insecure-Requests': 1,
            'Host': 'item.jd.com',

        })
        yield SplashRequest(product_url, endpoint='render.html', splash_headers=headers,
                            args={'image': 0, 'timeout': 15, 'wait': 1}, meta={'praise': praise}
                            )
        print('Now request url is:', product_url)


