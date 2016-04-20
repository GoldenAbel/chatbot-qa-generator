class QAPair(object):

    def __init__(self, question, answer, context_map):
        self.question = question
        self.answer = answer
        self.context_map = context_map
        self.ranked_answers = [{
            'question': question,
            'answer': answer,
            'score': 100
        }]

    def __repr__(self):
        return 'Q: %s, A: %s' % (self.question, self.answer)

    def add_other_qa_with_score(self, question, answer, score):
        self.ranked_answers.append({
            'question': question,
            'answer': answer,
            'score': score
        })

    def to_json_dict(self, is_for_training=False):
        result = {
            'question': self.question,
            'answer': self.answer,
            'context': self.context_map,
        }
        if is_for_training:
            result.update({
                'question_topic_words': [],
                'answer_topic_words': [],
                'ranked_answers': self.ranked_answers
            })
        return result

