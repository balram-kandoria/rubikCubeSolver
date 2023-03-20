'''Define a structure to contain the positions of all the cubes.'''
'''A cube has 8 corner peices with 3 colors associated with it'''
'''Will need to define a direction of the color which implies having global axes and a fixed cube position'''
'''A cube has 8 side peices with 2 colors associted with it'''
'''A cube has 6 colored centered peices which never move'''

'''Matrix position for every type of peice (corner, side, center), orientation (of the colors within a specified peice)'''

'''Structure: Center Peice reference: Type of Peice: Orientation'''


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import random
import time
'Axis is define with the white, orange, and green faces. Where the White is on the XY-Plane, Green is on the XZ-Plane, and orange is on the YZ-Plane (Assuming Positive Quadrant)'
'(X,Y,Z)'


class RubikCube:
    def __init__(self):  # constructor method
        # Define RGB Values
        self.Blue = '#00FFFF'
        self.Yellow = '#FFFF00'
        self.Red = '#FF0000'
        self.Green = '#006400'
        self.White = '#D3D3D3'
        self.Orange = '#FFB52E'

        # Define Corner Peices
        # Locations: x, z, y
        # Directions: XY Plane, XZ Plane, and the YZ Plane
        self.CornerPeices = {
            # Bottom Corners start from Lower left on White face
            'C1': {'Location': (0, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0), 'Orange': (-1, 0, 0)},
            'C2': {'Location': (2, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0), 'Red': (1, 0, 0)},
            'C3': {'Location': (2, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0), 'Red': (1, 0, 0)},
            'C4': {'Location': (0, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0), 'Orange': (-1, 0, 0)},

            # Top Corners start from top left on white face
            'C5': {'Location': (0, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0), 'Orange': (-1, 0, 0)},
            'C6': {'Location': (2, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0), 'Red': (1, 0, 0)},
            'C7': {'Location': (2, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0), 'Red': (1, 0, 0)},
            'C8': {'Location': (0, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0), 'Orange': (-1, 0, 0)},
        }

        self.CornerDict = {
            # Bottom Corners start from Lower left on White face
            'C1': {'Location': (0, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0), 'Orange': (-1, 0, 0)},
            'C2': {'Location': (2, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0), 'Red': (1, 0, 0)},
            'C3': {'Location': (2, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0), 'Red': (1, 0, 0)},
            'C4': {'Location': (0, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0), 'Orange': (-1, 0, 0)},

            # Top Corners start from top left on white face
            'C5': {'Location': (0, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0), 'Orange': (-1, 0, 0)},
            'C6': {'Location': (2, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0), 'Red': (1, 0, 0)},
            'C7': {'Location': (2, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0), 'Red': (1, 0, 0)},
            'C8': {'Location': (0, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0), 'Orange': (-1, 0, 0)},
        }

        # Group the Corners by Position (Column and Row)
        self.bottomRowC = ['C1', 'C2', 'C3', 'C4']
        self.topRowC = ['C5', 'C6', 'C7', 'C8']

        self.leftColumnC = ['C1', 'C5', 'C8', 'C4']
        self.rightColumnC = ['C2', 'C6', 'C7', 'C3']

        self.frontFaceC = ['C2', 'C1', 'C5', 'C6']
        self.backFaceC = ['C4', 'C8', 'C7', 'C3']

        # Define Side Peices
        self.SidePeices = {
            # Bottom Row
            'S1': {'Location': (1, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0)},
            'S2': {'Location': (2, 1, 0), 'Red': (1, 0, 0), 'Green': (0, -1, 0)},
            'S3': {'Location': (1, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0)},
            'S4': {'Location': (0, 1, 0), 'Orange': (-1, 0, 0), 'Green': (0, -1, 0)},
            # Middle Row
            'S5': {'Location': (0, 0, 1), 'White': (0, 0, 1), 'Orange': (-1, 0, 0)},
            'S6': {'Location': (2, 0, 1), 'White': (0, 0, 1), 'Red': (1, 0, 0)},
            'S7': {'Location': (2, 2, 1), 'Yellow': (0, 0, -1), 'Red': (1, 0, 0)},
            'S8': {'Location': (0, 2, 1), 'Yellow': (0, 0, -1), 'Orange': (-1, 0, 0)},
            # Top Row
            'S9': {'Location': (0, 1, 2), 'Orange': (-1, 0, 0), 'Blue': (0, 1, 0)},
            'S10': {'Location': (1, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0)},
            'S11': {'Location': (2, 1, 2), 'Red': (1, 0, 0), 'Blue': (0, 1, 0)},
            'S12': {'Location': (1, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0)}
        }

        self.SideDict = {
            # Bottom Row
            'S1': {'Location': (1, 0, 0), 'White': (0, 0, 1), 'Green': (0, -1, 0)},
            'S2': {'Location': (2, 1, 0), 'Red': (1, 0, 0), 'Green': (0, -1, 0)},
            'S3': {'Location': (1, 2, 0), 'Yellow': (0, 0, -1), 'Green': (0, -1, 0)},
            'S4': {'Location': (0, 1, 0), 'Orange': (-1, 0, 0), 'Green': (0, -1, 0)},
            # Middle Row
            'S5': {'Location': (0, 0, 1), 'White': (0, 0, 1), 'Orange': (-1, 0, 0)},
            'S6': {'Location': (2, 0, 1), 'White': (0, 0, 1), 'Red': (1, 0, 0)},
            'S7': {'Location': (2, 2, 1), 'Yellow': (0, 0, -1), 'Red': (1, 0, 0)},
            'S8': {'Location': (0, 2, 1), 'Yellow': (0, 0, -1), 'Orange': (-1, 0, 0)},
            # Top Row
            'S9': {'Location': (0, 1, 2), 'Orange': (-1, 0, 0), 'Blue': (0, 1, 0)},
            'S10': {'Location': (1, 0, 2), 'White': (0, 0, 1), 'Blue': (0, 1, 0)},
            'S11': {'Location': (2, 1, 2), 'Red': (1, 0, 0), 'Blue': (0, 1, 0)},
            'S12': {'Location': (1, 2, 2), 'Yellow': (0, 0, -1), 'Blue': (0, 1, 0)}
        }

        # Group the Sides by Positions (Column and Row)
        self.bottomRowS = ['S1', 'S2', 'S3', 'S4']
        self.topRowS = ['S9', 'S10', 'S11', 'S12']

        self.leftColumnS = ['S5', 'S9', 'S8', 'S4']
        self.rightColumnS = ['S2', 'S6', 'S11', 'S7']

        self.frontFaceS = ['S1', 'S6', 'S10', 'S5']
        self.backFaceS = ['S3', 'S7', 'S12', 'S8']

        self.__rubixInit = {'White': {'Location': (1, 0, 1), 'Direction': (0, 0, 1)},
                            'Yellow': {'Location': (1, 3, 1), 'Direction': (0, 0, -1)},
                            'Green': {'Location': (1, 1, 0), 'Direction': (0, -1, 0)},
                            'Blue': {'Location': (1, 1, 3), 'Direction': (0, 1, 0)},
                            'Orange': {'Location': (0, 1, 1), 'Direction': (-1, 0, 0)},
                            'Red': {'Location': (3, 1, 1), 'Direction': (1, 0, 0)}}

        # Insert Corner Peices
        for faceColor in (self.__rubixInit.keys()):
            Ctemp = []
            Stemp = []
            for CornerPeice in self.CornerPeices.keys():
                for CornerColorI in self.CornerPeices[CornerPeice].keys():
                    if self.CornerPeices[CornerPeice][CornerColorI] == self.__rubixInit[faceColor]['Direction']:
                        Ctemp += [CornerPeice]

            for SidePeice in self.SidePeices.keys():
                for SideColorI in self.SidePeices[SidePeice].keys():
                    if self.SidePeices[SidePeice][SideColorI] == self.__rubixInit[faceColor]['Direction']:
                        Stemp += [SidePeice]

            self.__rubixInit[faceColor].update(Corners=[Ctemp])
            self.__rubixInit[faceColor].update(Sides=[Stemp])

        self.Rubik = self.__rubixInit

    def SetColor(self, currentFace):  # returns setColor

        if currentFace == 'Blue':
            setColor = self.Blue

        elif currentFace == 'Red':
            setColor = self.Red

        elif currentFace == 'Orange':
            setColor = self.Orange

        elif currentFace == 'Yellow':
            setColor = self.Yellow

        elif currentFace == 'Green':
            setColor = self.Green

        elif currentFace == 'White':
            setColor = self.White

        return setColor

    def PlotRubik(self, PlotSide, PlotCorner):
        print('Printing Rubik')
        panel = 2j
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_autoscale_on(True)
        for faceColor in self.Rubik.keys():
            # print(rub1[faceColor]['Location'])
            x, y, z = self.Rubik[faceColor]['Location']
            u, v, w = self.Rubik[faceColor]['Direction']
            setColor = self.SetColor(faceColor)

            # Plot Centers
            if abs(u) == 1:  # orange, red
                Y, Z = np.mgrid[0:1:panel, 0:1:panel]
                X = np.zeros_like(Z)
                ax.plot_surface(X+x, Y+y, Z+z, color=setColor)
            elif abs(v) == 1:  # green, blue
                X, Y = np.mgrid[0:1:panel, 0:1:panel]
                Z = np.zeros_like(X)
                ax.plot_surface(X+x, Y+y, Z+z, color=setColor)
            else:  # yellow, white
                Z, X = np.mgrid[0:1:panel, 0:1:panel]
                Y = np.zeros_like(Z)
                ax.plot_surface(X+x, Y+y, Z+z, color=setColor)

        for Corner in PlotCorner.keys():
            x, y, z = PlotCorner[Corner]['Location']

            for cornerColor in PlotCorner[Corner].keys():

                if cornerColor != 'Location':
                    # if Corner == 'C1':
                    for CenterRefColor in rub.Rubik:
                        if PlotCorner[Corner][cornerColor] == rub.Rubik[CenterRefColor]['Direction']:

                            xCFL, yCFL, zCFL = self.Rubik[CenterRefColor]['Location']

                    u, v, w = PlotCorner[Corner][cornerColor]

                    setColor = self.SetColor(cornerColor)

                    # Plot Centers
                    if abs(u) == 1:  # orange, red
                        Y, Z = np.mgrid[0:1:panel, 0:1:panel]
                        X = np.zeros_like(Z)
                        ax.plot_surface(X+xCFL, Y+y, Z+z, color=setColor)
                    elif abs(v) == 1:  # green, blue
                        X, Y = np.mgrid[0:1:panel, 0:1:panel]
                        Z = np.zeros_like(X)
                        ax.plot_surface(X+x, Y+y, Z+zCFL, color=setColor)
                    else:  # yellow, white
                        Z, X = np.mgrid[0:1:panel, 0:1:panel]
                        Y = np.zeros_like(Y)
                        ax.plot_surface(X+x, Y+yCFL, Z+z, color=setColor)

        for Sides in PlotSide.keys():

            x, y, z = PlotSide[Sides]['Location']

            for SideColor in PlotSide[Sides].keys():

                if SideColor != 'Location':
                    for CenterRefColor in rub.Rubik:
                        if PlotSide[Sides][SideColor] == rub.Rubik[CenterRefColor]['Direction']:

                            xCFL, yCFL, zCFL = self.Rubik[CenterRefColor]['Location']

                    u, v, w = PlotSide[Sides][SideColor]

                    setColor = self.SetColor(SideColor)

                    # Plot Centers
                    if abs(u) == 1:  # orange, red
                        Y, Z = np.mgrid[0:1:panel, 0:1:panel]
                        X = np.zeros_like(Z)
                        ax.plot_surface(X+xCFL, Y+y, Z+z, color=setColor)
                    elif abs(v) == 1:  # green, blue
                        X, Y = np.mgrid[0:1:panel, 0:1:panel]
                        Z = np.zeros_like(X)
                        ax.plot_surface(X+x, Y+y, Z+zCFL, color=setColor)
                    else:  # yellow, white
                        Z, X = np.mgrid[0:1:panel, 0:1:panel]
                        Y = np.zeros_like(Y)
                        ax.plot_surface(X+x, Y+yCFL, Z+z, color=setColor)
        plt.show()

    def moveKeyForward(self, mainDict, refKey):
        varSave = mainDict[refKey[0]]
        for i in range(len(refKey)):
            if i != len(refKey)-1:
                mainDict[refKey[i]] = mainDict.pop(refKey[i+1])
            else:
                mainDict[refKey[i]] = varSave
        return mainDict

    def moveKeyBack(self, mainDict, refKey):
        varSave = mainDict[refKey[len(refKey)-1]]
        for i in range(len(refKey)-1, -1, -1):
            if i == 0:
                mainDict[refKey[i]] = varSave
            else:
                mainDict[refKey[i]] = mainDict.pop(refKey[i-1])
        return mainDict

    # Insert Corner Peices
    def UpdateLocations(self, rubik, CornerInfo, SideInfo):

        for faceColor in (rubik.keys()):
            Ctemp = []
            Stemp = []
            for CornerPeice in CornerInfo.keys():
                for CornerColorI in CornerInfo[CornerPeice].keys():
                    if CornerInfo[CornerPeice][CornerColorI] == rubik[faceColor]['Direction']:
                        Ctemp += [CornerPeice]

            for SidePeice in SideInfo.keys():
                for SideColorI in SideInfo[SidePeice].keys():
                    if SideInfo[SidePeice][SideColorI] == rubik[faceColor]['Direction']:
                        Stemp += [SidePeice]

            rubik[faceColor].update(Corners=Ctemp)
            rubik[faceColor].update(Sides=Stemp)

    def rotRowCorner(self, CP, rowCallOuts, RotDirection):
        # Define the Bottom Row
        tempStore = []
        for CornerLocation in rowCallOuts:
            tempStore += [CP[CornerLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(rowCallOuts)):
                # Rotate Row by 90 degrees CCW
                if i == len(rowCallOuts)-1:
                    CP[rowCallOuts[i]
                       ]['Location'] = tempStore[0]
                elif i < len(rowCallOuts)-1:
                    CP[rowCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Corner names to adhere to convention
            # print('Before')
            # self.prettyPrint(CP)
            self.moveKeyBack(CP, rowCallOuts)
            # print('After')
            # self.prettyPrint(CP)
            # Redefined the directions of the newly rotated faces
            for Row in rowCallOuts:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, 0, -1)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, 0, 1)
                        elif CP[Row][Color] == (0, 0, 1):
                            CP[Row][Color] = (1, 0, 0)
                        elif CP[Row][Color] == (0, 0, -1):
                            CP[Row][Color] = (-1, 0, 0)

        elif RotDirection == 'CW':
            for i in range(len(rowCallOuts)-1, -1, -1):
                # Rotate Row by 90 degrees CW
                if i == 0:
                    CP[rowCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    CP[rowCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyForward(CP, rowCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in rowCallOuts:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, 0, 1)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, 0, -1)
                        elif CP[Row][Color] == (0, 0, 1):
                            CP[Row][Color] = (-1, 0, 0)
                        elif CP[Row][Color] == (0, 0, -1):
                            CP[Row][Color] = (1, 0, 0)

    def rotRowSide(self, SP, rowCallOuts, RotDirection):
        # Define the Bottom Row
        tempStore = []
        for SideLocation in rowCallOuts:
            tempStore += [SP[SideLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(rowCallOuts)):
                # Rotate Row by 90 degrees CCW
                if i == len(rowCallOuts)-1:
                    SP[rowCallOuts[i]]['Location'] = tempStore[0]
                else:
                    SP[rowCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyBack(SP, rowCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in rowCallOuts:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, 0, -1)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, 0, 1)
                        elif SP[Row][Color] == (0, 0, 1):
                            SP[Row][Color] = (1, 0, 0)
                        elif SP[Row][Color] == (0, 0, -1):
                            SP[Row][Color] = (-1, 0, 0)

        elif RotDirection == 'CW':
            for i in range(len(rowCallOuts)-1, -1, -1):
                # Rotate Row by 90 degrees CW
                if i == 0:
                    SP[rowCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    SP[rowCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyForward(SP, rowCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in rowCallOuts:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, 0, 1)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, 0, -1)
                        elif SP[Row][Color] == (0, 0, 1):
                            SP[Row][Color] = (-1, 0, 0)
                        elif SP[Row][Color] == (0, 0, -1):
                            SP[Row][Color] = (1, 0, 0)

    def rotColCorner(self, CP, colCallOuts, RotDirection):
        # Define the Bottom Col
        tempStore = []
        for CornerLocation in colCallOuts:
            tempStore += [CP[CornerLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(colCallOuts)):
                # Rotate Col by 90 degrees CCW
                if i == len(colCallOuts)-1:
                    CP[colCallOuts[i]
                       ]['Location'] = tempStore[0]
                elif i < len(colCallOuts)-1:
                    CP[colCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Corner names to adhere to convention
            # print('Before')
            # self.prettyPrint(CP)
            self.moveKeyForward(CP, colCallOuts)
            # print('After')
            # self.prettyPrint(CP)
            # Redefined the directions of the newly rotated faces
            for Col in colCallOuts:
                for Color in CP[Col]:
                    if Color != 'Location':
                        if CP[Col][Color] == (0, 1, 0):
                            CP[Col][Color] = (0, 0, 1)
                        elif CP[Col][Color] == (0, -1, 0):
                            CP[Col][Color] = (0, 0, -1)
                        elif CP[Col][Color] == (0, 0, 1):
                            CP[Col][Color] = (0, -1, 0)
                        elif CP[Col][Color] == (0, 0, -1):
                            CP[Col][Color] = (0, 1, 0)

        elif RotDirection == 'CW':
            for i in range(len(colCallOuts)-1, -1, -1):
                # Rotate Col by 90 degrees CW
                if i == 0:
                    CP[colCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    CP[colCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyBack(CP, colCallOuts)
            # Redefined the directions of the newly rotated faces
            for Col in colCallOuts:
                for Color in CP[Col]:
                    if Color != 'Location':
                        if CP[Col][Color] == (0, 1, 0):
                            CP[Col][Color] = (0, 0, -1)
                        elif CP[Col][Color] == (0, -1, 0):
                            CP[Col][Color] = (0, 0, 1)
                        elif CP[Col][Color] == (0, 0, 1):
                            CP[Col][Color] = (0, 1, 0)
                        elif CP[Col][Color] == (0, 0, -1):
                            CP[Col][Color] = (0, -1, 0)

    def rotColSide(self, SP, colCallOuts, RotDirection):
        # Define the Bottom Col
        tempStore = []
        for SideLocation in colCallOuts:
            tempStore += [SP[SideLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(colCallOuts)):
                # Rotate Col by 90 degrees CCW
                if i == len(colCallOuts)-1:
                    SP[colCallOuts[i]]['Location'] = tempStore[0]
                else:
                    SP[colCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Side names to adhere to convention
            self.moveKeyForward(SP, colCallOuts)
            # Redefined the directions of the newly rotated faces
            for Col in colCallOuts:
                for Color in SP[Col]:
                    if Color != 'Location':
                        if SP[Col][Color] == (0, 1, 0):
                            SP[Col][Color] = (0, 0, 1)
                        elif SP[Col][Color] == (0, -1, 0):
                            SP[Col][Color] = (0, 0, -1)
                        elif SP[Col][Color] == (0, 0, 1):
                            SP[Col][Color] = (0, -1, 0)
                        elif SP[Col][Color] == (0, 0, -1):
                            SP[Col][Color] = (0, 1, 0)

        elif RotDirection == 'CW':
            for i in range(len(colCallOuts)-1, -1, -1):
                # Rotate Col by 90 degrees CW
                if i == 0:
                    SP[colCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    SP[colCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Side names to adhere to convention
            self.moveKeyBack(SP, colCallOuts)
            # Redefined the directions of the newly rotated faces
            for Col in colCallOuts:
                for Color in SP[Col]:
                    if Color != 'Location':
                        if SP[Col][Color] == (0, 1, 0):
                            SP[Col][Color] = (0, 0, -1)
                        elif SP[Col][Color] == (0, -1, 0):
                            SP[Col][Color] = (0, 0, 1)
                        elif SP[Col][Color] == (0, 0, 1):
                            SP[Col][Color] = (0, 1, 0)
                        elif SP[Col][Color] == (0, 0, -1):
                            SP[Col][Color] = (0, -1, 0)

    # Rotate Both Sides and Corners
    def rotateRow(self, CP, CornerGrouping, SP, SideGrouping, RotDirection):
        self.rotRowCorner(CP, CornerGrouping, RotDirection)
        self.rotRowSide(SP, SideGrouping, RotDirection)

        return CP, SP
    # Rotate Both Sides and Corners

    def rotateColumn(self, CP, CornerGrouping, SP, SideGrouping, RotDirection):
        self.rotColCorner(CP, CornerGrouping, RotDirection)
        CP = self.cornerQuirk(CP)
        self.rotColSide(SP, SideGrouping, RotDirection)
        SP = self.sideQuirk(SP)
        return CP, SP

    def prettyPrint(self, Dict):
        for key in Dict:
            print(f"Corner {key}: {Dict[key]}")

    def cornerQuirk(self, CP):
        for Corner in CP:
            if Corner == 'C1':
                CP[Corner]['Location'] = (0, 0, 0)
            elif Corner == 'C2':
                CP[Corner]['Location'] = (2, 0, 0)
            elif Corner == 'C3':
                CP[Corner]['Location'] = (2, 2, 0)
            elif Corner == 'C4':
                CP[Corner]['Location'] = (0, 2, 0)
            elif Corner == 'C5':
                CP[Corner]['Location'] = (0, 0, 2)
            elif Corner == 'C6':
                CP[Corner]['Location'] = (2, 0, 2)
            elif Corner == 'C7':
                CP[Corner]['Location'] = (2, 2, 2)
            elif Corner == 'C8':
                CP[Corner]['Location'] = (0, 2, 2)
        return CP

    def sideQuirk(self, SP):
        for Corner in SP:
            if Corner == 'S1':
                SP[Corner]['Location'] = (1, 0, 0)
            elif Corner == 'S2':
                SP[Corner]['Location'] = (2, 1, 0)
            elif Corner == 'S3':
                SP[Corner]['Location'] = (1, 2, 0)
            elif Corner == 'S4':
                SP[Corner]['Location'] = (0, 1, 0)
            elif Corner == 'S5':
                SP[Corner]['Location'] = (0, 0, 1)
            elif Corner == 'S6':
                SP[Corner]['Location'] = (2, 0, 1)
            elif Corner == 'S7':
                SP[Corner]['Location'] = (2, 2, 1)
            elif Corner == 'S8':
                SP[Corner]['Location'] = (0, 2, 1)
            elif Corner == 'S9':
                SP[Corner]['Location'] = (0, 1, 2)
            elif Corner == 'S10':
                SP[Corner]['Location'] = (1, 0, 2)
            elif Corner == 'S11':
                SP[Corner]['Location'] = (2, 1, 2)
            elif Corner == 'S12':
                SP[Corner]['Location'] = (1, 2, 2)
        return SP

    def randomizer(self, CP, SP, Turns):
        Squares = ['Top', 'Bottom', 'Left', 'Right', 'Front', 'Back']
        Direction = ['CCW', 'CW']
        check = True

        for i in range(Turns):
            RubikPortion = random.choice(Squares)
            RubikDirection = random.choice(Direction)
            # print(RubikPortion)
            # print(RubikDirection)
            if RubikPortion == 'Top':
                CP, SP = self.rotateRow(CP, self.topRowC, SP,
                                        self.topRowS, RubikDirection)
            elif RubikPortion == 'Bottom':
                CP, SP = self.rotateRow(CP, self.bottomRowC, SP,
                                        self.bottomRowS, RubikDirection)
            if RubikPortion == 'Left':
                CP, SP = self.rotateColumn(CP, self.leftColumnC,
                                           SP, self.leftColumnS, RubikDirection)
            elif RubikPortion == 'Right':
                CP, SP = self.rotateColumn(CP, self.rightColumnC,
                                           SP, self.rightColumnS, RubikDirection)
            if RubikPortion == 'Front':
                CP, SP = self.rotateFace(
                    CP, self.frontFaceC, SP, self.frontFaceS, RubikDirection)
            if RubikPortion == 'Back':
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, RubikDirection)

            time.sleep(0)

            if CP['C1']['Location'] != (0, 0, 0) and check:
                # print(i)
                check = False
        return CP, SP

    def rotFaceCorners(self, CP, faceCallOuts, RotDirection):
        tempStore = []
        for CornerLocation in faceCallOuts:
            tempStore += [CP[CornerLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(faceCallOuts)):
                # Rotate Row by 90 degrees CCW
                if i == len(faceCallOuts)-1:
                    CP[faceCallOuts[i]
                       ]['Location'] = tempStore[0]
                elif i < len(faceCallOuts)-1:
                    CP[faceCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Corner names to adhere to convention
            # print('Before')
            # self.prettyPrint(CP)
            self.moveKeyBack(CP, faceCallOuts)
            # print('After')
            # self.prettyPrint(CP)
            # Redefined the directions of the newly rotated faces
            for Row in faceCallOuts:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (0, 1, 0):
                            CP[Row][Color] = (-1, 0, 0)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, -1, 0)
                        elif CP[Row][Color] == (0, -1, 0):
                            CP[Row][Color] = (1, 0, 0)
                        elif CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, 1, 0)

        elif RotDirection == 'CW':
            for i in range(len(faceCallOuts)-1, -1, -1):
                # Rotate Row by 90 degrees CW
                if i == 0:
                    CP[faceCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    CP[faceCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyForward(CP, faceCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in faceCallOuts:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (0, 1, 0):
                            CP[Row][Color] = (1, 0, 0)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, 1, 0)
                        elif CP[Row][Color] == (0, -1, 0):
                            CP[Row][Color] = (-1, 0, 0)
                        elif CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, -1, 0)

    def rotFaceSide(self, SP, faceCallOuts, RotDirection):
        tempStore = []
        for SideLocation in faceCallOuts:
            tempStore += [SP[SideLocation]['Location']]

        if RotDirection == 'CCW':
            for i in range(len(faceCallOuts)):
                # Rotate Col by 90 degrees CCW
                if i == len(faceCallOuts)-1:
                    SP[faceCallOuts[i]]['Location'] = tempStore[0]
                else:
                    SP[faceCallOuts[i]
                       ]['Location'] = tempStore[i+1]
            # Adjust the Side names to adhere to convention
            self.moveKeyBack(SP, faceCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in faceCallOuts:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, 1, 0)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, -1, 0)
                        elif SP[Row][Color] == (0, 1, 0):
                            SP[Row][Color] = (-1, 0, 0)
                        elif SP[Row][Color] == (0, -1, 0):
                            SP[Row][Color] = (1, 0, 0)
        elif RotDirection == 'CW':
            for i in range(len(faceCallOuts)-1, -1, -1):
                # Rotate Row by 90 degrees CW
                if i == 0:
                    SP[faceCallOuts[i]
                       ]['Location'] = tempStore[len(tempStore)-1]
                else:
                    SP[faceCallOuts[i]
                       ]['Location'] = tempStore[i-1]
            # Adjust the Corner names to adhere to convention
            self.moveKeyForward(SP, faceCallOuts)
            # Redefined the directions of the newly rotated faces
            for Row in faceCallOuts:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, -1, 0)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, 1, 0)
                        elif SP[Row][Color] == (0, 1, 0):
                            SP[Row][Color] = (1, 0, 0)
                        elif SP[Row][Color] == (0, -1, 0):
                            SP[Row][Color] = (-1, 0, 0)

    def rotateFace(self, CP, corners, SP, sides, direction):
        if direction == 'CW':
            CP = self.moveKeyBack(CP, corners)
            SP = self.moveKeyForward(SP, sides)
        elif direction == 'CCW':
            CP = self.moveKeyForward(CP, corners)
            SP = self.moveKeyBack(SP, sides)

        for i in corners:
            # print(i)
            if i == 'C1':
                CP[i]['Location'] = (0, 0, 0)
            if i == 'C2':
                CP[i]['Location'] = (2, 0, 0)
                # print(CP[i]['Location'])
            if i == 'C3':
                CP[i]['Location'] = (2, 2, 0)
            if i == 'C4':
                CP[i]['Location'] = (0, 2, 0)
            if i == 'C5':
                CP[i]['Location'] = (0, 0, 2)
            if i == 'C6':
                CP[i]['Location'] = (2, 0, 2)
            if i == 'C7':
                CP[i]['Location'] = (2, 2, 2)
            if i == 'C8':
                CP[i]['Location'] = (0, 2, 2)
        SP = self.sideQuirk(SP)

        if direction == 'CW':
            for Row in corners:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (0, 1, 0):
                            CP[Row][Color] = (1, 0, 0)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, 1, 0)
                        elif CP[Row][Color] == (0, -1, 0):
                            CP[Row][Color] = (-1, 0, 0)
                        elif CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, -1, 0)
            for Row in sides:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (0, 1, 0):
                            SP[Row][Color] = (1, 0, 0)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, 1, 0)
                        elif SP[Row][Color] == (0, -1, 0):
                            SP[Row][Color] = (-1, 0, 0)
                        elif SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, -1, 0)
        elif direction == 'CCW':
            for Row in corners:
                for Color in CP[Row]:
                    if Color != 'Location':
                        if CP[Row][Color] == (0, 1, 0):
                            CP[Row][Color] = (-1, 0, 0)
                        elif CP[Row][Color] == (-1, 0, 0):
                            CP[Row][Color] = (0, -1, 0)
                        elif CP[Row][Color] == (0, -1, 0):
                            CP[Row][Color] = (1, 0, 0)
                        elif CP[Row][Color] == (1, 0, 0):
                            CP[Row][Color] = (0, 1, 0)
            for Row in sides:
                for Color in SP[Row]:
                    if Color != 'Location':
                        if SP[Row][Color] == (0, 1, 0):
                            SP[Row][Color] = (-1, 0, 0)
                        elif SP[Row][Color] == (-1, 0, 0):
                            SP[Row][Color] = (0, -1, 0)
                        elif SP[Row][Color] == (0, -1, 0):
                            SP[Row][Color] = (1, 0, 0)
                        elif SP[Row][Color] == (1, 0, 0):
                            SP[Row][Color] = (0, 1, 0)
        return CP, SP

    def unmixer(self, SP):
        # print(SP)
        temp = {}
        for Side in SP:
            if SP[Side]['Location'] == (1, 0, 0):
                temp['S1'] = SP[Side]
            elif SP[Side]['Location'] == (2, 1, 0):
                temp['S2'] = SP[Side]
            elif SP[Side]['Location'] == (1, 2, 0):
                temp['S3'] = SP[Side]
            elif SP[Side]['Location'] == (0, 1, 0):
                temp['S4'] = SP[Side]
            elif SP[Side]['Location'] == (0, 0, 1):
                temp['S5'] = SP[Side]
            elif SP[Side]['Location'] == (2, 0, 1):
                temp['S6'] = SP[Side]
            elif SP[Side]['Location'] == (2, 2, 1):
                temp['S7'] = SP[Side]
            elif SP[Side]['Location'] == (0, 2, 1):
                temp['S8'] = SP[Side]
            elif SP[Side]['Location'] == (0, 1, 2):
                temp['S9'] = SP[Side]
            elif SP[Side]['Location'] == (1, 0, 2):
                temp['S10'] = SP[Side]
            elif SP[Side]['Location'] == (2, 1, 2):
                temp['S11'] = SP[Side]
            elif SP[Side]['Location'] == (1, 2, 2):
                temp['S12'] = SP[Side]
            # SP = temp
        return temp

    def rowColumnFaceC(self, cornerpeice):
        try:
            if self.backFaceC.index(cornerpeice) >= 0:
                print('Back Face')
            backface = True
        except:
            backface = False

        try:
            if self.frontFaceC.index(cornerpeice) >= 0:
                print('Front Face')
            frontface = True
        except:
            frontface = False

        try:
            if self.topRowC.index(cornerpeice) >= 0:
                print('Top Row')
            toprow = True
        except:
            toprow = False

        try:
            if self.bottomRowC.index(cornerpeice) >= 0:
                print('Bottom Row')
            bottomrow = True

        except:
            bottomrow = False

        try:
            if self.leftColumnC.index(cornerpeice) >= 0:
                print('Left Column')
            leftcolumn = True

        except:
            leftcolumn = False

        try:
            if self.rightColumnC.index(cornerpeice) >= 0:
                print('Right Column')
            rightcolumn = True
        except:
            rightcolumn = False

        return frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn

    def rowColumnFaceS(self, sidepeice):
        try:
            if self.backFaceS.index(sidepeice) >= 0:
                print('Back Face')
            backface = True
        except:
            backface = False

        try:
            if self.frontFaceS.index(sidepeice) >= 0:
                print('Front Face')
            frontface = True
        except:
            frontface = False

        try:
            if self.topRowS.index(sidepeice) >= 0:
                print('Top Row')
            toprow = True
        except:
            toprow = False

        try:
            if self.bottomRowS.index(sidepeice) >= 0:
                print('Bottom Row')
            bottomrow = True

        except:
            bottomrow = False

        try:
            if self.leftColumnS.index(sidepeice) >= 0:
                print('Left Column')
            leftcolumn = True

        except:
            leftcolumn = False

        try:
            if self.rightColumnS.index(sidepeice) >= 0:
                print('Right Column')
            rightcolumn = True
        except:
            rightcolumn = False

        return frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn

    def switchOrientation1(self, CP, SP, Side):
        frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
            Side)
        # Switch Orientation while preserving Front Cross
        if toprow:
            if leftcolumn:
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')

                # Fix Front Cross
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
            elif rightcolumn:
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                # Fix Front Cross
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
            elif backface:
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')

                # Fix Front Cross
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
        if backface:
            if leftcolumn:
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CW')

                # Fix Front Cross
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
            elif rightcolumn:
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CW')

                # Fix Front Cross
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
        if bottomrow:
            if leftcolumn:
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CW')

                # Fix Front Cross
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
            elif backface:
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CW')

                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')

                # Fix Front Cross
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CW')
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')

                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            elif rightcolumn:
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                CP, SP = self.rotateFace(
                    CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CW')

                # Fix Front Cross
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, rub.bottomRowS, 'CW')
        return CP, SP

    def SolveWhiteCross(self, CP, SP):
        ColorFlag = True
        fail = 0
        solve = 0
        temp = 0
        lim = 20
        while ColorFlag:
            fix = 0
            spKeys = list(SP.keys())
            for i in range(len(SP)):
                # Get a list of Keys to navigate through to the colors within a specific side peice
                spSpecificKeys = list(SP[spKeys[i]].keys())
                for j in range(len(spSpecificKeys)):
                    # if the side peice has a 'White' face
                    ran = False
                    if spSpecificKeys[j] == 'White':
                        # Does the 'White' Face exist on the 'Yellow' face
                        if SP[spKeys[i]][spSpecificKeys[j]] == (0, 0, -1):
                            ran = True
                            CP, SP = self.WonYFace(
                                CP, SP, i, j, spSpecificKeys, spKeys)
                        # Does White exist on the x or y faces
                        if not ran:
                            if (abs(SP[spKeys[i]][spSpecificKeys[j]][0]) == 1 or abs(SP[spKeys[i]][spSpecificKeys[j]][1]) == 1) or (SP[spKeys[i]][spSpecificKeys[j]] == (0, 0, 1)):
                                ran = True
                                # print('White on either the x or y faces')

                                # Get the index of the other color
                                if j == 2:
                                    # print(spSpecificKeys[1])
                                    otherColorIndex = 1
                                    whiteColorIndex = 2
                                else:
                                    # print(spSpecificKeys[2])
                                    otherColorIndex = 2
                                    whiteColorIndex = 1

                                sidePeiceLocation = SP[spKeys[i]
                                                       ][spSpecificKeys[otherColorIndex]]
                                whitePeiceLocation = SP[spKeys[i]
                                                        ][spSpecificKeys[whiteColorIndex]]
                                currentCenter = self.Rubik[spSpecificKeys[otherColorIndex]]['Direction']
                                # print(
                                # f"Color Peice Direction: {sidePeiceLocation}")
                                # print(
                                # f"Current Center Direction: {currentCenter}")
                                # print(
                                # f"White Peice Direction: {whitePeiceLocation}")

                                if (SP[spKeys[i]][spSpecificKeys[j]][0]) == 1:
                                    # print('Flipping Pos X side piece')
                                    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
                                        spKeys[i])
                                    # print(frontface)
                                    # print(backface)
                                    # print(toprow)
                                    # print(bottomrow)
                                    # print(rightcolumn)
                                    # print(leftcolumn)
                                    # print(spSpecificKeys[j])
                                    if toprow:
                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CCW')

                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break

                                    elif bottomrow:
                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CCW')

                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break
                                    elif frontface:

                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                                        CP, SP = self.rotateColumn(
                                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')
                                        break
                                    else:
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')
                                        break

                                elif (SP[spKeys[i]][spSpecificKeys[j]][0]) == -1:
                                    # print('Flipping Neg X side piece')
                                    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
                                        spKeys[i])
                                    # print(frontface)
                                    # print(backface)
                                    # print(toprow)
                                    # print(bottomrow)
                                    # print(rightcolumn)
                                    # print(leftcolumn)
                                    # print(spSpecificKeys[j])
                                    if toprow:
                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break

                                    elif bottomrow:
                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break
                                    elif frontface:

                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')

                                        CP, SP = self.rotateColumn(
                                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S8')
                                        break
                                    else:
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S8')
                                        break

                                elif (SP[spKeys[i]][spSpecificKeys[j]][1]) == 1:
                                    # print('Flipping Pos Y side piece')
                                    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
                                        spKeys[i])
                                    # print(frontface)
                                    # print(backface)
                                    # print(toprow)
                                    # print(bottomrow)
                                    # print(rightcolumn)
                                    # print(leftcolumn)
                                    # print(spSpecificKeys[j])
                                    if leftcolumn:
                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CCW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')
                                        break

                                    elif rightcolumn:
                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CCW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')
                                        break
                                    elif frontface:

                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CCW')

                                        CP, SP = self.rotateRow(
                                            CP, self.topRowC, SP, self.topRowS, 'CCW')
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break
                                    else:
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S12')
                                        break

                                elif (SP[spKeys[i]][spSpecificKeys[j]][1]) == -1:
                                    # print('Flipping Neg Y side piece')
                                    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
                                        spKeys[i])
                                    # print(frontface)
                                    # print(backface)
                                    # print(toprow)
                                    # print(bottomrow)
                                    # print(rightcolumn)
                                    # print(leftcolumn)
                                    # print(spSpecificKeys[j])
                                    if leftcolumn:
                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')

                                        break

                                    elif rightcolumn:
                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')

                                        CP, SP = self.rotateFace(
                                            CP, self.backFaceC, SP, self.backFaceS, 'CCW')
                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CW')

                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S7')
                                        break
                                    elif frontface:

                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')

                                        CP, SP = self.rotateRow(
                                            CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S3')
                                        break
                                    else:
                                        CP, SP = self.switchOrientation1(
                                            CP, SP, 'S3')
                                        break

                                elif (SP[spKeys[i]][spSpecificKeys[j]][2]) == 1:

                                    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = self.rowColumnFaceS(
                                        spKeys[i])
                                    # print(frontface)
                                    # print(backface)
                                    # print(toprow)
                                    # print(bottomrow)
                                    # print(rightcolumn)
                                    # print(leftcolumn)

                                    # print(spSpecificKeys[j])
                                    # print('Flipping Neg Y side piece')

                                    if toprow:
                                        if spSpecificKeys[otherColorIndex] != 'Blue':
                                            CP, SP = self.rotateRow(
                                                CP, self.topRowC, SP, self.topRowS, 'CCW')
                                            CP, SP = self.rotateRow(
                                                CP, self.topRowC, SP, self.topRowS, 'CCW')
                                            break
                                    elif bottomrow:
                                        if spSpecificKeys[otherColorIndex] != 'Green':
                                            CP, SP = self.rotateRow(
                                                CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                                            CP, SP = self.rotateRow(
                                                CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                                            break
                                    elif leftcolumn:
                                        if spSpecificKeys[otherColorIndex] != 'Orange':
                                            CP, SP = self.rotateColumn(
                                                CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                                            CP, SP = self.rotateColumn(
                                                CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                                            break
                                    elif rightcolumn:
                                        if spSpecificKeys[otherColorIndex] != 'Red':
                                            CP, SP = self.rotateColumn(
                                                CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                                            CP, SP = self.rotateColumn(
                                                CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                                            break
            temp += 1
            try:
                if (SP['S1']['White'][2] == 1) and (SP['S5']['White'][2] == 1) and (SP['S6']['White'][2] == 1) and (SP['S10']['White'][2] == 1):
                    if (SP['S1']['Green'][1] == -1) and (SP['S5']['Orange'][0] == -1) and (SP['S6']['Red'][0] == 1) and (SP['S10']['Blue'][1] == 1):
                        # print('ALL MATCHING')
                        ColorFlag = False
                        solve += 1
            except:
                print('NOT MATCHED')
                if temp == lim:
                    fail += 1
                    self.PlotRubik(CP, SP)
                    break

        # print(f"The Cube Could not be Solved {fail} times")
        # print(f"The Cube was Solved {solve} times")
        return CP, SP

    def WonYFace(self, CP, SP,  i, j, spSpecificKeys, spKeys):
        # print('White on the yellow face')

        # Get the index of the other color
        if j == 2:
            # print(spSpecificKeys[1])
            otherColorIndex = 1
            whiteColorIndex = 2
        else:
            # print(spSpecificKeys[2])
            otherColorIndex = 2
            whiteColorIndex = 1

        sidePeiceLocation = SP[spKeys[i]
                               ][spSpecificKeys[otherColorIndex]]
        currentCenter = self.Rubik[spSpecificKeys[otherColorIndex]]['Direction']

        # Does the Other Color match the center color
        if sidePeiceLocation == currentCenter:
            if currentCenter[1] == 1:
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.topRowC, SP, self.topRowS, 'CCW')
                # print(
                # f'Matched Top Row: {spSpecificKeys[otherColorIndex]}')

            elif currentCenter[1] == -1:
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                CP, SP = self.rotateRow(
                    CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
                # print(
                # f'Matched Bottom Row: {spSpecificKeys[otherColorIndex]}')

            elif currentCenter[0] == 1:
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                # print(
                # f'Matched Right Column: {spSpecificKeys[otherColorIndex]}')

            elif currentCenter[0] == -1:
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                CP, SP = self.rotateColumn(
                    CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                # print(
                # f'Matched Left Column: {spSpecificKeys[otherColorIndex]}')

        else:
            # if abs(sidePeiceLocation[0]) == abs(currentCenter[0]) and abs(sidePeiceLocation[1]) == abs(currentCenter[1]) and abs(sidePeiceLocation[2]) == abs(currentCenter[2]):
            #     # if the corresponding center is on the opposite face rotate twice
            #     CP, SP = self.rotateFace(
            #         CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            #     CP, SP = self.rotateFace(
            #         CP, self.backFaceC, SP, self.backFaceS, 'CCW')

            #     if currentCenter[1] == 1:
            #         CP, SP = self.rotateRow(
            #             CP, self.topRowC, SP, self.topRowS, 'CCW')
            #         CP, SP = self.rotateRow(
            #             CP, self.topRowC, SP, self.topRowS, 'CCW')
            #         print(
            #             f'Matched Top Row: {spSpecificKeys[otherColorIndex]}')

            #     elif currentCenter[1] == -1:
            #         CP, SP = self.rotateRow(
            #             CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
            #         CP, SP = self.rotateRow(
            #             CP, self.bottomRowC, SP, self.bottomRowS, 'CCW')
            #         print(
            #             f'Matched Bottom Row: {spSpecificKeys[otherColorIndex]}')

            #     elif currentCenter[0] == 1:
            #         CP, SP = self.rotateColumn(CP, self.rightColumnC, SP,
            #                                   self.rightColumnS, 'CCW')
            #         CP, SP = self.rotateColumn(CP, self.rightColumnC, SP,
            #                                   self.rightColumnS, 'CCW')
            #         print(
            #             f'Matched Right Column: {spSpecificKeys[otherColorIndex]}')

            #     elif currentCenter[0] == -1:
            #         CP, SP = self.rotateColumn(CP, self.leftColumnC, SP,
            #                                   self.leftColumnS, 'CCW')
            #         CP, SP = self.rotateColumn(CP, self.leftColumnC, SP,
            #                                   self.leftColumnS, 'CCW')
            #         print(
            #             f'Matched Left Column: {spSpecificKeys[otherColorIndex]}')

            # else:

            # rotate white side peice on yellow face until the other color matches the center color
            # print('Rotating until face matches')
            matched = False
            sidePeiceRotating = spKeys[i]
            while not matched:
                # Rotate Face
                CP, SP = self.rotateFace(CP, self.backFaceC, SP,
                                         self.backFaceS, 'CCW')
                # Get the index of the side we're rotating
                rotatedSide = self.backFaceS.index(
                    sidePeiceRotating)
                # if the index is the last item in the list set the value to -1 to avoid indexing errors
                if rotatedSide == len(self.backFaceS) - 1:
                    rotatedSide = -1
                # Increment the side being rotated to account for the side name change which occurred due to rotation
                sidePeiceRotating = self.backFaceS[rotatedSide+1]
                sidePeiceLocation = SP[sidePeiceRotating
                                       ][spSpecificKeys[otherColorIndex]]
                currentCenter = self.Rubik[spSpecificKeys[otherColorIndex]]['Direction']

                if sidePeiceLocation == currentCenter:
                    matched = True

            # Rotate corner to white face
            if currentCenter[1] == 1:
                CP, SP = self.rotateRow(CP, self.topRowC, SP,
                                        self.topRowS, 'CCW')
                CP, SP = self.rotateRow(CP, self.topRowC, SP,
                                        self.topRowS, 'CCW')
                # print(
                # f'Matched Top Row: {spSpecificKeys[otherColorIndex]}')
            elif currentCenter[1] == -1:
                CP, SP = self.rotateRow(CP, self.bottomRowC, SP,
                                        self.bottomRowS, 'CCW')
                CP, SP = self.rotateRow(CP, self.bottomRowC, SP,
                                        self.bottomRowS, 'CCW')
                # print(
                # f'Matched Bottom Row: {spSpecificKeys[otherColorIndex]}')
            elif currentCenter[0] == 1:
                CP, SP = self.rotateColumn(CP, self.rightColumnC, SP,
                                           self.rightColumnS, 'CCW')
                CP, SP = self.rotateColumn(CP, self.rightColumnC, SP,
                                           self.rightColumnS, 'CCW')
                # print(
                # f'Matched Right Column: {spSpecificKeys[otherColorIndex]}')
            elif currentCenter[0] == -1:
                CP, SP = self.rotateColumn(CP, self.leftColumnC, SP,
                                           self.leftColumnS, 'CCW')
                CP, SP = self.rotateColumn(CP, self.leftColumnC, SP,
                                           self.leftColumnS, 'CCW')
                # print(
                # f'Matched Left Column: {spSpecificKeys[otherColorIndex]}')

        return CP, SP

    def RightHandRule(self, CP, SP, Peice):
        if Peice == 'C6':
            rightRuleC = self.rightColumnC
            rightRuleS = self.rightColumnS

            CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CCW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CW')

        elif Peice == 'C1':
            rightRuleC = self.leftColumnC
            rightRuleS = self.leftColumnS

            CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CCW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CW')

        elif Peice == 'C2':
            rightRuleC = self.bottomRowC
            rightRuleS = self.bottomRowS

            CP, SP = self.rotateRow(CP, rightRuleC, SP, rightRuleS, 'CCW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            CP, SP = self.rotateRow(CP, rightRuleC, SP, rightRuleS, 'CW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CW')

        elif Peice == 'C5':
            rightRuleC = self.topRowC
            rightRuleS = self.topRowS

            CP, SP = self.rotateRow(CP, rightRuleC, SP, rightRuleS, 'CW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CCW')
            CP, SP = self.rotateRow(CP, rightRuleC, SP, rightRuleS, 'CCW')
            CP, SP = self.rotateFace(
                CP, self.backFaceC, SP, self.backFaceS, 'CW')

        return CP, SP

    def SolveWhiteCorners(self, CP, SP):
        # Solve White Corners
        cpKeys = ['C2', 'C1', 'C5', 'C6']
        otherCPKeys = ['C3', 'C4', 'C8', 'C7']

        CornerMatch = False
        while not CornerMatch:
            for i in range(len(cpKeys)):
                orientationCount = 0
                colorKeys = list(CP[cpKeys[i]].keys())
                # print(f"Current Corner is {cpKeys[i]}")
                orgDictColors = list(self.CornerDict[cpKeys[i]].keys())

                # print(f"Corner Colors should be: {orgDictColors}")
                # print(f"Current Colors are: {colorKeys}")

                # If Corner exists with all the correct color but not necessarily in the right orientation
                if (colorKeys[1] in orgDictColors) and (colorKeys[2] in orgDictColors) and (colorKeys[3] in orgDictColors):
                    # print('Correct Position but Incorrect Orientation')
                    # Check Orientation and Turn Corner
                    correctOrientation = 0
                    while correctOrientation != 4:

                        correctOrientation = 0
                        for j in range(len(colorKeys)):
                            if (self.CornerDict[cpKeys[i]][colorKeys[j]] == CP[cpKeys[i]][colorKeys[j]]):
                                correctOrientation += 1
                                orientationCount += 1

                        if correctOrientation != 4:
                            CP, SP = self.RightHandRule(CP, SP, cpKeys[i])
                            CP, SP = self.RightHandRule(CP, SP, cpKeys[i])
                else:
                    # print('Peice stuck')
                    if cpKeys[i] == 'C1':
                        CP, SP = self.rotateColumn(
                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                        CP, SP = self.rotateFace(
                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                        CP, SP = self.rotateColumn(
                            CP, self.leftColumnC, SP, self.leftColumnS, 'CW')
                    elif cpKeys[i] == 'C2':
                        CP, SP = self.rotateColumn(
                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')
                        CP, SP = self.rotateFace(
                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                        CP, SP = self.rotateColumn(
                            CP, self.rightColumnC, SP, self.rightColumnS, 'CW')
                    elif cpKeys[i] == 'C5':
                        CP, SP = self.rotateColumn(
                            CP, self.leftColumnC, SP, self.leftColumnS, 'CW')
                        CP, SP = self.rotateFace(
                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                        CP, SP = self.rotateColumn(
                            CP, self.leftColumnC, SP, self.leftColumnS, 'CCW')
                    elif cpKeys[i] == 'C6':
                        CP, SP = self.rotateColumn(
                            CP, self.rightColumnC, SP, self.rightColumnS, 'CW')
                        CP, SP = self.rotateFace(
                            CP, self.backFaceC, SP, self.backFaceS, 'CW')
                        CP, SP = self.rotateColumn(
                            CP, self.rightColumnC, SP, self.rightColumnS, 'CCW')

                for j in range(len(otherCPKeys)):
                    backFaceColors = list(CP[otherCPKeys[j]].keys())
                    SpecifiedCornerColor = list(
                        self.CornerDict[cpKeys[i]].keys())
                    if (SpecifiedCornerColor[1] in backFaceColors) and (SpecifiedCornerColor[2] in backFaceColors) and (SpecifiedCornerColor[3] in backFaceColors):
                        # print('Corner peice on the back face')
                        # rub.PlotRubik(CP, SP)
                        # print(True)
                        # print(otherCPKeys[j])
                        # print(backFaceColors)
                        # print()
                        if otherCPKeys[j] != otherCPKeys[i]:
                            # print('Rot')

                            match = False
                            tempLocation = j
                            # print('1')
                            while not match:
                                CP, SP = self.rotateFace(
                                    CP, self.backFaceC, SP, self.backFaceS, 'CW')

                                # Adjust other Color location to account for rotation
                                tempLocation += 1
                                if tempLocation >= len(otherCPKeys):
                                    tempLocation = 0

                                # Check if the Corner with the target color is in the right position
                                if otherCPKeys[tempLocation] == otherCPKeys[i]:
                                    match = True
                                    CP, SP = self.RightHandRule(
                                        CP, SP, cpKeys[i])
                        # print('2')
                        # colorKeys = list(CP[cpKeys[i]].keys())
                        # if (colorKeys[1] in orgDictColors) and (colorKeys[2] in orgDictColors) and (colorKeys[3] in orgDictColors):
                        #     # Check Orientation and Turn Corner
                        #     correctOrientation = 0
                        #     while correctOrientation != 4:

                        #         correctOrientation = 0
                        #         for k in range(len(colorKeys)):
                        #             try:
                        #                 if (rub.CornerDict[cpKeys[i]][colorKeys[k]] == CP[cpKeys[i]][colorKeys[k]]):
                        #                     correctOrientation += 1
                        #                     orientationCount += 1
                        #             except:
                        #                 break

                        #         if correctOrientation != 4:
                        #             CP, SP = RightHandRule(CP, SP, cpKeys[i])
                        #             CP, SP = RightHandRule(CP, SP, cpKeys[i])
                        # print('3')

                try:
                    checkCount = 0
                    for m in range(len(cpKeys)):
                        colorKeys = list(CP[cpKeys[m]].keys())
                        orgDictColors = list(rub.CornerDict[cpKeys[m]].keys())
                        if (colorKeys[1] in orgDictColors) and (colorKeys[2] in orgDictColors) and (colorKeys[3] in orgDictColors):
                            if CP[cpKeys[m]]['White'][2] == 1:
                                checkCount += 1
                    if checkCount == 4:
                        print('All Matching')
                        CornerMatch = True
                except:
                    break
        return CP, SP


def CorrectSideCube(SP):
    count = 0
    if SP['S1']['Location'] != (1, 0, 0):
        count += 1
    elif SP['S2']['Location'] != (2, 1, 0):
        count += 1
    elif SP['S3']['Location'] != (1, 2, 0):
        count += 1
    elif SP['S4']['Location'] != (0, 1, 0):
        count += 1
    elif SP['S5']['Location'] != (0, 0, 1):
        count += 1
    elif SP['S6']['Location'] != (2, 0, 1):
        count += 1
    elif SP['S7']['Location'] != (2, 2, 1):
        count += 1
    elif SP['S8']['Location'] != (0, 2, 1):
        count += 1
    elif SP['S9']['Location'] != (0, 1, 2):
        count += 1
    elif SP['S10']['Location'] != (1, 0, 2):
        count += 1
    elif SP['S11']['Location'] != (2, 1, 2):
        count += 1
    elif SP['S12']['Location'] != (1, 2, 2):
        count += 1
    return count


def CorrectCornerCube(CP):
    count = 0
    if CP['C1']['Location'] != (0, 0, 0):
        count += 1
    elif CP['C2']['Location'] != (2, 0, 0):
        count += 1
    elif CP['C3']['Location'] != (2, 2, 0):
        count += 1
    elif CP['C4']['Location'] != (0, 2, 0):
        count += 1
    elif CP['C5']['Location'] != (0, 0, 2):
        count += 1
    elif CP['C6']['Location'] != (2, 0, 2):
        count += 1
    elif CP['C7']['Location'] != (2, 2, 2):
        count += 1
    elif CP['C8']['Location'] != (0, 2, 2):
        count += 1
    return count


def wcCurrESide(CP, SP, sidePeiceLocation):
    # print('Rotating until X or Y face matches the front White face')
    matched = False
    sidePeiceRotating = spKeys[i]
    row = False
    column = False

    # Set Arrays to Generic Variables
    if sidePeiceLocation[0] == 1:
        cornerArray = rub.rightColumnC
        sideArray = rub.rightColumnS
        column = True
    elif sidePeiceLocation[0] == -1:
        cornerArray = rub.leftColumnC
        sideArray = rub.leftColumnS
        column = True
    elif sidePeiceLocation[1] == 1:
        cornerArray = rub.topRowC
        sideArray = rub.topRowS
        row = True
    elif sidePeiceLocation[1] == -1:
        cornerArray = rub.bottomRowC
        sideArray = rub.bottomRowS
        row = True

    while not matched:

        # print(sideArray)
        # Rotate Column
        if column:
            CP, SP = rub.rotateColumn(CP, cornerArray, SP,
                                      sideArray, 'CCW')
        elif row:
            CP, SP = rub.rotateRow(CP, cornerArray, SP,
                                   sideArray, 'CCW')
        # Get the index of the side we're rotating
        rotatedSide = sideArray.index(
            sidePeiceRotating)

        # Increment the side being rotated to account for the side name change which occurred due to rotation
        if column:
            # if the index is the last item in the list set the value to -1 to avoid indexing errors
            if rotatedSide == 0:
                rotatedSide = len(sideArray)
            sidePeiceRotating = sideArray[rotatedSide-1]
        elif row:
            # if the index is the last item in the list set the value to -1 to avoid indexing errors
            if rotatedSide == len(sideArray) - 1:
                rotatedSide = -1
            sidePeiceRotating = sideArray[rotatedSide+1]
        sidePeiceLocation = SP[sidePeiceRotating
                               ][spSpecificKeys[otherColorIndex]]

        whitePeiceLocation = SP[sidePeiceRotating
                                ][spSpecificKeys[whiteColorIndex]]

        currentCenter = rub.Rubik[spSpecificKeys[otherColorIndex]]['Direction']

        if sidePeiceLocation == currentCenter and whitePeiceLocation[2] == 1:
            matched = True
    return CP, SP


def wcCurrOppSide(CP, SP, sidePeiceLocation, currentCenter, i):
    if (currentCenter[0] + sidePeiceLocation[0] == 0 and (abs(currentCenter[0]) > 0 and abs(sidePeiceLocation[0]) > 0)) or (currentCenter[1] + sidePeiceLocation[1] == 0 and (abs(currentCenter[1]) > 0 and abs(sidePeiceLocation[1]) > 0)):
        # print('Opposite Found')

        front, back, top, bottom, right, left = rub.rowColumnFaceS(
            spKeys[i])
        # print(spKeys[i])
        if bottom:
            # print('Bottom')
            if right:
                # print('Right')

                for i in range(2):
                    if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                        CP, SP = rub.rotateColumn(
                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                    else:
                        CP, SP = rub.rotateRow(
                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                    CP, SP = rub.rotateRow(
                        CP, rub.topRowC, SP, rub.topRowS, 'CW')
                    CP, SP = rub.rotateColumn(
                        CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                    CP, SP = rub.rotateColumn(
                        CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                else:
                    CP, SP = rub.rotateColumn(
                        CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
                    CP, SP = rub.rotateRow(
                        CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                    CP, SP = rub.rotateRow(
                        CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')

                # print('Placed')
            elif left:
                # print('CW')
                CP, SP = rub.rotateFace(CP, rub.frontFaceC,
                                        SP, rub.frontFaceS, 'CW')
                for i in range(2):
                    if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                        CP, SP = rub.rotateColumn(
                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                    else:
                        CP, SP = rub.rotateRow(
                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                CP, SP = rub.rotateFace(CP, rub.frontFaceC,
                                        SP, rub.frontFaceS, 'CCW')
                CP, SP = rub.rotateRow(CP, rub.topRowC,
                                       SP, rub.topRowS, 'CCW')
                # print('Placed')
        if top:
            # print('top')
            if right:
                # print('Right')
                CP, SP = rub.rotateFace(CP, rub.frontFaceC,
                                        SP, rub.frontFaceS, 'CCW')
                for i in range(2):
                    if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                        CP, SP = rub.rotateColumn(
                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                    else:
                        CP, SP = rub.rotateRow(
                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                CP, SP = rub.rotateFace(CP, rub.frontFaceC,
                                        SP, rub.frontFaceS, 'CW')
                CP, SP = rub.rotateRow(CP, rub.bottomRowC,
                                       SP, rub.bottomRowS, 'CW')
                # print('Placed')
            elif left:
                # print('Left')
                # CP, SP = rub.rotateFace(CP, rub.frontFaceC,
                #                         SP, rub.frontFaceS, 'CW')
                for i in range(2):
                    if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                        CP, SP = rub.rotateColumn(
                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                    else:
                        CP, SP = rub.rotateRow(
                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')

                if spSpecificKeys[otherColorIndex] == 'Green' or spSpecificKeys[otherColorIndex] == 'Blue':
                    # Move White Peice to align with White Center
                    CP, SP = rub.rotateRow(
                        CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')

                    # Move Left Column to ensure the left side Peice remains undisturbed
                    CP, SP = rub.rotateColumn(
                        CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
                    CP, SP = rub.rotateColumn(
                        CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
                else:
                    # Move White Peice to align with White Center
                    CP, SP = rub.rotateColumn(
                        CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')

                    # Move top Row to ensure the left side Peice remains undisturbed
                    CP, SP = rub.rotateRow(
                        CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                    CP, SP = rub.rotateRow(
                        CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                # print('Placed')
    return CP, SP


def RightHandRule(self, CP, SP, SidePeice, Color):

    if Peice == 'C6':
        rightRuleC = self.rightColumnC
        rightRuleS = self.rightColumnS

        CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CW')
        CP, SP = self.rotateFace(
            CP, self.backFaceC, SP, self.backFaceS, 'CCW')
        CP, SP = self.rotateColumn(CP, rightRuleC, SP, rightRuleS, 'CCW')
        CP, SP = self.rotateFace(
            CP, self.backFaceC, SP, self.backFaceS, 'CW')

    return CP, SP


def leftAndRightHandRuleSides(CP, SP, sideKeys, i, backpeiceList, backpeice):
    frontface, backface, toprow, bottomrow, rightcolumn, leftcolumn = rub.rowColumnFaceS(
        sideKeys[i])

    print(backpeiceList[backpeice])

    if backpeiceList[backpeice] == 'Orange':

        print('Left Column')
        if toprow:
            print('S9: Left')
            # Left Column
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            # Back Face
            # Top Row
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
        else:
            print('S4: Right')
            # Left Column
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            # Back Face
            # Bottom Row
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
    elif backpeiceList[backpeice] == 'Red':
        print('Right Column')
        if toprow:
            print('S11: Right')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            # Back Face
            # Top Row
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
        else:
            print('S2: Left')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            # Back Face
            # Bottom Row
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
    elif backpeiceList[backpeice] == 'Blue':
        print('Top Row')
        if rightcolumn:
            print('S11: Left')
            # Top Row
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            # Back Face
            # Right Column
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
        else:
            print('S9: Right')
            # Top Row
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateRow(
                CP, rub.topRowC, SP, rub.topRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            # Back Face
            # Left Column
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
    elif backpeiceList[backpeice] == 'Green':
        print('Bottom Row')
        if rightcolumn:
            print('S2: : Right')
            # Bottom Row
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            # Back Face
            # Right Column
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateColumn(
                CP, rub.rightColumnC, SP, rub.rightColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')

        else:
            print('S4: Left')
            # Bottom Row
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
            CP, SP = rub.rotateRow(
                CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            # Back Face
            # Left Column
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CCW')
            CP, SP = rub.rotateColumn(
                CP, rub.leftColumnC, SP, rub.leftColumnS, 'CW')
            CP, SP = rub.rotateFace(
                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')

    return CP, SP


Countc = 0
Counts = 0
matches = 0

# Initialize
rub = RubikCube()
OrderedCube = rub.Rubik
CP = rub.CornerPeices
SP = rub.SidePeices

fail = 0
for run in range(1000):
    # Next Steps
    CP, SP = rub.randomizer(CP, SP, 500)
    # Solve White Cross
    CP, SP = rub.SolveWhiteCross(CP, SP)
    # Solve White Corners
    CP, SP = rub.SolveWhiteCorners(CP, SP)

    # Solve Second Layer Sides
    sideKeys = ['S2', 'S4', 'S9', 'S11']
    backKeys = ['S3', 'S7', 'S12', 'S8']
    SecondLayerSolved = False
    # rub.PlotRubik(CP, SP)

    attempt = 0

    while not SecondLayerSolved:
        attempt += 1
        for i in range(len(sideKeys)):

            # print(SP[sideKeys[i]])
            sideKeysList = list(SP[sideKeys[i]])
            # Check if side peice is not in the correct position
            if (rub.Rubik[sideKeysList[1]]['Direction'] != SP[sideKeys[i]][sideKeysList[1]]) or (rub.Rubik[sideKeysList[2]]['Direction'] != SP[sideKeys[i]][sideKeysList[2]]):
                # Check the back face for the correct peice
                print(rub.SideDict[sideKeys[i]].keys())

                sideDictKeys = list(rub.SideDict[sideKeys[i]].keys())
                for j in range(len(backKeys)):
                    matched = False
                    applicableBackPeice = False
                    backpeiceList = list(SP[backKeys[j]])
                    if (sideDictKeys[1] == backpeiceList[1]) and (sideDictKeys[2] == backpeiceList[2]):
                        applicableBackPeice = True
                        # print(backpeiceList)
                        # print('True')
                        # Find the color adjacent to the back face
                        adjacentPeice = 0
                        for k in range(len(backpeiceList)):
                            if backpeiceList[k] != 'Location':
                                if SP[backKeys[j]][backpeiceList[k]][2] != -1:
                                    # print(SP[backKeys[j]][backpeiceList[k]])
                                    # print(backpeiceList[k])
                                    adjacentPeice = k
                                    if k == 1:
                                        backpeice = 2
                                    else:
                                        backpeice = 1

                        # print(backpeiceList[adjacentPeice])
                        # if adjacentPeice != 0:
                        # print(SP[backKeys[j]][backpeiceList[adjacentPeice]])
                        # print(backpeiceList[adjacentPeice])
                        # print(rub.Rubik[backpeiceList[adjacentPeice]]['Direction'])

                        if rub.Rubik[backpeiceList[adjacentPeice]]['Direction'] != SP[backKeys[j]][backpeiceList[adjacentPeice]]:

                            tempLoc = j
                            while not matched:

                                # print(SP[backKeys[tempLoc]][backpeiceList[adjacentPeice]])
                                # print(SP[backKeys[tempLoc]])
                                # print(backKeys[tempLoc])
                                # print(tempLoc)
                                # Rotate Backface
                                CP, SP = rub.rotateFace(
                                    CP, rub.backFaceC, SP, rub.backFaceS, 'CW')

                                # Adjust References
                                tempLoc -= 1
                                if tempLoc == -1:
                                    tempLoc = len(backKeys)-1

                                # print()
                                # print(SP[backKeys[tempLoc]][backpeiceList[adjacentPeice]])
                                # print(SP[backKeys[tempLoc]])
                                # print(backKeys[tempLoc])
                                # print(tempLoc)

                                # backpeiceList = list(SP[backKeys[tempLoc]])
                                if SP[backKeys[tempLoc]][backpeiceList[adjacentPeice]] == rub.Rubik[backpeiceList[adjacentPeice]]['Direction']:
                                    print('Matched')
                                    matched = True
                                    print(
                                        rub.Rubik[backpeiceList[backpeice]]['Direction'])

                                    destinationFaceX = -1 * \
                                        rub.Rubik[backpeiceList[backpeice]
                                                  ]['Direction'][0]
                                    destinationFaceY = -1 * \
                                        rub.Rubik[backpeiceList[backpeice]
                                                  ]['Direction'][1]
                                    destinationFaceZ = -1 * \
                                        rub.Rubik[backpeiceList[backpeice]
                                                  ]['Direction'][2]

                                    destinationFace = (
                                        destinationFaceX, destinationFaceY, destinationFaceZ)

                                    destinationMatch = False
                                    while not destinationMatch:
                                        CP, SP = rub.rotateFace(
                                            CP, rub.backFaceC, SP, rub.backFaceS, 'CW')

                                        # Adjust References
                                        tempLoc -= 1
                                        if tempLoc == -1:
                                            tempLoc = len(backKeys)-1

                                        if SP[backKeys[tempLoc]][backpeiceList[adjacentPeice]] == destinationFace:
                                            destinationMatch = True

                                    CP, SP = leftAndRightHandRuleSides(
                                        CP, SP, sideKeys, i, backpeiceList, backpeice)
                            # rub.PlotRubik(CP, SP)
                            break
                        else:
                            CP, SP = rub.rotateFace(
                                CP, rub.backFaceC, SP, rub.backFaceS, 'CW')
                if not applicableBackPeice:

                    # print('Before')
                    # rub.PlotRubik(CP, SP)

                    # backpeiceList = list(SP[backKeys[j]])

                    CP, SP = leftAndRightHandRuleSides(
                        CP, SP, sideKeys, i, sideDictKeys, 1)

                    # print('After')
                    # rub.PlotRubik(CP, SP)

                print(f"Appliable Back Peice: {applicableBackPeice}")

        matchCount = 0
        for m in range(len(sideKeys)):
            # print(SP[sideKeys[i]])
            sideKeysList = list(SP[sideKeys[m]])
            # Check if side peice is not in the correct position
            if (rub.Rubik[sideKeysList[1]]['Direction'] != SP[sideKeys[m]][sideKeysList[1]]) or (rub.Rubik[sideKeysList[2]]['Direction'] != SP[sideKeys[m]][sideKeysList[2]]):
                continue
            else:
                matchCount += 1

        if matchCount == 4:
            SecondLayerSolved = True

        if attempt == 15:
            fail += 1
            # rub.PlotRubik(CP, SP)
            SecondLayerSolved = True

print(f"Number of failures: {fail}")
# print(matchCount)
# rub.PlotRubik(CP, SP)
