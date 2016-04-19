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

    def get_all_instaces_of(self, entity_class):
        return self.entity_map[entity_class]


class WebCrawlerKnowledgeDataProvider(object):

    def __init__(self):
        super(WebCrawlerKnowledgeDataProvider, self).__init__()

        print 'Initializing company:A16Z'
        self.add_entity(A16Z(
            name='Andreesen Horowitz',
            founder='Marc Andreesen and Ben Horowitz',
            location='Melo Park, California',
            website='a16z.com',
            type_of_business='venture capital',
            stage=None,
            contact_info='a16z.com/about/contact',
        ))