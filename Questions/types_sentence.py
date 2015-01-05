from question import make_packets
"""types of sentences#2"""
def make_packet(n=1):
	return make_packets(n,qdict={
		"Simple Sentence":[
            "The stars fill the sky.",
			"I hear a cat hiss.",
			"Dwarves are known to be scared of the dark.",
			"Have you completed all your research on the dangers of smoking?",
            "At the end of the road near the hill is a modern gas station.",
			],
		"Compound Sentence":[
			"I know the main highways well, but I usually get lost on the side roads.",
			"We often visit the Poconos; sometimes, we stay a full week.",
			"I will attend or I will send someone.",
			"I prefer roomy American-made cars; my brother likes foreign models.",
			"Did you buy the cake today, or will you get it later?",
            "The plane landed, and the passengers left.",
			],
		"Complex Sentence":[
			"My older sister drives, but my younger one has yet to learn.",
			"When I travel to the Atlantic Provinces, I hope to visit Nova Scotia and New Brunswick.",
			"Since I left, the town has changed greatly.",
			"This is the book which I have been trying to get.",
            "Although the children found the letter, they couldn’t read it.",
			],
		"Compound-Complex":[
			"Since I am ready to begin, I will outline the project, and Ted will give you the details.",
			"My night school class is crowded now, but it will diminish in size as soon as winter comes.",
			"When  the  economic  situation  changes,  I  will  sell  my  old  house,  and  I  will  buy  another  closer  to  the city.",
            "The earth is bountiful; we may destroy it if we abuse it.",
			],
		}, qprompt="Identify the kind of sentence below:",qsection="Sentence Complexity and Type")

if __name__=="__main__":
	print "testing"
	print make_packet(5)