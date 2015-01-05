import random
from nltk.corpus import brown
import re

tagged_sents = brown.tagged_sents(categories=
	['news','editorial', 'reviews','lore','fiction','mystery',
	'science_fiction','adventure','religion'])
len_choices = len(tagged_sents)



MAX_SENTLEN = 22
MIN_SENTLEN = 7

def check_NP(tagged_sent):
	"""
	checks for a noun phrase in the tagged sentence
	"""
	for (w,t) in tagged_sent[:6]:
		if t.startswith("N"): return True
	return False


def recombine(words):
	sent = ' '.join(words)
	# fix the quotation marks
	sent = re.sub("`` +","\"",sent)
	sent = re.sub(" +''","\"",sent)
	sent = re.sub(" \.+",".",sent)
	sent = re.sub("\( ","(",sent)
	sent = close_begining_paranthesis(sent)

	for token in [",",".",":", "!",";","?",")"]:
		pattern = "( \\"+str(token)+")+"
	 	sent = re.sub(pattern,str(token),sent)

	sent = capitlize_first(sent)
	return sent

def capitlize_first(sent):
	if sent[0].islower():
		return sent[0].upper()+sent[1:]
	else: return sent

def find_type_with_function(fn):
	sent_found = False
	interation_counter = 0
	iteration_max = 100
	traversed_list = []
	while len(traversed_list)<100 or not sent_found:
		choice = random.choice(range(len_choices))
		if choice not in traversed_list: 
			choice = random.choice(range(len_choices))
		traversed_list+=[choice]

		sent = tagged_sents[choice]
		not_forbidden = len([w.lower() for w in ['sexual','sex','orgasim','climax','negro'] if w in sent])<1
		find_kind = fn(sent)
		if find_kind and not_forbidden and len(sent)<MAX_SENTLEN and len(sent)>MIN_SENTLEN and check_NP(sent):
			new_sent = []
			# only add once
			add_count = 0
			word_found = False
			for w,t in sent:
				if w.lower()==find_kind.lower() and add_count<1 and not word_found:
					new_sent.append("<u>"+w+"</u>")
					word_found=True
					add_count+=1					
				else: new_sent.append(w)
			return recombine(new_sent)+" "+recombine([w for w,t in tagged_sents[choice+1]])
		interation_counter+=1			
		if interation_counter>iteration_max:
			sent_found=True
	return ""
		#print "looking for word"

def get_sent_and_ans_with_function(fn):
	sent_found = False
	interation_counter = 0
	iteration_max = 100000
	while not sent_found:
		choice = random.choice(range(len_choices))
		sent = tagged_sents[choice]
		find_kind = fn(sent)
		if find_kind and len(sent)<MAX_SENTLEN and len(sent)>MIN_SENTLEN and check_NP(sent):
			second_sent = recombine([w for w,t in tagged_sents[choice+1]])
			return (recombine([w for w,t in sent])+" "+second_sent,find_kind)
		interation_counter+=1			
		if interation_counter>iteration_max:
			sent_found=True
			return ""

# def get_sent_underline_multiple(fn):
# 	sent_found = False
# 	interation_counter = 0
# 	iteration_max = 100000
# 	while not sent_found:
# 		choice = random.choice(range(len_choices))
# 		sent = recombine([w for w,t in tagged_sents[choice]])
# 		find_kind = fn(sent)
# 		if find_kind and len(sent)<MAX_SENTLEN and len(sent)>MIN_SENTLEN and check_NP(sent):
# 			return (sent,find_kind)
# 		interation_counter+=1			
# 		if interation_counter>iteration_max:
# 			sent_found=True
# 			return ""

#assert capitlize_first("he had helped fight an oil-well fire <u>that</u> raged six days and nights."),\
#"He had helped fight an oil-well fire <u>that</u> raged six days and nights."

def close_begining_paranthesis(sent):
	if sent.count("\"")%2:
		return sent+"\""
	return sent



# s2 = """After reading "Plowman's Folly" by Edward H. Faulkner, he stopped plowing."""
# s1 = """"<u>Listen</u>, Ekstrohm, I want to give you the benefit of every doubt. But you aren't exactly the model of a surveyor, you know."""
# print close_begining_paranthesis(s1)
# print close_begining_paranthesis(s2)

