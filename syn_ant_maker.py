# -*- coding: utf-8 -*-
#from nltk.corpus import wordnet as wn
from pattern.en import wordnet as wn
from pattern.en import lemma

words= """sodden
scurry
mortify
malignant
inflict
inflammable
void
wayward
wince
""".strip().splitlines()



for w in words:
	for syn in wn.synsets(lemma(w):
		print [x for x in syn.synonyms if x!=w]

		# for lemma in syn.lemmas():
		# 	print lemma.antonyms()
print words

