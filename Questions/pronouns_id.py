from question import make_packets
"""pronouns id"""
def make_packet(n=1):
	return make_packets(n,qdict={
		"Relative Pronoun":[
		"The cake <u>that</u> we baked was delicious.",
		"That day the sun, <u>which</u> covered over the entire planet, was blazing and very bright!",
		],
		"Intensive Pronoun":[
		"Freddie <u>himself</u> asked Julie out.",
		"The robot <u>itself</u> found a way to be happy among the humans.",
		],
		"Reflexive Pronoun":[
		"They psyched <u>themselves</u> up for the football game.",
		"The girls talked to <u>themselves</u> about the disturbing matter at school.",
		"They girls and boys joked with <u>themselves</u> about the incident at school.",
		],
		"Demonstrative Pronoun":[
		"<u>That</u> is a good idea!",
		"<u>Those</u> are my friends.",
		],
		"Personal Pronoun":[
		"<u>She</u> was very much appalled at the rude behavior of her classmates.",
		"During the night, <u>I</u> found the boy sitting near the fireplace.",
		],
		"Possessive Pronoun":[
		"She owned <u>her</u> own shop in the middle of the dragon lair and sold all manner of dragon-scaled trinkets.",
		"They found <u>their</u> ship to be in ruin after the storm.",
		"He did not fancy having <u>his</u> sword taken in the goblin's layer.",
		"Sarah and John missed their bus.",
		"<u>My</u> father and I haven't ever camped beside a river.",
		],
		"Idenfinite Pronoun":[
		"<u>Everyone</u> has already voted.",
		"<u>No one</u> should enter without knocking.",
		],
		"Interrogative Pronoun":[
		"<u>Which</u> is your choice?",
		"<u>With</u> whom were you playing video games?",
		],				
		}, qprompt="Identify the kind of pronoun underlined below:",qsection="Pronoun Identify")

if __name__=="__main__":
	print "testing"
	print make_packet(10)