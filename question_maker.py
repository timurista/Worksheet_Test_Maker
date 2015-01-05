# -*- coding: utf-8 -*-
import sys
import os
from random import shuffle
from worksheet_maker import Worksheet
# gets all question files
sys.path.append(os.getcwd()+'/Questions/q_base')
sys.path.append(os.getcwd()+"/Questions/Vocab")
import sent_maker
print sent_maker
from Questions import *
import make_vocab

class q_maker:
	def make_file(self,name,data,directory):
		if not os.path.exists(directory):
		    os.makedirs(directory)
		file_ = open(directory+"/"+name,'w')
		file_.write(data)
		file_.close

	def make_test(self,list,number=1):
		s=""
		s+=self.make_vocab(self.vocab)
		print s
		for f in list:
			try:
				print "making questions for {}".format(f)
				s+= eval(f).make_packet(40)
			except Exception, e:
				print e,f
				continue
		
		#self.make_file(self.name+".csv",s.strip(),"./Tests")
		print s
		Worksheet("Test 6 on Parts of Sentence and Vocabulary",s).make_worksheet(type="Test")
		return s.strip()[:20]+"...\n**Made file for your test**"

	def make_vocab(self,vocab_words):
		#vocab_words = vocab_words.strip().split('\n')
		#shuffle(vocab_words)
		#print vocab_sents.get_vocab_questions(vocab_words,11)
		try:
			return vocab_sents.get_vocab_questions(vocab_words,11)
			#return make_vocab.make_vocab_qs(vocab_words[:12])
		except Exception, e:
			print "error, "+str(e)
			return ""


	def __init__(self,**kwargs):
		#keys = sys.modules.keys()​
		# grabs everything but the init file first entry
		self.vocab = kwargs.get("vocab","")
		self.name = kwargs.get("name","Demo Test")
		self.directory = kwargs.get("directory","./")
		self.files = [f[:-3] for f in os.listdir(self.directory) if f.endswith(".py")][1:]

		# imports all files into directory

#print q_maker().keys
vocab = """humdrum
interminable
germinate
interrogate
alliance
fruitless
mortify
spirited
bewilder
hostile
orthodox
inflammable
procure
void
controversial
inflict
scurry
wayward
dishearten
malignant
sodden
wince
"""
q =  q_maker(directory="./Questions",name="Test 6", vocab=vocab)
# files =q.files
# print files
#print q.make_vocab()
#q.make_test(['adj_advb', 'conjunctions', 'pronouns_q_maker', 'subj_pred',])

#q2 = q_maker(directory="./Questions",name="Practice for Test 5 # 1", vocab="")
print q.make_test(['do_text'])