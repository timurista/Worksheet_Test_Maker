"""Identifying Antecedent Pronoun"""
from question import Question,Packet

qdict={
"correct pronoun-antecedent agreement":[
"<u>He</u> came home to <u>his</u> own car.",
"<u>He</u> found <u>his</u> sneakers in the garage.",
"<u>Harry</u> gave <u>himself</u> a baseball for Christmas.",
"<u>Jill</u> found <u>her</u> missing sock on top of the dresser.",
"<u>The man named Voldemort</u> gave the girl named Hermione <u>his</u> own surprising gift for Christmas.",
"<u>The boy</u> gave the girl <u>his</u> tiny little pot for Christmas.",
"<u>They</u> found <u>themselves</u> in the midst of a great struggle with Greyback.",
"<u>The man named Voldemort</u> discovered that he held the secret to <u>his</u> success in his own hands.",
"<u>The man named Voldemort</u> hated <u>himself</u> after Harry defeated him.",
"The man named Voldemort found his wand to be too weak for Dumbledore.",
"The man named Voldemort found his wand in need of serious repair.",
"We found ourselves in the midst of a huge explosion.",
"I found myself in a real fit of pain.",
"Somebody has left their bag on the floor.",
"A can of lima beans sits on its shelf.",
"Josh and Jill made their presentation Monday.",
"Josh and Fiona made their presentation yesterday.",
"On Tuesday, Gandalf and Bilbo made their speech.",
"The jury read its verdict.",
"The crowd found its home inside the tree.",
"The flock went its own way for the summer.",
"Jury members gave their individual opinions.",
"The flocks gave their quaks in agreement with the jury.",
"The school had its roof repaired over the summer.",
"The swarm of bees had its nest inside Greyback's werewolf home.",
"The herd of cattle gathered into its cramp little barn for the night.",
"The two boys who owned that <u>home</u> found fortune inside one of <u>its</u> rooms.",
"The children, who were sometimes happy, had their own rooms.",
"They were so bored with the lecture, <u>they</u> found themselves drooling on <u>their</u> own homework.",
],
"incorrect pronoun-antecedent agreement":[
"The boy gave the girl its tiny little pot for Christmas.",
"He found yourself sneakers in the garage.",
"They found them sneakers to be in the locker.",
"He gave themselves a baseball outside the locker.",
"They gave himself something fun to do during the lecture.",
"The man named Voldemort gave the girl named Hermione their own surprising gift for Christmas.",
"The man named Voldemort discovered that he held the secret to her success in her own hands.",
"The man named Voldemort hated myself after Harry defeated them.",
"The man named Voldemort found herself to be too weak for Dumbledore.",
"The man named Voldemort found yourself in need of serious repair.",
"President Lincoln delivered her Gettysburg Address in 1863.",
"A can of pinto beans sits on it's shelf.",
"Josh and Jill made his presentation Monday.",
"Josh and Jane made her presentation yesterday.",
"On Tuesday, Tom and Mr Riddle made his speech.",
"The jury read their verdict.",
"The crowd found their home inside the tree.",
"The flock went their own way for the summer.",
"Jury members gave his individual opinions.",
"The flocks gave its quaks in agreement with the jury.",
"The school had their roof repaired over the summer.",
"The swarm of bees had their nest inside Greyback's werewolf home.",
"The herd of cattle gathered into their cramp barn for the night.",
"The two <u>boys</u> who owned that home found fortune inside one of <u>his</u> own rooms.",
"The two <u>boys</u> who owned that home found fortune inside one of <u>her</u> own rooms.",
"The <u>children</u>, who were sometimes happy, had <u>its</u> own rooms.",
"They were so bored with the lecture, <u>they</u> found themselves drooling on <u>his</u> own homework.",
"He was so tired <u>he</u> fell asleep on <u>their</u> own chair.",
"<u>She</u> was so tired <u>he</u> fell asleep on his own chair.",
"He was so tired <u>he</u> fell asleep on <u>her</u> own chair.",
"They found himself strong in the face of Greyback.",
]
}
def make_packet(number=1):
	return Packet([Question(x,qdict=qdict,qsection="Antecedent Agreement") for x in qdict.keys()]).make_packet(number)

if __name__=="__main__":
	print "testing..."
	assert [Question(x,qdict=qdict,qsection="Antecedent Agreement") for x in qdict.keys()][0].get_Question()
	print make_packet(10)