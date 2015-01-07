from question import Packet,Question,sent_Question, make_packets

def make_packet(number=1):
	return make_packets(number,qdict={
		"transitive main verb":[
		"She <u>ate</u> a bag of chips for dinner.",
		"He <u>ate</u> a large stack of pancakes for breakfast.",
		"She <u>wore</u> a coat in the evening.",
		"They <u>wore</u> coats during the winter.",
		"All of them <u>ate</u> pie in the morning.",		
		"Brian <u>memorized</u> the opening line of his speech.",
		],
		"intransitive main verb":[
		"She <u>slept</u> all day.",
		"She <u>ran</u> to the mall.",
		"Huffing and puffing, we <u>arrived</u> at the classroom door with only seven seconds to spare.",
		"James <u>went</u> to the campus cafe for a steaming bowl of squid eyeball stew.",
		"Around fresh ground pepper, Sheryl <u>sneezes</u> with violence.",
		"He <u>slept</u> until the day was over.",
		"In the evening, he <u>slept</u> for an interminable amount of time.",
		"All of them <u>drove</u> there during the day.",
		"The telephone <u>rings</u> in both offices.",
		"In the evenings, Glenda <u>sits</u> on the front porch to admire her immaculate lawn.",
		],
		"linking main verb":[
		"I <u>am</u> I true hero.",
		"She <u>was</u> a young girl.",
		"She <u>looked</u> the young teenager.",
		"They <u>appeared</u> tired after the long journey up the mountain.",
		"Irish Americans <u>are</u> one of this country's largest immigrant groups.",
		"Milk <u>turns</u> bad quickly unless refrigerated.",
		"His forehead <u>feels</u> cool to the touch.",
		"Many Irish felt hopeful about the endless job opportunities in America.",
		"Irish immigrants were important in building the famous Erie Canal and many highways, railroads, and cities.",
		"You <u>look</u> exhausted after studying all night.",
		],
		"auxiliary or helping verb":[
		"She <u>was</u> helping her.",
		"He <u>could</u> have helped them.",
		"We <u>would</u> like to do it.",
		"I <u>am</u> baking chocolate-broccoli muffins today.",
		"Alex must wait a while longer because the muffins <u>are</u> cooling by the window.",
		"I <u>am</u> renting my guest house to my neighbor.",
		"She <u>had</u> stolen the car already by then.",
		],
		},qprompt="In the following sentence, what is the verb type?",qsection="Verb Types")

if __name__=="__main__":
	print "testing..."
	print make_packet(10)


"""
Question 2

In the following sentence, what is the verb type?

linking

intransitive

transitive

none of the above

Correct answer: B
"""

