import os
#from nltk.parse import stanford
import nltk
from pattern.en import parse, pprint, tag, lemma

	
from nltk.corpus import conll2000
print conll2000.chunked_sents()[2]
#pprint(conll2000)
# s = "My friend Naomi ran 100 miles this morning."
# s = "An A-grade was given to Jorge by Professor Villa."
# p = parse(s,True,True,True,True)
# pprint(p)
#os.environ['STANFORD_PARSER'] = '/folder/with/standford/jars'
#os.environ['STANFORD_MODELS'] = '/folder/with/standford/jars'

# print conll2000.chunked_sents()[3]
# print conll2000.tagged_sents()[2]
#parser = stanford.StanfordParser(model_path="/location/of/the/englishPCFG.ser.gz")
#sentences = parser.raw_batch_parse(("Hello, My name is Melroy.", "What is your name?"))
#print sentences

# GUI
#for sentence in sentences:
#    sentence.draw()
