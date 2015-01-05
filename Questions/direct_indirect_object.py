# -*- coding: utf-8 -*-
import random
import sys
import os
from pattern.en import parse
print parse("Early astronomers observed the heavens constantly. The movements of the sky fascinated them.")
print parse("I gave her the drug")
sys.path.append(os.getcwd()+'/q_base')
from q_base import question_template
from nltk import ngrams

def has_direct_object(sentence):
	for (w1,t1),(w2,t2),(w3,t3) in ngrams(sentence,3):
		if t1.startswith('VB') and t2.startswith('N'):
			return w3
		elif (t2.startswith('DT') and t3.startswith('N')):
			return w3
		elif t1.startswith('VB') and t2.startswith('PRP'):
			return w2


fn_list = {"direct object":has_direct_object}

qt = question_template("Complements",fn_list=fn_list)
print qt.make_packet(1)
