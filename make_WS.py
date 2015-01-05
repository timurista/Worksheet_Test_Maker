# -*- coding: utf-8 -*-
import sys
import os
from random import shuffle
from worksheet_maker import Worksheet
#from Questions import errors_adv,characterization,conflict,gerund_apps,vocab_sents
from Questions import main_sub_clauses,type_sentence,mechanics,verb_tense, lit_devices,antecedent_pronouns,subj_obj_pronouns,vocab_sents,apostrophe,pronouns_id, personal_pronouns

#words = ["humdrum","interminable","germinate","interrogate","alliance","anecdote","entreat","iota","consolidate","fallible","maul","counterfeit","fickle","potential","docile","fugitive","radiant","dominate","grimy",]
words = ["alliance","spirited",
"browse","substantial","tamper","tactful",
"anonymous","dynamic","eradicate","grim","dupe",
"frustrate","transparent"]
def main():
	s=""
	#s+=vocab_sents.make_packet(words,10)
	# s+=conflict.make_packet()
	# s+=errors_adv.make_packet()
	# s+=characterization.make_packet()
	# s+=gerund_apps.make_packet(1)
	#s+=lit_devices.make_packet(5)
	s+=main_sub_clauses.make_packet(3)
	#s+=verb_tense.make_packet(4)
	#s+=antecedent_pronouns.make_packet(5)
	#s+=apostrophe.make_packet(5)
	#s+=subj_obj_pronouns.make_packet(3)
	#s+=type_sentence.make_packet(3)
	#s+=mechanics.make_packet(5)
	s+=pronouns_id.make_packet(5)
	s+=personal_pronouns.make_packet(2)
	Worksheet("Practice Mon Wk 19",s).make_worksheet(type="Worksheet",questions_per_page="6",delimmter="<br>")

main()