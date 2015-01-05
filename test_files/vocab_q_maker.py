from nltk.corpus import wordnet as wn
w = 'adumbrate'
def get_sent(w):
	syn = wn.synsets(w)
	for s in syn:
		print s.examples()

#get_sent(w)

def get_sim(w1,w2):
	word1 =  wn.synsets(w1)[0]
	word2 = wn.synsets(w2)[0]

	return word1.path_similarity(word2), word1.wup_similarity(word2)

print get_sim('films','shows')

def stress(pron):
	return [char for phone in pron for char in phone if char.isdigit()]

import nltk
entries = nltk.corpus.cmudict.entries()

prondict = nltk.corpus.cmudict.dict()

#print prondict['adumbrate']


