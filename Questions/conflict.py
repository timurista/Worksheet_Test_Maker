conflict_dict ={
	"man vs self":[
	"Here a character struggles to overcome fear, addiction, emotional damage or other crippling personal issue.",
	"the following is an example: a doctor is driven mad by his feelings of guilt after his creation murders his lover.",
	"the following is an example: the protagonist has an inner struggle in his/her mind",
	"the following is an example: After lowering himself into the damp and dark cave Tom began to reprimand himself for not having replaced his flashlight batteries.",
	"the following is an example: Coming to a new planet, the alien struggled to fit and adapt to the new culture while remaining true to herself.",
	"the following is an example: Batman has to struggle with either saving his love interest or saving the city.",
	"Is defined as a character having conflicting desires, thoughts or motivations",
	],
	"man vs nature":[
	"This pits a story's main character or characters against a natural force such as a flood, predatory animal, or disease epidemic.",
	"the following is an example: Captain Ahab must capture a great white whale named Moby Dick.",
	"the following is an example: Two doctors must race against time to stop the spread of a deadly plague.",
	"the following is an example: A few scientists must work to stop an asteroid from hitting the earth.",
	"the following is an example: A captain must guide his ship through a dangerous storm.",
	"the following is an example: A local ranger must stop a group of wolves from terrorizing the village.",
	],
	"man vs society":[
	"In this example the protagonist battles an unjust element of government or culture.",
	"the following is an example: Jonas must face the harsh rules of his community.",
	"the following is an example: Katniss challenges the injustice of the Hunger Games.",
	"the following is an example: A soldier tries to change the political system but discovers a larger conspiracy.",
	"the following is an example: A hero learns that his government has lied to its' citizens and is trying to supress the truth.",
	"the following is an example: A sniper tries to expose the evil practices of government officials.",
	"the following is an example: A criminal is brought to justice and must face the court system.",
	],
	"man vs man":[
	"This pits the protagonist directly against another character with apparently opposing aims.",
	"the following is an example: Batman faces the Joker.",
	"the following is an example: the plumber Mario fights Bowser for the Princess Toad.",
	"the following is an example: Harry Potter battles against his nemesis Lord Voldemort.",
	"the following is an example: John and Jill have an argument over who is going to do the dishes.",
	"the following is an example: A talking dog joins the humans in driving a small little bird named Tweety from his home.",
	],
}
false_types = ["man vs alien","man vs other self","man vs the world","man vs everything"]

types = conflict_dict.keys()

import random

def identify_conflict():
	s=""
	for key,value in conflict_dict.items():
		s+="Conflict Examples\tThe following is a true statement about what kind of conflict? (there may be none or more than one)\t%s\t" % random.choice(value).capitalize()
		choices = [x for x in conflict_dict.keys() if x!=key]
		s+=	"%s\t%s\t%s\t%s\n" % (key, choices[0],choices[1],choices[2])
	return s

def make_packet(number=1):
	s=""
	random.shuffle(types)
	random.shuffle(false_types)
	correct = types[:random.randrange(0,4)]
	choices = correct+false_types
	#print choices
	s+= 'Conflict\t\tIdentify the correct type(s) of conflict (there can be none or more than one):\t'+'\t'.join(choices[:4])+"\n"
	for x in range(number):
		#s+=identify_conflict()
		for key,value in conflict_dict.items():
			possible= [l for x in conflict_dict.values() for l in x if x!=value]
			random.shuffle(value)
			correct = value[0]
			random.shuffle(possible)
			choices = [x for x in possible if x!=value]
			#print key, types
			s+="Identify the Kind of Conflict\t\tWhich of the following is true of this kind of conflict: %s\t %s\t" % (key,correct)+'\t'.join(choices[:3])
			s+="\n"
	return s
print make_packet()