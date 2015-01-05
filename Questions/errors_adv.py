# -*- coding: utf-8 -*-
import random

noun_s = """
He
She
John
Gabriel
Jim
Mr. Horton
"""

noun_pl = """
They
We
We all
All of you
Those guys
Those girls
"""

predicate = """
runs
jumps
swims
plays the violin
plays tennis
plays volleyball
plays the flute
plays soccer
plays the game
throws the ball
reads the book
feels
plays the trumpet
plays video games
draws
plays football
kicks the ball
eats the ice cream cone
eats dinner
plays the piano 
"""

very="""
I am very tired
I am very happy
He is very happy
He is very tired
She is very exhausted
Bob is very exhausted
Jerry is very sleepy
Jerry can be very annoying
John can be very silly
We can be very silly
You are very silly
He is very excited
"""

incorrect_very = [s.replace("very","very much") for s in very.strip().split("\n")]

adverb_mistakes ="""
He talked quiet.
He sang the song good.
He jumped quickly over the fence.
She is so poor to pay the dues.
It is very hot to go out.
She carefully drove.
She angrily spoke.
The room is enough spacious for us.
I know to swim.
He is not clever to solve the problem.
He is now too strong to walk.
She drove careful.
It was bitter cold.
I couldn’t help not overhearing their conversation.
I ever remember having seen a more interesting film.
The story was too interesting.
This lesson was too interesting.
She hasn’t got no children.
He hasn't got no life.
They haven't got no education.
This hardly won liberty cannot be lightly abandoned.
This hardly won justice will not last long.
I am much happy to see you.
No one writes as neat as he does.
I cannot by no means allow you to do so.
I cannot by no means make you do it.
I will not in no way do it for you.
You cannot by no means do it.
She sang sweet.
She sang soft.
She talked soft.
She whispered soft.
She sang loud.
She sang good.
She sang bad.
I don’t know nothing about the matter.
He ran good.
He knew nothing about no person.
She took care of dogs good.
She often stops sudden.
"""
adverb_corrections="""
She is too poor to pay the dues.
It is too hot to go out.
She spoke angrily.
The room is spacious enough for us.
I know how to swim.
He is not clever enough to solve the problem.
He is now strong enough to walk.
She drove carefully.
It was bitterly cold.
I couldn’t help overhearing their conversation.
I never remember having seen a more interesting film.
The story was very interesting.
She has not got any children. 
This hard won liberty cannot be lightly abandoned.
I am very happy to see you.
No one writes as neatly as he does.
I cannot by any means allow you to do so.
I can by no means allow you to do so.
She sang sweetly.
I felt very lonely.
I don’t know anything about the matter. 
I know nothing about the matter.
"""

adverb_mistakes_dict = {
	"too should be used here because too has a negative connotation and means more than is needed or excessive":[
		"She is so poor to pay the dues.",
		"It is very hot to go out.",
		"He is so tired to hike the trail.",
		],
	"the adverb should come after the verb in this case":[	
		"She carefully drove.",
		"She angrily spoke.",
		"She heartedly laughted.",
		"They sweetly sang.",
		"The room is enough spacious for us."
		],
	"the negative adverb here makes the sentence confusing":[
		"He is not clever to solve the problem.",
		"The boy is not smart to figure out the math solution.",
		],
	"the adjective instead of the adverb form was used here":[
		"She drove careful.",
		"It was bitter cold.",
		"I am much happy to see you.",
		"No one writes as neat as he does.",
		"She sang sweet.",
		"She sang soft.",
		"She talked soft.",
		"She whispered soft.",
		"He sang loud.",
		"They sang good.",
		"We sang bad.",
		"This is an easy exam.",
		"We sing more good than they.",
		"He laughed silly.",
		"He behaved cowardly.",
		],
	"double negative used":[
		"I couldn’t help not overhearing their conversation.",
		"She hasn’t got no children.",
		"He hasn't got no life.",
		"They haven't got no education.",
		"I cannot by no means allow you to do so.",
		"I cannot by no means make you do it.",
		"I will not in no way do it for you.",
		"You cannot by no means do it.",
		"I don’t know nothing about the matter.",
		],
	"used wrong adverb":[
		"I ever remember having seen a more interesting film.",
		"I ever felt good after exam.",
		"I am deadly certain he is making a mistake.",
		"She is the mostly beautiful woman in the world.",
		"We are near home from our trip.",
		],
	"adverb instead of adjective used":[
		"This hardly won liberty cannot be lightly abandoned.",
		"This hardly won justice will not last long.",
		"I can do that assignment easy.",
		"Marta plays the violin real good.",
		"It often stops sudden.",
		"This is an easily test.",
		"This an unkindly thing to say.",
		"That was an unkindly thing to say.",
		"The riders were on a peacefully journey.",
		],
}

def good_bad_adv():
	s="Using Adverbs Correctly\t\tChoose the grammatically correct statement:"
	for x in range(4):
		good_bad=random.choice(["good","bad"])
		well_badly=random.choice(["well","badly"])
		subj = random.choice(noun_s.strip().split("\n"))	
		pl_subj = random.choice(noun_pl.strip().split("\n"))
		pred = random.choice(predicate.strip().split("\n"))
		pl_pred = ' '.join([pred.split(" ")[0][:-1]]+pred.split(" ")[1:])
		if x<1:
			if random.randint(0,1)==1:
				s+="\t%s %s %s" % (pl_subj,pl_pred,well_badly)
			else:
				s+="\t{} {} {}".format(subj, pred,well_badly)
		if random.randint(0,1)==1:		
			s+="\t{} {} {}".format(subj, pred,good_bad)
		else:
			s+="\t{} {} {}".format(pl_subj, pl_pred,good_bad)
	return s+"\n"


def very_mistakes():
	s="Using Adverbs Correctly\t\tChoose the grammatically correct statement:"
	incorrect = incorrect_very[:]
	random.shuffle(incorrect)
	for x in range(4):
		if x==0:
			s+="\t%s" % random.choice(very.strip().split("\n"))
		else:
			s+="\t%s" % incorrect[x-1]
	return s+"\n"

def get_adverb_common_mistakes():
	s=""
	for i in range(2):
		s+="Using Adverbs Correctly\t\tChoose the grammatically correct statement:"
		incorrect = adverb_mistakes.strip().split("\n")
		random.shuffle(incorrect)

		for x in range(4):
			if x==0:
				s+="\t%s" % random.choice(adverb_corrections.strip().split("\n"))
			else:
				s+="\t%s" % incorrect[x-1]
		s+="\n"
	return s

def id_adverb_errors():
	s=""	
	for key,value in adverb_mistakes_dict.items():
		choices= [k for k in adverb_mistakes_dict if k!=key]
		random.shuffle(choices)
		s+="Finding Adverb Mistakes\tIdentify the kind of grammatical mistake in the following sentence:\t"
		s+="%s\t%s\t%s\t%s\t%s\t\n" % (random.choice(value),key,choices[0],choices[1],choices[2])
	return s

def make_packet(number=1):
	for i in range(number):
		s=""
		s+=good_bad_adv()
		#s+=good_bad_adv()
		#s+=very_mistakes()
		s+=get_adverb_common_mistakes()
		s+=id_adverb_errors()
		#s+=id_adverb_errors()
	return s

#print make_packet()
