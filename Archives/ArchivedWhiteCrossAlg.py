
# Alg Tests:
fail = 0
solve = 0
for i in range(500):
    ColorFlag = True

    temp = 0
    lim = 10
    CP, SP = rub.randomizer(CP, SP, 500)
    # rub.PlotRubik(CP, SP)
    spKeys = list(SP.keys())

    while ColorFlag:
        fix = 0
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
                        CP, SP = WonYFace(
                            CP, SP, i)
                    # Does White exist on the x or y faces
                    if not ran:
                        if (abs(SP[spKeys[i]][spSpecificKeys[j]][0]) == 1 or abs(SP[spKeys[i]][spSpecificKeys[j]][1]) == 1):
                            ran = True
                            print('White on either the x or y faces')

                            # Get the index of the other color
                            if j == 2:
                                print(spSpecificKeys[1])
                                otherColorIndex = 1
                                whiteColorIndex = 2
                            else:
                                print(spSpecificKeys[2])
                                otherColorIndex = 2
                                whiteColorIndex = 1

                            sidePeiceLocation = SP[spKeys[i]
                                                   ][spSpecificKeys[otherColorIndex]]
                            whitePeiceLocation = SP[spKeys[i]
                                                    ][spSpecificKeys[whiteColorIndex]]
                            currentCenter = rub.Rubik[spSpecificKeys[otherColorIndex]]['Direction']
                            print(
                                f"Color Peice Direction: {sidePeiceLocation}")
                            print(
                                f"Current Center Direction: {currentCenter}")
                            print(
                                f"White Peice Direction: {whitePeiceLocation}")

                            if currentCenter == sidePeiceLocation:
                                CP, SP = wcCurrESide(
                                    CP, SP, sidePeiceLocation)

                            elif (currentCenter[0] + sidePeiceLocation[0] == 0 and (abs(currentCenter[0]) > 0 and abs(sidePeiceLocation[0]) > 0)) or (currentCenter[1] + sidePeiceLocation[1] == 0 and (abs(currentCenter[1]) > 0 and abs(sidePeiceLocation[1]) > 0)):
                                CP, SP = wcCurrOppSide(
                                    CP, SP, sidePeiceLocation, currentCenter, i)

                            elif spKeys[i] in ['S1', 'S5', 'S6', 'S10']:
                                if spKeys[i] == 'S1':
                                    if (spSpecificKeys[otherColorIndex] == 'Green' and (sidePeiceLocation[2] == 1)) or (whitePeiceLocation[1] == -1):
                                        print('Rotating S1')
                                        CP, SP = rub.rotateRow(
                                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                                        CP, SP = rub.rotateRow(
                                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                                elif spKeys[i] == 'S5':
                                    if (spSpecificKeys[otherColorIndex] == 'Orange' and (sidePeiceLocation[2] == 1)) or (whitePeiceLocation[0] == -1):
                                        print('Rotating S5')
                                        CP, SP = rub.rotateColumn(
                                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                                        CP, SP = rub.rotateColumn(
                                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                                elif spKeys[i] == 'S6':
                                    if (spSpecificKeys[otherColorIndex] == 'Red' and (sidePeiceLocation[2] == 1)) or (whitePeiceLocation[0] == 1):
                                        print('Rotating S6')
                                        CP, SP = rub.rotateColumn(
                                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                                        CP, SP = rub.rotateColumn(
                                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                                elif spKeys[i] == 'S10':
                                    if (spSpecificKeys[otherColorIndex] == 'Blue' and (sidePeiceLocation[2] == 1)) or (whitePeiceLocation[1] == 1):
                                        print('Rotating S10')
                                        CP, SP = rub.rotateRow(
                                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                                        CP, SP = rub.rotateRow(
                                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')

                            # abs(sidePeiceLocation[0]) == 1 or abs(sidePeiceLocation[1]) == 1:
                            else:
                                print('FLIPPED')
                                if currentCenter != sidePeiceLocation:
                                    print(spKeys[i])
                                    CP, SP = rub.switchOrientation1(
                                        CP, SP, spKeys[i])
                                    currentCenter = rub.Rubik[spSpecificKeys[otherColorIndex]]['Direction']
                                    sidePeiceLocation = SP[spKeys[i]
                                                           ][spSpecificKeys[otherColorIndex]]
                                    print(currentCenter)
                                    print(sidePeiceLocation)
                                    if currentCenter == sidePeiceLocation:
                                        print('Here')
                                        CP, SP = wcCurrESide(
                                            CP, SP, sidePeiceLocation)
                                    else:
                                        print('Now')
                                        CP, SP = wcCurrOppSide(
                                            CP, SP, sidePeiceLocation, currentCenter, i)

        # print(f"The COLOR WE ARE LOOKING FOR: {SP['S1']}")

        # ''' FLIP SIDE PEICES IF THEY ARE ON THE FRONT FACE IN THE RIGHT POSITION IN THE WRONG DIRECTION'''
        # try:
        #     color_list = list(SP['S1'].keys())
        #     for m in range(len(color_list)):
        #         if color_list[m] in ['Green']:
        #             if SP['S1']['White'][2] != 1:
        #                 print('FINAL FLIP GREEN')
        #                 CP, SP = rub.rotateRow(CP, rub.bottomRowC, SP,
        #                                        rub.bottomRowS, 'CCW')
        #                 CP, SP = rub.switchOrientation1(
        #                     CP, SP, 'S2')
        #                 CP, SP = rub.rotateRow(
        #                     CP, rub.bottomRowC, SP, rub.bottomRowS, 'CW')

        #     color_list = list(SP['S5'].keys())
        #     for m in range(len(color_list)):
        #         if color_list[m] in ['Orange']:
        #             if SP['S5']['White'][2] != 1:
        #                 print('FINAL FLIP ORANGE')
        #                 CP, SP = rub.rotateColumn(CP, rub.leftColumnC, SP,
        #                                           rub.leftColumnS, 'CW')
        #                 CP, SP = rub.switchOrientation1(
        #                     CP, SP, 'S9')
        #                 CP, SP = rub.rotateColumn(CP, rub.leftColumnC, SP,
        #                                           rub.leftColumnS, 'CCW')

        #     color_list = list(SP['S10'].keys())
        #     for m in range(len(color_list)):
        #         if color_list[m] in ['Blue']:
        #             if SP['S10']['White'][2] != 1:
        #                 print('FINAL FLIP Blue')
        #                 CP, SP = rub.rotateRow(
        #                     CP, rub.topRowC, SP, rub.topRowS, 'CCW')
        #                 CP, SP = rub.switchOrientation1(
        #                     CP, SP, 'S11')
        #                 CP, SP = rub.rotateRow(
        #                     CP, rub.topRowC, SP, rub.topRowS, 'CW')

        #     color_list = list(SP['S6'].keys())
        #     for m in range(len(color_list)):
        #         if color_list[m] in ['Red']:
        #             if SP['S6']['White'][2] != 1:
        #                 print('FINAL FLIP Red')
        #                 CP, SP = rub.rotateColumn(CP, rub.rightColumnC, SP,
        #                                           rub.rightColumnS, 'CW')
        #                 CP, SP = rub.switchOrientation1(
        #                     CP, SP, 'S11')
        #                 CP, SP = rub.rotateColumn(
        #                     CP, rub.topRowC, SP, rub.topRowS, 'CCW')
        # except:
        #     continue

        # rub.PlotRubik(CP, SP)
        temp += 1

        try:
            if (SP['S1']['White'][2] == 1) and (SP['S5']['White'][2] == 1) and (SP['S6']['White'][2] == 1) and (SP['S10']['White'][2] == 1):
                if (SP['S1']['Green'][1] == -1) and (SP['S5']['Orange'][0] == -1) and (SP['S6']['Red'][0] == 1) and (SP['S10']['Blue'][1] == 1):
                    print('ALL MATCHING')
                    ColorFlag = False
                    solve += 1
        except:
            print('NOT MATCHED')
            if temp == lim:
                fail += 1
                rub.PlotRubik(CP, SP)
                break
            else:
                try:
                    if (SP['S1']['Green'][1] == -1):
                        continue
                except:
                    if fix == 0:
                        CP, SP = rub.rotateRow(
                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                        CP, SP = rub.rotateRow(
                            CP, rub.bottomRowC, SP, rub.bottomRowS, 'CCW')
                        if SP['S1']['White'] == (0, 0, -1):
                            CP, SP = WonYFace(
                                CP, SP, i)
                            fix += 1

                try:
                    if (SP['S5']['Orange'][0] == -1):
                        continue
                except:
                    if fix == 0:
                        CP, SP = rub.rotateColumn(
                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                        CP, SP = rub.rotateColumn(
                            CP, rub.leftColumnC, SP, rub.leftColumnS, 'CCW')
                        fix += 1
                try:
                    if (SP['S10']['Blue'][1] == 1):
                        continue
                except:
                    if fix == 0:
                        CP, SP = rub.rotateRow(
                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                        CP, SP = rub.rotateRow(
                            CP, rub.topRowC, SP, rub.topRowS, 'CCW')
                        fix += 1
                try:
                    if (SP['S6']['Red'][0] == 1):
                        continue
                except:
                    if fix == 0:
                        CP, SP = rub.rotateColumn(
                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                        CP, SP = rub.rotateColumn(
                            CP, rub.rightColumnC, SP, rub.rightColumnS, 'CCW')
                        fix += 1


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
