# -*- coding: utf-8 -*-
"""apostrophe"""
from question import make_packets
def make_packet(n=1):
	return make_packets(n,qdict={
		"correct apostrophe use":[
		"I've seen many students' projects, but this is the best.",
		"These are the two girls' books.",
		"The snowglobe is the two boys'.",
		"Don't take the three boys' snowboards.",
		"The two mens' black potion was not wanted during the day.",
		"Angela's and Tommy's papers were really well done.",
		"Angela and Tommy's house is lovely.",
		"Its binding was almost falling off.",
		"The one clock's hands seemed to move slower as class continued.",
		"I've seen many children's writings, but this is the best.",
		"I'd say Christmas is the best season.",
		"I would've found it had they not hid it so well.",
		"Cars of the 90s were nondescript.",
		"Many 80's and 90's were scored on the test.",
		#"Fashion of the 80s was very unusual.",
		"The student's paper used many &'s instead of the actual word and.",
		],
		"incorrect apostrophe use":[
		"I'm glad it's back to it's original condition.",
		"We like your gardens's layout. It makes me feel like I'm in nature.",
		"Our governors' plan is to make Arizonas' future better.",
		"This is the one girls' book.",
		"This is the one girls' book.",
		"This is the two girls books'.",
		"The one clocks' hands seemed to move slower as class continued.",
		"I've seen many students' project's, but this is the best.",
		"I've seen many students' projects, but this's the best.",
		"I've seen many students projects, but this is the best.",
		"Justins' toy is very small.",
		"Id say Christmas is the best season.",
		"I wouldve found it had they not hid it so well.",
		"The student's paper used many &s instead of the actual word and.",
		"Many 80s and 90s were scored on the test.",
		#"Fashion of the 80's was very unusual.",
		],
		},qsection="Apostrophe")

if __name__ == "__main__":
	print "testing..."
	print make_packet(2)

# """
# Which item below correctly uses an apostrophe to rewrite the following phrase?

# a book belonging to two girls

# two girl's book

# two girls' book

# two girl's books

# two girls books'
# """

# """
# Which of the following shows correct apostrophe use?

# I've seen many childrens' project's, but this is the best.

# I'm glad it's back to it's original condition.

# We like your garden's layout. It makes me feel like I'm in nature.

# Our governors' plan is to make Arizonas' future better.
# """