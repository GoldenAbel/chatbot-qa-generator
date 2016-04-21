import json
import random
from qagen.data_provider.knowledge_data_providers import *
from qagen.data_provider.qa_concept_providers import *
from qagen.qa.generators import DefaultQAPairGenerator
from qagen.knowledge.entities import *

# data_provider = WebCrawlerKnowledgeDataProvider()
data_provider = JsonFileKnowledgeDataProvider('data.json')
concept_provider = DefaultQAConceptProvider(data_provider)

qa_generator = DefaultQAPairGenerator(data_provider)

qa_pairs = []
for qa_concept in concept_provider.get_all_qa_concepts():
    qa_pairs.extend(qa_generator.generate_qa_pairs_about_concept(qa_concept))

print '%d QA pairs collected.' % len(qa_pairs)


is_for_training = False
TRAINING_DATA_SAMPLE = 200
RANKED_ANSWER_COUNT = 5

if is_for_training:
    output_path = 'qa_pairs_labeled.json'
    # select random samples
    output_qa_pairs = random.sample(qa_pairs, TRAINING_DATA_SAMPLE)

    print 'Adding additional random answers for rank labeling...'
    for qa_pair in output_qa_pairs:
        random_qa_sampling = random.sample(qa_pairs, RANKED_ANSWER_COUNT)
        for random_qa in random_qa_sampling:
            qa_pair.add_qa_pair_with_matching_score(random_qa.question, random_qa.answer, 0)

else:
    output_path = 'qa_pairs_unlabeled.json'
    output_qa_pairs = qa_pairs

print 'Dumping QA pairs to JSON file...'
qa_pairs_json_data = [qa_pair.to_json_dict(is_for_training=is_for_training) for qa_pair in output_qa_pairs]
qa_json_str = json.dumps(qa_pairs_json_data, indent=2, sort_keys=True)
with open(output_path, 'w') as output_file:
    output_file.write(qa_json_str)
print 'All QA pairs dumped at ' + output_path

