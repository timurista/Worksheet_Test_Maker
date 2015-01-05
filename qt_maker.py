import re
import nltk
from sent_maker import find_type_with_function, get_sent_and_ans_with_function, recombine
import inspect
import random

class pos_finder:

	def __init__(self):
		pass


	def has_simple_subject(self,sentence):
		if self.is_passive(sentence):
			pass
		else:
			for (w1,t1),(w2,t2) in nltk.bigrams(sentence):
				# test simple subject for here, there

				# remove prepositional phrases, or else you don't match neither with verb

				# test simple subject for passive

				if (t1.startswith('N') or t1.startswith('PRP')) and (t2.startswith('V') and t2 not in ['VBG']):
					return w1
	def is_passive(self, sentence):
		return False

	def has_past_simple_subject(self,sentence):
		pass

	def has_simple_predicate(self,sentence):
		for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
			if (t1.startswith('N') or t1.startswith('PRP')) and (t2.startswith('V') and t2 not in ['VBG']):
				if t3.startswith('V'):
					return w2+" "+w3
				else:
					return w2

	def has_complex_subject(self,sentence):
		tags = [w[1] for w  in sentence]
		print ' '.join(tags)
		print ' '.join([w[0] for w in sentence])
		return ""

	def remove_pphrases(self,sentence):
		pass

	def has_compound_subject(self, sentence):
		pass


#	def has_complete_subject
		#pass
#parser = pos_finder()
pos_fns = {
	"simple subject":pos_finder().has_simple_subject,
	"simple predicate":pos_finder().has_simple_predicate,
	"complex subject":pos_finder().has_complex_subject,
	}

#print inspect.getmembers(pos_finder)

def make_question(type_name):
	sent,correct = get_sent_and_ans_with_function(pos_fns[type_name])
	example_sent = sent.replace(correct,"<u>"+correct+"</u>",1)
	choices = [key for key,value in pos_fns.items() if key!=type_name]

	sent_words = ''.join([w for w in sent if w not in ['"\'?/.,:;[]{}!)(']])
	random.shuffle(choices)
	
	string = "Part of Speech Application\tIdentify the kind of <u>word</u> in the following sentence(s):\t"+example_sent+"\t"+type_name
	for c in choices[:5]:
		string+="\t"+c
	# random choice at end
	return string

print make_question("simple subject")
print make_question("simple predicate")
print make_question("complex subject")

# for i in inspect.getmembers(parser, predicate=inspect.ismethod)[1:]:
# 	print make_question(str(pos_finder)+"."+i[0][0])


#question_to_test_maker

# import questions

# make test

# export questions
# in print and html format


