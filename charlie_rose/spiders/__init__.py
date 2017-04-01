# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from datetime import datetime
import scrapy
from charlie_rose.items import CharlieRoseItem

class EpisodeSpider(scrapy.Spider):
    name = 'cr_episodes'

    start_urls = [
        'https://charlierose.com/episodes'
    ]

    def parse(self, response):

        # get the reference to the main location where the data is stored
        target = response.css('#ajax_target')

        # episodes are grouped by month (i.e. November 2016, March 2017)
        months = target.css('h2::text').extract()
        episode_listing = target.css('.listing-episodes')

        # for each month
        for month_year, episodes in zip(months, episode_listing):

            # go thru each episode
            for episode in episodes.css('li'):

                # parse details and pull out the guest list
                day = int(episode.css('i::text').extract_first().split(' ')[1])
                guests = episode.css('b::text').extract_first().split(';')
                date_str = '{0} {1}'.format(month_year, day)

                # create item to store
                item = CharlieRoseItem()
                print(datetime.strptime(date_str, '%B %Y %d'))
                item['date'] = datetime.strptime(date_str, '%B %Y %d')
                item['url'] = response.urljoin(episode.css('a::attr(href)').extract_first())
                item['seen'] = False

                # parse guest list; for each item, yield item for each distinct guest
                for guest in guests:
                    item['guest'] = guest.strip()
                    yield item

        # follow pagination links
        # we only need to do this the first time
        next_pg = response.css('.pagination .next::attr(href)').extract_first()
        if next_pg is not None:
            next_pg = response.urljoin(next_pg)
            yield scrapy.Request(next_pg, callback=self.parse)
