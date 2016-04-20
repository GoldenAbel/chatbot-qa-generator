

class ConceptType(object):

    THING = 1,
    PERSON = 2,
    URL = 3,

    __wh_type_map = {
        THING: 'what',
        PERSON: 'who',
        URL: 'where'
    }

    @classmethod
    def get_wh_type(cls, concept_type):
        return cls.__wh_type_map[concept_type]


class EntityProperty(object):

    def __init__(self, property_name, concept_type, is_hidden=False):
        self.property_name = property_name
        self.concept_type = concept_type
        self.is_hidden = is_hidden


class EntityRelation(object):

    ONE_TO_ONE = 1
    ONE_TO_MANY = 2

    def __init__(self, relation_name, related_entity_class, relation_type):
        self.relation_name = relation_name
        self.related_entity_class = related_entity_class
        self.relation_type = relation_type


class BaseEntity(object):

    entity_concept_type = ConceptType.THING
    property_def_map = {}
    relation_def_map = {}

    def __init__(self, **kwargs):
        # check the required metadata
        if not hasattr(self, 'entity_concept_type'):
            raise Exception("entity_concept_type is not specified")
        if not hasattr(self, 'property_def_map'):
            raise Exception("property_def_map is not specified")
        if not hasattr(self, 'relation_def_map'):
            raise Exception("relation_def_map is not specified")

        for key in kwargs:
            if key not in self.__class__.property_def_map:
                raise Exception(key + ' is not found in the property definition map in ' + type(self))

        # copy over all the input variables as property value
        self.property_value_map = dict(kwargs)
        self.relation_value_map = {}

    def __repr__(self):
        entity_type = self.__class__.__name__
        entity_name = self.property_value_map['name']
        return '%s[%s]' % (entity_type, entity_name)

    def get_entity_id(self):
        # by default use the name property as identifier among all entity instances
        # subclass can use different property as id by overriding this method
        return self.property_value_map['name']


# Entity types and definitions

class Company(BaseEntity):
    pass


class Job(BaseEntity):
    pass


class Investor(BaseEntity):
    pass


class A16Z(Company):
    pass


Company.entity_concept_type = ConceptType.THING
Company.property_def_map = {
    'name': EntityProperty('name', ConceptType.THING),
    'founder': EntityProperty('founder', ConceptType.PERSON),
    'location': EntityProperty('location', ConceptType.THING),
    'website': EntityProperty('website', ConceptType.URL),
    'type_of_business': EntityProperty('type of business', ConceptType.THING),
    'business_model': EntityProperty('business model', ConceptType.THING),
    'stage': EntityProperty('stage', ConceptType.THING),
    # company_id is only for answer generation, hence hidden
    'company_id': EntityProperty('company_idd', ConceptType.THING, is_hidden=True)
}
Company.relation_def_map = {
    'jobs': EntityRelation('jobs', Job, EntityRelation.ONE_TO_MANY)
}


Job.entity_concept_type = ConceptType.THING
Job.property_def_map = {
    'function': EntityProperty('function', ConceptType.THING),
    'location': EntityProperty('location', ConceptType.THING),
    # name is only for context replacement, hence hidden
    'name': EntityProperty('name', ConceptType.THING, is_hidden=True),
    # function_id and location_id are only for answer generation, hence hidden
    'function_id': EntityProperty('function_idn', ConceptType.THING, is_hidden=True),
    'location_id': EntityProperty('location_id', ConceptType.THING, is_hidden=True)
}
Job.relation_def_map = {
    'company': EntityRelation('company', Company, EntityRelation.ONE_TO_ONE)
}


Investor.entity_concept_type = ConceptType.PERSON
Investor.property_def_map = {
    'name': EntityProperty('name', ConceptType.THING),
    'role': EntityProperty('role', ConceptType.THING),
    'picture': EntityProperty('picture', ConceptType.THING),
    'profile': EntityProperty('profile', ConceptType.URL),
    'linkedin': EntityProperty('linkedin', ConceptType.URL),
}
Investor.relation_def_map = {}


A16Z.entity_concept_type = Company.entity_concept_type
A16Z.property_def_map = dict(Company.property_def_map)
A16Z.relation_def_map = dict(Company.relation_def_map)
# additional properties and relations
A16Z.property_def_map['contact_info'] = EntityProperty('contact info', ConceptType.URL)
A16Z.relation_def_map['portfolio'] = EntityRelation('portfolio', Company, EntityRelation.ONE_TO_MANY)
A16Z.relation_def_map['team'] = EntityRelation('team', Investor, EntityRelation.ONE_TO_MANY)

def find_entity_class_by_name(entity_class_name):
    for known_entity_type in [Company, Job, Investor, A16Z]:
        if known_entity_type.__name__ == entity_class_name:
            return known_entity_type
    return None
