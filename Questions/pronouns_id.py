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
		"I <u>myself</u> am tired of doing homework.",
		"The president <u>himself</u> appeared at the rally.",
		"My sister made the bread <u>herself</u>.",
		],
		"Reflexive Pronoun":[
		"They psyched <u>themselves</u> up for the football game.",
		"The girls talked to <u>themselves</u> about the disturbing matter at school.",
		"They girls and boys joked with <u>themselves</u> about the incident at school.",
		"We bought <u>ourselves</u> pretzels at the fair.",
		"My brother made <u>himself</u> some dinner.",
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
		"Sarah and John missed <u>their</u> bus.",
		"<u>My</u> father and I haven't ever camped beside a river.",
		],
		"Idenfinite Pronoun":[
		"<u>Everyone</u> has already voted.",
		"<u>No one</u> should enter without knocking.",
		"That ice-cream was good. Can I have <u>another</u>?",
		"Can <u>anyone</u> answer this question?",
		"The doctor needs to know if you have eaten <u>anything</u> in the last two hours.",
		"<u>Each</u> has his own thoughts.",
		"Do you want tea or coffee? I don't mind. <u>Either</u> is good for me.",
		"<u>Enough</u> is enough.",
		"They have no house or possessions. They lost <u>everything</u> in the earthquake.",
		"<u>Little</u> is known about his early life.",
		"<u>All</u> is forgiven.",
		"<u>Few</u> have ever disobeyed him and lived.",
		"<u>Many</u> have come already.",
		"I'm sure that <u>others</u> have tried before.",
		"John likes coffee but not tea. I think <u>both</u> are good.",
		"<u>Some</u> have arrived tonight.",
		],
		"Interrogative Pronoun":[
		"<u>Which</u> is your choice?",
		"With <u>whom</u> were you playing video games?",
		],				
		}, qprompt="Identify the kind of pronoun underlined below:",qsection="Pronoun Identify")

if __name__=="__main__":
	print "testing"
	print make_packet(10)