from random import choice, randint
from worksheet_maker import Worksheet

p_phrase = """
in the morning
in the afternoon
at the end of the day
during school hours
outside the school
after hours
after the snowstorm
at lunch
during the beginning of the class
in the middle of the lesson
by the entrance to the restaurant
by the post office
by the shopping mall
by the cactus
away from the cacti
after the movies
outside the building
with a smile
with a frown
with a smirk
in the evening
at noon
at midnight
at twilight
during the rainstorm
during the monsoon
after the monsoon
after the big freeze
with an air of confidence
"""

s_nouns = """
the legendary Hyrulean Link
the cunning Samus
the dangerous master Toad
the sleek ninja
the speedy Sonic
the first-year student
a boy
the wizard Dumbeldore
the wizard girl Hermione
the boy Harry
the boy John
the student named Tom
his mother
her mother
their mother
his friend
his friend's sister
the girl
the dark lord Voldermort
the man
a small man
the teacher
a short boy
a tall boy
the Giver
a zombie
a scrawny little girl
a robust and powerful girl
the sith lord Vader
the Jedi knight Obi-Wan
the girl
the boy
the teacher
the space-pirate Han
the hairy beast Chewbacca 
the legendary Jedi master Yoda
the rebel fighter
the imperial stormtrooper
the zombie
the young girl Fiona
the eleven-year old boy Jonas
the esteemed princess Leia
an orange-colored banana
Bilbo's friend
the Receiver
the adventurer
the powerful Superman
the cunning Batman
the great and powerful OZ
the blood-thirsty vampire
the scrawny Aladin
the wise Elder
the plumber Mario
the other plumber Luigi
the princess Peach
the sullen King Koopa
the quirky captain Falcon
"""

s_ios = """
a boy
Dumbeldore
Hermione
Harry
John
Tom
my mother
my friend's sister
her
him
the teacher
a short boy
a tall boy
the Giver
Jonas
a zombie
a scrawny little girl
a robust and powerful girl
Vader
Obi-Wan
Luke
Leia
Fiona
Bilbo
Gandalf
John
Jerry
Superman
Batman
Sonic
Zelda
Link
Mario
Luigi
Riddler
Joker
"""

adj_pphrase = """
with happiness inside
with medicine inside
with water inside
with children's laughter inside
from the dragon's layer
of the finest quality
of the strongest soldier
of the strongest material
of the greatest strength
from my room
from my grandmother
from the store
from the pharmacy
from the doctor
from the local healer
from the purest land
with golden pieces inside
at the back
along the side
amid the crowd
behind the door
beside the table
below the desk
opposite the door
outside the room
on the eve of battle
in the morning
on the morrow
"""

d_object = """
a note
a letter
a gigantic box
the glittering treasure
an artifact
a tiny little bottle
a bottle
a large container
a pokeball
a lightstaber
a twinkie
a small magical wand
a book
the red pill
a book
some magic
a red-feathered hat
two bottles
three bottles
two candlesticks
a new swimsuit
"""

s_verbs = """
gave
brought
sent
sold
threw
procured
delivered
bought
showed
"""

l_verbs ="""
seemed
appeared
looked
felt
remained
became
proved
looked
stayed
"""

# rejects = grew, turned needs l_verbs_adj and l_verbs_nom

n_verbs = """
named
considered
thought
elected
pronounced
proclaimed
called
"""

object_complement = """
"The Fabulous"
the silly speaker
the happy lord
the sad hero
the angry villian
a great friend
the absolute ruler
the greatest lord
the supreme authority
the troubled youth
the depressed soul
the distraught soul
a fascinating person
the helper
the triumphant
the joyous
"""

adjectives = """
sullen
moody
cheerful
upset
peevish
excited
indifferent
happy
peaceful
"""

nominatives = """a king
a lord
the powerful Jedi
a more dark and powerful wizard
a commander
a fallen hero
a worthless child
a scared child
a sad child
a happy child
a happy sight
the greatest hero
a warrior
"""

adverbs ="""quickly
slowly
more hastily
more quickly
hastily
calmly
gently
distractedly
hurriedly
angrily
quietly
loudly
disgustingly
"""

complete_predicate="""
ran into the store
threw the cone away
met Sally for dinner at the local coffe shop
came home
went away
traveled a long distance
jumped for joy
ran all the way home
found a key to unlock the treasure
discovered something amazing
found a friend and a life-long partner
discovered an enemy in his home
looked into the window
saw both the end and the beginning of the world
gave a lightsaber and a blaster to his friend
"""

compound_complete_predicate="""ran into the store and walked to the cash register
jumped and celebrated all the accomplishments
boasted and claimed victory
found the car and spent the night inside
walked into the gas station and bought a twinkie
drove home and discovered the front door was open
looked into the window and stood shocked by the horrific scene
gazed up at the night sky and wondered
walked into the grocery store and bought a hundred snickers
ran into the Costco s and purchased a slice of pizza
jumped and celebrated all the wondeful flavors of icecream
"""

compound_complete_subj = """the two boys and their dad
Darth Vader and Luke Skywalker
Obi-Wan and his friend
the Giver and Jonas
Fiona and Jonas
Gabriel and Jonas
John and Tom
Tom and Jerry
the little boy and the little girl
Batman and Robin
Superman and Batman
Lex Luthor and Superman
Wolverine and Professor X
Toad and Mario
Mario and Luigi
Princess Peach and Bowser
Link and Zelda
Han Solo and Chewbacca
"""

participle_adj = """a leading hero
a celebrated champion
a renowned teacher
a hated villian
"""

participle_phrases = """growing up alone
being awesome
rejected by others
accepted by all
feared by all
continuing to play
crouching hurriedly
"""


pphrases = p_phrase.strip().splitlines()
subjs = s_nouns.strip().splitlines()
ios =s_ios.strip().splitlines()
dos = d_object.strip().splitlines()
verbs = s_verbs.strip().splitlines()
advs =adverbs.splitlines()
ocs = object_complement.strip().splitlines()

def get_io():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(verbs)
	pp = choice(pphrases)
	adv = choice(advs)
	io = choice(ios).split(" ")
	# get last letter in io
	if len(io)>1:
		io = ' '.join(io[:-1])+" <u>"+io[-1]+"</u>"
	else: io = "<u>"+''.join(io)+"</u>"
	do = choice(dos)
	if i==1:
		s= "{}, {} {}{} {} {}.".format(pp.capitalize(),subj,adv+" ",verb,io,do)
	elif i==2:
		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do)
	else:
		s= "{} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do,pp)
	return s

def get_do():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(verbs)
	pp = choice(pphrases)
	adv = choice(advs)
	io = choice(ios)
	do = choice(dos).split(" ")
		# get last letter in do
	if len(do)>1:
		do = ' '.join(do[:-1])+" <u>"+do[-1]+"</u>"
	else: do = "<u>"+''.join(do)+"</u>"

	if i==1:
		s= "{}, {} {}{} {} {}.".format(pp.capitalize(),subj,adv+" ",verb,io,do)
	elif i==2:
		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do)
	else:
		s= "{} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do,pp)
	return s

def get_pa():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(verbs)
	pp = choice(pphrases)
	adv = choice(advs)
	io = choice(ios)
	do = choice(dos)
	pa = "<u>"+choice(adj_pphrase.strip().splitlines())+"</u>"

	# get last letter in oc
	if i==1:
		s= "{}, {} {}{} {} {}.".format(pp.capitalize(),subj,adv+" ",verb,do,pa)
	elif i==2:
		s= "{} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do,pa)
	else:
		s= "{} {} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do,pa,pp)
	return s

def get_padv():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(verbs)
	pp = "<u>"+choice(pphrases)+"</u>"
	adv = choice(advs)
	io = choice(ios)
	do = choice(dos)
	pa = choice(adj_pphrase.strip().splitlines())

	# get last letter in oc
	if i==1:
		s= "{}, {} {}{} {} {}.".format(pp[:3]+pp[3].upper()+pp[4:],subj,adv+" ",verb,do,pa)
	elif i==2:
		s= "{}, {}, {} {} {}.".format(subj[0].capitalize()+subj[1:],pp,verb,io,do,pa)
	else:
		s= "{} {} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,do,pa,pp)
	return s

def get_oc():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(n_verbs.strip().splitlines())
	pp = choice(pphrases)
	adv = choice(advs)
	io = choice(ios)
	do = choice(dos)

	# get last letter in oc
	oc = choice(ocs).split(" ")
	if len(oc)>1:
		oc = ' '.join(oc[:-1])+" <u>"+oc[-1]+"</u>"
	else: oc = "<u>"+''.join(oc)+"</u>"

	if i==1:
		s= "{}, {} {}{} {} {}.".format(pp.capitalize(),subj,adv+" ",verb,io,oc)
	elif i==2:

		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,oc)
		#print "OC",oc,s
	else:
		s= "{} {} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,io,oc,pp)
	return s


def get_pred_adj():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(l_verbs.strip().splitlines())
	pp = choice(pphrases)
	adv = choice(advs)
	do = "<u>"+choice(adjectives.strip().splitlines())+"</u>"

	if i==1:
		s= "{}, {} {}{} {}.".format(pp.capitalize(),subj,adv+" ",verb,do)
	elif i==2:
		s= "{} {} {}.".format(subj[0].capitalize()+subj[1:],verb,do)
	else:
		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,do,pp)
	return s


def get_pred_nom():
	i = randint(0,3)
	subj= choice(subjs)
	verb = choice(l_verbs.strip().splitlines())
	pp = choice(pphrases)
	adv = choice(advs)
	do = choice(nominatives.strip().splitlines()).split(" ")

	# get last letter in oc
	oc = choice(ocs).split(" ")
	if len(do)>1:
		do = ' '.join(do[:-1])+" <u>"+do[-1]+"</u>"
	else: do = "<u>"+''.join(do)+"</u>"

	if i==1:
		s= "{}, {} {}{} {}.".format(pp.capitalize(),subj,adv+" ",verb,do)
	elif i==2:
		s= "{} {} {}.".format(subj[0].capitalize()+subj[1:],verb,do)
	else:
		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],verb,do,pp)
	return s

def get_compound_complete_predicate():
	i = randint(0,4)
	subj= choice(subjs)
	pp = choice(pphrases)
	pred = "<u>"+choice(compound_complete_predicate.strip().splitlines())+"</u>"
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {}.".format(pp.capitalize(),subj,pred)
	elif i==2:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,adv,pred)
	elif i==3:
		s= "{} {} {}.".format(subj[0].capitalize()+subj[1:],adv,pred)
	else:
		s= "{} {}.".format(subj[0].capitalize()+subj[1:],pred)
	return s

def get_simple_predicate():
	i = randint(0,4)
	subj= choice(subjs)
	pp = choice(pphrases)
	pred = choice(compound_complete_predicate.strip().splitlines()).split(" ")
	s_pred = "<u>"+pred[0]+"</u>"
	rest_pred = ' '.join(pred[1:])
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,s_pred,rest_pred)
	elif i==2:
		s= "{}, {} {} {} {}.".format(pp.capitalize(),subj,adv,s_pred,rest_pred)
	elif i==3:
		s= "{} {} {} {}.".format(subj[0].capitalize()+subj[1:],adv,s_pred,rest_pred)
	else:
		s= "{} {} {}.".format(subj[0].capitalize()+subj[1:],s_pred,rest_pred)
	return s

def get_compound_complete_subject():
	i = randint(0,4)
	subj= "<u>"+choice(compound_complete_subj.strip().splitlines())+"</u>"
	pp = choice(pphrases)
	pred1 = choice(compound_complete_predicate.strip().splitlines())
	pred2 = choice(complete_predicate.strip().splitlines())
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {}.".format(pp.capitalize(),subj,pred1)
	elif i==2:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,adv,pred2)
	elif i==3:
		s= "{} {} {}.".format(subj[:3]+subj[3].capitalize()+subj[4:],adv,pred1)
	else:
		s= "{} {}.".format(subj[:3]+subj[3].capitalize()+subj[4:],pred2)
	return s

def get_simple_subject():
	i = randint(0,4)
	full_subj = choice(s_nouns.strip().splitlines()).split(" ")
	if len(full_subj)<2:
		full_subj=["they say"]+full_subj
	simple_s = ["<u>"+full_subj[-1]+"</u>"]
	rest_s = full_subj[:-1]
	subj= ' '.join(rest_s+simple_s)
	pp = choice(pphrases)
	pred1 = choice(compound_complete_predicate.strip().splitlines())
	pred2 = choice(complete_predicate.strip().splitlines())
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {}.".format(pp.capitalize(),subj,pred1)
	elif i==2:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,adv,pred2)
	elif i==3:
		s= "{} {} {}.".format(subj[0].capitalize()+subj[1:],adv,pred1)
	else:
		s= "{} {}.".format(subj[0].capitalize()+subj[1:],pred2)
	return s

def get_complete_subject():
	i = randint(0,4)
	subj= "<u>"+choice(subjs)+"</u>"
	pp = choice(pphrases)
	pred1 = choice(compound_complete_predicate.strip().splitlines())
	pred2 = choice(complete_predicate.strip().splitlines())
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {}.".format(pp.capitalize(),subj,pred1)
	elif i==2:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,adv,pred2)
	elif i==3:
		s= "{} {} {}.".format(subj[0:3]+subj[3].upper()+subj[4:],adv,pred1)
	else:
		s= "{} {}.".format(subj[0:3]+subj[3].upper()+subj[4:],pred2)
	return s

def get_complete_subject():
	i = randint(0,4)
	subj= "<u>"+choice(subjs)+"</u>"
	pp = choice(pphrases)
	pred1 = choice(compound_complete_predicate.strip().splitlines())
	pred2 = choice(complete_predicate.strip().splitlines())
	adv = choice(adverbs.strip().splitlines())

	if i==1:
		s= "{}, {} {}.".format(pp.capitalize(),subj,pred1)
	elif i==2:
		s= "{}, {} {} {}.".format(pp.capitalize(),subj,adv,pred2)
	elif i==3:
		s= "{} {} {}.".format(subj[0:3]+subj[3].upper()+subj[4:],adv,pred1)
	else:
		s= "{} {}.".format(subj[0:3]+subj[3].upper()+subj[4:],pred2)
	return s

def get_participle_phrase():
	i = randint(0,4)
	subj= choice(subjs)
	pp = choice(pphrases)
	verb = choice(l_verbs.strip().splitlines())
	do = choice(nominatives.strip().splitlines())
	#adv = choice(adverbs.strip().splitlines())
	p_phrase1 = "<u>"+choice(participle_phrases.strip().splitlines()).capitalize()+"</u>"
	p_phrase2 = "<u>"+choice(participle_phrases.strip().splitlines())+"</u>"
	part_adj = "<u>"+choice(participle_adj.strip().splitlines())+"</u>"

	if i==0:
		s= "{}, {}, {}, {} {}.".format(pp.capitalize(),subj,part_adj,verb,do)
	elif i==1:
		s= "{}, {} {} {}.".format(p_phrase1,subj,verb,do)
	else:
		s= "{}, {}, {} {}.".format(subj[0].capitalize()+subj[1:],p_phrase2,verb,do)
	return s


def make_packet(questions=40):
	fns = {"indirect object":get_io,
			"direct object":get_do,
			"adjectival prepositional phrase":get_pa,
			"adverbial prepositional phrase":get_padv,
			"object complement":get_oc,
			"predicate nominative":get_pred_nom,
			"predicate adjective":get_pred_adj,
			"compound complete predicate":get_compound_complete_predicate,
			"simple predicate":get_simple_predicate,
			"simple subject":get_simple_subject,
			"compound complete subject":get_compound_complete_subject,
			"complete subject":get_complete_subject,
			"participle phrase":get_participle_phrase,
			}
	#length = (60/len(fns))
	#for x in range(length):
	i=0
	s=""
	while i<questions:
		all_keys = fns.keys()
		# 7%4 = 3, 1%4 = 1
		key = all_keys[i%len(all_keys)]
		#key = choice(fns.keys())
		choices = [x for x in fns.keys() if x!=key]
		s+= "Part of the Sentence\tChoose the best answer for the <u>underlined word</u> in the following sentence:"
		
		s+="\t{0}\t{1}\t{2[0]}\t{2[1]}\t{2[2]}\t".\
			format(
				fns[key](),key,choices)
		i+=1
		s+="\n"
	#print s
	return s
	

#print make_packet()
#Worksheet("practice questions 3",s.rstrip()).make_worksheet()