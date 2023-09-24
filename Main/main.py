import sys
sys.path.append("../Rubik")
from Rubik import RubikCube



# Initialize Cube
rub = RubikCube("../Solution/Solution.txt")
OrderedCube = rub.Rubik
CP = rub.CornerPeices
SP = rub.SidePeices

# Next Steps
# CP, SP = rub.randomizer(CP, SP, 500)
CP, SP = rub.rotateRow(CP=CP, CornerGrouping=rub.topRowC, SP=SP, SideGrouping=rub.topRowS, RotDirection="CW")

rub.PlotRubik(CP, SP)

CP, SP = rub.BeginnerAlgorithm(CP,SP)


rub.PlotRubik(CP, SP)
print(len(rub.commands))


rub.sendCommands()

