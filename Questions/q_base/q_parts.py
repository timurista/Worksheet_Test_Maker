# -*- coding: utf-8 -*-
import re
import random

def make_question_tuples(**kwargs):
	section_name = kwargs.get("section_name","Question")
	prompt = kwargs.get("prompt","Prompt")
	correct = kwargs.get("correct",[])
	wrong_answers = kwargs.get("wrong",[])
	choice_number = int(kwargs.get("choice_number",4))
	return (section_name,prompt,correct,wrong_answers,choice_number)



