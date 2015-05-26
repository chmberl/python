# -*- coding: utf-8 -*-

# Scrapy settings for doubanmovie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'doubanmovie'

SPIDER_MODULES = ['doubanmovie.spiders']
NEWSPIDER_MODULE = 'doubanmovie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmovie (+http://www.yourdomain.com)'
ITEM_PIPELINES={
    'doubanmovie.pipelines.DoubanmoviePipeline':500,
}
LOG_LEVEL='INFO'
CONCURRENT_REQUESTS = 100
AJAXCRAWL_ENABLED = True
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
                'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
                        'doubanmovie.rotate_useragent.RotateUserAgentMiddleware' :400
                          }


