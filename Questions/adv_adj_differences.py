from question import make_packets
"""Differentiate Adjectives and Adverbs"""

def make_packet(n=1):
	return make_packets(n,qdict={
	"underlined word is an adjective":[
		"example1",
		"",],
	"underlined word is an adverb":[
		"example2"],
	},qsection="Narrative Point of View")

if __name__=="__main__":
	print "testing"
	print make_packet(1)
