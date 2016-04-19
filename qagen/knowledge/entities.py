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


# Entity types and definitions

class Company(BaseEntity):

    entity_concept_type = ConceptType.THING
    property_def_map = {
        'name': EntityProperty('name', ConceptType.THING),
        'founder': EntityProperty('founder', ConceptType.PERSON),
        'location': EntityProperty('location', ConceptType.THING),
        'website': EntityProperty('website', ConceptType.URL),
        'type_of_business': EntityProperty('type of business', ConceptType.THING),
        'stage': EntityProperty('stage', ConceptType.THING),
        # company_id is only for answer generation, hence hidden
        'company_id': EntityProperty('company_idd', ConceptType.THING, is_hidden=True)
    }
    relation_def_map = {
        'jobs': EntityRelation('jobs', Job, EntityRelation.ONE_TO_MANY)
    }


class Job(BaseEntity):

    entity_concept_type = ConceptType.THING
    property_def_map = {
        'function': EntityProperty('function', ConceptType.THING),
        'location': EntityProperty('location', ConceptType.THING),
        # name is only for context replacement, hence hidden
        'name': EntityProperty('name', ConceptType.THING, is_hidden=True),
        # function_id and location_id are only for answer generation, hence hidden
        'function_id': EntityProperty('function_idn', ConceptType.THING, is_hidden=True),
        'location_id': EntityProperty('location_id', ConceptType.THING, is_hidden=True)
    }
    relation_def_map = {
        'company': EntityRelation('company', Company, EntityRelation.ONE_TO_ONE)
    }


class Investor(BaseEntity):

    entity_concept_type = ConceptType.PERSON
    property_def_map = {
        'name': EntityProperty('name', ConceptType.THING),
        'role': EntityProperty('role', ConceptType.THING),
        'profile': EntityProperty('profile', ConceptType.URL),
        'linkedin': EntityProperty('linkedin', ConceptType.URL),
    }
    relation_def_map = {}


class A16Z(Company):

    entity_concept_type = Company.entity_concept_type
    property_def_map = Company.property_def_map
    relation_def_map = Company.relation_def_map

    # additional properties and relations
    property_def_map['contact_info'] = EntityProperty('contact info', ConceptType.URL)
    relation_def_map['portfolio'] = EntityRelation('portfolio', Company, EntityRelation.ONE_TO_MANY)
    relation_def_map['team'] = EntityRelation('team', Investor, EntityRelation.ONE_TO_MANY)


# Common structure of an entity definition

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
