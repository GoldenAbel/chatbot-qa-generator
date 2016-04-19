from bs4 import BeautifulSoup
import urllib2

from qagen.knowledge.entities import *


class KnowledgeDataProvider(object):

    def __init__(self):
        self.entity_map = {
            A16Z: [],
            Company: [],
            Investor: [],
            Job: []
        }

    def add_entity(self, entity_instance):
        self.entity_map[entity_instance.__class__].append(entity_instance)

    def all_entity_types(self):
        return self.entity_map.keys()

    def get_all_instaces_of_type(self, entity_class):
        return self.entity_map[entity_class]


class WebCrawlerKnowledgeDataProvider(KnowledgeDataProvider):

    def __init__(self):
        super(WebCrawlerKnowledgeDataProvider, self).__init__()

        print 'Initializing company:A16Z...'
        self.add_entity(A16Z(
            name='Andreesen Horowitz',
            founder='Marc Andreesen and Ben Horowitz',
            location='Melo Park, California',
            website='a16z.com',
            type_of_business='venture capital',
            business_model=None,
            stage=None,
            contact_info='a16z.com/about/contact',
        ))

        print 'Crawling http://a16z.com/portfolio/...'
        for div in self.__find_company_data_divs_from_url('http://a16z.com/portfolio/'):
            self.add_entity(self.__parse_company_data(div))
        for div in self.__find_seed_company_data_divs_from_url('http://a16z.com/portfolio/'):
            self.add_entity(self.__parse_seed_company_data(div))

        print self.entity_map

    @staticmethod
    def __find_company_data_divs_from_url(url):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        return soup.findAll('div', 'company')

    @staticmethod
    def __parse_company_data(div):
        name = div.select_one('.meta > li:nth-of-type(1) > h2').next_sibling.strip()
        founder = div.select_one('.meta > li:nth-of-type(2) > h2').next_sibling.strip()
        location = div.select_one('.meta > li:nth-of-type(3) > h2').next_sibling.strip()
        website = div.select_one('.meta > li:nth-of-type(4) > a')['href'].strip()
        type_of_business = div.select_one('.meta > li:nth-of-type(5) > h2').next_sibling.strip()
        business_model = 'to consumer' if 'consumer' in div['class'] else 'to enterprise'
        stage = 'venture' if 'venture' in div['class'] else 'growth'

        return Company(
            name=name,
            founder=founder,
            location=location,
            website=website,
            type_of_business=type_of_business,
            business_model=business_model,
            stage=stage,
        )

    @staticmethod
    def __find_seed_company_data_divs_from_url(url):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        return soup.findAll('div', 'company-seed')

    @staticmethod
    def __parse_seed_company_data(div):
        website = div.select_one('.img-wrapper')['href'].strip()

        return Company(
            name=WebCrawlerKnowledgeDataProvider.__guess_company_name_by_website(website),
            founder=None,
            location=None,
            website=website,
            type_of_business=None,
            business_model=None,
            stage='seed',
        )

    @staticmethod
    def __guess_company_name_by_website(url):
        return url.split('.')[-2]
