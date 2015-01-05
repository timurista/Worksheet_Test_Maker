import re
import sys
import csv
import os
import random
from os import listdir

# constants
LETTERS = {0:"a) ",1:"b) ",2:"c) ",3:"d) ",4:"e) "}

class Worksheet():
	def __init__(self,name,questions):
		self.name = name
		self.questions = questions
	def make_worksheet(self,**kwargs):
		directory= kwargs.get("directory","./Worksheets")
		test_type = kwargs.get("type","Worksheet")
		qper_page = kwargs.get("questions_per_page",6)
		delimmter= kwargs.get("delimmter",", ")
		qarray = [s.split("\t") for s in self.questions.split("\n")]
		print len(qarray)
		html_css = """
			<style> body {font-size: 11pt; } li{ margin-bottom: 10pt;} 
			li:nth-of-type(%sn+%s) { background-color: lightblue; page-break-after:always;} 
			.edit [contenteditable="true"]
			</style>
			""" % (qper_page,qper_page)
		html_css+="<title>English II -- tim.urista@basis.orovalley.org -- {}</title>".format(self.name[:10]+"...")
		html ="<html><meta charset=\"UTF-8\">"+html_css+"<body>"
		html+="<div contenteditable=\"true\"><h2>"+test_type+": "+self.name+"&nbsp;</h2>"

		html_ans ="<h1>Test ANSWERS "+self.name+"</h1>"

		# setup the ol
		html+="<ol>"
		html_ans+="<ol>"

		# header

		all_questions = {}
		all_ans = {}
		counter = 0;
		for question in qarray:
			# make dict with headers as set of questions1
			if question[0] not in all_questions and len(question[0])>1:
				all_questions[question[0]]=""
				all_ans[question[0]]=""

		assert len(all_questions)>0, "all questions dict not working"
		
		# append questions to dict
		for question in qarray:
			if len(question)>1:
				counter+=1
				#print counter
				section = question[0]
				all_questions[section]+="<li>&nbsp;"
				
				if len(question[1])>1: all_questions[section]+= question[1]+"<br>"
				if len(question[2])>1: all_questions[section]+= question[2]

				right_answer = question[3]
				# make answer
				choices = question[3:7]

				# shuffle choices
				random.shuffle(choices)

				# make answer
				l = choices.index(right_answer)
				#print len(all_ans),section

				all_ans[section]+="<div><li>"+LETTERS[l]+right_answer+"</li>"

				# make choices appear as li in text
				all_questions[section]+="<ul>"
				all_questions[section]+=""+LETTERS[0]+choices[0]+delimmter
				all_questions[section]+=""+LETTERS[1]+choices[1]+delimmter
				all_questions[section]+=""+LETTERS[2]+choices[2]+delimmter
				all_questions[section]+=""+LETTERS[3]+choices[3]
				#all_questions[section]+="<br>"+LETTERS[4]+choices[4]+""
				all_questions[section]+="</ul></li>"
				#counter+=1;
				#if counter%6==0:
				#	all_questions[section]+="<div style=\"page-break-after:always;\"></div>"
		
		# make the proper html
		for section in all_questions:
			html+="<h3>"+section+" Section</h3>"	
			html+=str(all_questions[section])

			# do answers
			html_ans+="<p><strong>"+section+"</strong></p>"				
			html_ans+=str(all_ans[section])


		# close questions
		html+="</ol></div>"
		html_ans+="</ol>"

		# make directory if it does not exist
		direc = directory+"/"+self.name.replace(" ","_")
		if not os.path.exists(direc):
			os.makedirs(direc)

		# write files
		html_file = open(direc+"/WS_"+self.name+".html",'w')
		html_file.write(html)
		html_file.close

		# make ans file
		html_file_ans = open(direc+"/WS_ANS_"+self.name+".html",'w')
		html_file_ans.write(html_ans)
		html_file_ans.close
		print "made test... %s in %s  " % (self.name,direc)




