"""Script to crawl Top Posts across sub reddits and store results in MongoDB
"""

import logging
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from charlie_rose.spiders import EpisodeSpider


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    crawler = CrawlerProcess(get_project_settings())

    crawler.crawl(EpisodeSpider)
    crawler.start() # the script will block here until the crawling is finished

    # # only run on saturdays (once a week)
    # if date.strftime(date.today(), '%A').lower() == 'saturday':
    #     crawler = CrawlerProcess(get_project_settings())

    #     crawler.crawl(PostSpider)
    #     crawler.start() # the script will block here until the crawling is finished

    #     email_last_scraped_date()
    #     logger.info('Scrape complete and email sent.')
    # else:
    #     logger.info('Script did not run.')
