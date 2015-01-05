"""Subjective and Objective Case Pronouns	21	5	16	76 %"""
from question import Question,Packet

qdict={
"Correct Pronoun Object Case":[
"I gave it to <u>him</u>.",
"We are doing it to <u>them</u>.",
"I did it to <u>her</u>.",
"I gave it to <u>me</u>.",
"They are giving it to <u>me</u>.",
"We are doing it to <u>me</u>.",
"She did it to <u>them</u>.",
"We gave it to <u>him</u>.",
"They are giving it to <u>me</u>.",
"I gave it to <u>her</u>.",
"We are doing it to <u>us</u>.",
"They are giving it to <u>me</u>.",
"They are giving it to <u>me</u>.",
"He tried to tell <u>them</u>.",
"We gave it to <u>us</u>.",
"I tried to tell <u>them</u>.",
"He did it to <u>me</u>.",
"We gave it to <u>us</u>.",
"She gave it to <u>them</u>.",
"I tried to tell <u>us</u>.",
"She tried to tell <u>me</u>.",
"They are giving it to <u>him</u>.",
"We gave it to <u>ourselves</u>.",
"They gave it to <u>us</u>.",
"He did it to <u>me</u>.",
"He did it to <u>her</u>.",
"She tried to tell <u>us</u>.",
"I did it to <u>me</u>.",
"They are giving it to <u>them</u>.",
"I gave a banana to <u>him</u>.",
"They are doing it to <u>me</u>.",
"We are doing it to <u>me</u>.",
"I gave a banana to <u>him</u>.",
"She gave it to <u>him</u>.",
"They gave it to <u>him</u>.",
"They gave it to <u>me</u>.",
"I tried to tell <u>us</u>.",
"They gave it to <u>me</u>.",
"I tried to tell <u>us</u>.",
"I tried to tell <u>us</u>.",
"We are doing it to <u>her</u>.",
"He tried to tell <u>her</u>.",
"He gave a banana to <u>them</u>.",
"We are giving it to <u>me</u>.",
"We gave it to <u>her</u>.",
"I gave a banana to <u>her</u>.",
"They are doing it to <u>them</u>.",
"We are giving it to <u>me</u>.",
"We are doing it to <u>them</u>.",
"We gave it to <u>her</u>.",
],
"Incorrect Pronoun Subject Case":[
"<u>Her</u> did it to me.",
"<u>Me</u> did it to me.",
"<u>Her</u> did it to her.",
"<u>Her</u> gave a banana to him.",
"<u>Us</u> are doing it to me.",
"<u>Them</u> are giving it to her.",
"<u>Us</u> are giving it to us.",
"<u>Us</u> are giving it to him.",
"<u>Them</u> are giving it to them.",
"<u>Her</u> gave a banana to them.",
"<u>Us</u> are giving it to me.",
"<u>Us</u> are giving it to us.",
"<u>Him</u> gave it to us.",
"<u>Us</u> are giving it to me.",
"<u>Us</u> are giving it to them.",
"<u>Her</u> tried to tell him.",
"<u>Us</u> are giving it to them.",
"<u>Us</u> are giving it to me.",
"<u>Me</u> tried to tell them.",
"<u>Us</u> are giving it to us.",
"<u>Her</u> did it to him.",
"<u>Me</u> did it to her.",
"<u>Them</u> are giving it to her.",
"<u>Me</u> tried to tell me.",
"<u>Them</u> are doing it to me.",
"<u>Her</u> did it to her.",
"<u>Us</u> are giving it to us.",
"<u>Her</u> gave a banana to her.",
"<u>Us</u> are doing it to her.",
"<u>Me</u> gave it to her.",
"<u>Him</u> gave a banana to me.",
"<u>Me</u> did it to me.",
"<u>Us</u> are doing it to him.",
"<u>Her</u> gave it to us.",
"<u>Them</u> are giving it to me.",
"<u>Them</u> gave it to him.",
"<u>Them</u> gave it to her.",
"<u>Him</u> gave it to him.",
"<u>Her</u> gave a banana to them.",
"<u>Me</u> did it to them.",
"<u>Us</u> gave it to them.",
"<u>Them</u> are doing it to them.",
"<u>Them</u> are giving it to us.",
"<u>Us</u> are giving it to them.",
"<u>Us</u> are doing it to her.",
"<u>Him</u> gave a banana to her.",
"<u>Her</u> did it to them.",
"<u>Her</u> gave it to him.",
"<u>Him</u> gave it to him.",
"<u>Him</u> tried to tell her.",
],
"Incorrect Pronoun Object Case":[
"He tried to tell <u>I</u>.",
"She gave a banana to <u>they</u>.",
"They are doing it to <u>we</u>.",
"He gave a banana to <u>she</u>.",
"She gave it to <u>she</u>.",
"They gave it to <u>we</u>.",
"He did it to <u>he</u>.",
"We are doing it to <u>we</u>.",
"We are doing it to <u>they</u>.",
"They gave it to <u>I</u>.",
"They gave it to <u>she</u>.",
"They gave it to <u>she</u>.",
"He gave it to <u>I</u>.",
"They gave it to <u>we</u>.",
"I did it to <u>they</u>.",
"They are giving it to <u>he</u>.",
"They gave it to <u>she</u>.",
"We are doing it to <u>he</u>.",
"I did it to <u>he</u>.",
"We are giving it to <u>we</u>.",
"We are doing it to <u>they</u>.",
"They are doing it to <u>he</u>.",
"We are doing it to <u>he</u>.",
"She tried to tell <u>we</u>.",
"We gave it to <u>we</u>.",
"They gave it to <u>he</u>.",
"They are doing it to <u>she</u>.",
"We are giving it to <u>we</u>.",
"She gave it to <u>I</u>.",
"He did it to <u>they</u>.",
"They are giving it to <u>he</u>.",
"They are giving it to <u>she</u>.",
"They are giving it to <u>she</u>.",
"They are doing it to <u>she</u>.",
"They gave it to <u>she</u>.",
"We gave it to <u>they</u>.",
"I gave it to <u>they</u>.",
"I tried to tell <u>we</u>.",
"We are giving it to <u>she</u>.",
"He did it to <u>we</u>.",
"I did it to <u>we</u>.",
"She did it to <u>they</u>.",
"He tried to tell <u>they</u>.",
"We are doing it to <u>she</u>.",
"They are doing it to <u>he</u>.",
"They gave it to <u>she</u>.",
"He did it to <u>he</u>.",
"They are giving it to <u>they</u>.",
"We gave it to <u>he</u>.",
"I tried to tell <u>they</u>.",
],
}
def make_packet(number=1):
	return Packet([Question(x,qdict=qdict,qsection="Antecedent Agreement") for x in qdict.keys()]).make_packet(number)

from random import choice
if __name__=="__main__":
	print "testing..."
	subj_s = ["he","she","I"]
	subj_p =["they","we"]
	verb_s = ["gave it to","did it to","gave a banana to","tried to tell"]
	verb_p = ["gave it to","are doing it to","are giving it to"]
	io_s = ["him","her","me"]
	io_p = ["us","them"]
	
	# s=""
	# for x in range(50):
	# 	if choice([0,1]):
	# 		subj = choice(subj_s)
	# 		verb = choice(verb_s)
	# 	else:
	# 		subj = choice(subj_p)
	# 		verb = choice(verb_p)
	# 	s+="\"%s %s <u>%s</u>.\"," % (subj.capitalize(),verb,choice(io_s+io_p))+"\n"
	# print "\"Correct Pronoun Object Case\":[\n",s,"],"

	# s=""
	# for x in range(50):

	# 	if choice([0,1]):
	# 		subj = choice(io_s)
	# 		verb = choice(verb_s)
	# 	else:
	# 		subj = choice(io_p)
	# 		verb = choice(verb_p)
	# 	s+="\"<u>%s</u> %s %s.\"," % (subj.capitalize(),verb,choice(io_s+io_p))+"\n"
	# print "\"Incorrect Pronoun Subject Case\":[\n",s,"],"
	# s=""
	# for x in range(50):

	# 	if choice([0,1]):
	# 		subj = choice(subj_s)
	# 		verb = choice(verb_s)
	# 	else:
	# 		subj = choice(subj_p)
	# 		verb = choice(verb_p)
	# 	s+="\"%s %s <u>%s</u>.\"," % (subj.capitalize(),verb,choice(subj_s+subj_p))+"\n"
	# print "\"Incorrect Pronoun Object Case\":[\n",s,"],"

	assert [Question(x,qdict=qdict,qsection="Subjective Objective Case Pronouns") for x in qdict.keys()][0].get_Question()
	print make_packet(10)
