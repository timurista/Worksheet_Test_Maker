# -*- coding: utf-8 -*-
from random import choice, shuffle
import re

class Question:
	def __init__(self,name,**kwargs):
		self.qdict = kwargs.get("qdict",None)
		self.name = name
		self.qsection = kwargs.get("qsection","Section")
		self.qprompt = kwargs.get("qprompt","Prompt")
		self.examples = kwargs.get("examples",self.get_examples(self.name))
		self.options = self.qdict.keys() if self.qdict else ["personification","simile","metaphor","hyperbole"]

	def get_examples(self,name):
		"""finds examples from the question dictionary if there"""
		return self.qdict.get(name,None) if self.qdict else None

	def get_example(self):
		#print "EX",self.examples
		return choice(self.examples)

	def get_rand_example(self,qtype):
		return choice(self.qdict[qtype]) if self.qdict else None

	def get_Question(self,q_type="",prompt=""):	
		"""returns a question with 4 options, first being correct"""
		choices = [x for x in self.options if x!=self.name]

		if len(choices)>2:
			#print len(choices),choices
			s = "%s\t%s\t" % (self.qsection,self.qprompt)
			s+="%s\t%s\t%s\t%s\t%s" % (self.get_example(),self.name,choices[0],choices[1],choices[2])
		else:
			#print choices
			correct,options = self.get_examples_question(self.name,choices)
			s="%s\t\tIn which passage does \"%s\" apply:\t%s\t%s\t%s\t%s" % (self.qsection,self.name,correct, options[0],options[1],options[2])
		return s

	def get_examples_question(self,key,choices):
		"""returns tuple of 4 options and the correct sentence"""
		#print choices
		assert len(choices)>0, "not enough choices to make question! %s %s" % (choices,key)

		options = list(set([self.get_rand_example(x) for x in choices*4 if x!=key]))
		return self.get_rand_example(key),options[:4]


#from pattern.en import lemma, conjugate
class sent_Question(Question):
	def __init__(self,name,**kwargs):
		Question.__init__(self,name,**kwargs)
		self.underline = kwargs.get("underline","verb")
		self.s_part = {
		"subj_s":["Lord Voldemort","Leiah","John","I","Citizen Kane","Harry Potter","Hermoine","Bilbo Baggins","Thorin"],
		"subj_p":["the boys","we","the men","all the hobbits","the men of Northern lands","the wizards","the elves","the citizens"],
		#'present participle': , 'base form': ['come', 'do', 'drive', 'give', 'go', 'have', 'know', 'say', 'see', 'sing', 'speak', 'tell', 'think', 'write'], 'past participle': , 'past form': 
		"verb_s_present":['comes', 'does', 'drives', 'gives', 'goes', 'has', 'knows', 'says', 'sees', 'sings', 'speaks', 'tells', 'thinks', 'writes'],
		"verb_s_progressive_present":['coming', 'doing', 'driving', 'giving', 'going', 'having', 'knowing', 'saying', 'seeing', 'singing', 'speaking', 'telling', 'thinking', 'writing'],
		"verb_s_progressive_past":['come', 'done', 'driven', 'given', 'gone', 'had', 'known', 'said', 'seen', 'sung', 'spoken', 'told', 'thought', 'written'],
		"verb_s_past":['came', 'did', 'drove', 'gave', 'went', 'had', 'knew', 'said', 'saw', 'sang', 'spoke', 'told', 'thought', 'wrote'],
		"verb_p_present":['come', 'do', 'drive', 'give', 'go', 'have', 'know', 'say', 'see', 'sing', 'speak', 'tell', 'think', 'write'],
		"verb_p_progressive_present":['coming', 'doing', 'driving', 'giving', 'going', 'having', 'knowing', 'saying', 'seeing', 'singing', 'speaking', 'telling', 'thinking', 'writing'],
		"verb_p_progressive_past":['come', 'done', 'driven', 'given', 'gone', 'had', 'known', 'said', 'seen', 'sung', 'spoken', 'told', 'thought', 'written'],
		"verb_p_past":['came', 'did', 'drove', 'gave', 'went', 'had', 'knew', 'said', 'saw', 'sang', 'spoke', 'told', 'thought', 'wrote'],
		"prep_present":["today","suddenly","now"],
		"prep_past":["last week","last summer","in the past"],
		"pred":["at home"],
		"preps":['aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'anti', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'excepting', 'excluding', 'following', 'for', 'from', 'in', 'inside', 'into', 'like', 'minus', 'near', 'of', 'off', 'on', 'onto', 'opposite', 'outside', 'over', 'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than', 'through', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without'],
		"prep_obj":["a ship","the library","the river"],
		"prep_phrase":["above the cupboard","across the valley"]
		}
		self.verb_pred_do = {
		"gave":["a sandwich","a twinkie","a hug"],
		"have":["a needle","a twinkie","a grey beard"],
		"had":["a needle","a twinkie","a full beard"],
		"did":["that thing"]
		}
		self.options = kwargs.get("options",['verb singular present', 
			'verb singular progressive present', 'verb plural present', 
			'verb plural progressive present', 'verb plural progressive past', 
			'verb singular progressive past', 'verb singular past', 'verb plural past'])

	def types(self):
		print "POSSIBLE TYPES",self.s_part.keys()
		return self.s_part.keys()

	def get_example(self,**kwargs):
		sent_type = kwargs.get("sent_type","simple")
		return {
		"simple":self.get_simple_sent(),
		}[sent_type]

	def get_simple_sent(self, **kwargs):
		underline = self.underline
		subj_type = kwargs.get("subj_type","p")
		verb_type = kwargs.get("verb_type","s_past")
		self.name = "verb "+verb_type.replace("s_"," singular ").replace("p_"," plural ").replace("_"," ")

		if verb_type.endswith("past"):
			pred = choice(self.s_part["prep_past"])
		elif verb_type.endswith("present"):
			pred = choice(self.s_part["prep_present"])

		subj = choice(self.s_part["subj_"+subj_type])
		verb = choice(self.s_part["verb_"+verb_type])
		prep_phrase = choice(self.s_part["preps"])+" "+choice(self.s_part["prep_obj"])

		pred = choice(self.verb_pred_do[verb])+" "+pred if verb in self.verb_pred_do else pred
		s ="%s, %s %s %s." % (prep_phrase.capitalize(),subj,verb,pred)
		try:
			replace_with = eval(underline)
		#	print replace_with,underline
			return s.replace(replace_with,"<u>"+replace_with+"</u>",1)
		except:
			return s
	#def get_Question(self):


# possibly rewrite the question selection process
class select_Quesion(sent_Question):
	def get_Question(self):
		passage = self.get_example()
		correct = re.findall("<u>(.+)</u>",passage)[0]
		# remove underline comments
		passage_new = passage.replace("<u>","").replace("</u>","")
		inc1 = re.findall("(\w* %s *\w*)" % (correct),passage_new)
		inc2 = re.findall("(\w* \w* %s *\w*)" % (correct),passage_new)
		inc3 = re.findall("(\w* %s *)" % (correct),passage_new)
		words = passage_new.split(" ")
		inc1 = inc1[0] if inc1 else words[0]
		inc2 = inc2[0] if inc2 else words[-1]
		inc3 = inc3[0] if inc3 else words[-2]
		self.options = [inc1,inc2,inc3] + [words[x] for x in range(len(words))]
		choices = [x for x in self.options if x!=correct]
		assert len(choices)>=2,"Choices "+choices
		s = "%s\t%s\t" % (self.qsection,self.qprompt)
		s+="%s\t%s\t%s\t%s\t%s" % (passage_new,correct,choices[0],choices[1],choices[2])
		return s



class Packet:
	"""given a list of questions, will make a packet for n number"""
	def __init__(self,fn_list):
		self.fn_list = fn_list
	def make_packet(self,number):
		s=""
		_range = list(range(number))
		shuffle(_range)
		#print _range
		for x in _range:
			try:
				#s+=choice(self.fn_list).get_Question()+"\n"
				s+=self.fn_list[x%len(self.fn_list)].get_Question()+"\n"
			except:
				continue
		return s
def make_packets(number=1,**kwargs):
	Qname = kwargs.get("Qname","Question")
	qdict = kwargs.get("qdict",None)

	if Qname=="Question":
		assert qdict,"No question dictionary to pull questions from!"
		if not qdict:
			return "No Questions made, no qdict"
		# shuffle if more than 3 options
		#if len(qdict)>3:
			#shuffle(qdict)
	qs = kwargs.get("questions",[])
	qsection = kwargs.get("qsection","Section")
	qprompt = kwargs.get("qprompt",None)
	# test if dictionary, else generate questions
	if len(qdict)>=4:
		if not qprompt:
			qs2 = [eval(Qname)(q,qdict=qdict,qsection=qsection,
			qprompt="Identify the %s below:" %q) for q in qdict]
		else:
			qs2 = [eval(Qname)(q,qdict=qdict,qsection=qsection,
			qprompt=qprompt) for q in qdict]
	else:
		qs2=[eval(Qname)(q,qdict=qdict,qsection=qsection) for q in qdict]
		shuffle(qs2)
	return Packet(qs+qs2).make_packet(number)

if __name__=="__main__":
	print "testing..."
	p = Packet([sent_Question("verb",qsection="Verb Identify",qprompt="Identify the correct verb type in the sentence below")])
	print p.make_packet(2)
	print make_packets(4,qdict={"question 1":["a","b","c","q","ab"],"question 2":["d","e","f","cd","ef"]})
	print select_Quesion("preposition",underline="verb").get_Question()
	print make_packets(4,qdict={
		"option1":["a","b","c"],
		"option2":["a","b","c"],
		"option3":["a","b","c"],
		"option4":["a","b","c"],
		})
