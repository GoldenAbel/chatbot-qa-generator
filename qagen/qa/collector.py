from qagen.qa.generators import BaseEntityQaGenerator
from qagen.data_provider.knowledge_data_providers import KnowledgeDataProvider


class KnowledgeDataQaPairCollector(object):

    def __init__(self):
        self.qa_generator_map = {}
        self.qa_pairs = []

    def register_generator(self, entity_class, generator):
        if not isinstance(generator, BaseEntityQaGenerator):
            raise Exception('The generator instance is not a subclass of BaseEntityQaGenerator')

        self.qa_generator_map[entity_class] = generator

    def collect_from(self, data_provider):
        if not isinstance(data_provider, KnowledgeDataProvider):
            raise Exception('The provider instance is not a subclass of KnowledgeDataProvider')

        for entity_class in data_provider.get_all_entity_types():
            if entity_class not in self.qa_generator_map:
                raise Exception('No QA generator is registered for entity type ' + entity_class.__name__)
            qa_generator = self.qa_generator_map[entity_class]

            # class-level questions
            self.qa_pairs.extend(qa_generator.generate_qa_pairs_for_entity_class(entity_class))

            # instance-level questions
            for entity_instance in data_provider.get_all_instances_of_type(entity_class):
                self.qa_pairs.extend(qa_generator.generate_qa_pairs_for_entity_instance(entity_instance))
