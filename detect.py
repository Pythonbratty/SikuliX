from guide import*
text( Pattern("P2-1.PNG").similar(0.95),"Press Table")
type("Press Table")

text( Pattern("P3-1.PNG").similar(0.71),"Floor Court side")
type("Floor Court side")
text(Pattern("1531297835830.png").exact(),"Floor Court Side")
type("Floor Court side")
text( Pattern("P4-1.PNG").similar(0.78).targetOffset(-110,-9),"Floor Court Logo")
type("Floor Court Logo")
text( Pattern("1530885319211.png").similar(0.60),"Floor Court Logo")
type("Floor Court Logo")
text( Pattern("_iig_35_E711.png").exact().targetOffset(-7,-29),"Chair Covers")
type("Chair Covers")
text(Pattern("Cr_CI5C1CCC3.png").similar(0.96).targetOffset(3,-17),"Chair Covers")
type("Chair Covers")
show(3)
exit(1)