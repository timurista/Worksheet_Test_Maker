import re
from pattern.en import parse
from nltk import ngrams

p = [
"Every year we hear more and more people complaining about the extended commercialism of the winter holiday season.",
"Every year stores put out decorations and holiday merchandise earlier and earlier.",
"Yet every year retailers complain that sales are not what they should be.",
"When will retailers learn?",
"The public knows how to keep its own schedule.",
"When we do not buy holiday gifts far in advance, shoppers are saying that they do not want to think about the winter holidays too early.",
]

parsed = [[y.split("/")[:2] for y in parse(x).split(" ")] for x in p]
subj = []
for p in parsed[-2:]:
	subj = []
	#print parsed.index(p)
	for word1,word2,word3 in ngrams(p,3):
		if (word1[1].startswith('N') or word1[1].startswith('P')) and word2[1].startswith('V'):
			#print word1,word2
			subj+=[word1]
			if len(subj)>2:
				for w1,w2,w3 in ngrams(subj,3):
					if w1[1].startswith('PR') and w2[1].startswith('N') and w3[1].startswith('PR') and w1!=w3:
						print "This sentence does not have agreement with its pronouns, remove first pronoun: {}".format(p)

print subj
"""
Question 1
Which of the following is the best version of the underlined portion of sentence 6 (reproduced below)?
When we do not buy holiday gifts far in advance, shoppers are saying that they do not want to think about the winter holidays too early.

(A) When we do not buy holiday gifts far in advance, shoppers
(B) When shoppers do not buy holiday gifts far in advance, they
(C) In fact, shoppers' holiday gifts are not bought far in advance; they
(D) Consequently, by our not buying these far in advance, shoppers
(E) In contrast, when we do not do so, it is because shoppers
"""