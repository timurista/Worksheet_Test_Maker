from sent_maker import find_type_with_function
from nltk import trigrams,util
import random
from pattern.en import lemma
import re

def has_transitive_verb(sentence):
	#remove adverbs so direct objects can be seen more easily
	sentence = [(word,tag) for (word,tag) in sentence if tag!=('RB')]

	for (w1,t1), (w2,t2), (w3,t3), (w4,t4) in util.ngrams(sentence,4):		
		# case 1 with passive
		if t1[0] in ['N'] and lemma(w2) in ['be'] and t3[0] in ['VBG']:
			return w3
		#if lemma(w1) in ['be'] and 


		# case 2 without passive
		elif ((t1.startswith('V') and t1 not in ['VBG']) and lemma(w1) not in ['be'] and (t2.startswith('DT') \
			or (t3.startswith('N')) and (t2 not in ['TO','IN','AT']))):
			return w1
			#return True

def has_intransitive_verb(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in trigrams(sentence):
		if (t1.startswith('V') and (t2.startswith('TO') or t2.startswith('IN') or \
			(t2.startswith('JJ') and not t3.startswith('N')) or t2.startswith('RB'))\
			and not t3.startswith('VB')):
			return w1
			#return True

def has_modal_verb(sentence):
	for (word,tag) in sentence:
		if tag.startswith('M'):
			return word

def has_linking_verb(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in trigrams(sentence):
		l_verbs = ['be','seem','appear','become',"look", "smell", "sound" ,"taste" ,"feel"]
		if (t1.startswith('V') and (lemma(w1) in l_verbs) and t2.startswith('JJ')):
			return w1

verb_fns = {"transitive verb":has_transitive_verb,
			"intransitive verb":has_intransitive_verb,
			"linking verb":has_linking_verb,
			"auxiliary verb":has_modal_verb,
			}


def make_verb_selection_question(type_name,fn):
	choices = [v for (k,v) in verb_fns.items() if v!=fn]
	string="Verbs\t\tIdentify the <b>"+type_name+"</b> in the following underlined <u>verb</u>:"
	string+="\t"+find_type_with_function(fn)
	for r in range(4):
		string+="\t"+find_type_with_function(random.choice(choices))
	return string

def make_verb_id_question(type_name):
	correct = type_name
	choices = [k for (k,v) in verb_fns.items() if k!=type_name]
	string = "Verbs\tIdentify the <u>word</u> in the following sentence:"+"\t"+find_type_with_function(verb_fns[correct])+"\t"+correct
	for c in choices:
		string+="\t"+c
	# random choice at end
	string+="\t"+random.choice(["relative pronoun","demonstrative pronoun","interrogative pronoun"])
	return string

# generating function for question packets
def make_packet(number):
	s=""
	for n in range(number):
		for key in verb_fns:
			#s+=make_verb_selection_question(key,verb_fns[key])+"\n"
			s+=make_verb_id_question(key)+"\n"
	return s

#print has_transitive_verb()
#print make_verb_packet(2)




