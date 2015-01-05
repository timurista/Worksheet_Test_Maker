import sent_maker
import random
import re

# quetion template
class question_template:
	def __init__(self,name, **kwargs):
		self.name = name
		self.fn_list = kwargs.get("fn_list",[None])
		for key,value in kwargs.items():
			setattr(self, key, value)

	def make_word_question(self,type_name):
		#correct = 
		#re.findall('(\w+)+',sentence)
		pass


	def make_id_question(self,type_name):
		correct = type_name
		choices = [k for (k,v) in self.fn_list.items() if k!=type_name]
		random.shuffle(choices)

		string = self.name+"\tIdentify the <u>word</u> in the following sentence:"+"\t"
		string+= sent_maker.find_type_with_function(self.fn_list[correct])+"\t"+correct
		for c in choices[:4]:
			string+="\t"+c
		# random choice at end
		return string

	# generating function for question packets
	def make_packet(self,number):
		s=""
		for n in range(number):
			for key in self.fn_list:
				s+=self.make_id_question(key)+"\n"
		return s

#print question_template("question").fn_list