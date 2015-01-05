# -*- coding: utf-8 -*-
import re
import random

exp = {"Exposition ":
[
"Is at the base of the mountain or the beginning of the story. ",
"This is where the author sets up the story including characters, setting, and main conflicts."
], 
"The Rising Action ":["occurs as you begin to move throughout the story. ",
"This is where conflicts start to build just like when you climb a mountain you are moving further along.",
"This is a related series of incidents in a literary plot that build toward the point of greatest interest."
], 
"The Climax ":
[
"Is the turning point of the story. "
"You have reached the top of the mountain and you cannot go any further, you have to turn and go down.",
"This point in the story is when things finally start to move in a different direction and it may not always be a positive direction.",
],
"Falling Action":
[
"Occurs after the climax as things start to work themselves out in the story. "
"You are coming down the mountain just as you are coming down from the excitement of the climax."
],
"The Resolution":
[
"is the solution to the problem as you have reached the bottom of the mountain. "
"The solution might not be what you want, but the conflict has been resolved."
],
"The Inciting Incident":
[
"This is the event or decision that begins a story’s problem.",
"Everything up and until that moment is Backstory; everything after is the story.",
"Before this moment there is an equilibrium, a relative peace that the characters in a story have grown accustomed to.",
"This the plot point which occurs and upsets the balance of things. Suddenly there is a problem to be solved."
]
}
keys = exp.keys()

def make_packet(number):
	random.shuffle(keys)
	s=""
	for key in keys[:3]:
		new_l = [x for x in keys[:5] if x!=key]
		value= random.choice(exp[key]).capitalize()	#print new_l
		s +="{}\t{}\t{}\t{}".format("Plot Structure","Identify the plot structure associated with the following description: ",value,key)
		for key in new_l[:4]:
			s+="\t{}".format(key)
		s+="\n"
	return s

#print make_packet(1)