# -*- coding: utf-8 -*-
"""
essay question

"""


passage = """
A Closer Look at the Sameness
	" 'It wasn't a practical thing, so it became obsolete when we went to the Sameness.' " (84) The Giver, by Lois Lowry, is told from the perspective of a twelve-year-old boy named Jonas growing up in a Utopian society. At the Ceremony of Twelve, where every Twelve receives their life-long occupation. Jonas finds out he has been selected to be the Receiver of Memory, the most honored of Elders. The current Receiver, called Giver by Jonas, transfers memories of pain, joy, feelings, and color to him. As he receives each memory, he yearns for a life outside of the one he has been trapped in for so long. This book proves that being "perfect" is not as great as it sounds. The Sameness, what the Utopian society Jonas lives in was based upon, has no real benefits to the community because there are no feelings, no diversity, and no choices.
	Everyone in Jonas' community feels the same way towards each other, which means that they have no feelings. This makes it harder for them to have empathy. " 'It was your first Stirrings...you're ready for the pills.'....he swallowed the pill...the feelings had disappeared. The Stirrings were gone." (37-39) This quote is evidence that there are no feelings in this society. The Elders even make more emotional citizens (teenagers and adults) take pills to subdue their feelings. " 'Love.' It was a word and concept new to him." (125) When Jonas is transmitted the memory of love, he perceives the feeling and repeats the word to himself because he has never used that word before, let alone known what it meant. This is yet another fact that proves that the community cannot benefit from not having any feelings. Without feelings, you cannot have empathy. Empathy is important; it helps us understand what the other person is feeling and helps someone learn how to deal with a problem independently. But if the other person isn't feeling anything, then you cannot have empathy. Not having empathy also makes it harder to have friends. 
	Without diversity in a community, it's harder to have friends and learn team-building skills when you have so much in common with them. "His childhood, his friends...-all that seemed to be slipping away from him." (135) This quote was pulled from the part after Jonas has been transmitted all tons of memories via the Giver. Once he's had a taste of color and life and feelings and his knowledge has been augmented, he cannot relate to people so bland because he's had to much in common with them. " 'You ruined it,' Asher said in an irritated voice." (134) Asher says this when Jonas has been transmitted many memories by Giver. Jonas ruined their game because it depicted war, which is the memory Jonas was transmitted recently. Even though it doesn't explain it explicitly in the book, Jonas also stops it because he feels like he has too much in common with Asher and the others. Think about your best friendships over the years. In most cases, inseparable friends have a few similarities but some differences as well. Friends are vital; someone can learn the same skills they would working in a team and more: politeness, compromise, kindness, etc. These qualities are very important in a person. Someone can also learn some of these skills from mistakes. 
	In The Giver society, there are no choices that could make you more diverse than your peers. Without choices, citizens are missing out on important life lessons that can help you later on in life. "Asher ran through the standard apology phrase rapidly, still catching his breath." (3) One of the rules in The Giver society is that you must apologize each time you break one of the rules. If someone is given the choice to apologize, they will gradually understand why they apologize: to show that he/she is rueful of their action(s). If they are forced to do it, it becomes mindless and doesn't mean anything. "Two children-one male, one female-to each family unit. It was written very clearly in the rules." (8) Another rule in The Giver society is that there is a limit on how many children you can have. If you decide to have a third child (in the real world), but decide it is too much work, you can put the baby up for adoption and know you should only have two children. Without choices, there are no mistakes. Without mistakes, there are no lessons learned. 
	The community in The Giver is a boring and uneventful town in a Utopian society. There are no choices, no feelings, no diversity. Those are key elements on the road to being successful people with the ability to live in their own. Therefore, the Sameness has no real advantages. Think about not having any choice, having no diversity, no feelings. Essentially being brainwashed.  Without feelings, there cannot be empathy. Without diversity, there cannot be friends. Without choices, there cannot be life-lessons. In one part of the book, Giver explains to Jonas what the sameness is. He says that snow was not practical, so it became obsolete when they went to the Sameness. Even if snow was not practical, it still provides joy and happiness. It should be a right to have it, even though it is not necessary.  
"""

print passage

questions ={
'q':["Identify the thesis in the introduction:"],
'a':["The Sameness, what the Utopian society Jonas lives in was based upon, has no real benefits to the community because there are no feelings, no diversity, and no choices.",
"",
"",
],
'c':["\" 'It wasn't a practical thing, so it became obsolete when we went to the Sameness.' \" (84)"
]
}
"""

	" 'It wasn't a practical thing, so it became obsolete when we went to the Sameness.' " (84) The Giver, by Lois Lowry, is told from the perspective of a twelve-year-old boy named Jonas growing up in a Utopian society.
	 At the Ceremony of Twelve, where every Twelve receives their life-long occupation.
	  Jonas finds out he has been selected to be the Receiver of Memory, the most honored of Elders.
	   The current Receiver, called Giver by Jonas, transfers memories of pain, joy, feelings, and color to him.
	    As he receives each memory, he yearns for a life outside of the one he has been trapped in for so long.
	     This book proves that being "perfect" is not as great as it sounds.
"""

"THe first part of your essay","introduces your reader to the topic with a hook"
"The second part of your essay","states the topic"
"The third part","states the point of the essay."

"""
The first part .
Kenya's Culture
Building a Model Train Set
Public Transportation

The second part states the point of the essay.
has a rich and varied history
takes time and patience
can solve some of our city's most persistent and pressing problems
Or in the second part you could simply list the three main ideas you will discuss.
has a long history, blends traditions from several other cultures, and provides a rich heritage.
requires an investment in time, patience, and materials.
helps with traffic congestion, resource management, and the city budget.
Once you have formulated a thesis statement that fits this pattern and with which you are comfortable, you are ready to continue.\

"""

import random

s_nouns = ["He", "His mom", "The king", "Some guy", "A cat with rabies", "A sloth", "His sister", "This cool guy his gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of their mothers", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''

    print random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
sing_sen_maker()




