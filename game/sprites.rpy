

image dianne standby = ConditionSwitch(
    "clothes_ripped", "images/sprites/battle/standby2.png",
    "not clothes_ripped", "images/sprites/battle/standby.png",)
image dianne attack = ConditionSwitch(
    "clothes_ripped", "images/sprites/battle/attack2.png",
    "not clothes_ripped", "images/sprites/battle/attack.png",)
image dianne attack2 = ConditionSwitch(
    "clothes_ripped", LiveComposite((2168, 1818),(0, 0), "images/sprites/battle/attack2.png", (0, 0), "images/sprites/battle/slash.png"),
    "not clothes_ripped", LiveComposite((2168, 1818),(0, 0), "images/sprites/battle/attack.png", (0, 0), "images/sprites/battle/slash.png"),)
image dianne counter = ConditionSwitch(
    "clothes_ripped", "images/sprites/battle/counter2.png",
    "not clothes_ripped", "images/sprites/battle/counter.png",)
image dianne charge = ConditionSwitch(
    "clothes_ripped", "images/sprites/battle/charge2.png",
    "not clothes_ripped", "images/sprites/battle/charge.png",)
image dianne charge2 = "images/sprites/battle/charge2.png"
image dianne hurt = ConditionSwitch(
    "clothes_ripped", "images/sprites/battle/hurt2.png",
    "not clothes_ripped", "images/sprites/battle/hurt.png",)



image dianne con angryfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con angrygrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con angryhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con angryneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con angryopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con angrysmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con angrysmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con angryyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne con closedfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con closedgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con closedhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con closedneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con closedopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con closedsmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con closedsmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con closedyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne con starefrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con staregrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con starehappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con stareneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con stareopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con staresmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con staresmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con stareyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne con tiredfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con tiredgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con tiredhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con tiredneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con tiredopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con tiredsmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con tiredsmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con tiredyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne con widefrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con widegrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con widehappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con wideneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con wideopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con widesmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con widesmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con wideyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne con winkfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne con winkgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne con winkhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne con winkneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne con winkopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne con winksmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne con winksmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne con winkyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/yell.png")



image dianne conripped angryfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped angrygrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped angryhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped angryneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped angryopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped angrysmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped angrysmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped angryyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/angry.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne conripped closedfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped closedgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped closedhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped closedneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped closedopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped closedsmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped closedsmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped closedyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/closed.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne conripped starefrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped staregrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped starehappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped stareneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped stareopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped staresmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped staresmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped stareyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/stare.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne conripped tiredfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped tiredgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped tiredhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped tiredneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped tiredopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped tiredsmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped tiredsmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped tiredyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/tired.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne conripped widefrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped widegrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped widehappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped wideneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped wideopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped widesmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped widesmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped wideyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wide.png",    (0, 0), "images/sprites/base1/mouths/yell.png")

image dianne conripped winkfrown = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/frown.png")
image dianne conripped winkgrit = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/grit.png")
image dianne conripped winkhappy = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/happy.png")
image dianne conripped winkneutral = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/neutral.png")
image dianne conripped winkopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/open.png")
image dianne conripped winksmall = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/small.png")
image dianne conripped winksmile = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/smile.png")
image dianne conripped winkyell = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base1/base1rip.png",    (0, 0), "images/sprites/base1/eyes/wink.png",    (0, 0), "images/sprites/base1/mouths/yell.png")






image dianne con2 agonyclench = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/agony.png",    (0, 0), "images/sprites/base2/mouths/clench.png")
image dianne con2 agonydrool = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/agony.png",    (0, 0), "images/sprites/base2/mouths/drool.png")
image dianne con2 agonygape = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/agony.png",    (0, 0), "images/sprites/base2/mouths/gape.png")
image dianne con2 agonyopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/agony.png",    (0, 0), "images/sprites/base2/mouths/open.png")
image dianne con2 agonyshriek = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/agony.png",    (0, 0), "images/sprites/base2/mouths/shriek.png")

image dianne con2 emptyclench = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/empty.png",    (0, 0), "images/sprites/base2/mouths/clench.png")
image dianne con2 emptydrool = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/empty.png",    (0, 0), "images/sprites/base2/mouths/drool.png")
image dianne con2 emptygape = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/empty.png",    (0, 0), "images/sprites/base2/mouths/gape.png")
image dianne con2 emptyopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/empty.png",    (0, 0), "images/sprites/base2/mouths/open.png")
image dianne con2 emptyshriek = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/empty.png",    (0, 0), "images/sprites/base2/mouths/shriek.png")

image dianne con2 heartclench = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/clench.png")
image dianne con2 heartclenchleak = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/clench.png",    (0, 0), "images/sprites/base2/leak.png")
image dianne con2 heartdrool = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/drool.png")
image dianne con2 heartdroolleak = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/drool.png",    (0, 0), "images/sprites/base2/leak.png")
image dianne con2 heartgape = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/gape.png")
image dianne con2 heartgapeleak = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/gape.png",    (0, 0), "images/sprites/base2/leak.png")
image dianne con2 heartopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/open.png")
image dianne con2 heartopenleak = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/open.png",    (0, 0), "images/sprites/base2/leak.png")
image dianne con2 heartshriek = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/shriek.png")
image dianne con2 heartshriekleak = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/heart.png",    (0, 0), "images/sprites/base2/mouths/shriek.png",    (0, 0), "images/sprites/base2/leak.png")

image dianne con2 weakclench = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/weak.png",    (0, 0), "images/sprites/base2/mouths/clench.png")
image dianne con2 weakdrool = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/weak.png",    (0, 0), "images/sprites/base2/mouths/drool.png")
image dianne con2 weakgape = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/weak.png",    (0, 0), "images/sprites/base2/mouths/gape.png")
image dianne con2 weakopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/weak.png",    (0, 0), "images/sprites/base2/mouths/open.png")
image dianne con2 weakshriek = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/weak.png",    (0, 0), "images/sprites/base2/mouths/shriek.png")

image dianne con2 worriedclench = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/worried.png",    (0, 0), "images/sprites/base2/mouths/clench.png")
image dianne con2 worrieddrool = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/worried.png",    (0, 0), "images/sprites/base2/mouths/drool.png")
image dianne con2 worriedgape = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/worried.png",    (0, 0), "images/sprites/base2/mouths/gape.png")
image dianne con2 worriedopen = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/worried.png",    (0, 0), "images/sprites/base2/mouths/open.png")
image dianne con2 worriedshriek = LiveComposite(    (2168, 1818),    (0, 0), "images/sprites/base2/base2.png",    (0, 0), "images/sprites/base2/eyes/worried.png",    (0, 0), "images/sprites/base2/mouths/shriek.png")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
