from question import Question, Packet
from random import choice, shuffle

class verb_Question(Question):
 	def __init__(self,name,**kwargs):
 		Question.__init__(self,name,**kwargs)
		self.qsection = "Using Correct Verb Tense"
		self.qprompt = "Choose the correct verb to insert into the empty space"
# 		Question.__init__(self,examples,questions)

# 		
# 		self.all_types = []
# 		return Question.get_Question(self,"Verb Tense","Select verb tense that fits the sentence below")

"""
7.2.6 - Verb Tense 3 48 MT
3.3 -demonstrate
"""


"""
7.2.6.1 - Verb Tense - Past, Present, Future 0 48 MT
3.3 -demonstrate
"""

"""
7.2.6.2 - Verb Tense - Progressive 0 48 MT
3.3 -demonstrate
"""
"""
7.2.6.3 - Verb Tense - Perfect 0 48 MT 3.3 -demonstrate
"""

qdict = {
"perfect tense":[
"a","b","c"],
"progressive tense":[
"d","e","f"],
"past tense":[
"q","d","x"],	
"present tense":[
"x","h","j"],
"future tense":[
"p","g","i"],
}
s="""come coming came come
do doing did done
drive driving drove driven
give giving gave given
go going went gone
have having had had
know knowing knew known
say saying said said
see seeing saw seen
sing singing sang sung
speak speaking spoke spoken
tell telling told told
think thinking thought thought
write writing wrote written"""

qdict2 = {
"present participle":[
	"She is <u>coming</u> to the nearest gas station.",
	"She is <u>doing</u> that to the other house.",
	"They are <u>driving</u> a twinkie.",
	"She is <u>giving</u> to the shopping mall.",
	"My friends is <u>going</u> a job.",
	"I am <u>having</u> fun in the concert.",
	"Harry is <u>saying</u> he needs a job.",
	"Sally is <u>seeing</u> her to the nearest gas station.",
	"Everyone is <u>singing</u> about a twinkie.",
	"Harry is <u>speaking</u> to her.",
	"Bob is <u>telling</u> her about a new job.",
	"Citizens of the world are <u>thinking</u> about her.",
	"They are <u>writing</u> home.",
	"We are <u>coming</u> to I-HOP.",
	"Bob is <u>doing</u> this to her.",
	"Everyone is <u>driving</u> to them.",
	"The little hobbit is <u>giving</u> it to the other house.",
	"She is <u>going</u> to her.",
	"I am <u>having</u> fun at my job.",
	"Link is <u>saying</u> something about the other house.",
	"Harry is <u>seeing</u> my friend to I-HOP.",
	"The little hobbit is <u>singing</u> into the shopping mall.",
	"The white wizard is <u>speaking</u> at the concert.",
	"Link is <u>telling</u> us about his twinkie.",
	"Everyone is <u>thinking</u> about giving it to them.",
	"Mario is <u>writing</u> about his adventures in the nearest gas station.",
],
"past participle":[
	"I have <u>come</u> to the neighborhood.",
	"I have <u>done</u> nothing in the nearest gas station.",
	"We have <u>driven</u> them home.",
	"The white wizard had <u>given</u> something to them at home.",
	"Luigi had <u>gone</u> to the concert.",
	"My friends <u>had</u> her.",
	"The big troll had <u>known</u> about the other house.",
	"The white wizard had <u>said</u> something to her.",
	"The white wizard had <u>seen</u> a job posting.",
	"We had <u>sung</u> to the neighbor.",
	"He had <u>spoken</u> to the shopping mall clerk.",
	"She had <u>told</u> us about the concert.",
	"Link had <u>thought</u> about going to I-HOP.",
	"He had <u>written</u> a letter to the other house.",
	"She had <u>come</u> to her.",
	"I have <u>done</u> this to her.",
	"All the kings men had <u>driven</u> him to the nearest gas station.",
	"I had <u>given</u> it to the nearest gas station.",
	"She had <u>gone</u> to the nearest gas station.",
	"Luigi <u>had</u> it at the concert.",
	"Everyone had <u>known</u> her.",
	"The big troll had <u>said</u> something to the other house.",
	"Citizens of the world had <u>seen</u> a job posting.",
	"We had <u>sung</u> for home.",
	"He had <u>spoken</u> to the neighbor.",
	"Harry had <u>told</u> something to the neighbor.",
	"Citizens of the world had <u>thought</u> they wanted to own the other house.",
	"Mario had <u>written</u> to them.",
],
"base form":[
	"The white wizards <u>come</u> to the neighborhood.",
	"Link's men <u>do</u> it to I-HOP.",
	"Bob's men <u>drive</u> to them.",
	"The white wizards <u>give</u> it to the other house.",
	"The big trolls <u>go</u> to her.",
	"All the kings men <u>have</u> a job.",
	"The white wizards <u>know</u> how to get to the nearest gas station.",
	"My friends <u>say</u> hello to I-HOP.",
	"The big trolls <u>see</u> him to the nearest gas station.",
	"Citizens of the world <u>sing</u> of their home.",
	"They all <u>speak</u> about a job posting.",
	"The little hobbits <u>tell</u> it to them.",
	"All of them <u>think</u> about a twinkie.",
	"They <u>write</u> to the neighbor.",
	"Harry and his friends <u>come</u> to find a twinkie.",
	"All the kings men <u>do</u> that to her.",
	"The little hobbits <u>drive</u> to them.",
	"Luigi and Mario <u>give</u> it to I-HOP.",
	"The big trolls <u>go</u> buy a twinkie.",
	"All the women <u>have</u> to give it to them.",
	"They <u>know</u> how to get home.",
	"Sally and Suzy <u>say</u> good things to those in I-HOP.",
	"We <u>see</u> the boys to the nearest gas station.",
	"I <u>sing</u> about your job.",
	"We <u>speak</u> about your job.",
	"Harry and Hermione <u>tell</u> him about the nearest gas station.",
	"Luigi and Mario <u>think</u> something nasty about the nearest gas station.",
	"Sally and Suzy <u>write</u> a letter to a twinkie.",
],
"past form":[
	"The little hobbit <u>came</u> to the nearest gas station.",
	"She <u>did</u> not go to the neighbor.",
	"Sally <u>drove</u> to the shopping mall.",
	"Sally <u>gave</u> it to the nearest gas station.",
	"My friends <u>went</u> to her.",
	"They <u>had</u> something for the neighbor.",
	"Link <u>knew</u> about the neighbor.",
	"Link <u>said</u> goodbye to the shopping mall.",
	"Luigi <u>saw</u> a twinkie.",
	"Luigi <u>sang</u> a ballad inside the nearest gas station.",
	"She <u>spoke</u> kind words to those in the shopping mall.",
	"She <u>told</u> him about home.",
	"I <u>thought</u> about going to the shopping mall.",
	"The white wizard <u>wrote</u> to the other house.",
	"Link <u>came</u> to I-HOP.",
	"The big troll <u>did</u> something to the twinkie.",
	"The big troll <u>drove</u> to the other house.",
	"My friends <u>gave</u> her a home.",
	"My friends <u>went</u> to buy a twinkie.",
	"Citizens of the world <u>had</u> come to her.",
	"My friends <u>knew</u> about her job.",
	"The big troll <u>said</u> soemthing nasty to them.",
	"Link <u>saw</u> her.",
	"Bob <u>sang</u> to them.",
	"All the kings men <u>spoke</u> about home.",
	"She <u>told</u> it to them.",
	"The little hobbit <u>thought</u> about giving it to the neighbor.",
	"Citizens of the world <u>wrote</u> a long letter to the nearest gas station.",
],
}
#qdict2 = {'saying': ['We is _______ to the other house.', 'She is _______ to the neighbor.', 'They is _______ home.', 'She is _______ to her.', 'Harry is _______ to the neighbor.'], 'gone': ['All the kings men had _______ to the shopping mall.', 'Link had _______ to the concert.', 'She had _______ to the nearest gas station.', 'I had _______ to the neighbor.', 'My friends had _______ a job.'], 'doing': ['Luigi is _______ to I-HOP.', 'The little hobbit is _______ to the other house.', 'My friends is _______ to the neighbor.', 'Citizens of the world is _______ to her.', 'The big troll is _______ to I-HOP.'], 'telling': ['I is _______ to the neighbor.', 'We is _______ a twinkie.', 'Citizens of the world is _______ home.', 'My friends is _______ a twinkie.', 'He is _______ a job.'], 'say': ['All the kings men _______ to them.', 'She _______ to I-HOP.', 'The big troll _______ to the shopping mall.', 'Bob _______ to the neighbor.', 'He _______ to them.'], 'done': ['I had _______ to the nearest gas station.', 'Everyone had _______ to I-HOP.', 'Link had _______ a job.', 'They had _______ to her.', 'My friends had _______ to the other house.'], 'have': ['Mario _______ to them.', 'Sally _______ to the shopping mall.', 'I _______ home.', 'My friends _______ a twinkie.', 'I _______ to them.'], 'go': ['Citizens of the world _______ to the other house.', 'Link _______ to the other house.', 'They _______ to the neighbor.', 'My friends _______ to the concert.', 'Harry _______ to them.'], 'seen': ['My friends had _______ to the concert.', 'Harry had _______ to her.', 'He had _______ to I-HOP.', 'The big troll had _______ to the neighbor.', 'I had _______ to the concert.'], 'drove': ['She _______ to the neighbor.', 'She _______ to the shopping mall.', 'Luigi _______ a job.', 'He _______ to I-HOP.', 'Everyone _______ to the shopping mall.'], 'singing': ['Luigi is _______ to the other house.', 'They is _______ to the shopping mall.', 'He is _______ a job.', 'He is _______ to them.', 'Luigi is _______ to the concert.'], 'sung': ['We had _______ home.', 'Mario had _______ to them.', 'She had _______ to the nearest gas station.', 'We had _______ to the shopping mall.', 'They had _______ home.'], 'speak': ['All the kings men _______ a job.', 'All the kings men _______ to the concert.', 'We _______ to I-HOP.', 'Citizens of the world _______ to the shopping mall.', 'They _______ to the neighbor.'], 'given': ['Harry had _______ a twinkie.', 'The white wizard had _______ home.', 'They had _______ to the neighbor.', 'Mario had _______ to the other house.', 'Harry had _______ to I-HOP.'], 'said': ['Harry had _______ to the nearest gas station.', 'They had _______ to the other house.', 'The big troll had _______ to the other house.', 'Harry had _______ a twinkie.', 'Sally had _______ to I-HOP.', 'The little hobbit _______ to I-HOP.', 'Sally _______ to the other house.', 'They _______ to the other house.', 'She _______ home.', 'My friends _______ to her.'], 'spoke': ['Harry _______ to the nearest gas station.', 'Link _______ to the nearest gas station.', 'All the kings men _______ to the concert.', 'Bob _______ to her.', 'She _______ to I-HOP.'], 'driving': ['All the kings men is _______ to the neighbor.', 'Luigi is _______ home.', 'I is _______ to her.', 'Citizens of the world is _______ to her.', 'He is _______ a job.'], 'sang': ['Link _______ to I-HOP.', 'Harry _______ to the concert.', 'The white wizard _______ to the nearest gas station.', 'Luigi _______ to her.', 'Mario _______ to the concert.'], 'thinking': ['Mario is _______ to the shopping mall.', 'She is _______ home.', 'Harry is _______ to them.', 'My friends is _______ to the other house.', 'The big troll is _______ to the shopping mall.'], 'come': ['He had _______ to the nearest gas station.', 'We had _______ to her.', 'She had _______ to I-HOP.', 'They had _______ to the shopping mall.', 'All the kings men had _______ to them.', 'The little hobbit _______ to the neighbor.', 'The big troll _______ to I-HOP.', 'Citizens of the world _______ a twinkie.', 'Luigi _______ to the shopping mall.', 'Everyone _______ to the other house.'], 'saw': ['She _______ to the shopping mall.', 'Link _______ a twinkie.', 'Harry _______ to the shopping mall.', 'She _______ to the other house.', 'I _______ home.'], 'give': ['She _______ to them.', 'Mario _______ to the other house.', 'Everyone _______ a twinkie.', 'I _______ a job.', 'Bob _______ to the concert.'], 'had': ['They _______ to the nearest gas station.', 'We _______ to her.', 'He _______ to I-HOP.', 'The big troll _______ to her.', 'Harry _______ to the other house.', 'We _______ to I-HOP.', 'The big troll _______ to I-HOP.', 'Luigi _______ to the other house.', 'She _______ a job.', 'Sally _______ a twinkie.'], 'writing': ['I is _______ to the nearest gas station.', 'She is _______ to I-HOP.', 'Bob is _______ to her.', 'Harry is _______ to her.', 'All the kings men is _______ to them.'], 'write': ['I _______ to I-HOP.', 'Sally _______ to the neighbor.', 'We _______ to the neighbor.', 'I _______ to them.', 'I _______ to the other house.'], 'spoken': ['We had _______ to the nearest gas station.', 'Everyone had _______ to the other house.', 'Everyone had _______ to her.', 'The white wizard had _______ to I-HOP.', 'My friends had _______ to her.'], 'written': ['Luigi had _______ to the other house.', 'Harry had _______ to I-HOP.', 'Link had _______ to her.', 'The white wizard had _______ to the nearest gas station.', 'She had _______ a job.'], 'going': ['Mario is _______ to them.', 'Citizens of the world is _______ a twinkie.', 'Citizens of the world is _______ to the nearest gas station.', 'The little hobbit is _______ to the other house.', 'Citizens of the world is _______ to them.'], 'tell': ['My friends _______ a job.', 'They _______ a job.', 'The little hobbit _______ to I-HOP.', 'The big troll _______ a job.', 'The little hobbit _______ to I-HOP.'], 'speaking': ['I is _______ a job.', 'I is _______ to the other house.', 'Bob is _______ to I-HOP.', 'Everyone is _______ home.', 'We is _______ to her.'], 'told': ['Everyone had _______ a job.', 'The big troll had _______ to her.', 'He had _______ home.', 'She had _______ to the other house.', 'Citizens of the world had _______ to her.', 'The big troll _______ to the concert.', 'The little hobbit _______ home.', 'The big troll _______ a twinkie.', 'Harry _______ a twinkie.', 'She _______ a job.'], 'knowing': ['', '', '', '', ''], 'do': ['I _______ to the shopping mall.', 'Link _______ a job.', 'We _______ home.', 'We _______ to the concert.', 'Mario _______ to them.'], 'see': ['She _______ to her.', 'Sally _______ to I-HOP.', 'Citizens of the world _______ a twinkie.', 'All the kings men _______ to the nearest gas station.', 'He _______ to the other house.'], 'knew': ['Sally _______ a job.', 'We _______ to the concert.', 'She _______ to them.', 'Harry _______ to her.', 'Link _______ a twinkie.'], 'driven': ['The big troll had _______ to the nearest gas station.', 'Bob had _______ a twinkie.', 'The big troll had _______ to the neighbor.', 'Everyone had _______ to them.', 'Harry had _______ to the shopping mall.'], 'know': ['He _______ a twinkie.', 'Harry _______ to the concert.', 'The big troll _______ to her.', 'He _______ to the concert.', 'Sally _______ to the nearest gas station.'], 'coming': ['Mario is _______ a job.', 'I is _______ to them.', 'Bob is _______ to the neighbor.', 'All the kings men is _______ to the neighbor.', 'I is _______ to them.'], 'known': ['The big troll had _______ to the shopping mall.', 'She had _______ to them.', 'Bob had _______ to the other house.', 'Mario had _______ to the shopping mall.', 'Citizens of the world had _______ to her.'], 'sing': ['She _______ to her.', 'My friends _______ to her.', 'Mario _______ home.', 'Link _______ to the neighbor.', 'She _______ a twinkie.'], 'seeing': ['Sally is _______ to the shopping mall.', 'The white wizard is _______ to her.', 'The big troll is _______ to the neighbor.', 'All the kings men is _______ to her.', 'The big troll is _______ to her.'], 'did': ['Link _______ to the concert.', 'He _______ to the other house.', 'The little hobbit _______ to the neighbor.', 'Everyone _______ a twinkie.', 'She _______ to the other house.'], 'drive': ['Citizens of the world _______ to her.', 'Everyone _______ to I-HOP.', 'The big troll _______ a job.', 'Luigi _______ to the other house.', 'The big troll _______ a job.'], 'think': ['They _______ to her.', 'All the kings men _______ to the concert.', 'The white wizard _______ home.', 'Mario _______ to them.', 'They _______ home.'], 'thought': ['She had _______ to her.', 'He had _______ a twinkie.', 'The big troll had _______ a job.', 'She had _______ home.', 'We had _______ to the neighbor.', 'All the kings men _______ to the other house.', 'Luigi _______ to the nearest gas station.', 'She _______ to her.', 'The big troll _______ to the concert.', 'Link _______ to the concert.'], 'giving': ['I is _______ to her.', 'Luigi is _______ to the shopping mall.', 'They is _______ to her.', 'Bob is _______ home.', 'My friends is _______ to the neighbor.'], 'wrote': ['Sally _______ to I-HOP.', 'Everyone _______ to the other house.', 'Link _______ a twinkie.', 'All the kings men _______ to the nearest gas station.', 'Luigi _______ to them.'], 'went': ['They _______ to the concert.', 'My friends _______ to them.', 'The big troll _______ a job.', 'Link _______ to the concert.', 'They _______ to the neighbor.'], 'gave': ['They _______ to her.', 'I _______ a job.', 'The white wizard _______ to them.', 'I _______ home.', 'She _______ to the shopping mall.'], 'having': ['Mario is _______ to the neighbor.', 'I is _______ a twinkie.', 'The big troll is _______ home.', 'All the kings men is _______ to her.', 'The white wizard is _______ to I-HOP.'], 'came': ['We _______ home.', 'The white wizard _______ to the nearest gas station.', 'Mario _______ to the other house.', 'All the kings men _______ to them.', 'Luigi _______ a twinkie.']}


def make_packet(number=1):
	qs = [Question(k,qdict=qdict2,qsection="Verb Tense",qprompt="Identify the verb in the selection below:") for k in qdict2]
	#qs+=[Question(k,qdict=qdict2,qsection="Verb Tense",qprompt="Identify the correct tense below:") for k in qdict2]
	qs2 = [verb_Question("doing",qdict={'doing': ['Everyone is  _______ something at home.', 'Everyone is  _______ something at home.'], 'do': ['The small furry dwarves _______ something at a local brewery at this very moment.', 'The small furry dwarves _______ something at a local brewery at this very moment.'], 'done': ['Mario has  _______ something to the shopping mall.', 'Mario has  _______ something to the shopping mall.'], 'did': ['We _______ something to the nearest gas station a year ago.', 'We _______ something to the nearest gas station a year ago.']}),
verb_Question("do",qdict={'doing': ['Everyone is  _______ something at home.', 'Everyone is  _______ something at home.', 'The company of men are  _______ something to a twinkie.'], 'do': ['The small furry dwarves _______ something at a local brewery at this very moment.', 'The small furry dwarves _______ something at a local brewery at this very moment.', 'We _______ something to the other house now.'], 'done': ['Mario has  _______ something to the shopping mall.', 'Mario has  _______ something to the shopping mall.', 'Sally has  _______ something to the I-HOP manager.'], 'did': ['We _______ something to the nearest gas station a year ago.', 'We _______ something to the nearest gas station a year ago.', 'The goblins _______ something at a local brewery a year ago.']}),
verb_Question("done",qdict={'doing': ['Everyone is  _______ something at home.', 'Everyone is  _______ something at home.', 'The company of men are  _______ something to a twinkie.', 'Sally is  _______ something to the neighbor.'], 'do': ['The small furry dwarves _______ something at a local brewery at this very moment.', 'The small furry dwarves _______ something at a local brewery at this very moment.', 'We _______ something to the other house now.', 'The small furry dwarves _______ something to the concert organizer now.'], 'done': ['Mario has  _______ something to the shopping mall.', 'Mario has  _______ something to the shopping mall.', 'Sally has  _______ something to the I-HOP manager.', 'The big harry trolls have  _______ something to a twinkie.'], 'did': ['We _______ something to the nearest gas station a year ago.', 'We _______ something to the nearest gas station a year ago.', 'The goblins _______ something at a local brewery a year ago.', 'We _______ something at home last week.']}),
verb_Question("did",qdict={'doing': ['Everyone is  _______ something at home.', 'Everyone is  _______ something at home.', 'The company of men are  _______ something to a twinkie.', 'Sally is  _______ something to the neighbor.', 'The goblins are  _______ something to a fellow musician.'], 'do': ['The small furry dwarves _______ something at a local brewery at this very moment.', 'The small furry dwarves _______ something at a local brewery at this very moment.', 'We _______ something to the other house now.', 'The small furry dwarves _______ something to the concert organizer now.', 'The company of men _______ something down the rabbit hole now.'], 'done': ['Mario has  _______ something to the shopping mall.', 'Mario has  _______ something to the shopping mall.', 'Sally has  _______ something to the I-HOP manager.', 'The big harry trolls have  _______ something to a twinkie.', 'The white wizard has  _______ something to the I-HOP manager.'], 'did': ['We _______ something to the nearest gas station a year ago.', 'We _______ something to the nearest gas station a year ago.', 'The goblins _______ something at a local brewery a year ago.', 'We _______ something at home last week.', 'The big harry trolls _______ something to a fellow musician the day before.']}),
verb_Question("giving",qdict={'giving': ['The goblins are  _______ something at a local brewery.', 'The goblins are  _______ something at a local brewery.'], 'given': ['I have _______ something at the gas station.', 'I have _______ something at the gas station.'], 'gave': ['The big harry trolls _______ something to the neighbor a year ago.', 'The big harry trolls _______ something to the neighbor a year ago.'], 'give': ['All the good citizens _______ something to a twinkie now.', 'All the good citizens _______ something to a twinkie now.']}),
verb_Question("give",qdict={'giving': ['The goblins are  _______ something at a local brewery.', 'The goblins are  _______ something at a local brewery.', 'They are  _______ something to them.'], 'given': ['I have _______ something at the gas station.', 'I have _______ something at the gas station.', 'Mario has  _______ something to her.'], 'gave': ['The big harry trolls _______ something to the neighbor a year ago.', 'The big harry trolls _______ something to the neighbor a year ago.', 'The small furry dwarves _______ something to the nearest gas station the day before.'], 'give': ['All the good citizens _______ something to a twinkie now.', 'All the good citizens _______ something to a twinkie now.', 'The goblins _______ something to her now.']}),
verb_Question("given",qdict={'giving': ['The goblins are  _______ something at a local brewery.', 'The goblins are  _______ something at a local brewery.', 'They are  _______ something to them.', 'The small furry dwarves are  _______ something to a candy-bar lover.'], 'given': ['I have _______ something at the gas station.', 'I have _______ something at the gas station.', 'Mario has  _______ something to her.', 'They have  _______ something to the nearest gas station.'], 'gave': ['The big harry trolls _______ something to the neighbor a year ago.', 'The big harry trolls _______ something to the neighbor a year ago.', 'The small furry dwarves _______ something to the nearest gas station the day before.', 'The big harry trolls _______ something to the nearest gas station a year ago.'], 'give': ['All the good citizens _______ something to a twinkie now.', 'All the good citizens _______ something to a twinkie now.', 'The goblins _______ something to her now.', 'The big harry trolls _______ something at a local brewery suddenly.']}),
verb_Question("gave",qdict={'giving': ['The goblins are  _______ something at a local brewery.', 'The goblins are  _______ something at a local brewery.', 'They are  _______ something to them.', 'The small furry dwarves are  _______ something to a candy-bar lover.', 'The white wizard is  _______ something to her.'], 'given': ['I have _______ something at the gas station.', 'I have _______ something at the gas station.', 'Mario has  _______ something to her.', 'They have  _______ something to the nearest gas station.', 'The company of men have  _______ something at home.'], 'gave': ['The big harry trolls _______ something to the neighbor a year ago.', 'The big harry trolls _______ something to the neighbor a year ago.', 'The small furry dwarves _______ something to the nearest gas station the day before.', 'The big harry trolls _______ something to the nearest gas station a year ago.', 'All the good citizens _______ something at the gas station yesterday.'], 'give': ['All the good citizens _______ something to a twinkie now.', 'All the good citizens _______ something to a twinkie now.', 'The goblins _______ something to her now.', 'The big harry trolls _______ something at a local brewery suddenly.', 'The big harry trolls _______ something at a local brewery suddenly.']}),
verb_Question("breaking",qdict={'break': ['The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'The small furry dwarves _______ something to the I-HOP manager at this very moment.'], 'broken': ['Sally has  _______ something down the rabbit hole.', 'Sally has  _______ something down the rabbit hole.'], 'breaking': ['All the good citizens are  _______ something across the waterway.', 'All the good citizens are  _______ something across the waterway.'], 'broke': ['Pink monkeys _______ something to the shopping mall yesterday.', 'Pink monkeys _______ something to the shopping mall yesterday.']}),
verb_Question("break",qdict={'break': ['The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'All the good citizens _______ something to her suddenly.'], 'broken': ['Sally has  _______ something down the rabbit hole.', 'Sally has  _______ something down the rabbit hole.', 'The white wizard has  _______ something to a twinkie.'], 'breaking': ['All the good citizens are  _______ something across the waterway.', 'All the good citizens are  _______ something across the waterway.', 'The big troll is  _______ something to the concert organizer.'], 'broke': ['Pink monkeys _______ something to the shopping mall yesterday.', 'Pink monkeys _______ something to the shopping mall yesterday.', 'The goblins _______ something to a fellow musician a year ago.']}),
verb_Question("broken",qdict={'break': ['The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'All the good citizens _______ something to her suddenly.', 'We _______ something to the nearest gas station suddenly.'], 'broken': ['Sally has  _______ something down the rabbit hole.', 'Sally has  _______ something down the rabbit hole.', 'The white wizard has  _______ something to a twinkie.', 'The big harry trolls have  _______ something to her.'], 'breaking': ['All the good citizens are  _______ something across the waterway.', 'All the good citizens are  _______ something across the waterway.', 'The big troll is  _______ something to the concert organizer.', 'Sally is  _______ something at a local brewery.'], 'broke': ['Pink monkeys _______ something to the shopping mall yesterday.', 'Pink monkeys _______ something to the shopping mall yesterday.', 'The goblins _______ something to a fellow musician a year ago.', 'The big harry trolls _______ something at home the day before.']}),
verb_Question("broke",qdict={'break': ['The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'The small furry dwarves _______ something to the I-HOP manager at this very moment.', 'All the good citizens _______ something to her suddenly.', 'We _______ something to the nearest gas station suddenly.', 'Pink monkeys _______ something at the gas station at this very moment.'], 'broken': ['Sally has  _______ something down the rabbit hole.', 'Sally has  _______ something down the rabbit hole.', 'The white wizard has  _______ something to a twinkie.', 'The big harry trolls have  _______ something to her.', 'I have _______ something to the other house.'], 'breaking': ['All the good citizens are  _______ something across the waterway.', 'All the good citizens are  _______ something across the waterway.', 'The big troll is  _______ something to the concert organizer.', 'Sally is  _______ something at a local brewery.', 'The goblins are  _______ something to a candy-bar lover.'], 'broke': ['Pink monkeys _______ something to the shopping mall yesterday.', 'Pink monkeys _______ something to the shopping mall yesterday.', 'The goblins _______ something to a fellow musician a year ago.', 'The big harry trolls _______ something at home the day before.', 'The goblins _______ something to the neighbor yesterday.']}),
verb_Question("seeing",qdict={'seeing': ['Luigi is  _______ something in the distance.', 'Luigi is  _______ something in the distance.'], 'see': ['The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window suddenly.'], 'saw': ['The small furry dwarves _______ something in the window a year ago.', 'The small furry dwarves _______ something in the window a year ago.'], 'seen': ['We have  _______ something in the window.', 'We have  _______ something in the window.']}),
verb_Question("see",qdict={'seeing': ['Luigi is  _______ something in the distance.', 'Luigi is  _______ something in the distance.', 'The small furry dwarves are  _______ something up ahead.'], 'see': ['The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window now.'], 'saw': ['The small furry dwarves _______ something in the window a year ago.', 'The small furry dwarves _______ something in the window a year ago.', 'We _______ something in the distance a year ago.'], 'seen': ['We have  _______ something in the window.', 'We have  _______ something in the window.', 'The big troll has  _______ something at the corner.']}),
verb_Question("seen",qdict={'seeing': ['Luigi is  _______ something in the distance.', 'Luigi is  _______ something in the distance.', 'The small furry dwarves are  _______ something up ahead.', 'All the good citizens are  _______ something up ahead.'], 'see': ['The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window now.', 'The goblins _______ something up ahead suddenly.'], 'saw': ['The small furry dwarves _______ something in the window a year ago.', 'The small furry dwarves _______ something in the window a year ago.', 'We _______ something in the distance a year ago.', 'All the good citizens _______ something up ahead last week.'], 'seen': ['We have  _______ something in the window.', 'We have  _______ something in the window.', 'The big troll has  _______ something at the corner.', 'All the good citizens have  _______ something in the window.']}),
verb_Question("saw",qdict={'seeing': ['Luigi is  _______ something in the distance.', 'Luigi is  _______ something in the distance.', 'The small furry dwarves are  _______ something up ahead.', 'All the good citizens are  _______ something up ahead.', 'The big troll is  _______ something in the distance.'], 'see': ['The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window suddenly.', 'The big harry trolls _______ something in the window now.', 'The goblins _______ something up ahead suddenly.', 'The big harry trolls _______ something in the distance now.'], 'saw': ['The small furry dwarves _______ something in the window a year ago.', 'The small furry dwarves _______ something in the window a year ago.', 'We _______ something in the distance a year ago.', 'All the good citizens _______ something up ahead last week.', 'We _______ something in the window yesterday.'], 'seen': ['We have  _______ something in the window.', 'We have  _______ something in the window.', 'The big troll has  _______ something at the corner.', 'All the good citizens have  _______ something in the window.', 'The company of men have  _______ something at the corner.']}),
verb_Question("knowing",qdict={'knowing': ['The little hobbit is  _______ something about the woods.', 'The little hobbit is  _______ something about the woods.'], 'known': ['She has  _______ something about the woods.', 'She has  _______ something about the woods.'], 'knew': ['The company of men _______ something about the winter the day before.', 'The company of men _______ something about the winter the day before.'], 'know': ['The goblins _______ something about the sycamore at this very moment.', 'The goblins _______ something about the sycamore at this very moment.']}),
verb_Question("know",qdict={'knowing': ['The little hobbit is  _______ something about the woods.', 'The little hobbit is  _______ something about the woods.', 'The company of men are  _______ something about the winter.'], 'known': ['She has  _______ something about the woods.', 'She has  _______ something about the woods.', 'The big harry trolls have  _______ something about the sycamore.'], 'knew': ['The company of men _______ something about the winter the day before.', 'The company of men _______ something about the winter the day before.', 'We _______ something about the woods a year ago.'], 'know': ['The goblins _______ something about the sycamore at this very moment.', 'The goblins _______ something about the sycamore at this very moment.', 'We _______ something about that now.']}),
verb_Question("known",qdict={'knowing': ['The little hobbit is  _______ something about the woods.', 'The little hobbit is  _______ something about the woods.', 'The company of men are  _______ something about the winter.', 'All the good citizens are  _______ something about the sycamore.'], 'known': ['She has  _______ something about the woods.', 'She has  _______ something about the woods.', 'The big harry trolls have  _______ something about the sycamore.', 'We have  _______ something about the winter.'], 'knew': ['The company of men _______ something about the winter the day before.', 'The company of men _______ something about the winter the day before.', 'We _______ something about the woods a year ago.', 'Pink monkeys _______ something about the winter a year ago.'], 'know': ['The goblins _______ something about the sycamore at this very moment.', 'The goblins _______ something about the sycamore at this very moment.', 'We _______ something about that now.', 'The big harry trolls _______ something about the woods at this very moment.']}),
verb_Question("knew",qdict={'knowing': ['The little hobbit is  _______ something about the woods.', 'The little hobbit is  _______ something about the woods.', 'The company of men are  _______ something about the winter.', 'All the good citizens are  _______ something about the sycamore.', 'Pink monkeys are  _______ something about the sycamore.'], 'known': ['She has  _______ something about the woods.', 'She has  _______ something about the woods.', 'The big harry trolls have  _______ something about the sycamore.', 'We have  _______ something about the winter.', 'The goblins have  _______ something about the sycamore.'], 'knew': ['The company of men _______ something about the winter the day before.', 'The company of men _______ something about the winter the day before.', 'We _______ something about the woods a year ago.', 'Pink monkeys _______ something about the winter a year ago.', 'Pink monkeys _______ something about the winter the day before.'], 'know': ['The goblins _______ something about the sycamore at this very moment.', 'The goblins _______ something about the sycamore at this very moment.', 'We _______ something about that now.', 'The big harry trolls _______ something about the woods at this very moment.', 'The goblins _______ something about that at this very moment.']}),
verb_Question("having",qdict={'had': ['The little hobbit has  _______ something for them.', 'The little hobbit has  _______ something for them.', 'The big harry trolls _______ something from a friend the day before.'], 'having': ['Bob is  _______ something for them.', 'Bob is  _______ something for them.'], 'have': ['We _______ something to show them at this very moment.', 'We _______ something to show them at this very moment.']}),
verb_Question("have",qdict={'had': ['The little hobbit has  _______ something for them.', 'The little hobbit has  _______ something for them.', 'The big harry trolls _______ something from a friend the day before.', 'We have  _______ something to show them.', 'The company of men _______ something to show them the day before.'], 'having': ['Bob is  _______ something for them.', 'Bob is  _______ something for them.', 'Luigi is  _______ something for them.'], 'have': ['We _______ something to show them at this very moment.', 'We _______ something to show them at this very moment.', 'All the good citizens _______ something to give to them in the winter suddenly.']}),
verb_Question("had",qdict={'had': ['The little hobbit has  _______ something for them.', 'The little hobbit has  _______ something for them.', 'The big harry trolls _______ something from a friend the day before.', 'We have  _______ something to show them.', 'The company of men _______ something to show them the day before.', 'Harry has  _______ something to show them.', 'Pink monkeys _______ something to give to them in the winter the day before.'], 'having': ['Bob is  _______ something for them.', 'Bob is  _______ something for them.', 'Luigi is  _______ something for them.', 'The big troll is  _______ something to show them.'], 'have': ['We _______ something to show them at this very moment.', 'We _______ something to show them at this very moment.', 'All the good citizens _______ something to give to them in the winter suddenly.', 'Pink monkeys _______ something to give at this very moment.']}),
verb_Question("had",qdict={'had': ['The little hobbit has  _______ something for them.', 'The little hobbit has  _______ something for them.', 'The big harry trolls _______ something from a friend the day before.', 'We have  _______ something to show them.', 'The company of men _______ something to show them the day before.', 'Harry has  _______ something to show them.', 'Pink monkeys _______ something to give to them in the winter the day before.', 'The goblins have  _______ something from a friend.', 'The small furry dwarves _______ something to give last week.'], 'having': ['Bob is  _______ something for them.', 'Bob is  _______ something for them.', 'Luigi is  _______ something for them.', 'The big troll is  _______ something to show them.', 'They are  _______ something to give.'], 'have': ['We _______ something to show them at this very moment.', 'We _______ something to show them at this very moment.', 'All the good citizens _______ something to give to them in the winter suddenly.', 'Pink monkeys _______ something to give at this very moment.', 'The goblins _______ something to give to them in the winter at this very moment.']}),
verb_Question("going",qdict={'go': ['The big harry trolls _______ somewhere to visit the sick suddenly.', 'The big harry trolls _______ somewhere to visit the sick suddenly.'], 'gone': ['The big harry trolls have  _______ somewhere for no reason.', 'The big harry trolls have  _______ somewhere for no reason.'], 'went': ['They _______ somewhere for no reason a year ago.', 'They _______ somewhere for no reason a year ago.'], 'going': ['Everyone is  _______ somewhere to visit a friend.', 'Everyone is  _______ somewhere to visit a friend.']}),
verb_Question("go",qdict={'go': ['The big harry trolls _______ somewhere to visit the sick suddenly.', 'The big harry trolls _______ somewhere to visit the sick suddenly.', 'Pink monkeys _______ somewhere for their health now.'], 'gone': ['The big harry trolls have  _______ somewhere for no reason.', 'The big harry trolls have  _______ somewhere for no reason.', 'Citizen Cane has  _______ somewhere to meet people.'], 'went': ['They _______ somewhere for no reason a year ago.', 'They _______ somewhere for no reason a year ago.', 'The small furry dwarves _______ somewhere interesting last week.'], 'going': ['Everyone is  _______ somewhere to visit a friend.', 'Everyone is  _______ somewhere to visit a friend.', 'They are  _______ somewhere to meet people.']}),
verb_Question("gone",qdict={'go': ['The big harry trolls _______ somewhere to visit the sick suddenly.', 'The big harry trolls _______ somewhere to visit the sick suddenly.', 'Pink monkeys _______ somewhere for their health now.', 'Pink monkeys _______ somewhere to visit a friend now.'], 'gone': ['The big harry trolls have  _______ somewhere for no reason.', 'The big harry trolls have  _______ somewhere for no reason.', 'Citizen Cane has  _______ somewhere to meet people.', 'The small furry dwarves have  _______ somewhere for no reason.'], 'went': ['They _______ somewhere for no reason a year ago.', 'They _______ somewhere for no reason a year ago.', 'The small furry dwarves _______ somewhere interesting last week.', 'The small furry dwarves _______ somewhere to visit a friend a year ago.'], 'going': ['Everyone is  _______ somewhere to visit a friend.', 'Everyone is  _______ somewhere to visit a friend.', 'They are  _______ somewhere to meet people.', 'The company of men are  _______ somewhere to meet them.']}),
verb_Question("went",qdict={'go': ['The big harry trolls _______ somewhere to visit the sick suddenly.', 'The big harry trolls _______ somewhere to visit the sick suddenly.', 'Pink monkeys _______ somewhere for their health now.', 'Pink monkeys _______ somewhere to visit a friend now.', 'Pink monkeys _______ somewhere interesting now.'], 'gone': ['The big harry trolls have  _______ somewhere for no reason.', 'The big harry trolls have  _______ somewhere for no reason.', 'Citizen Cane has  _______ somewhere to meet people.', 'The small furry dwarves have  _______ somewhere for no reason.', 'The company of men have  _______ somewhere interesting.'], 'went': ['They _______ somewhere for no reason a year ago.', 'They _______ somewhere for no reason a year ago.', 'The small furry dwarves _______ somewhere interesting last week.', 'The small furry dwarves _______ somewhere to visit a friend a year ago.', 'They _______ somewhere for no reason last week.'], 'going': ['Everyone is  _______ somewhere to visit a friend.', 'Everyone is  _______ somewhere to visit a friend.', 'They are  _______ somewhere to meet people.', 'The company of men are  _______ somewhere to meet them.', 'Everyone is  _______ somewhere interesting.']}),
verb_Question("singing",qdict={'sing': ['They _______ something at a local brewery suddenly.', 'They _______ something at a local brewery suddenly.'], 'singing': ['Pink monkeys are  _______ something to them.', 'Pink monkeys are  _______ something to them.'], 'sung': ['The small furry dwarves have  _______ something to a fellow musician.', 'The small furry dwarves have  _______ something to a fellow musician.'], 'sang': ['The small furry dwarves _______ something to the I-HOP manager last week.', 'The small furry dwarves _______ something to the I-HOP manager last week.']}),
verb_Question("sing",qdict={'sing': ['They _______ something at a local brewery suddenly.', 'They _______ something at a local brewery suddenly.', 'Pink monkeys _______ something to the nearest gas station at this very moment.'], 'singing': ['Pink monkeys are  _______ something to them.', 'Pink monkeys are  _______ something to them.', 'They are  _______ something down the rabbit hole.'], 'sung': ['The small furry dwarves have  _______ something to a fellow musician.', 'The small furry dwarves have  _______ something to a fellow musician.', 'We have  _______ something across the waterway.'], 'sang': ['The small furry dwarves _______ something to the I-HOP manager last week.', 'The small furry dwarves _______ something to the I-HOP manager last week.', 'The big harry trolls _______ something down the rabbit hole a year ago.']}),
verb_Question("sung",qdict={'sing': ['They _______ something at a local brewery suddenly.', 'They _______ something at a local brewery suddenly.', 'Pink monkeys _______ something to the nearest gas station at this very moment.', 'The company of men _______ something to her now.'], 'singing': ['Pink monkeys are  _______ something to them.', 'Pink monkeys are  _______ something to them.', 'They are  _______ something down the rabbit hole.', 'The small furry dwarves are  _______ something at the gas station.'], 'sung': ['The small furry dwarves have  _______ something to a fellow musician.', 'The small furry dwarves have  _______ something to a fellow musician.', 'We have  _______ something across the waterway.', 'The company of men have  _______ something to a fellow musician.'], 'sang': ['The small furry dwarves _______ something to the I-HOP manager last week.', 'The small furry dwarves _______ something to the I-HOP manager last week.', 'The big harry trolls _______ something down the rabbit hole a year ago.', 'We _______ something to the I-HOP manager last week.']}),
verb_Question("sang",qdict={'sing': ['They _______ something at a local brewery suddenly.', 'They _______ something at a local brewery suddenly.', 'Pink monkeys _______ something to the nearest gas station at this very moment.', 'The company of men _______ something to her now.', 'The small furry dwarves _______ something to the concert organizer at this very moment.'], 'singing': ['Pink monkeys are  _______ something to them.', 'Pink monkeys are  _______ something to them.', 'They are  _______ something down the rabbit hole.', 'The small furry dwarves are  _______ something at the gas station.', 'Link is  _______ something to the concert organizer.'], 'sung': ['The small furry dwarves have  _______ something to a fellow musician.', 'The small furry dwarves have  _______ something to a fellow musician.', 'We have  _______ something across the waterway.', 'The company of men have  _______ something to a fellow musician.', 'The goblins have  _______ something across the waterway.'], 'sang': ['The small furry dwarves _______ something to the I-HOP manager last week.', 'The small furry dwarves _______ something to the I-HOP manager last week.', 'The big harry trolls _______ something down the rabbit hole a year ago.', 'We _______ something to the I-HOP manager last week.', 'The goblins _______ something to the nearest gas station a year ago.']}),
verb_Question("coming",qdict={'come': ['Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Link has  _______ from someplace to a fellow musician.'], 'came': ['The goblins _______ from someplace to a twinkie last week.', 'The goblins _______ from someplace to a twinkie last week.'], 'coming': ['The big troll is  _______ from someplace down the rabbit hole.', 'The big troll is  _______ from someplace down the rabbit hole.']}),
verb_Question("come",qdict={'come': ['Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Link has  _______ from someplace to a fellow musician.', 'Pink monkeys _______ from someplace at home suddenly.', 'Luigi has  _______ from someplace to her.'], 'came': ['The goblins _______ from someplace to a twinkie last week.', 'The goblins _______ from someplace to a twinkie last week.', 'The big harry trolls _______ from someplace to a twinkie yesterday.'], 'coming': ['The big troll is  _______ from someplace down the rabbit hole.', 'The big troll is  _______ from someplace down the rabbit hole.', 'All the good citizens are  _______ from someplace down the rabbit hole.']}),
verb_Question("come",qdict={'come': ['Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Link has  _______ from someplace to a fellow musician.', 'Pink monkeys _______ from someplace at home suddenly.', 'Luigi has  _______ from someplace to her.', 'The goblins _______ from someplace down the rabbit hole now.', 'The big harry trolls have  _______ from someplace to the other house.'], 'came': ['The goblins _______ from someplace to a twinkie last week.', 'The goblins _______ from someplace to a twinkie last week.', 'The big harry trolls _______ from someplace to a twinkie yesterday.', 'The goblins _______ from someplace at home yesterday.'], 'coming': ['The big troll is  _______ from someplace down the rabbit hole.', 'The big troll is  _______ from someplace down the rabbit hole.', 'All the good citizens are  _______ from someplace down the rabbit hole.', 'The goblins are  _______ from someplace at a local brewery.']}),
verb_Question("came",qdict={'come': ['Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Pink monkeys _______ from someplace to a candy-bar lover suddenly.', 'Link has  _______ from someplace to a fellow musician.', 'Pink monkeys _______ from someplace at home suddenly.', 'Luigi has  _______ from someplace to her.', 'The goblins _______ from someplace down the rabbit hole now.', 'The big harry trolls have  _______ from someplace to the other house.', 'The big harry trolls _______ from someplace down the rabbit hole suddenly.', 'Luigi has  _______ from someplace at the gas station.'], 'came': ['The goblins _______ from someplace to a twinkie last week.', 'The goblins _______ from someplace to a twinkie last week.', 'The big harry trolls _______ from someplace to a twinkie yesterday.', 'The goblins _______ from someplace at home yesterday.', 'The goblins _______ from someplace at the gas station the day before.'], 'coming': ['The big troll is  _______ from someplace down the rabbit hole.', 'The big troll is  _______ from someplace down the rabbit hole.', 'All the good citizens are  _______ from someplace down the rabbit hole.', 'The goblins are  _______ from someplace at a local brewery.', 'We are  _______ from someplace at the gas station.']}),
verb_Question("speaking",qdict={'spoken': ['They have  _______ something to the shopping mall.', 'They have  _______ something to the shopping mall.'], 'spoke': ['They _______ something to a candy-bar lover last week.', 'They _______ something to a candy-bar lover last week.'], 'speaking': ['We are  _______ something to them.', 'We are  _______ something to them.'], 'speak': ['They _______ something to the I-HOP manager now.', 'They _______ something to the I-HOP manager now.']}),
verb_Question("speak",qdict={'spoken': ['They have  _______ something to the shopping mall.', 'They have  _______ something to the shopping mall.', 'The big harry trolls have  _______ something to the other house.'], 'spoke': ['They _______ something to a candy-bar lover last week.', 'They _______ something to a candy-bar lover last week.', 'The goblins _______ something down the rabbit hole the day before.'], 'speaking': ['We are  _______ something to them.', 'We are  _______ something to them.', 'We are  _______ something to the neighbor.'], 'speak': ['They _______ something to the I-HOP manager now.', 'They _______ something to the I-HOP manager now.', 'The big harry trolls _______ something to the I-HOP manager suddenly.']}),
verb_Question("spoken",qdict={'spoken': ['They have  _______ something to the shopping mall.', 'They have  _______ something to the shopping mall.', 'The big harry trolls have  _______ something to the other house.', 'She has  _______ something to the neighbor.'], 'spoke': ['They _______ something to a candy-bar lover last week.', 'They _______ something to a candy-bar lover last week.', 'The goblins _______ something down the rabbit hole the day before.', 'The small furry dwarves _______ something to the nearest gas station a year ago.'], 'speaking': ['We are  _______ something to them.', 'We are  _______ something to them.', 'We are  _______ something to the neighbor.', 'We are  _______ something to them.'], 'speak': ['They _______ something to the I-HOP manager now.', 'They _______ something to the I-HOP manager now.', 'The big harry trolls _______ something to the I-HOP manager suddenly.', 'We _______ something to the concert organizer at this very moment.']}),
verb_Question("spoke",qdict={'spoken': ['They have  _______ something to the shopping mall.', 'They have  _______ something to the shopping mall.', 'The big harry trolls have  _______ something to the other house.', 'She has  _______ something to the neighbor.', 'I have _______ something across the waterway.'], 'spoke': ['They _______ something to a candy-bar lover last week.', 'They _______ something to a candy-bar lover last week.', 'The goblins _______ something down the rabbit hole the day before.', 'The small furry dwarves _______ something to the nearest gas station a year ago.', 'The company of men _______ something across the waterway the day before.'], 'speaking': ['We are  _______ something to them.', 'We are  _______ something to them.', 'We are  _______ something to the neighbor.', 'We are  _______ something to them.', 'Citizen Cane is  _______ something at home.'], 'speak': ['They _______ something to the I-HOP manager now.', 'They _______ something to the I-HOP manager now.', 'The big harry trolls _______ something to the I-HOP manager suddenly.', 'We _______ something to the concert organizer at this very moment.', 'The big harry trolls _______ something to the nearest gas station suddenly.']}),
verb_Question("driving",qdict={'driven': ['The goblins have  _______ somewhere for no reason.', 'The goblins have  _______ somewhere for no reason.'], 'drove': ['The company of men _______ somewhere to meet people the day before.', 'The company of men _______ somewhere to meet people the day before.'], 'drive': ['The company of men _______ somewhere interesting suddenly.', 'The company of men _______ somewhere interesting suddenly.'], 'driving': ['I am _______ somewhere for no reason.', 'I am _______ somewhere for no reason.']}),
verb_Question("drive",qdict={'driven': ['The goblins have  _______ somewhere for no reason.', 'The goblins have  _______ somewhere for no reason.', 'I have _______ somewhere interesting.'], 'drove': ['The company of men _______ somewhere to meet people the day before.', 'The company of men _______ somewhere to meet people the day before.', 'We _______ somewhere to visit the sick the day before.'], 'drive': ['The company of men _______ somewhere interesting suddenly.', 'The company of men _______ somewhere interesting suddenly.', 'They _______ somewhere to visit the sick now.'], 'driving': ['I am _______ somewhere for no reason.', 'I am _______ somewhere for no reason.', 'We are  _______ somewhere to visit the sick.']}),
verb_Question("driven",qdict={'driven': ['The goblins have  _______ somewhere for no reason.', 'The goblins have  _______ somewhere for no reason.', 'I have _______ somewhere interesting.', 'Pink monkeys have  _______ somewhere for no reason.'], 'drove': ['The company of men _______ somewhere to meet people the day before.', 'The company of men _______ somewhere to meet people the day before.', 'We _______ somewhere to visit the sick the day before.', 'The goblins _______ somewhere to meet them a year ago.'], 'drive': ['The company of men _______ somewhere interesting suddenly.', 'The company of men _______ somewhere interesting suddenly.', 'They _______ somewhere to visit the sick now.', 'All the good citizens _______ somewhere for their health suddenly.'], 'driving': ['I am _______ somewhere for no reason.', 'I am _______ somewhere for no reason.', 'We are  _______ somewhere to visit the sick.', 'He is  _______ somewhere to meet them.']}),
verb_Question("drove",qdict={'driven': ['The goblins have  _______ somewhere for no reason.', 'The goblins have  _______ somewhere for no reason.', 'I have _______ somewhere interesting.', 'Pink monkeys have  _______ somewhere for no reason.', 'Pink monkeys have  _______ somewhere for their health.'], 'drove': ['The company of men _______ somewhere to meet people the day before.', 'The company of men _______ somewhere to meet people the day before.', 'We _______ somewhere to visit the sick the day before.', 'The goblins _______ somewhere to meet them a year ago.', 'The small furry dwarves _______ somewhere to visit the sick last week.'], 'drive': ['The company of men _______ somewhere interesting suddenly.', 'The company of men _______ somewhere interesting suddenly.', 'They _______ somewhere to visit the sick now.', 'All the good citizens _______ somewhere for their health suddenly.', 'The goblins _______ somewhere to meet them suddenly.'], 'driving': ['I am _______ somewhere for no reason.', 'I am _______ somewhere for no reason.', 'We are  _______ somewhere to visit the sick.', 'He is  _______ somewhere to meet them.', 'We are  _______ somewhere interesting.']}),
verb_Question("telling",qdict={'telling': ['She is  _______ it to a twinkie.', 'She is  _______ it to a twinkie.'], 'tell': ['The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to a candy-bar lover now.'], 'told': ['The big harry trolls have  _______ it to the nearest gas station.', 'The big harry trolls have  _______ it to the nearest gas station.', 'All the good citizens _______ it to the concert organizer last week.']}),
verb_Question("tell",qdict={'telling': ['She is  _______ it to a twinkie.', 'She is  _______ it to a twinkie.', 'The small furry dwarves are  _______ it to the shopping mall.'], 'tell': ['The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to them at this very moment.'], 'told': ['The big harry trolls have  _______ it to the nearest gas station.', 'The big harry trolls have  _______ it to the nearest gas station.', 'All the good citizens _______ it to the concert organizer last week.', 'The goblins have  _______ it to the I-HOP manager.', 'We _______ it to a twinkie the day before.']}),
verb_Question("told",qdict={'telling': ['She is  _______ it to a twinkie.', 'She is  _______ it to a twinkie.', 'The small furry dwarves are  _______ it to the shopping mall.', 'The big harry trolls are  _______ it to a twinkie.'], 'tell': ['The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to them at this very moment.', 'We _______ it to a candy-bar lover now.'], 'told': ['The big harry trolls have  _______ it to the nearest gas station.', 'The big harry trolls have  _______ it to the nearest gas station.', 'All the good citizens _______ it to the concert organizer last week.', 'The goblins have  _______ it to the I-HOP manager.', 'We _______ it to a twinkie the day before.', 'Bob has  _______ it to them.', 'The big harry trolls _______ it to a candy-bar lover a year ago.']}),
verb_Question("told",qdict={'telling': ['She is  _______ it to a twinkie.', 'She is  _______ it to a twinkie.', 'The small furry dwarves are  _______ it to the shopping mall.', 'The big harry trolls are  _______ it to a twinkie.', 'The small furry dwarves are  _______ it to the shopping mall.'], 'tell': ['The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to a candy-bar lover now.', 'The company of men _______ it to them at this very moment.', 'We _______ it to a candy-bar lover now.', 'They _______ it at a local brewery suddenly.'], 'told': ['The big harry trolls have  _______ it to the nearest gas station.', 'The big harry trolls have  _______ it to the nearest gas station.', 'All the good citizens _______ it to the concert organizer last week.', 'The goblins have  _______ it to the I-HOP manager.', 'We _______ it to a twinkie the day before.', 'Bob has  _______ it to them.', 'The big harry trolls _______ it to a candy-bar lover a year ago.', 'The small furry dwarves have  _______ it to them.', 'The company of men _______ it to the other house the day before.']}),
verb_Question("writing",qdict={'write': ['Pink monkeys _______ something at a local brewery now.', 'Pink monkeys _______ something at a local brewery now.'], 'written': ['All the good citizens have  _______ something to a fellow musician.', 'All the good citizens have  _______ something to a fellow musician.'], 'wrote': ['We _______ something across the waterway a year ago.', 'We _______ something across the waterway a year ago.'], 'writing': ['Pink monkeys are  _______ something to the nearest gas station.', 'Pink monkeys are  _______ something to the nearest gas station.']}),
verb_Question("write",qdict={'write': ['Pink monkeys _______ something at a local brewery now.', 'Pink monkeys _______ something at a local brewery now.', 'The small furry dwarves _______ something at a local brewery now.'], 'written': ['All the good citizens have  _______ something to a fellow musician.', 'All the good citizens have  _______ something to a fellow musician.', 'Everyone has  _______ something to a candy-bar lover.'], 'wrote': ['We _______ something across the waterway a year ago.', 'We _______ something across the waterway a year ago.', 'Pink monkeys _______ something at a local brewery the day before.'], 'writing': ['Pink monkeys are  _______ something to the nearest gas station.', 'Pink monkeys are  _______ something to the nearest gas station.', 'I am _______ something to a twinkie.']}),
verb_Question("written",qdict={'write': ['Pink monkeys _______ something at a local brewery now.', 'Pink monkeys _______ something at a local brewery now.', 'The small furry dwarves _______ something at a local brewery now.', 'The small furry dwarves _______ something to a twinkie at this very moment.'], 'written': ['All the good citizens have  _______ something to a fellow musician.', 'All the good citizens have  _______ something to a fellow musician.', 'Everyone has  _______ something to a candy-bar lover.', 'Mario has  _______ something to a twinkie.'], 'wrote': ['We _______ something across the waterway a year ago.', 'We _______ something across the waterway a year ago.', 'Pink monkeys _______ something at a local brewery the day before.', 'The small furry dwarves _______ something to them last week.'], 'writing': ['Pink monkeys are  _______ something to the nearest gas station.', 'Pink monkeys are  _______ something to the nearest gas station.', 'I am _______ something to a twinkie.', 'Luigi is  _______ something at home.']}),
verb_Question("wrote",qdict={'write': ['Pink monkeys _______ something at a local brewery now.', 'Pink monkeys _______ something at a local brewery now.', 'The small furry dwarves _______ something at a local brewery now.', 'The small furry dwarves _______ something to a twinkie at this very moment.', 'The goblins _______ something to the I-HOP manager now.'], 'written': ['All the good citizens have  _______ something to a fellow musician.', 'All the good citizens have  _______ something to a fellow musician.', 'Everyone has  _______ something to a candy-bar lover.', 'Mario has  _______ something to a twinkie.', 'The company of men have  _______ something to them.'], 'wrote': ['We _______ something across the waterway a year ago.', 'We _______ something across the waterway a year ago.', 'Pink monkeys _______ something at a local brewery the day before.', 'The small furry dwarves _______ something to them last week.', 'The goblins _______ something to the nearest gas station yesterday.'], 'writing': ['Pink monkeys are  _______ something to the nearest gas station.', 'Pink monkeys are  _______ something to the nearest gas station.', 'I am _______ something to a twinkie.', 'Luigi is  _______ something at home.', 'The company of men are  _______ something to the other house.']}),
]
	#print Question("say",qdict={"saying":["We are  _______ home."], "say":["They _______ a job."], "said":["Citizen Cane has  _______ home."], "said":["The goblins _______ to the neighbor."], "saying":["Bob is  _______ a job."], "say":["They _______ down the rabbit hole."], "said":["All the good citizens have  _______ across the waterway."], "said":["All the good citizens _______ a twinkie."], "saying":["They are  _______ a twinkie."], "say":["We _______ to the neighbor."], "said":["We have  _______ a twinkie."], "said":["Pink monkeys _______ down the rabbit hole."], }).get_Question()
	questions=[]
	qs_copy = qs[:]
	qs2_copy = qs2[:]
	for x in range(len(qs+qs2)):
		#print x
		if x%2 and len(qs_copy):
			questions+=[qs_copy.pop()]
		else:
			questions+=[qs2_copy.pop()]
	#questions = 
	shuffle(qs2)

	packet = Packet(qs2)
	#qs2 = 
	return packet.make_packet(number)



if __name__=="__main__":
	print "testing..."
	#print make_packet(10)
	dic1 ={}
	subj_s = ["He","She","Bob","Harry","Sally","Mario","Luigi","Link","Citizen Cane","I","She","Everyone","I","The white wizard","The little hobbit","The big troll"]	
	subj_p = ["We","They","The goblins","The big harry trolls","The small furry dwarves","The company of men","Pink monkeys","All the good citizens"]
	subj_I = ["I"]
	pred = ["to her","to them","to the other house",
	"to the neighbor","at home","to the shopping mall",
	"to a twinkie","to the concert organizer","to the I-HOP manager",
	"to the nearest gas station","across the waterway","down the rabbit hole",
	"at the gas station","at a local brewery","to a fellow musician",
	"to a candy-bar lover"]
	#do = ["a twinkie"]
	for x in s.split("\n"):
		dic2 = dict(zip(["base form","present participle","past form","past participle"],x.split(" ")))
		for key in dic2.keys():
		    if key in dic2: dic1.setdefault(key, []).append(dic2[key])
		#dictionary[x.split(" ")[0]]=dict(zip(["base form","present participle","past form","past participle"],x.split(" ")))
	print dic1
	qdict2={'do': {'present participle': 'doing', 'past participle': 'done', 'base form': 'do', 'past form': 'did'}, 'see': {'present participle': 'seeing', 'past participle': 'seen', 'base form': 'see', 'past form': 'saw'}, 'give': {'present participle': 'giving', 'past participle': 'given', 'base form': 'give', 'past form': 'gave'}, 'drive': {'present participle': 'driving', 'past participle': 'driven', 'base form': 'drive', 'past form': 'drove'}, 'think': {'present participle': 'thinking', 'past participle': 'thought', 'base form': 'think', 'past form': 'thought'}, 'write': {'present participle': 'writing', 'past participle': 'written', 'base form': 'write', 'past form': 'wrote'}, 'say': {'present participle': 'saying', 'past participle': 'said', 'base form': 'say', 'past form': 'said'}, 'know': {'present participle': 'knowing', 'past participle': 'known', 'base form': 'know', 'past form': 'knew'}, 'have': {'present participle': 'having', 'past participle': 'had', 'base form': 'have', 'past form': 'had'}, 'go': {'present participle': 'going', 'past participle': 'gone', 'base form': 'go', 'past form': 'went'}, 'sing': {'present participle': 'singing', 'past participle': 'sung', 'base form': 'sing', 'past form': 'sang'}, 'come': {'present participle': 'coming', 'past participle': 'come', 'base form': 'come', 'past form': 'came'}, 'tell': {'present participle': 'telling', 'past participle': 'told', 'base form': 'tell', 'past form': 'told'}, 'speak': {'present participle': 'speaking', 'past participle': 'spoken', 'base form': 'speak', 'past form': 'spoke'},
	'break':{'present participle': 'breaking', 'past participle': 'broken', 'base form': 'break','past form': 'broke'}
	}

	qdict = {'present participle': ['coming', 'doing', 'driving', 'giving', 'going', 'having', 'knowing', 'saying', 'seeing', 'singing', 'speaking', 'telling', 'thinking', 'writing'], 'base form': ['come', 'do', 'drive', 'give', 'go', 'have', 'know', 'say', 'see', 'sing', 'speak', 'tell', 'think', 'write'], 'past participle': ['come', 'done', 'driven', 'given', 'gone', 'had', 'known', 'said', 'seen', 'sung', 'spoken', 'told', 'thought', 'written'], 'past form': ['came', 'did', 'drove', 'gave', 'went', 'had', 'knew', 'said', 'saw', 'sang', 'spoke', 'told', 'thought', 'wrote']}

	# for key,q in qdict.items():
	# 	dictionary = {}
	# 	for value in q*5:

	# 		string = ""
	# 		string=""
	# 		if "past participle" in key and value!="had":
	# 			string= "%s had _______ %s." % (choice(subj),choice(pred))
	# 		elif "present participle" in key:
	# 			if value!="knowing":
	# 				string= "%s is _______ %s." % (choice(subj),choice(pred))
	# 		else:
	# 			string= "%s _______ %s." % (choice(subj),choice(pred))
	# 		#string+="], "
	# 		if value in dictionary:
	# 			dictionary[value]+=[string]
	# 		else:
	# 			dictionary[value]=[string]
	# 		#print "\t\"%s %s %s.\"," % (choice(subj),value,choice(pred))
	# 	print dictionary
	string= "["
	for k,dic3 in qdict2.items():
		dictionary={}
		for type_key in dic3.values():
			string+= "verb_Question(\"%s\",qdict=" % (type_key)
			for key,v in dic3.items():
				choices = [c for c in dic3.values() if c!=v]
				#print dic3.values()
				#string+= "\"%s\":[" % v
				string2=""
				singular = choice([0,1])
				if k in ["go","drive"]:
					pred_c = "somewhere "+choice(["to meet them","to visit the sick","for their health","to visit a friend","for no reason","interesting","to meet people"])
				elif k in ["come"]:
					pred_c = "from someplace "+choice(pred)
				elif k in ["tell"]:
					pred_c= "it "+choice(pred)
				elif k in ["think","know"]:
					pred_c="something "+choice(["about the winter","about that","about the woods","about the sycamore"])
				elif k in ["have"]:
					pred_c="something "+choice(["to give to them in the winter","to show at night","to show them","to give","for them","from a friend","from an enemy"])
				elif k in ["see"]:
					pred_c="something "+choice(["up ahead","in the distance","at the corner","in the window"])
				else:
					pred_c="something "+choice(pred)
	
				if "past participle" in key:
					subj = choice(subj_s)+" has " if singular else choice(subj_p)+" have "
					subj = "I have" if subj.startswith("I") else subj
					string2+="%s _______ %s." % (subj,pred_c)
				elif "present participle" in key and key!="had":
					subj = choice(subj_s)+" is " if singular else choice(subj_p)+" are "
					subj = "I am" if subj.startswith("I") else subj
					string2+="%s _______ %s." % (subj,pred_c)
				elif "past form" in key:
					subj = choice(subj_p)
					string2+="%s _______ %s %s." % (subj,pred_c,choice(['yesterday',"the day before","last week","a year ago"]))
				else:
					subj = choice(subj_p)
					string2+="%s _______ %s %s." % (subj,pred_c,choice(['now','at this very moment','suddenly']))			
				dictionary[v] = [string2] if v not in dictionary else dictionary[v]+[string2] 

			#print dictionary
			#string+="], "
			string+="%s),\n" % str(dictionary)
	print string+"]"

	"""
	past progressive
	Question 1

	In the following sentence, what is the indirect object?

	We gave the grammarian many interesting examples of sentence transformations.

	grammarian

	examples

	transformations

	There is no indirect object in the sentence above.
	vs present progressive
	"""





	#	for y in x.split(" "):
	"""
	qdict2 = {
	"past form":[
	Howard spoke for one hour.
	The chorus sang the school song.

	],
	"past participle":
	[
	I know how much Carla likes horses.
	]
	"present progressive":[
	How many hours have you driven today?

	past form 5.I (think, thought) of the answer after the test.
	present participle
	6.We are (giving, given) some money to the hunger center.
	],
	"base form":[
	]
	"future tense":[
	],
	}"""

	"""break (am, is, or are) breaking broke (has, have, or had) broken"""
	q_write=Question("present participle",qdict={"present participle":"He is________to them", "base form":"She________to them", "past participle":"He had________to her", "past form":"She________to her", })
	q_think=Question("present participle",qdict={"present participle":"She is________to the neighbor", "base form":"Bob________to them", "past participle":"She had________to her", "past form":"She________to the other house", })
	q_say=Question("present participle",qdict={"present participle":"She is________to the other house", "base form":"He________to them", "past participle":"He had________to the neighbor", "past form":"He________to them", })
	#print q_write.get_Question()
	#print Packet([q_write,q_think,q_say]).make_packet(3)
	qs = [Question(k,qdict=qdict,qsection="Verb Tense",qprompt="Identify the verb in the selection below:") for k in qdict]
	#qs+=[Question(k,qdict=qdict2,qsection="Verb Tense",qprompt="Identify the correct tense below:") for k in qdict2]

	packet = Packet(qs)
	print make_packet(10)

	# print make_packet(2)