# -*- coding: utf-8 -*-
import random
questions =[
{
"topic: castles; purpose: describe":"Castles are often characterized by a majestic atmosphere.",
"topic: castles; purpose: narrate":"The castle housed the notoriously brutal and malicious king Henry VIII.",
"topic: castles; purpose: inform":"The castle is made of very sturdy material for its time.",
"topic: castles; purpose: persuade":"Castles while castles seemed safe, some argue they were the perfect environment for the spread of deadly infectious diseases.",
},
{
"topic: basketball; purpose: describe":"Basketball is depicted as a game of skill and speed.",
"topic: basketball; purpose: narrate":"The home team lost its championship game against overwhelming odds.",
"topic: basketball; purpose: inform":"The basketball has a very elaborate construction process.",
"topic: basketball; purpose: persuade":"Basketball is arguably the most dangerous and demanding sport for your knees and joints.",
},
{
"topic: airplanes; purpose: describe":"The magnificent airplane is a wonderful sight to behold in the night sky.",
"topic: airplanes; purpose: narrate":"Mutant snakes took over a plane with passangers still onboard.",
"topic: airplanes; purpose: inform":"Jet engines have a very intricate design and style.",
"topic: airplanes; purpose: persuade":"Jet engines should be considered dangerous for the environment.",
},
{
"topic: languages; purpose: describe":"The French language is characterized by syllables run together with soft sounds.",
"topic: languages; purpose: narrate":"The story of the English language began when William the Conqueror invaded England in 1066 CE.",
"topic: languages; purpose: inform":"Noam Chompsky demonstrated that all languages have a common, underlying universal grammar.",
"topic: languages; purpose: persuade":"Learning English grammar is arguably the most important part of learning the English language.",
},
{
"topic: cars; purpose: describe":"The modern process for creating a car is characterized by a complicated system of inter-connected machines.",
"topic: cars; purpose: narrate":"In the movie \"Hurby The Love Bug,\" a compact car, the Volkswagen Beetle, comes to life and begins to develop a will of its own.",
"topic: cars; purpose: inform":"Cars have been an essential part of the American lifestyle since the early 1900s.",
"topic: cars; purpose: persuade":"The Porsche is the best-designed sports car.",
},
{
"topic: painting; purpose: describe":"The bright colors and broad strokes contributes to a feeling of enthusiasm and joy in the painting.",
"topic: painting; purpose: narrate":"When Pablo Piccaso became frustrated with traditional painting, he began to experiment with mutliple dimensions in his later Cubist period.",
"topic: painting; purpose: inform":"Painting is a process that involves an initial sketch, a thin coating (or wash) of paint, and then multiple layers of paint.",
"topic: painting; purpose: persuade":"Painting is the superior form of art, perhaps the best, since it requires patience, skills, and mastery of the steady hand.",
},

]

thesis_questions ={
"Choose the best complete thesis statement created from the theme: the significance of the invention of the telephone.":
	{
		"correct":[
			"The invention of the telephone pioneered the ever-expanding business of telecommunications.",
			"The invention of the telephone changed culture by allowing societies to communicate in real-time.",
			],
		"incorrect":[
			"The telephone contributed to development of civilization.",
			"The telephone has helped me to communicate with my friends, and you can now communicate with the world.",
			"I think the telephone is the best invention in the world.",
			"The telephone started a revolution.",
			"The telephone is great but no longer needed now that everyone has facebook.",
			"There are many reasons the telephone is a really good invention.",
			"Creating the telephone was good for many reasons.",	
			"The telephone made travel easier.",
			"Because of the telephone things became better.",		
			]
	},
"What is the crucial piece that the following thesis missing: \"Sexist language in college textbooks is harmful.\"?":
	{
		"correct":[
			"A reason why sexist language is harmful.",
			"Support for the assertion sexist language in college textbooks is harmful.",
			"A clause linked by \"because\" which explains why sexist language is harmful."
			],
		"incorrect":[
			"A specific example of sexist language the author is talking about.",
			"A specific example of the kinds of textbooks where sexist language can be a problem",
			"An explanation of what sexist language is.",
			"A long list of sexist language that has harmed people in the past.",
			"A call to action, asking people to change how college textbooks are made!",
			"A description of the kinds of sexist language that will be discussed later.",
			"A clause linked with \"For example\" showing instances of sexist language in textbooks.",
			]
	}
,	

"An effective thesis has to have (choose the best answer):":
	{
		"correct":[
			"a claim and a reason",
			"an assertion or main idea that you are making and a reason or support for that assertion.",
			],
		"incorrect":[
			"either a statement or an opinion",
			"a clever opening which catches the reader's attention",
			"a major contention or argument about something",
			"general details about the story or subject",
			"identification of the main subject",
			"clear and unbiased evidence",
			"a statement of purpose such as \"I intend to show...\"",
			"a statement of belief about the subject \"I believe that...\"",
			]
	}
,
"An effective thesis must do which of the following (choose the best answer):":
	{
		"correct":[
			"answer the question of so what, or why does this matter?",
			"offer your readers a quick preview of what your paper is going to be about",
			"focus your paper on a very specific, debatable point",
			"give your audience guidance about the conclusions you draw in the paper",
			"be about a sentence to two sentences near the end of your first paragraph",
			"describe the main idea of your paper and the main argument that you are trying to make",
			],
		"incorrect":[
			"catch the reader's attention with a thought-provoking question or startling fact.",
			"offer a very general statement about the topic.",
			"tell the reader everything you intend to do in the paper.",
			"state your opinion on the subject clearly and simply: ex. I think war is a terrible thing.",
			"show the reader how your thesis developed",
			"tell your reader that you are going to create your thesis statement: ex. In this statement I will show you how...",
			"get your readers attention.",
			"give your reader something to excite them about your topic.",
			"show the reader you know what you are talking about by giving many specific examples",
			]
	},

	"Which of the following is TRUE about an effective thesis statement?":
	{
		"correct":[
			"Claim + Reason = Thesis Statement",
			"add a because clause to your assertion to support it.",
			"your thesis should guide your audience about the conclusions they should draw from your paper.",
			],
		"incorrect":[
			"Don't write your ",
			"Claim + Reaction = Thesis Statement",
			"add a for exampe clause to explain exactly what your claim means",
			"your thesis should not guide but state exactly what conclusions are the correct ones to draw about your subject",
			"restate the main topic",
			"always come at the end",
			"always state \"I intend to prove...\" in your paper",
			"be free of any specific details",
			"leave your subject vague and general so that you can develop it later"
			]
	},
	"Which of the following is an effective thesis statement?":
	{
		"correct":[
			"Magazine ads and commercials can ultimately influence how women see themselves and how they behave and can lead to harmful behaviors such as eating disorders.",
			"Prejudgments are harmful because they limit the lives of the stereotyped individual and the person doing the stereotyping.",
			"Frankenstein works for power and fame when the creature works for friendship and acceptance",
			"The deeper thoughts and internal feelings of Frankenstein and the creature mirror each other’s frustrations and thirst for revenge. ",
			"In Frankenstein by Mary Shelley, Victor Frankenstein and the creature are compared as selfish beings but are also contrasted as Frankenstein being emotionally unstable and the creature being bent on revenge; these characteristics cause death and hurt in their own lives based off of the hatred they have for each other",
			"The untitled poem by William Strafford shows the contrast between war and peace. Society as a whole has accepted war as a necessary evil, but overall has praised war as a viable solution to solving problems. War is made into heroic and romantic images and stories, but in reality war is a terrible, destructive thing.  William Strafford’s poem shows how equally grand and pristine a field is, free from the scars that war leaves on nature",
			"Death opens the eyes to the many people who took advantage of what they had living. Although at first Emily wants to return to what she knows as normal, she realizes that the living live blind and ignorant",
			],
		"incorrect":[
			"Many women suffer from eating disorders.",
			"Many people in the world are victims of stereotyping.",
			"When Our Town takes a twist and describes death and life you begin to see a contrast that contributes to the meaning of the work.",
			"The two different points of views of Victor and the creature tell two different stories that at the end come together to piece the story together.",
			"By showing the difference in living and dead, what each represents, and how the contrast contributes to the meaning of the work makes this piece of work very dynamic.",
			"The play “Our Town” has a little town like our Monett.",
			"“Our Town” leaves the setting to your imagination and the town I imagined and the actual town described are a lot alike and a lot different.",
			"The characters Victor and the creature share their sides of the same story, describing two contrasting ideas of the other in order to spark thought in the reader.",
			]
	},
}



type_s = "Writing Process"
prompt = "Choose the best complete sentence which identifies a theme that is consistent with the topic and the purpose given."
prompt2 = "Choose a complete thesis statement created from the theme given below."

def make_thesis_questions(number):
	choices = thesis_questions.items()
	s=""
	for x in range(number):
		random.shuffle(choices)
		for key,value_dict in choices:
			
			s+="Writing Process\t\t"
			correct= random.choice(value_dict["correct"])
			random.shuffle(value_dict["incorrect"])
			incorrect = value_dict["incorrect"][:4]
			s+=key+"\t"
			s+='\t'.join([correct]+incorrect)
			s+="\n"

	return s

	#return thesis_questions.


def make_packet(**kwargs):
	s=""+make_thesis_questions(2)
	#print make_thesis_questions(2)
	type_s = kwargs.get("type_s","Writing Process")
	number = kwargs.get("number",1)
	prompt = kwargs.get("prompt","Choose the best complete sentence which identifies a theme that is consistent with the following: ")
	#questions = kwargs.get("questions","")
	for x in range(number):
		random.shuffle(questions)
		for packet in questions[:2]:
			#print packet
			choice = random.choice(packet.keys())

			correct = packet[choice]
			#print choice
			s+="{}\t{}\t{}{}\t{}\t".format(type_s,"",prompt,choice,correct)

			for key in packet.keys():
				if key !=choice:
					s+="\t"+packet[key]
			s+="\n"
	return s


print make_packet(number=4)