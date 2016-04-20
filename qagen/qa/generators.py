import itertools

from qagen.knowledge.entities import ConceptType, EntityRelation
from qagen.qa.utils import make_context_map
from qagen.qa.qa_pair import QAPair


class BaseEntityQaGenerator(object):
    """This generator generates common QA pairs that are shared by all entities"""

    def __init__(self, data_provider):
        self.data_provider = data_provider

    def generate_qa_pairs_for_entity_class(self, entity_class):
        """class level queries about this entity type, e.g. how many companies do we know in total"""
        return []

    def generate_qa_pairs_for_entity_instance(self, entity_instance):
        """query about a specific instance of an entity"""
        return list(itertools.chain(
            self.generate_qa_pairs_about_self(entity_instance),
            self.generate_qa_pairs_about_properties(entity_instance),
            self.generate_qa_pairs_about_relations(entity_instance)
        ))

    # default implementation of QA generation. subclass can extend these method to generate additional QA pairs

    def generate_qa_pairs_about_self(self, entity_instance):
        wh_type = ConceptType.get_wh_type(entity_instance.__class__.entity_concept_type)
        entity_name = entity_instance.property_value_map['name']

        return [
            QAPair(question_text, entity_instance.get_entity_self_description(), make_context_map(entity_instance))
            for question_text in [
                '%s is %s' % (wh_type, entity_name),
                'information about %s' % entity_name,
                'tell me about %s' % entity_name,
                'show me %s' % entity_name,
                'I want to know about %s' % entity_name
            ]
        ]

    def generate_qa_pairs_about_properties(self, entity_instance):
        return [qa_pair
                for property_name, property_def in entity_instance.__class__.property_def_map.iteritems()
                for qa_pair in self.generate_qa_pairs_about_one_property(entity_instance, property_def)]

    def generate_qa_pairs_about_one_property(self, entity_instance, property_def):

        # Don't ask questions about a hidden property
        if property_def.is_hidden:
            return []

        property_wh_type = ConceptType.get_wh_type(property_def.concept_type)
        property_name = property_def.property_name
        entity_name = entity_instance.property_value_map['name']

        property_value = entity_instance.property_value_map.get(property_name)
        if property_value:
            if property_def.concept_type == ConceptType.URL:
                answer = 'You can find the %s of %s at %s' %(property_name, entity_name, property_value)
            else:
                answer = 'The %s of %s is %s.' %(property_name, entity_name, property_value)
        else:
            answer = 'Sorry the %s of %s is not found on the a16z.com website.' % (property_name, entity_name)

        return [
            QAPair(question_text, answer, make_context_map(entity_instance))
            for question_text in [
                '%s is the %s of %s' % (property_wh_type, property_name, entity_name),
                'show me the %s of %s' % (property_name, entity_name)
            ]
        ]

    def generate_qa_pairs_about_relations(self, entity_instance):
        return [qa_pair
                for relation_name, relation_def in entity_instance.__class__.relation_def_map.iteritems()
                for qa_pair in self.generate_qa_pairs_about_one_relation(entity_instance, relation_def)]

    def generate_qa_pairs_about_one_relation(self, entity_instance, relation_def):

        relation_wh_type = ConceptType.get_wh_type(relation_def.related_entity_class.entity_concept_type)
        relation_name = relation_def.relation_name
        entity_name = entity_instance.property_value_map['name']

        related_entity_value = entity_instance.relation_value_map.get(relation_name)

        if relation_def.relation_type == EntityRelation.ONE_TO_ONE:
            question_texts = [
                '%s is the %s of %s' % (relation_wh_type, relation_name, entity_name),
                'show me the %s of %s' % (relation_name, entity_name)
            ]
            #TODO
            answer = 'n/a'
        else:
            question_texts = [
                '%s are the %s of %s' % (relation_wh_type, relation_name, entity_name),
                'list all %s of %s' % (relation_name, entity_name),
                'show me all %s of %s' % (relation_name, entity_name),
                'how many %s of %s' % (relation_name, entity_name),
                'the number of %s of %s' % (relation_name, entity_name),
            ]
            if related_entity_value:
                example = ', '.join([single_intance.get_entity_id() for single_intance in related_entity_value][0:3])
                answer = 'There are %d %s in total, including %s...' % (len(related_entity_value), relation_name, example)
            else:
                answer = "Sorry, there doesn't seem to be any."

        return [
            QAPair(question_text, answer, make_context_map(entity_instance))
            for question_text in question_texts
        ]


# Type-specific generators

class CompanyQaGenerator(BaseEntityQaGenerator):

    def generate_qa_pairs_for_entity_class(self, entity_class):
        #TODO
        return []

    def generate_qa_pairs_about_self(self, entity_instance):
        qa_pairs = super(CompanyQaGenerator, self).generate_qa_pairs_about_self(entity_instance)
        entity_name = entity_instance.property_value_map['name']

        # additional questions about self
        qa_pairs.extend([
            QAPair('what does %s do' % entity_name, entity_instance.get_entity_self_description(), make_context_map(entity_instance)),
        ])

        return qa_pairs

    def generate_qa_pairs_about_one_property(self, entity_instance, property_def):
        qa_pairs = super(CompanyQaGenerator, self).generate_qa_pairs_about_one_property(entity_instance, property_def)
        entity_name = entity_instance.property_value_map['name']

        if property_def.property_name == 'name':
            qa_pairs.extend([
                QAPair('what is %s called' % entity_name, entity_instance.property_value_map['name'], make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'founder':
            founder = entity_instance.property_value_map.get('founder')
            if founder:
                answer = '%s is founded by %s.' % (entity_name, founder)
            else:
                answer = 'Sorry the founder information of %s is not listed on the a16z website. ' \
                         'Please checkout their website at %s' \
                         % (entity_name, entity_instance.property_value_map['website'])
            for qa_pair in qa_pairs:
                qa_pair.answer = answer
            qa_pairs.extend([
                QAPair('who founded %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('who created %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('who started %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what is the founding team of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('who are the founders of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('list all the founders of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('show me the founders of %s' % entity_name, answer, make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'location':
            location = entity_instance.property_value_map.get('location')
            if location:
                answer = '%s is located in %s.' % (entity_name, location)
                for qa_pair in qa_pairs:
                    qa_pair.answer = answer
            else:
                # keep existing answer
                answer = qa_pairs[0].answer
            qa_pairs.extend([
                QAPair('where is %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('where is %s located' % entity_name, answer, make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'website':
            answer = qa_pairs[0].answer
            qa_pairs.extend([
                QAPair('take me to the website of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('more information about %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('do you have a link to the website of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('show me the link to the website of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('I want to checkout more about %s' % entity_name, answer, make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'type of business':
            type_of_business = entity_instance.property_value_map.get('type of business')
            if type_of_business:
                answer = type_of_business.lower().capitalize()
                for qa_pair in qa_pairs:
                    qa_pair.answer = answer
            else:
                # keep existing answer
                answer = qa_pairs[0].answer
            qa_pairs.extend([
                QAPair('what kind of business does %s do' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what is the industry of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('in what industry does %s work on' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('in what area does %s work on' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what kind of problem does %s solve' % entity_name, answer, make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'business model':
            business_model = entity_instance.property_value_map.get('business model')
            if business_model == 'to consumer':
                answer = '%s is a b2c (business-to-consumer) company.' % entity_name
            elif business_model == 'to enterprise':
                answer = '%s is a b2b (business-to-business) company.' % entity_name
            else:
                # keep existing answer
                answer = qa_pairs[0].answer
            for qa_pair in qa_pairs:
                qa_pair.answer = answer
            qa_pairs.extend([
                QAPair('is %s a 2b or 2c company' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('is %s a to-business or to-consumer company' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what is target market of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('who are the customers of %s' % entity_name, answer, make_context_map(entity_instance)),
            ])
            # additional yes/no questions
            if business_model == 'to consumer':
                qa_pairs.extend([
                    QAPair('is %s a 2b company' % entity_name, 'yes', make_context_map(entity_instance)),
                    QAPair('is %s a 2c company' % entity_name, 'no', make_context_map(entity_instance)),
                ])
            elif business_model == 'to enterprise':
                qa_pairs.extend([
                    QAPair('is %s a 2b company' % entity_name, 'yes', make_context_map(entity_instance)),
                    QAPair('is %s a 2c company' % entity_name, 'no', make_context_map(entity_instance)),
                ])

        elif property_def.property_name == 'stage':
            stage = entity_instance.property_value_map.get('stage')
            if stage:
                answer = 'As far as I know, %s has received %s funding from A16Z.' % (entity_name, stage.lower())
            else:
                # keep existing answer
                answer = qa_pairs[0].answer
            for qa_pair in qa_pairs:
                qa_pair.answer = answer
            qa_pairs.extend([
                QAPair('current stage of %s' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('is %s funded' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('is %s seeded' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('how is %s doing' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('has %s raised any capital' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('has %s raised any money' % entity_name, answer, make_context_map(entity_instance)),
            ])

        return qa_pairs


class JobQaGenerator(BaseEntityQaGenerator):

    def generate_qa_pairs_for_entity_class(self, entity_class):
        #TODO
        return []

    def generate_qa_pairs_about_one_property(self, entity_instance, property_def):
        qa_pairs = super(JobQaGenerator, self).generate_qa_pairs_about_one_property(entity_instance, property_def)
        entity_name = entity_instance.property_value_map['name']

        if property_def.property_name == 'name':
            qa_pairs.extend([
                QAPair('what is the position for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
                QAPair('what do I work on for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
                QAPair('what expertise do I need for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
                QAPair('what is the requirement for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
            ])

        elif property_def.property_name == 'location':
            qa_pairs.extend([
                QAPair('where is the office for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
                QAPair('where do I need to work for %s' % entity_name, 'n/a', make_context_map(entity_instance)),
            ])

        return qa_pairs

    def generate_qa_pairs_about_one_relation(self, entity_instance, relation_def):
        qa_pairs = super(JobQaGenerator, self).generate_qa_pairs_about_one_relation(entity_instance, relation_def)
        entity_name = self.property_value_map['name']

        if relation_def.relation_name == 'company':
            qa_pairs.extend([
                QAPair('who is the employer of %s' % entity_name, 'n/a', make_context_map(entity_instance)),
                QAPair('which company is %s for' % entity_name, 'n/a', make_context_map(entity_instance)),
            ])

        return qa_pairs


class InvestorQaGenerator(BaseEntityQaGenerator):

    def generate_qa_pairs_for_entity_class(self, entity_class):
        #TODO
        return []

    def generate_qa_pairs_about_one_property(self, entity_instance, property_def):
        qa_pairs = super(InvestorQaGenerator, self).generate_qa_pairs_about_one_property(entity_instance, property_def)
        entity_name = entity_instance.property_value_map['name']

        if property_def.property_name == 'role':
            answer = entity_instance.get_role_description()
            for qa_pair in qa_pairs:
                qa_pair.answer = answer
            qa_pairs.extend([
                QAPair('what does %s do' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what does %s work on' % entity_name, answer, make_context_map(entity_instance)),
                QAPair('what is the responsibility of %s' % entity_name, answer, make_context_map(entity_instance)),
            ])

        return qa_pairs


class A16zQaGenerator(CompanyQaGenerator):

    def generate_qa_pairs_about_one_property(self, entity_instance, property_def):
        qa_pairs = super(A16zQaGenerator, self).generate_qa_pairs_about_one_property(entity_instance, property_def)
        entity_name = entity_instance.property_value_map['name']

        #TODO
        return qa_pairs

    def generate_qa_pairs_about_one_relation(self, entity_instance, relation_def):
        qa_pairs = super(A16zQaGenerator, self).generate_qa_pairs_about_one_relation(entity_instance, relation_def)
        entity_name = entity_instance.property_value_map['name']

        #TODO
        return qa_pairs
