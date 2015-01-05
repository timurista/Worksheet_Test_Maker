from question import make_packets
"""15.6 - Narrative Point of View 1 115 MT 2.5 - identify"""

def make_packet(n=1):
	return make_packets(n,qdict={
	"Narrator":["example1"],
	"Author":["example2"],
	},qsection="Narrative Point of View")

if __name__=="__main__":
	print "testing"
	print make_packet(1)
