import re
tags = "Of/IN the/AT women/NNS and/CC children/NNS stayed/VBD at/IN the/AT Albrights'/NPS$ ./."
#tags = "With/IN a/AT roar/NN of/IN pain/NN and/CC fury/NN Jess/NP made/VBD his/PP$ attack/NN ./."
#tags = "Of/IN This/DT time/NN no/AT wire/NN came/VBD whipping/VBG into/IN the/AT"
tags = "The/AT bartender/NN brought/VBD Rourke's/NP$ drink/NN and/CC Shayne/NP laid/VBD"
pattern = "(\w+\/[I]\w+ ){0,}(?:(\S+)\/[NJ]\w+ ){0,}(?:(\S+)\/[NJ]\w+ ){1,}(?:([any]?[nore][drt])\/\w+ ){1,}(?:(\S+)\/[J]\w+ ){0,}(?:(\S+)\/N\w+ )(?:\w+\/V\w+)"
finds = re.findall(pattern,tags)


print len(finds),finds

from pattern.en import parse

print parse("""Here is your birthday present.""")