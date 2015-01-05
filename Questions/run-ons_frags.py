from question import make_packets
"""run-ons and fragments"""

def make_packet(n=1):
	return make_packets(n,qdict={
		"Run-on Sentence":[
			"I know the answer, I won't tell it to you.",
			"The trains are quicker the buses are less expensive.",
			"This is my repply I won't change my mind.",
			"Farnsworth likes to play two-square, his sister enjoys tag.",
			"We went to the store and we bought some bananas and we talked to our neighbor who just returned from his vacation.",
			"With winter approaching, I become more anxious about skiing, sledding is going to be fun too, I mostly like to ice skate on a frozen lake.",
			],
		"Fragment Sentence":[
			"After the students learned about the Aztecs of Mexico.",
			"Jerry during the winter storm.",
			"The room in the attic.",
			"On a cool damp morning.",
			"Suddenly, at the crack of dawn.",
			"Whenever I am lonely.",
			"Welcomed the visitors.",
			"Drew several pictures for us.",
			"Tomorrow.",
			],
		"Valid Sentence":[
			"He ran home and welcomed the visitors.",
			"On a cool, damp morning, I left to join the navy.",
			"Tomorrow, I will be going home.",
			"Bilbo found the dwarves to be very lonely at the end of their journey.",
			],
		}, qsection="Commmon Sentence Errors")

if __name__=="__main__":
	print "testing"
	print make_packet(5)