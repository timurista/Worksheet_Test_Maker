# insert path to sent_maker
import sys
import os
# now get sent_maker from opened directory
from sent_maker import find_type_with_function, get_sent_and_ans_with_function, recombine
from q_base import question_template
import nltk
import random
from pattern.en import lemma
import string

#.4 - Adjective - apply
def has_adj(sentence):
	for w1,t1 in sentence:
		if t1.startswith('JJ'):
			return w1
#7.5 - Adverb - apply
def has_adv(sentence):
	for w1,t1 in sentence:
		if t1.startswith('RB'):
			return w1
# has preposition
def has_prep(sentence):
	for w1,t1 in sentence:
		if t1.startswith('IN'):
			return w1


#RBR	adverb, comparative	better
def has_adv_compar(sentence):
	for w1,t1 in sentence:
		if t1.startswith('RBR'):
			return w1

#RBS	adverb, superlative	best
def has_adv_super(sentence):
	for w1,t1 in sentence:
		if w1 in ['best','biggest','smallest','strongest','brightest','lightest','roundest','coolest']:		
			return w1

# 7.6 - Conjunction
def has_cc(sentence):
	for w1,t1 in sentence:
		if t1.startswith('CC'):		
			return w1

# 7.6.1 - Coordinating (FANBOYS) Conjunction
def has_cc_fanboys(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if t1.startswith(',') and w2 in ['for','and','nor','but','yet','so']:		
			return w2
# 7.6.2 - Correlative Conjunction
#      both ... and           neither ... nor
#    either ... or          not only ... but also


def has_correlative_cc(sentence):
	sentence2 = [(w,t) for (w,t) in sentence if t not in ['IN','RB','JJ','VBG','TO','FW','DT']]
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if (w1,w3) in [("both","and"),("either","or"),("neither","nor")]:		
			return w1


# 7.6.3 - Subordinating Conjunction
def has_subordinating_cc(sentence):
	subs = [" after ","even if"," while "
	"although","even though"," though ",
	"as if","if ","unless",
	"as though","in order that","until",
	"as long as","rather than","when ","whenver",
	"because","since","where ","wherever",
	"before","so that","whether"]
	s = recombine([w for w,t in sentence])
#	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
#		if (w1,w2) in [("as","if"),("either","though"),("even","if")]:			
	for w in subs:
		if w in s:
			return w


# 8.1 - Subject
def has_subject(sentence):
	sentence2 = [(w,t) for (w,t) in sentence if t not in ['IN','RB','JJ','VBG','TO','FW','DT']]
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence2[:6]):
		if t1 in ['NN','NNS','NNP','NNPS','PRP'] and t2.startswith('VB') and t2 not in ['VBZ'] and t3 in ['NN','NNS','NNP','NNPS','PRP']:		
			return w1

# 8.2 - Predicate
def has_predicate(sentence):
	sentence2 = [(w,t) for (w,t) in sentence if t not in ['IN','RB','JJ','VBG','TO','FW','DT']]
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence2[:6]):
		if t1 in ['NN','NNS','NNP','NNPS','PRP'] and t2.startswith('VB') and t2 not in ['VBZ'] and t3 in ['NN','NNS','NNP','NNPS','PRP']:		
			return w3

pos_fns = {
	 "adjective":has_adj,
	 "adverb":has_adv,
	 "preposition":has_prep,
	 "comparative adverb":has_adv_compar,
	 "superlative adverb":has_adv_super,
	 "coordinating conjunction (fanboys)":has_cc_fanboys,
	 "correlative conjunction":has_correlative_cc,
	 "subordinate conjunction":has_subordinating_cc,
} 

def make_adj_apply_question(type_name):
	sent,correct = get_sent_and_ans_with_function(pos_fns[type_name])
	sent_words = ''.join([w for w in sent if w not in ['"\'?/.,:;[]{}!)(']])
	choices = [remove_punctuation(k) for k in sent_words.split(" ") if k!=correct and len(k)>1]
	random.shuffle(choices)
	
	string = "Part of Speech Application\tIdentify the <b>"+type_name+"</b> in the following sentence:"+"\t"+sent+"\t"+correct
	for c in choices[:4]:
		string+="\t"+c
	# random choice at end
	return string

def make_subodinating_coordination_question(type_name):
	sent,correct = get_sent_and_ans_with_function(pos_fns[type_name])



def remove_punctuation(s):
	#print s
	return ''.join([c for c in s if c not in ["\"',./?][|\\+-;:&%$*--"]])
	#return s.translate(string.maketrans("",""), string.punctuation)

# generating function for question packets
def make_packet(number):
	s=""
	for n in range(number):
		for key in pos_fns:
			s+=make_adj_apply_question(key)+"\n"
	return s
#print make_pos_packet(6)

#print nltk.help.upenn_tagset()
#print get_sent_and_ans_with_function(pos_fns["subordinating coordinating conjunction"])
#print make_adj_apply_question("subordinating coordinating conjunction")