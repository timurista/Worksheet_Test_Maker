from question import Question, Packet
"""
Identify the sentence type.
When do you want to go to lunch?
interrogative
declarative
exclamatory
imperative
Correct answer: A
P/PBR/HME: 0.9298999999999999 / 0.3952 / E
"""
def make_packet(number=1):
	qdict = {
		"interrogative":[
		"Where did she go?",
		"Where did you find that?",
		"What time is it?",
		"What does she know about me?",
		"What do they know about the subject?",
		"What do they think about the subject?",
		"Who showed me that yesterday?",
		"How did she do it in the morning?",
		"How did they dsicover the problem last night?",
		"When do you want to go to dinner?",
		],
		"declarative":[
		"She was always a lovely person.",
		"There was nothing wrong with him.",
		"There were no problems with them.",
		"Everyone loved him like a son.",
		"I love chocolate cake.",
		"Lee has never caught a decent bass.",
		"It was like a million voices suddenly cired out in terror.",
		"Only a Sith Lord deals in absolutes.",
		"These aren't the droids your looking for.",
		"No one can hear you scream in space.",
		],
		"exclamatory":[
		"This is the best cake ever!",
		"We love all that you do for us!",
		"This is the best trip!",
		"The Beatles are the best band in all history!",
		"Our treats are the best!",
		"Jeepers! You scared the life out of me!",
		"I'm really going to miss this place!",
		"No one can hear you scream now!",
		],
		"imperative":[
		"Go to the store and buy some socks.",
		"Get your brother some ice-cream!",
		"Get yourselves something nice for Christmas.",
		"Get into that dress now!",
		"Go try on some of those old clothes.",
		"Fish somewhere else!",
		"Please find someplace else to go.",
		"Get clothes for us now!",
		"Get ready for the exam!",
		"Try and be polite please.",
		"Make sure you have friends for this activity.",
		"Make sure its prepared.",
		],
	}
	return Packet([Question(q,qdict=qdict,qprompt="Identify the kind of sentence below:",
		qsection="Kind of Sentence"
		) for q in qdict]).make_packet(number)

if __name__ == "__main__":
	print "testing..."
	print make_packet(4)

