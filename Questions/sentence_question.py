from random import choice, shuffle
from question import Question

class Sentence_Question(Question):
	s_parts_dict= {
	"s_subj_s":[""],
	"c_subj_s":[],
	"s_subj_p":[""],
	"c_subj_p":[],
	"ns":["John","Jill","Luke","Mario","Luigi","Cathy","Leiah","Vader",],
	"np":[],
	"rel_pronouns":[],
	"int_pronouns":[],
	"ind_pronouns":[],
	""
	"predicate_past":["ran home","ate a cow","loved to be home"],
	"trans_verb":[],
	"do_s":[],
	"do_p":[],
	"io":[],
	"trans_verb":[],
	"intr_verb":[],
	"linking_verb":[],
	}
	def __init__(self,name):
		self.name = name
	def get_question(self):
		pass	

if __name__=="__main__":
	print Sentence_Question("sentence1")