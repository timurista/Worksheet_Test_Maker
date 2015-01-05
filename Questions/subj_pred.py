# insert path to sent_maker
import sys
import os
sys.path.append(os.getcwd()+'/q_base')
from sent_maker import find_type_with_function, get_sent_and_ans_with_function, recombine
from q_base import question_template
#import q_base
import nltk
import inspect
import random
import re

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


	def has_inverted_order_pred(self, sentence):
		try:
			if sentence[0][1].startswith('RB'):
				for x in range(1,2):
					if sentence[x][1] in ['VB','VBD']:
						return sentence[x][0]
		except:
			pass


	def has_simple_predicate(self,sentence):
		for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
			if (t1.startswith('N') or t1.startswith('PRP')) and (t2.startswith('V') and t2 not in ['VBG']):
				if t3.startswith('V'):
					return w2+" "+w3
				else:
					return w2

	def has_complex_subject(self,sentence):
		tags = ' '.join([w+"/"+t for w,t in sentence[:8]])
		if '/P' not in tags:
			# find one
			pattern = "(\w+\/[I]\w+ ){0,}"
			pattern+= "(?:(\S+)\/[AD]T )?(?:(\S+)\/N\w+ )+(?:(\S+)\/J\w+ ){0,}(?:(\S+)\/N\w+ )+(?:\w+\/V\w+)"


			finds = re.findall(pattern,tags)
			#print finds
			if len(finds):
			#	print tags
				s = re.sub(" +"," ",' '.join(finds[0]))
				if '/IN' not in s:
					return s.lstrip().rstrip()


	def has_compound_subj(self,sentence):
		tags = ' '.join([w+"/"+t for w,t in sentence[:6]])
		pattern = "(\w+\/[I]\w+ ){0,}"
		pattern += "(?:\S+\/[J]\w+ ){0,}(?:(\S+)\/[N]\w+ ){1,}(?:[any]?[nore][drt]\/\w+ ){1,}(?:\S+\/[J]\w+ ){0,}(?:(\S+)\/N\w+ )(?:\w+\/V\w+)"
		# "(?:(\S+)\/[AD]T )?(?:(\S+)\/N\w+ )+(?:(\S+)\/J\w+ ){0,}(?:(\S+)\/CC ){0,}(?:(\S+)\/N\w+ )+?(?:\w+\/V\w+)"
		finds = re.findall(pattern,tags)

		if len(finds):
			if "don't" not in finds[0]:
				s = re.sub(" +"," ",' '.join(finds[0]))
				if '/IN' not in s:
				#	print tags
					return s.lstrip().rstrip()

	def remove_pphrases(self,sentence):
		pass

	def has_compound_pred(self, sentence):
		tags = ' '.join([w+"/"+t for w,t in sentence])
		pattern = "(?:(\w+)\/V\w+ )(?:\S+ )+(?:[any]?[noe][drt]\/\w+ )(?:(\w+)\/V\w+ ?)"
		# "(?:(\S+)\/[AD]T )?(?:(\S+)\/N\w+ )+(?:(\S+)\/J\w+ ){0,}(?:(\S+)\/CC ){0,}(?:(\S+)\/N\w+ )+?(?:\w+\/V\w+)"
		finds = re.findall(pattern,tags)

		if len(finds):
			s = re.sub(" +"," ",' '.join(finds[0]))
		#	print tags
		#	print s
			return s.lstrip().rstrip()


#	def has_complete_subject
		#pass
#parser = pos_finder()
fn_list = {
	"simple subject":pos_finder().has_simple_subject,
	"simple predicate":pos_finder().has_simple_predicate,
	"complete subject":pos_finder().has_complex_subject,
	"compound subject":pos_finder().has_compound_subj,
	"compound predicate":pos_finder().has_compound_pred,
	"inverted order predicate":pos_finder().has_inverted_order_pred
	}

#print inspect.getmembers(pos_finder)

def make_question(type_name):
	sent,correct = get_sent_and_ans_with_function(fn_list[type_name])
	example_sent = sent
	for c in correct.split(" "):
		example_sent = example_sent.replace(c,"<u>"+c+"</u>",1)
	choices = [key for key,value in fn_list.items() if key!=type_name]

	sent_words = ''.join([w for w in sent if w not in ['"\'?/.,:;[]{}!)(']])
	random.shuffle(choices)
	
	string = "Part of Sentence\tIdentify the kind of <u>word(s)</u> in the following sentence:\t"+example_sent+"\t"+type_name
	for c in choices[:4]:
		string+="\t"+c
	# random choice at end
	return string

def make_packet(number):
	s=""
	for n in range(number):
		for key in fn_list:
			s+=make_question(key)+"\n"
	return s
#	return question_template("Subject and Predicate",fn_list=fn_list).make_packet(number)

#print make_packet(1)
# print make_question("simple subject")
# print make_question("simple predicate")
# print make_question("complex subject")

# for i in inspect.getmembers(parser, predicate=inspect.ismethod)[1:]:
# #	print make_question(str(pos_finder)+"."+i[0][0])


#question_to_test_maker

# import questions

# make test

# export questions
# in print and html format


