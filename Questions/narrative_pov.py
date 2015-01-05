from question import make_packets
"""15.6 - Narrative Point of View 1 115 MT 2.5 - identify"""

def make_packet(n=1):
	return make_packets(n,qdict={
	"First Person":[],
	"Third Person":[],
	"Objective Narrator":[],
	"Limited Narrator":[],
	"Omniscient Narrator":[],
	},qprompt="Identify the kind of narration used in the passage below:",qsection="Narrative Point of View")

if __name__=="__main__":
	print "testing"
	print make_packet(1)
