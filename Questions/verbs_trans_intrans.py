from question import Packet,Question,sent_Question, make_packets

def make_packet(number=1):
	return make_packets(number,qdict={
		"transitive main verb":[
		"She <u>ate</u> a bag of chips for dinner.",
		"He <u>ate</u> a large stack of pancakes for breakfast.",
		"She <u>wore</u> a coat in the evening.",
		"They <u>wore</u> coats during the winter.",
		"All of them <u>ate</u> pie in the morning.",		
		"Brian <u>memorized</u> the opening line of his speech."
		],
		"intransitive main verb":[
		"She slept all day.",
		"She ran to the mall.",
		"He slept all day.",
		"In the evening, he slept all day",
		"All of them drove there during the day.",
		"The telephone <u>rings</u> in both offices."	
		],
		"linking main verb":[
		"She was a young girl.",
		"She looked the young teenager.",
		"They appeared tired after the long journey up the mountain.",
		"Milk  turns  bad  quickly  unless  refrigerated.",
		"His  forehead feels cool to the touch.",
		],
		"None of the above":[
		"She was helping her.",
		"He could have helped them.",
		"We will like to do it.",
		],
		},qprompt="In the following sentence, what is the verb type?")

if __name__=="__main__":
	print "testing..."
	print make_packet(10)


"""
Question 2

In the following sentence, what is the verb type?

linking

intransitive

transitive

none of the above

Correct answer: B
"""

