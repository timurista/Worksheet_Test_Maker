from question import make_packets
def make_packet(n=1):
	return make_packets(n,qdict = {
	"all prepositions are underlined":[
	"<u>Out</u> <u>of</u> the frying pan and <u>into</u> the fire.",
	"<u>Beneath</u> the fire is <u>where</u> I will find the treasure.",
	"<u>Along</u> the way we found that life can be wonderful <u>since</u> it is so wonderful.",
	"<u>Outside</u> <u>of</u> the stadium and <u>before</u> the start of the next match, John and Jill plan their revenge.",
	"<u>Before</u> they discovered the remains <u>of</u> the hero, they saw a birght light blaze <u>across</u> the sky.",
	"<u>Against</u> the dock, the ship sat dead <u>in</u> the water.",
	"<u>Outside</u> the school the students found the turtle <u>off</u> the table and <u>underneath</u> the dresser.",
	],
	"not all prepositions are underlined":[
	"Out <u>of</u> the frying pan and <u>into</u> the fire.",
	"<u>Out</u> <u>of</u> the frying pan and into the fire.",
	"Out <u>of</u> the frying <u>pan</u> and <u>into</u> the fire.",	
	"Beneath the <u>fire</u> is where I <u>will</u> find the treasure.",
	"<u>Beneath</u> the fire is where I <u>will</u> find the treasure.",
	"<u>Outside</u> of the stadium and <u>before</u> the start of the next match, John and Jill plan their revenge.",
	"<u>Against</u> the dock, the ship sat dead in the water.",
	"<u>Outside</u> the school the students found the turtle off the table and <u>underneath</u> the dresser.",
	"Outside the school the students found the turtle off the table and <u>underneath</u> the dresser.",
	"<u>Outside</u> the school the students found the turtle <u>off</u> the table and underneath the dresser.",
	],
	},
	qsection="Prepositional Phrases")

if __name__=="__main__":
	print "testing..."
	print make_packet(5)

"""
Which of the following are prepositions in the sentence below:
Before the concert, Manny and Margaret ate dinner at the Italian restaurant across the street.
Before, ate, at, across
Before, ate, at
Before, at, across
at, across
"""

preps = ['aboard', 'as', 'in', 'out', 
'toward', 'about', 'at', 'by', 'inside', 
'outside', 'under', 'above', 'before', 
'concerning', 'into', 'over', 'underneath', 
'across', 'behind', 'despite', 'like', 'past', 
'until', 'after', 'below', 'down', 'near', 
'pending', 'unto', 'against', 'beneath', 
'during', 'of', 'regarding', 'up', 'along', 
'beside', 'except', 'off', 'since', 'upon', 
'amid', 'besides', 'excepting', 'on', 'through', 
'with', 'among', 'between', 'for', 'onto', 
'throughout', 'within', 'around', 'beyond', 
'from', 'opposite', 'to', 'out']
#print preps