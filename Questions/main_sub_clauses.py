# -*- coding: utf-8 -*-
"""main subordinate clauses"""
from question import make_packets
def make_packet(n=1):
	return make_packets(n,qdict={
		"subordinate clause underlined":[
		"<u>While I chop the tree down</u>, will you bring in the wood?",
		"<u>After the storm cleared</u>, we found some lemons on the street.",
		"I know a girl <u>who sings in the chorus</u>.",
		"Jess is from a part of Italy <u>where few people speak English.</u>",
		"<u>When we arrived at the hotel</u>, we discovered that our reservation had been cancelled.",
		],
		"main clause underlined":[
		"<u>Jess is from a part of Italy</u> where few people speak English.",
		"<u>I know a girl</u> who sings in the chorus.",		
		"While I chop the tree down, <u>will you bring in the wood?</u>",
		"<u>After the storm cleared</u>, we found some lemons on the street.",
		"After the storm cleared, <u>we found some lemons on the street</u>.",
		"When we arrived at the hotel, <u>we discovered that our reservation had been cancelled</u>.",		
		],		
		"neither main or subordinate clause underlined":[
		"While <u>I chop the tree down</u>, will you bring in the wood?",
		"While I <u>chop the tree down</u>, will you bring in the wood?",
		"<u>While</u> I jumped for joy, the frog <u>lept for encouragment</u>.",
		"After <u>the storm cleared</u>, we found some lemons on the street.",
		"After <u>the storm cleared</u>, we <u>found some lemons</u> on the street.",
		"I know <u>a girl</u> who sings in the chorus.",
		"I know a girl <u>who</u> sings in the chorus.",
		"Jess is from a part of Italy <u>where</u> few people speak English.",		
		"Jess is from a part of Italy <u>where</u> few people speak English.",
		"Jess is <u>from a part of Italy</u> where few people speak English.",
		"Jess is from a part of Italy where <u>few people speak English</u>.",
		"Jess is from a part of Italy <u>where</u> few people speak English.",		
		"When we arrived at the hotel, we <u>discovered that our reservation had been cancelled.</u>",
		"<u>When</u> we arrived at the hotel, we discovered that our reservation had been cancelled.",
		],
		},qsection="Main vs Subordinate clause")

if __name__ == "__main__":
	print "testing..."
	print make_packet(3)
