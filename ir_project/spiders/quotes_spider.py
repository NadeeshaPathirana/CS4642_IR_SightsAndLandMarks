import scrapy


class SightsSpider(scrapy.Spider):
    name = "sights"
    sights_array=[]
    count = 0
    start_urls = [
        # Sri Lanka Historic Sites
        # Historic Sites
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t17-Sri_Lanka.html',
        # Sacred and Religious sites
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t10-Sri_Lanka.html',
        # Points of interests and Landmarks
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t163-Sri_Lanka.html',
        # Churches & Cathedrals in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t175-Sri_Lanka.html',
        # Sri Lanka Ancient Ruins
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t2-Sri_Lanka.html',
        # Monuments & Statues in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t26-Sri_Lanka.html',
        # Architectural Buildings in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t3-Sri_Lanka.html',
        # Lighthouses
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t22-Sri_Lanka.html',
        # Bridges in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t5-Sri_Lanka.html',
        # Scenic Walking Areas in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t76-Sri_Lanka.html',
        # Castles in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t6-Sri_Lanka.html',
        # Farms in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t122-Sri_Lanka.html',
        # Arenas & Stadiums in Sri Lanka
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c47-t120-Sri_Lanka.html',
    ]



    def parse_details(self, response):
        yield {
            'title': response.css('h1.heading_title::text').extract(),
            'overeview': response.css('div.text::text').extract(),
            'location_town': response.css('span.locality::text').extract_first(),
            'location_country': response.css('span.country-name::text').extract_first(),
            'duration': response.css('div.detail_section.duration::text').extract(),
            'details': response.css('div.detail a::text').extract(),
            'Nearby': response.css('div.poiName::text').extract(),
            'Distance': response.css('div.distance::text').extract(),
            'Review_category': response.css('span.row_label.row_cell::text').extract(),
            'Review_percentage': response.css('span.row_count.row_cell::text').extract(),
            'Tag_words': response.css('div.tagWord::text').extract(),

        }

    def parse(self, response):

        sights = response.xpath('//div[contains(@class,"listing_title")]/a/@href').extract()

        for sight in sights:

            yield response.follow(sight, self.parse_details)