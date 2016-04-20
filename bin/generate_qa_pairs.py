from qagen.data_provider.knowledge_data_providers import WebCrawlerKnowledgeDataProvider
from qagen.qa.collector import KnowledgeDataQaPairCollector
from qagen.qa.generators import *
from qagen.knowledge.entities import *

data_provider = WebCrawlerKnowledgeDataProvider()

qa_collector = KnowledgeDataQaPairCollector()
qa_collector.register_generator(A16Z, A16zQaGenerator(data_provider))
qa_collector.register_generator(Company, CompanyQaGenerator(data_provider))
qa_collector.register_generator(Investor, InvestorQaGenerator(data_provider))
qa_collector.register_generator(Job, JobQaGenerator(data_provider))

qa_collector.collect_from(data_provider)

print '%d QA pairs collected:' % len(qa_collector.qa_pairs)
for qa_pair in qa_collector.qa_pairs:
    print qa_pair

