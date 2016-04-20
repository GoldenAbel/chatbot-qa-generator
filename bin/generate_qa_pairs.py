import json
from qagen.data_provider.knowledge_data_providers import *
from qagen.qa.collector import KnowledgeDataQaPairCollector
from qagen.qa.generators import *
from qagen.knowledge.entities import *

# data_provider = WebCrawlerKnowledgeDataProvider()
data_provider = JsonFileKnowledgeDataProvider('data.json')

qa_collector = KnowledgeDataQaPairCollector()
qa_collector.register_generator(A16Z, A16zQaGenerator(data_provider))
qa_collector.register_generator(Company, CompanyQaGenerator(data_provider))
qa_collector.register_generator(Investor, InvestorQaGenerator(data_provider))
qa_collector.register_generator(Job, JobQaGenerator(data_provider))

qa_collector.collect_from(data_provider)
print '%d QA pairs collected.' % len(qa_collector.qa_pairs)

is_for_training = True

if is_for_training:
    print 'Adding additional random answers for rank labeling...'
    output_path = 'qa_pairs_labeled.json'
else:
    output_path = 'qa_pairs_unlabeled.json'

qa_pairs_json_data = [qa_pair.to_json_dict(is_for_training=is_for_training) for qa_pair in qa_collector.qa_pairs]
qa_json_str = json.dumps(qa_pairs_json_data, indent=2, sort_keys=True)
with open(output_path, 'w') as output_file:
    output_file.write(qa_json_str)
print 'All QA pairs dumped at ' + output_path

