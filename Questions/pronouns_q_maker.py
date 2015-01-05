from sent_maker import find_type_with_function
import nltk
import random
from pattern.en import lemma

def has_possessive_pronoun(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		condition_a = (t1.startswith('PP$') or t1.startswith('PRP$'))
		condition_b = (t2.startswith('N') or t3.startswith('N'))
		if  (condition_a and condition_b):
			return w1

def has_relative_pronoun(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if t1.startswith('WD') or t1.startswith('WP'):
			if w1 in ['that'] and t2.startswith('PRP'):
				return w1
			elif w1 not in ['that']:
				return w1

def has_interrogative_pronoun(sentence):
	# check beginning
	if sentence[len(sentence)-1][0] =="?":
		for (word,tag) in sentence[:4]:
			if word.lower() in ["what", "which", "who", "whom","whose","whoever","that","whatever","whomever","whichever","whosoever"]:
				return word

def has_indefinite_pronoun(sentence):
	list_indefs = ["all", "both" ,"another" ,"each","any" ,"either" ,
	"anybody", "enough", "anyone", "everybody", "anything", "everyone",
	"everything", "none", "few", "no one", "many" ,"nothing", "most", "neither", "other", "nobody", "others",
	"several", "some", "somebody", "someone", "something"]
	for (word,tag) in sentence:
		if word in list_indefs:
			return word

def has_personal_pronoun(sentence):
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if  w1 in ['he','she','it','they','him','her','them','I','you','our','us','we'] and not t2.startswith('N'):
			return w1

def has_demonstrative_pronoun(sentence):
	#check for interrogatives first
	if has_interrogative_pronoun(sentence):
		return
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if ((t1.startswith('VB') and w2 in ['this','those','that',"these"] and t3.startswith('RB')) or\
			(t1.startswith('VB') and w2 in ['this','those','that',"these"] and t3.startswith('IN'))):
			return w2
		if w1 in ['this','those',"these"] and t2.startswith('N') and t3.startswith('VB'):
			return w1

def has_reflexive_pronoun(sentence):
	refs = ["myself", "yourself","himself", "herself", "itself", "ourselves", "yourselves", "themselves"]
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if (t1.startswith('V')):
			if w2 in refs:
				return w2
			if w3 in refs and (t2.startswith('IN') or w2 in ['of']):
				return w3

def has_intensive_pronoun(sentence):
	refs = ["myself", "yourself","himself", "herself", "itself", "ourselves", "yourselves", "themselves"]
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
		if (not t3.startswith('V') and w2 in refs and t3.startswith('V')) or (t1.startswith('IN') and w2 in refs):
			return w2

pron_fns = {"relative pronoun":has_relative_pronoun,
			"possessive pronoun":has_possessive_pronoun,
			"interrogative pronoun":has_interrogative_pronoun,
			"indefinite pronoun":has_indefinite_pronoun,
			"demonstrative pronoun":has_demonstrative_pronoun,
			"reflexive pronoun":has_reflexive_pronoun,
			"intensive pronoun":has_intensive_pronoun,
			"personal pronoun": has_personal_pronoun
			}

# for x in range(1):
# 	print find_type_with_function(has_demonstrative_pronoun)
# 	print find_type_with_function(has_intensive_pronoun)
# 	print find_type_with_function(has_reflexive_pronoun)
# 	print find_type_with_function(has_relative_pronoun)
# 	print find_type_with_function(has_personal_pronoun)
# 	print find_type_with_function(has_relative_pronoun)


def make_pron_id_question(type_name):
	correct = type_name
	choices = [k for (k,v) in pron_fns.items() if k!=type_name]
	random.shuffle(choices)

	string = "Pronouns\tIdentify the <u>word</u> in the following sentence:"+"\t"+find_type_with_function(pron_fns[correct])+"\t"+correct
	for c in choices[:4]:
		string+="\t"+c
	# random choice at end
	return string

# generating function for question packets
def make_packet(number):
	s=""
	for n in range(number):
		for key in pron_fns:
			s+=make_pron_id_question(key)+"\n"
	return s



#print make_pronoun_packet(5)

#assert make_pron_id_question("demonstrative pronoun")
#assert make_pron_id_question("relative pronoun")
#for x in range(30):
#	print find_type_with_function(has_relative_pronoun)

# test 7.3.7 - Subjective and Objective Case Pronouns
# 7.3.9 - Identifying Antecedent Pronoun
