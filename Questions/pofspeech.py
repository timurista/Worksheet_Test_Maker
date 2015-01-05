"""parts of speeech"""
from question import make_packets

def make_packet(n=1):
	return make_packets(n, qdict={
		"adjective underlined":[]
		"adverb underlined":[]
		"preposition underlined":[]
		"noun underlined":[]
		},qsection="Parts of Speech Identification")

