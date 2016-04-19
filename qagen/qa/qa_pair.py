class QAPair(object):

    def __init__(self, question, answer, context_map):
        self.question = question
        self.answer = answer
        self.context_map = context_map

    def __repr__(self):
        return 'Q: %s, A: %s' % (self.question, self.answer)


