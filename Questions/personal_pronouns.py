from question import make_packets
"""personal_pronouns"""
def make_packet(n=1):
	return make_packets(n,qdict={
		"Correct Personal Pronoun Used":[
		"Someone must sit near me.",
		"We want a new kite.",
		"The kitten followed us.",
		"The principal presented Tom and me awards.",
		"My father and I refinished an old cart.",
		"The applicants for that job were Frank and I.",
		"Who bought them a magazine?",
		"Rosa asked them a question.",
		"My partner and I agreed to meet at six o'clock.",
		"Our best actors are Cliff and she.",
		"Someone gave us a new picture.",
		"The cat scratches her nearly every day",
		"Did anyone discuss the subject with him?",
		"Great Grandpa sent them airplane tickets to Seattle.",
		"Will you take me to Hong Kong?",
		],
		"Incorrect Personal Pronoun Used":[
		"Someone must sit near I.",		
		"Us want a new kite.",
		"The kitten followed we.",
		"The principal presented Tom and me awards.",
		"My father and me refinished an old cart.",
		"The applicants for that job were Frank and me.",
		"Who bought they a magazine?",
		"Rosa asked they a question.",
		"My partner and me agreed to meet at six o'clock.",
		"Our best actors are Cliff and her.",
		"Someone gave we a new picture.",
		"The cat scratches she nearly every day",
		"Did anyone discuss the subject with he?",
		"Great Grandpa sent they airplane tickets to Seattle.",
		"Will you take I to Hong Kong?",
		],				
		}, qsection="Pronoun Use")

if __name__=="__main__":
	print "testing"
	print make_packet(10)
