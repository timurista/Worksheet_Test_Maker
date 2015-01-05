#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

 """
from bs4 import BeautifulSoup
import random
import urllib
import re
import sys
from nltk.corpus import wordnet as wn
from pattern.en import lemma, wordnet

words = """
alight
lubricate
customary
mutual
brood
culminate
downright
drone
goad
indulge
ingredient
literate
loom
luster
miscellaneous
oration
peevish
"""
words = words.strip().split('\n')

def make_test(words):
	#date for worksheet
	#today = datetime.date.today()
	#date = today.strftime("%a-%b-%Y")
	title = words[0]+"-"+words[len(words)-1]
	csv=""
	html=""
	html_ans=""

	# for the worksheet
	html = "<html><meta charset=\"UTF-8\"><body><h1>Vocab Test: "+title+"</h1>"
	# TEST
	html_ans+="<h2>TEST Answers</h2>"
	
	# shuffle words
	random.shuffle(words)

	html+="<ol>"
	html_ans+="<ol>"

	reload(sys)
	sys.setdefaultencoding("utf-8")

	#print words
	for word in words:
		# Get a file-like object for the Python Web site's home page.
		f = urllib.urlopen("http://www.reference.com/example-sentences/"+word)
		# Read from the object, storing the page's contents in 's'.
		s = f.read()
		f.close()
		if s:
			try:
				# make soup to parse contents
				soup = BeautifulSoup(s)
				#if soup:
				sentences = soup.findAll("div" , { "class" : "example" })

				#print sentences
				# make random choice
				sent = random.choice(sentences).text

				#print sent
				if sent:
					new_sent = re.compile(re.escape(word), re.IGNORECASE)
					syn_word = "<u>"+random.choice(get_synonym_words(word))+"</u>"

					new_sent.sub(syn_word, sent)

					# to replace, we need to use case insensitive words
					#html+= "<li>"+sent.replace(word,syn_word)
					html+="<li>"+new_sent.sub(syn_word, sent)

					new_words = [w for w in words if w != word]

					random.shuffle(new_words)
					answers = [word,new_words[0],new_words[1],new_words[2],new_words[3]]

					# save ans to new html
					#sent.replace(word,"<b><u>"+word+"</b></u>")
					html_ans +="<li>"+new_sent.sub("<b><u>"+word+"</b></u>", sent)+"</p>"
					csv+="Vocabulary\t\t"+new_sent.sub(syn_word, sent)+"\t"+answers[0]+"\t"+answers[1]+"\t"+answers[2]+"\t"+answers[3]+"\t"+answers[4]+"\n"

					#print answers
					random.shuffle(answers)
					choices_string = "a) "+answers[0]+",&nbsp;&nbsp; b) "+answers[1]+",&nbsp;&nbsp; c) "+answers[2]+",&nbsp;&nbsp;d) "+answers[3]+",&nbsp;&nbsp;e) "+answers[4]
					html+= "<br>"+choices_string+"<p></li>"
					html_ans += "<br>"+choices_string+"</p></li>"
			except Exception, e:
				print e
				continue



	#return
	print csv
	# html_file = open("Worksheet_"+title+".html",'w')
	# html_file.write(html)
	# html_file.close

def get_synonym_words(word):
	syns_list = []
	word = word.encode('utf-8')
	#print word
	if len(word)>2:
		syns = wn.synsets(lemma(word))
		if not len(syns):
			syns = wn.synsets(word)
		#print syns,lemma(word)
		#print "syns",syns
		for syn in syns:
			if syn.name not in syns_list:
				#print "syn lemma names", syn.lemma_names
				syns_list+=syn.lemma_names
				#print syns_list
			
			for h in syn.hypernyms():
				syns_list+=h.lemma_names
			#for holo in syn.hyponyms():
			#	syns_list+=holo.lemma_names
	#print "final syn list",syns_list
	return [w.replace("_"," ") for w in syns_list if w not in [word]]


random.shuffle(words)
#print words
#print get_synonym_words('adjacent')
#print wn.synsets('vicious')
#print wordnet.synsets('vicious')
make_test(words)