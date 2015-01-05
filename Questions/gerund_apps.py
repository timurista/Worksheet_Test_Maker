# # -*- coding: utf-8 -*-
from random import choice, randrange,shuffle
import re

def get_participle_phrase():
	participle_phrases = {
		"s_subj":["Bullroarer","the white wizard","Jonas","Asher","Fiona","Belladonna"],
		"p_subj":["those creeps","men","humans","alien creatures","children","hobbits",],
		"s_verb":["likes","enjoys","is disgusted by","is repulsed by","hates","relishes","appreciates","fancies","revels in","adores","dislikes"],
		"p_verb":["like","enjoy","are disgusted by","are repulsed by","hate","relish","appreciate","fancy","revel in","adore","dislike"],
		"participle":["refined","running","enlightening","starving","hard-working","twisted"],
		"do":["toys","evil men","children","unfortunate souls","happy kids","sad kids"],
		"phrase":["walking on the beach","eating the leftover pizza","running home","tired from the long journey"],
		"s_passive":["is hated by","is enjoyed by","is disliked by","is relished by"],
		"prep":["today","on the eve of battle","in the spring","this morning","at midnight","in the fall","in the winter"],
	}
	if choice([0,1]):
		subj = choice(participle_phrases["p_subj"])
		verb = choice(participle_phrases["p_verb"])
	else:
		subj = choice(participle_phrases["s_subj"])
		verb = choice(participle_phrases["s_verb"])
		
	prep = choice(participle_phrases["prep"])
	do = choice(participle_phrases["do"])

	switch = choice([0,1,2,3])
	if switch==0:
		participle = "<u>"+choice(participle_phrases["phrase"])+"</u>"
		return "%s %s %s %s." %(subj.capitalize(),verb,do,participle)
	elif switch==1:
		participle= "<u>"+choice(participle_phrases["participle"])+"</u>"
		return "%s, %s %s %s %s." %(prep.capitalize(),subj,verb,participle,do)
	elif switch==2:
		participle = "<u>"+choice(participle_phrases["phrase"])+"</u>"
		return "%s %s %s %s %s." %(subj.capitalize(),verb,do,participle,prep)	
	else:
		participle = "<u>"+choice(participle_phrases["phrase"])+"</u>"
		return "%s, %s %s %s." %(participle[:3]+participle[3].capitalize()+participle[4:],subj,verb,do)



def get_gerund_phrase():
	gerund_phrases = {
		"s_subj":["Bullroarer","the white wizard","Jonas","Asher","Fiona","Belladonna"],
		"p_subj":["those creeps","men","humans","alien creatures","children","hobbits",],
		"s_verb":["likes","enjoys","is disgusted by","is repulsed by","hates","relishes","appreciates","fancies","revels in","adores","dislikes"],
		"p_verb":["like","enjoy","are disgusted by","are repulsed by","hate","relish","appreciate","fancy","revel in","adore","dislike"],
		"gerund":["eating","quitting","skating","recycling","terrorizing","barking"],
		"phrase":["eating healthy foods","recycling unused paper",
		"saving the environment","constant bickering","painting the barn",
		"learning the secrets of Mordor","finding friends",
		"fleeing from enemies","capturing innocent civilians"],
		"phrase_at_end":["the creatures' loud yelling",
		"the man's constant shouting"],
		"s_passive":["is hated by","is enjoyed by","is disliked by","is relished by"],
		"prep":["today","on the eve of battle","in the spring","this morning","at midnight","in the fall","in the winter"],
	}
	if choice([0,1]):
		subj = choice(gerund_phrases["p_subj"])
		verb = choice(gerund_phrases["p_verb"])
	else:
		subj = choice(gerund_phrases["s_subj"])
		verb = choice(gerund_phrases["s_verb"])

	c = choice([0,1,2,3])
	if c==0:
		gerund = "<u>"+choice(gerund_phrases["phrase"])+"</u>"
	elif c==1: 
		gerund = "<u>"+choice(gerund_phrases["gerund"])+"</u>"
	else:
		c = choice(gerund_phrases["gerund"]).split()
		gerund = ' '.join(c[:-1])+"<u>"+c[-1]+"</u>"

		
	prep = choice(gerund_phrases["prep"])

	switch = choice([0,1,2,3])
	if switch==0:
		return "%s %s %s." %(subj.capitalize(),verb,gerund)
	elif switch==1:
		return "%s, %s %s %s." %(prep.capitalize(),subj,verb,gerund)
	elif switch==2:
		return "%s %s %s %s." %(subj.capitalize(),verb,gerund,prep)	
	else:
		verb = choice(gerund_phrases["s_passive"])
		return "%s %s %s." %(gerund[:3]+gerund[3].capitalize()+gerund[4:],verb,subj)

def appositives():
	apps = {
	"app_phrases":[
	"a dancer in her own right","a hard-working student",
	"a humanitarian","the class clown","a quicker learner",
	"a well-versed student","a smart cookie",
	],
	"subj":["John","Jill","Mariel","Jerome"],
	"pred":["watched the special dance",
	"visited the hospital", 
	"took care of the sick",
	"fed the crowd","healed the dying","clothed the sick","robbed the poor",
	"robbed the rich"],
	"app_noun":["Molly","Dr Jimenez"],
	"subj2":["the fish","the learned scholar","my dog","my cat"],
	"pred2":["watched the special dance","visited the hospital", "took care of the sick",
	"fed the crowd"],
	"prep":["today","on the eve of battle","in the spring","this morning","at midnight","in the fall","in the winter"],

	}
	switch = choice([0,1,2])
	if switch==0:
		return "%s <u>%s</u> %s." %(choice(apps["subj2"]).capitalize(),
			choice(apps["app_noun"]),choice(apps["pred2"]))
	elif switch==1:
		return "%s, <u>%s</u>, %s." %((choice(apps["subj"]).capitalize(),
			choice(apps["app_phrases"]),choice(apps["pred"])))
	else:
		return "%s, %s, <u>%s</u>, %s." %(choice(apps["prep"]).capitalize(),choice(apps["subj"]),
			choice(apps["app_phrases"]),choice(apps["pred"]))
	


def create_gp_question(number=1):
	s=""
	for x in range(number):
		if choice([0,1]):
			s+="Kind of Phrase\t\tIdentify the correct <u>%s</u> in the following sentence (there can be more than one):" % "gerunds or gerund phrases"
			choices = [get_gerund_phrase() for x in range(randrange(0,4))]+[appositives() for x in range(4)]
			s+="\t%s\t%s\t%s\t%s\t" % (choices[0],choices[1],choices[2],choices[3])
		else:
			s+="Kind of Phrase\t\tIdentify the correct <u>%s</u> in the following sentence (there can be more than one):" % "appositive or appositive phrases"
			choices = [get_gerund_phrase() for x in range(randrange(0,4))]+[appositives() for x in range(4)]
			s+="\t%s\t%s\t%s\t%s\t" % (choices[0],choices[1],choices[2],choices[3])
		s+="\n"
	return s

def create_group_questions():
	s=""
	key_dict = {
	"gerund or gerund phrase":"get_gerund_phrase",
	"participle or participle phrase":"get_participle_phrase",
	"appositive or appositive phrase":"appositives"}
	for key,func in key_dict.items():
		correct= eval(func).__call__()
		incorrect = [eval(f).__call__() for f in key_dict.values()*2 if f!=func]
		s+="Kind of Phrase\t\tIdentify the <b>%s</b> in the phrase below:" % key
		s+="\t%s\t%s\t%s\t%s\n" % (correct,incorrect[0],incorrect[1],
			incorrect[2])
	return s
#print create_group_questions()
#print create_gp_question()

def create_gerrund_question():
	question =""
	old_sent = get_gerund_phrase()
	correct = re.findall("<u>(.+(?:</u>)[.?!]?)",old_sent)
	sent = re.sub("</*u>","",old_sent)
	#print correct
	c = correct[0].replace("</u>","")
	words = c.split()
	wrong = ""
	if len(words)>1:
		idx = randrange(1,len(words))
		#print idx
		if choice([0,1]):
			wrong= ' '.join(words[idx:])
		else:
			wrong= ' '.join(words[:idx])

	choices = [x for x in sent.split()]
	n2 = [' '.join(choices[i:i+2]) for i in range(len(choices)-1)]
	n3 = [' '.join(choices[i:i+3]) for i in range(len(choices)-1)]
	all_choices = list(set([x for x in choices+n2+n3 if x!=wrong or x!=c and bool(x)]))
	#print "CHOICES",choices
	shuffle(all_choices)
	question = "Identify the gerund phrase"
	if not wrong:
		incorrect= all_choices[:3]
	else:
		incorrect= [wrong]+all_choices[:2]
	#print incorrect,sent
	#print correct[0],incorrect[0]
	#print "LEN INCORRECT",len(incorrect)
	question+="\tIdentify the correct words to complete a gerund or gerund phrase in the following sentence:\t%s\t%s\t%s\t%s\t%s" % (sent,c,incorrect[0],incorrect[1],incorrect[2])
	#print question
	return question

def make_packet(number=1):
	s=""
	for x in range(number):
		#s += create_gp_question()
		s+=create_group_questions()
		s+= create_gerrund_question()+"\n"
	return s

print make_packet(5)
#print get_gerund_phrase()
#print appositives()
# We went to the movie at the last minute.
# Which of the barbells is heavier?
# Melissa earned the money for her new dress.
# When Jo forgot her key, she knocked on the window.
# The boy in the red jacket plays on my soccer team.
# The doctor told him that joining the track team would be healthful for him.
# She was taught table manners at a young age.
# We found sticky paw prints on the kitchen floor.
# Let’s meet the new coach at four o’clock.
# Bill hit the ball into the bleachers.
# Each of the girls wanted some pizza.
# The computer in the lab was used frequently.
# The school band performed during the half-time show.
# Did you pass your driving test with flying colors?
# At the museum we saw paintings and sculptures.

# Identify the prepositional phrase
# My sister took her books off the table at dinnertime.
# At the party, we met students who did not go to our school.
# Which of the movies is your favorite?
# Tim sat motionless for a long time.
# We ran toward the water when we reached the beach.
# Sheila always gets nervous before a performance.
# Inside the auditorium people talked loudly until the end of the show.
# I ran around the table and hid beneath the chair.
# Sue promised me her recipe for stew.
# Cheers filled the stadium throughout the football game.
# Would you rather live in Alaska or in Africa?
# By two o’clock on the day of the bake sale, all of the cookies had been sold.
# Derek looked behind the garage and saw his roller skates.
# The four of us swam laps in the pool after school.
# We laughed at the joke, though it wasn’t very funny.
# Marty proved she could compete against any member of the other team.
# Did you travel by car or by train?
# The students were encouraged in their efforts.
# The parking garage below the mall is always full.
# He studies hard, and his grades are always above the average.
# """
