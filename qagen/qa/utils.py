from qagen.knowledge.entities import BaseEntity


def make_context_map(*args):
    for arg in args:
        if arg is not BaseEntity:
            raise Exception('Arguements must be instances of entity')

    return {entity_instance._class__.__name__: entity_instance.property_value_map['name']
            for entity_instance in args}


