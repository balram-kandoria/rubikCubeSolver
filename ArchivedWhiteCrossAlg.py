
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
