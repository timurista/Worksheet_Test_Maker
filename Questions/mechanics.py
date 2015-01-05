from question import Question, Packet
# The antecedent of a pronoun is the word or group of words referred to by the pronoun. Ben rode his bike to school. (Ben is the antecedent of his.)
# Mechanics
from random import randrange, choice

def get_comma_large_numbers_question():
	number1 = "%s" % randrange(1000,100000,1000)
	number2 = "%s" % randrange(110000,2000000,1000)	
	c_number1 = "{0:,}".format(int(number1))
	c_number2 = "{0:,}".format(int(number2))
	randidx = int(choice([1,2,4]))
	l1 = list(number1)
	l2 = list(number2)
	l1.insert(randidx,',')
	l2.insert(randidx,',')
	num_error1 = ''.join(l1)
	num_error2 = ''.join(l2)
	stems = [
	"They may have arrived as recently as XX1 million years ago or as long as XX2 years.",
	"We think they arrived at least XX1 years ago but some say they are older than XX2 years.",
	"The ancient artifact was at least XX1 years old but some argue it dates back more than XX2 years."
	]
	incorrect = choice(stems).replace("XX1",number1).replace("XX2",number2)
	incorrect1 = choice(stems).replace("XX1",num_error1).replace("XX2",c_number2)
	incorrect2 = choice(stems).replace("XX1",c_number1).replace("XX2",num_error2)
	incorrect3 = choice(stems).replace("XX1",num_error1).replace("XX2",num_error2)
	correct = choice(stems).replace("XX1",c_number1).replace("XX2",c_number2)
	return "Comma\tWhich sentence correctly formats the number with commas?\t{}\t{}\t{}\t{}\t{}\t".format(incorrect,correct,incorrect1,incorrect2,incorrect3)

# 11.1 - Capitalization

def make_packet(number=1):
	qdict = {"correct capitalization":
		[
		"After visiting the zoo, Vader and Sally caught sight of a lion near Magee Road.",
		"Once she came to the water park, Jill caught sight of a giant turtle outside Oak Street.",
		"John and Jill found Martha and Sam at the water park.",
		"Due to the success of her children's books, J. K. Rowling is now one of the most well-known and best-selling British authors of all time.",
		"China is the largest country entirely in Asia, the world's largest continent.",
		"Last Wednesday my boss flew to Europe for a technology conference on parallel-programming.",
		"In terms of attendance, New York City has the largest  St. Patrick's Day parade in the country.",
		"John D. Rockefeller was a famous American business magnate and philanthropist who earned his fortune from an oil company he co-founded in Ohio.",
		"In Canada, Thanksgiving is always celebrated on the second Monday in October.",
		"Over 2,000 people attended the rally for Harold Brown, governor of Texas.",
		"Over 2,000 people attended the rally for Governor Brown.",		
		"At night, she spoke to Uncle Vernon on the phone.",
		
		],
		"incorrect capitalization":[
		"After visiting the zoo, Vader and Sally caught sight of a lion near magee road.",
		"After visiting the Zoo, Vader and Sally caught sight of a lion near magee road.",
		"After visiting the Zoo, Vader and Sally caught sight of a lion near Magee Road.",
		"After visiting the zoo, Vader and Sally caught sight of a Lion near Magee Road.",
		"John and Jill found Martha and Sam at the Water Park.",
		"Due to the success of her children's books, J. K. rowling is now one of the most well-known and best-selling british authors of all time.",
		"Due to the success of her children's books, J. K. Rowling is now one of the most well-known and best-selling british authors of all time.",
		"Due to the success of her children's books, J. K. rowling is now one of the most well-known and best-selling British authors of all time.",
		"China is the largest country entirely in asia, the World's largest continent.",
		"China is the largest country entirely in asia, the world's largest continent.",
		"Last wednesday my boss flew to Europe for a technology conference on parallel-programming.",
		"Last Wednesday my boss flew to europe for a technology conference on parallel-programming.",
		"Last Wednesday my boss flew to Europe for a Technology conference on Parallel-Programming.",
		"Once she came to the water park, Jill caught sight of a giant turtle outside oak street.",
		"Once she came to the water park, Jill caught sight of a giant Turtle outside Oak Street.",
		"Once she came to the Water Park, Jill caught sight of a giant Turtle outside Oak Street.",
		"In terms of attendance, New York city has the largest  St. Patrick's Day parade in the country.",
		"In terms of attendance, New York City has the largest  St. Patrick's day parade in the country.",
		"John D. Rockefeller was a famous American business magnate and philanthropist who earned his fortune from an oil Company he co-founded in ohio.",
		"John D. Rockefeller was a famous American business magnate and philanthropist who earned his fortune from an oil Company he co-founded in Ohio.",
		"In canada, Thanksgiving is always celebrated on the second monday in October.",
		"In canada, Thanksgiving is always celebrated on the second monday in october.",
		"In Canada, Thanksgiving is always celebrated on the second monday in october.",
		"Over 2,000 people attended the rally for Harold Brown, Governor of Texas.",
		"At night, she spoke to uncle Vernon on the phone.",
		]
	}
	#print qdict
	p = Packet([Question(q,qdict=qdict,qsection="Capitalization") for q in qdict])
	return p.make_packet(number)
	#+get_comma_large_numbers_question()

if __name__=="__main__":
	print "testing..."
	#print get_comma_large_numbers_question()
	print make_packet(5)


# 11.2 - End Punctuation
# 11.2.1 - End Punctuation Mechanics - Period
# 11.2.2 - End Punctuation Mechanics - Question Mark
# 11.2.3 - End Punctuation Mechanics - Exclamation Point
# 11.3 - Comma
# 11.3.1 - Comma Mechanics - Series (Oxford)
# 11.3.2 - Comma Mechanics - Compound Sentences
# 11.3.3 - Comma Mechanics - Introductory Phrases
# 11.3.4 - Comma Mechanics - Nonessential Elements
# 11.3.5 - Comma Mechanics - Dates
# 11.3.6 - Comma Mechanics - Addresses
# 11.4 - Semicolon
# 11.4.1 - Semicolon Mechanics - Combining Related Independent Clauses 
# 11.4.2 - Semicolon Mechanics - Series
# 11.5 - Colon
# 11.5.1 - Colon Mechanics - List
# 11.5.2 - Colon Mechanics - Introducing Explanations 11.6 - Parentheses
# 11.7 - Dash
# 11.8 - Hyphen
# 11.9 - Apostrophe
# 11.9.1 - Apostrophe Mechanics - Possessives 11.9.2 - Apostrophe Mechanics - Contractions
# 11.10 - Formatting Titles
#11.10.1 - Quotation Marks (Poem, Story, Article, Chapter, Song, Webpage, TV Episode) 11.10.2 - Underline or Italics (Book, Periodical, Play, Film, Artworks, TV Show, Website)
# 11.11 - Punctuating Dialogue

# capitalization
# end punctuation
# comma
# 

# 15.2 - Setting
# 15.3 - Conflict
# 15.3.1 - Internal
# 15.3.2 - External
