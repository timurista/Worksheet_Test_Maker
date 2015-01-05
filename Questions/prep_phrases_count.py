# -*- coding: utf-8 -*-
"""prepositional_phrases"""
from question import make_packets
def make_packet(n=1):
	return make_packets(n,qdict = {
	"one prepositional phrase":[
	"During the exam, Shawn said something.",
	"On the way home, Gabriel learned something.",
	"After school, I walked home.",
	"After school, the boy walked his dog.",
	"Before the day ends, Vader is going to find a home.",
	"Before the rebels defeat the empire, Luke will come home.",
	"Bilbo loves to eat snack foods inside the magical tree.",
	],
	"two prepositional phrases":[
	"After school, the boy walked with his dog.",
	"After school but before the day ended, Bilbo found a friend.",
	"Along the road she found him hiding in the santuary.",
	"About the water she saw the man lying against the boat.",
	"Outside the store, Vader saw her sitting among the trees.",
	"Before it was over, Vader found victory to be just around the corner.",
	],
	"three prepositional phrases":[
	"On the way to school, Claire’s shoes filled with snow.",
	"Through the snow and upon the house sat a small bird with brightly colored feathers.",
	"Within the home under the hill, Bilbo and his company traveled towards Rivendell.",	
	],
	"four prepositional phrases":[
	"After school and during the night, the boy walked with his dog inside the store.",
	"He loved to live under the hill, which was round the bend and through the woods.",
	"Opposite the couch sits a small cat near the stove and ontop of my favorite pair of pants.",
	],
	},qprompt="Identify the number of prepositional phrases below:",
	qsection="Prepositional Phrases")

if __name__=="__main__":
	print "test..."
	print make_packet(5)
