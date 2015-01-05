# -*- coding: utf-8 -*-
from random import choice, randrange
def get_sub_combine_q():
	"""
	4.2.1 - Sentence Structure - 
	Sentence Combining 0 27 MT 3.3 -demonstrate
	fanboys
	sub conjunction

	Two Sentences: Dad is going to take us to get pizza. We’re going after he drives 
	 Mom to the airport.
	 Complex Sentence: After Dad drives Mom to the airport, he’s going to take us to get
	 pizza.
	"""
	ms_subjs = ["Dad","Jim","Bob","Vader","Bilbo","Gandalf","Superman","Mr Hero","Superwoman","Katniss","Jar-Jar"]
	ms_sub_conj = [
	"after he drives Mom to the airport",
	"once he drives my sister to her appoinment",
	"after he drives my sister to the airport",
	"after he decides its time to come home",
	"after he finishes at work",
	"once he gets home"
	]
	pred = ["is going to take us to the movies",
	"is going to tuck us into bed","is going to feed us dinner","is going to read us a bed-time story",
	"is going to take us to the airport","is going to give us a snack","will take us on a vacation",
	"will give us some desert"
	]
	subj2_pl = ["We","My friends and I","All of us"]
	pred2_pl = ["will go do it"]
	sent = get_combined_sent(choice(ms_subjs),
		choice(pred),choice(subj2_pl),
		choice(pred2_pl),choice(ms_sub_conj))
	#print sent
	return sent

def get_combined_sent(subj,pred,subj2,pred2,conj):
	conj_correct = conj.capitalize().replace(" he "," "+subj+" ")
	inc1= "%s %s. %s %s %s." %(subj,pred,subj2,pred2,conj)
	inc2 ="%s, %s %s." %(conj_correct,subj,pred)
	inc3 = "%s %s %s." %(subj2,pred2, conj)
	inc4 = "%s %s." %(subj,pred)
	correct = "%s, he %s." % (conj_correct, pred)
	s= "Sentence Combining\tWhich best combines the following sentence: \t"
	return s+'\t'.join([inc1,correct,inc2,inc3,inc4])

def make_packet(number=1):
	s=""
	for x in range(number):
		types = [get_sub_combine_q]
		i = x%len(types)
		s+=types[i].__call__()+"\n"
	return s
#print get_sub_combine_q()

from random import choice
def join_subordinate():

	"""
	4.2.1.1 - Subordination v. Coordination 0 27 MT
	4.2 -differentiate
	"""
	ex = "He enjoys walking through the country."
	ex2 = "He often goes backpacking on his vacations."
	sub_c = ["after", "although", "as", "as if", "because", "before", "even if", "even though", "if", "if only", "rather than", "since", "that", "though", "unless","until", "when", "where", "whereas", "wherever", "whether", "which", "and while"]
	print "%s, %s %s"% (ex,choice(sub_c),ex2)
	print ex

"""
4.2.2 - Sentence Structure - Sentence Expanding 0 27 MT
3.3 -demonstrate
"""

"""
4.2.3 - Sentence Structure - Sentence Variation 0 27 MT
3.3 -demonstrate
use relative pronouns for variety here
"""


def get_misplaced_modifer():	
	"""4.2.4 - Sentence Structure - 
	Placement of Modifiers 0 27 MT
	Modifiers are words, phrases, or clauses that provide description in sentences. Modifiers allow writers to take the picture that they have in their heads and transfer it accurately to the heads of their readers. Essentially, modifiers breathe life into sentences. Take a look at this "dead" sentence:
	Modifiers can be adjectives, adjective clauses, adverbs, adverb clauses, absolute phrases, infinitive phrases, participle phrases, and prepositional phrases. The sentence above contains at least one example of each:

	misplaced modifiers
	If too much distance separates a modifier and its target, the modifier is misplaced:

	Sauced with lumpy gravy, the waitress served Gilbert a plate of gray meatloaf.
	The waitress is sauced with lumpy gravy? That's not logical!

	If the sentence fails to include a target, the modifier is dangling:
	Studying the unappetizing plate of food, all appetite was lost.

	3.3 -demonstrate"""
	pass


"""
Clauses and sentence structure
There are two types of clauses: main and subordinate. A main clausecontains a subject
and a predicate. This type of clause is also called independent, because it can stand
alone as a sentence.
The baby cried.
A subordinate, or dependent, clausecontains a subject and predicate but cannot stand
alone. This type of clause must be used with a main clause in order to make sense. It
usually begins with a subordinating conjunction, such as after, although, as, as if,
because, if, since, so that, than, unless, until, when, where, or while; a relative pronoun
such aswho, whose, whom, which, that, or what; or a relative adverb, such aswhen,
where,or why.
The baby cried when the dog barked loudly.
"""

"""
Simple compound
Simple and Compound Sentences
A simple sentencecontains one main clause and no subordinate clauses. The simple
sentence may not appear to be simple. It may have a compound subject or a compound
predicate. It may also contain modifiers. As long as it has only one main clause, it is a
simple sentence.
Li-Ching and Maria sang a duet.
A compound sentencecontains two or more main clauses that are usually joined by a
comma and a coordinating conjunction.
Maria sang one of her own songs, and Robert danced.
Maria sang,Robert danced,and Li-Ching played the piano.
"""


"""
Complex and Compound
Complex and Compound-Complex Sentences
A complex sentencecontains one main clause and one or more subordinate clauses.
When she heard the applause, Beth felt proud.
A compound-complex sentencehas more than one main clause and one or more
subordinate clauses.
Although we had difficulty deciding, we finally chose a destination, and Dad bought
the airline tickets.
"""

"""
Adjective Clauses
An adjective clauseis a subordinate clause that modifies a noun or pronoun. Remember
that a subordinate clause contains a subject and verb but cannot stand alone. An
adjective clause usually begins with a relative pronoun, such as who, whom, whose, that,
and which, or a subordinating conjunction, such as where or when.
The book that I lent himis now overdue. (The adjective clause modifies the noun
)
Sometimes the relative pronoun or subordinating conjunction is left out.
The book I lent himis now overdue.
An adjective clause can be essential or nonessential to the meaning of a sentence. An
essential adjective clause is an adjective clause that cannot be omitted from a sentence
without changing its meaning. A nonessential adjective clause can be omitted from a
sentence, and the meaning of the sentence will remain the same.
Essential: The player who batted lastscored the winning run.
Nonessential: Jerome, who batted last, is the best player on the team.
"""




if __name__ == '__main__':
	print "running tests..."
	# test sent 1
	assert get_sub_combine_q()
	# test sent combining 3
	assert True
	#assert join_subordinate()
	print make_packet(10)

	pass
