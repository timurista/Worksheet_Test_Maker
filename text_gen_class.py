import random
import re
class TextGenerator():
	def underline_things(self,underlined=['subj'],excluded=['cc1']):
		self.__init__()
		#underlined_pos = underlined
		for u in underlined:
			s = "self.%s = " % (u)
			value = eval("self.%s" % (u))
			exec(s+"\"<u>%s</u>\"" % (value))

		for e in excluded:
			if len(e)>1:
				exec("self.%s = \"\"" %(e))

	def get_compound_subj(self):
		self.underline_things(['simplesubj1','simplesubj2'])
		s1 = ' '.join(self.subj1.split(" ")[:-1])+self.simplesubj1
		s2 = ' '.join(self.subj2.split(" ")[:-1])+self.simplesubj2
		formats = [
		"{pp}, {s1} {cc} {s2} {v1} {io} {do}.".format(pp=self.pp.capitalize(),\
			s1=s1,cc=self.cc1,s2=s2, v1=self.verb1,
			io=self.io1,do=self.do1),
		"{s1} {cc} {s2} {v1} {io} {do}.".format(s1=s1[0].\
			upper()+s1[1:],cc=self.cc1,s2=s2, v1=self.verb1,
			io=self.io1,do=self.do1),
		"{s1} {cc} {s2} {v1} {io} {do} {pp}.".format(pp=self.pp,s1=s1[0].\
			upper()+s1[1:],cc=self.cc1,s2=s2, v1=self.verb1,
			io=self.io1,do=self.do1),
		]
		return re.sub("\s+"," ",choice(formats))

	def get_complete_compound_subj(self):
		self.underline_things(['subj1','subj2','cc1'])

		formats = [
		"{pp}, {s1} {cc} {s2} {v1} {io} {do}.".format(pp=self.pp.capitalize(),\
			s1=self.subj1,cc=self.cc1,s2=self.subj2, v1=self.verb1,
			io=self.io1,do=self.do1),
		"{s1} {cc} {s2} {v1} {io} {do}.".format(s1=self.subj1[0].\
			upper()+self.subj1[1:],cc=self.cc1,s2=self.subj2, v1=self.verb1,
			io=self.io1,do=self.do1),
		"{s1} {cc} {s2} {v1} {io} {do} {pp}.".format(pp=self.pp,s1=self.subj1[0].\
			upper()+self.subj1[1:],cc=self.cc1,s2=self.subj2, v1=self.verb1,
			io=self.io1,do=self.do1),
		]
		return re.sub("\s+"," ",choice(formats))





	def __init__(self,**kwargs):
		self.subj1 = choice(kwargs.get("subj1",s_nouns.strip().splitlines()))
		self.subj2 = kwargs.get("subj2",choice(s_nouns.strip().splitlines()))
		self.simplesubj1=self.subj1.split(" ")[-1]
		self.simplesubj2=self.subj2.split(" ")[-1]
		self.cc1 = choice(["and also","and"])
		self.cc2 = choice(["and", "and also"])
		self.lverb = choice(kwargs.get("lverb",l_verbs.strip().splitlines()))
		self.verb1 = choice(kwargs.get("verb1",s_verbs.strip().splitlines()))
		self.io1 = choice(kwargs.get("io1",s_ios.strip().splitlines()))
		self.do1= choice(kwargs.get("do1",d_object.strip().splitlines()))
		self.pp = kwargs.get("pp",choice(p_phrase.strip().splitlines()))
		self.verb2 = choice(kwargs.get("verb2",s_verbs.strip().splitlines()))
		self.io2 = choice(kwargs.get("io2",s_ios.strip().splitlines()))
		self.do2= choice(kwargs.get("do2",d_object.strip().splitlines()))
		self.adv = kwargs.get("adv",choice(adverbs.strip().splitlines()))
		self.oc1 = kwargs.get("oc1",choice(object_complement.strip().splitlines()))
		self.oc2 = kwargs.get("oc2",choice(object_complement.strip().splitlines()))


print TextGenerator().get_compound_subj()
print TextGenerator().get_complete_compound_subj()
