import sys
import os
sys.path.append(os.getcwd()+'/q_base')
from sent_maker import find_type_with_function, get_sent_and_ans_with_function, recombine
import nltk
import random
from pattern.en import lemma
import string
import re

#prepositions
def has_preposition(sentence):
	for w1,t1 in sentence:
		if t1.startswith('IN') and w1 not in ['of']:
			return w1


#RBR	adverb, comparative	better
def has_adv_compar(sentence):
	for w1,t1 in sentence:
		if t1.startswith('RBR'):
			return w1

def has_adv2_compar(sentence):
	for (w1,t1),(w2,t2) in nltk.bigrams(sentence):
		if w1 in ['more','less'] and t2.startswith('RB'):
			return w1+" "+w2


#RBS	adverb, superlative	best
def has_adv_super(sentence):
	for w1,t1 in sentence:
		superlatives = ['best','biggest','smallest','strongest','brightest','lightest','roundest','coolest']
		if w1 in superlatives:		
			return w1

def has_adv2_supr(sentence):
	for (w1,t1),(w2,t2) in nltk.bigrams(sentence):
		if w1 in ['most','least'] and t2.startswith('RB'):
			return w1+" "+w2


# 7.6 - Conjunction
def has_cc(sentence):
	for w1,t1 in sentence:
		if t1.startswith('CC'):		
			return w1

# 7.6.1 - Coordinating (FANBOYS) Conjunction
def has_cc_fanboys(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if w1 in [','] and w2 in ['for','nor','but','yet','so','and']:
		#if w1 in ['for','nor','but','yet','so','and'] and (t2.startswith('PRP') or t2.startswith('N')) and t3.startswith('V'):		
			return w2

def has_correlative_cc(sentence):
	sent2 = ' '.join([w for w,t in sentence])
	#sentence2 = [(w,t) for (w,t) in sentence if t not in ['IN','RB','JJ','VBG','TO','FW','DT']]
	correlatives =  [("both","and"),("either","or"),("neither","nor"),("not only","but also"),("rather","than"),("no sooner","than")]		
	for (w1,w2) in correlatives:
		pattern = '( [{0}{1}]{2} ).+({3} )'.format(w1[0].lower(),w1[0].upper(),w1[1:],w2)
		finds = re.findall(pattern,sent2)
		if len(finds):
			return w1


	# for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence2):
	# 	if (w1,w3) in [("both","and"),("either","or"),("neither","nor"),("not only","but also"),("rather","than"),("no sooner","than")]:		
	# 		return w1
	# PATTERN '([eE]ither).+(or)' for finding correlative

# def has_correlative_cc(sentence):
# 	corr_c = []
# 	for (w,t) in sentence:
# 		if w in ["both","either","neither","not only","rather"]:
# 			for (w2,t2) in sentence[sentence.index((w,t)):]:
# 				print w2
# 				if w2 in ["and","or","nor","but also","than"]:
# 					return w

# 7.6.3 - Subordinating Conjunction
def has_subordinating_cc(sentence):
	subs = [
	"after ","even if","while "
	"although","even though ","though ",
	"as if","if ","unless",
	"as though","in order that","until",
	"as long as","rather than","when ","whenver",
	"because","since","where ","wherever",
	"before","so that","whether"
	]
	s = recombine([w for w,t in sentence])
	# for (w,t) in sentence:
	# 	found = re.sub(w)
	# 	if w in subs:
	for item in subs:
		found = re.findall("[,;]? ?([{}]{})".format(item[0].upper()+item[0].lower(),item[1:]),s)
		if len(found):
			#print found
			return found[0]			

pos_fns = {
	 "comparative adverb":has_adv_compar,
	 "superlative adverb":has_adv_super,
	 #"coordinating conjunction":has_cc,
	 "coordinating conjunction":has_cc_fanboys,
	 "correlative conjunction":has_correlative_cc,
	 "subordinating conjunction":has_subordinating_cc,
	 "superlative adv.":has_adv2_supr,
	 "comparative adv.":has_adv2_compar,
	 "preposition":has_preposition,

} 

# fanby = ['for','and','nor','but','yet','so']
# cor_c = ["both","either","neither""not only","but also"]
# sub_c = ["after ","even if"," while "
# 	"although","even though"," though ",
# 	"as if","if ","unless",
# 	"as though","in order that","until",
# 	"as long as","rather than","when ","whenver",
# 	"because","since","where ","wherever",
# 	"before","so that","whether"]

def make_conj_question(type_name):
	try:
		sent,correct = get_sent_and_ans_with_function(pos_fns[type_name])
		example_sent = sent.replace(correct,"<u>"+correct+"</u>",1)
		choices = [key for key,value in pos_fns.items() if key!=type_name]

		sent_words = ''.join([w for w in sent if w not in ['"\'?/.,:;[]{}!)(']])
		random.shuffle(choices)
		
		string = "Part of Speech Application\tIdentify the kind of <u>word</u> in the following sentence:\t"+example_sent+"\t"+type_name
		for c in choices[:4]:
			string+="\t"+c
		# random choice at end
		return string
	except Exception, e:
		print e
		return ""



def remove_punctuation(s):
	#print s
	return ''.join([c for c in s if c not in ["\"',./?][|\\+-;:&%$*--"]])
	#return s.translate(string.maketrans("",""), string.punctuation)

# generating function for question packets
def make_packet(number):
	s=""
	for n in range(number):
		for key in pos_fns:
			s+=make_conj_question(key)+"\n"
			#print "made question..."
	#print s
	return s
#print make_packet(1)

#print nltk.help.upenn_tagset()
#print get_sent_and_ans_with_function(pos_fns["subordinating coordinating conjunction"])
#print make_adj_apply_question("subordinating coordinating conjunction")