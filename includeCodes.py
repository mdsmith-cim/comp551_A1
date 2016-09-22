import csv
import itertools
import re

allRunnersEver = []
montrealParticipants = []
raceTypes = []


def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

def printPlayerOtherInfo(playerId, entireList):
    listOfPreviousEvents = list(filter(lambda r: r[0] == playerId, entireList))
    if len(listOfPreviousEvents) > 1:
        print(playerId)
        print("-------------------------------------------")
        for entry in listOfPreviousEvents:
            print (entry)
        print ("==========================================")

def getAverageTime(listOfTimes, listOfDistances, count):
    allSecondsAdded = 0
    secondsItem = []

    for item in range(0, len(listOfTimes)):
        distanceRan = int(listOfDistances[item])
        distanceMultiple = 40 / distanceRan

        if not distanceMultiple == 1:
            distanceMultiple = distanceMultiple * 1.15

        # print (listOfTimes[item])
        if not '-1' in listOfTimes[item]:
            dataSplit = listOfTimes[item].split(":")
            hours = int(dataSplit[0])
            minutes = int(dataSplit[1])
            seconds = int(dataSplit[2])

            convertedToSeconds = ((hours * 60 * 60) + (minutes * 60) + (seconds)) * distanceMultiple
            secondsItem.append(convertedToSeconds)
        else:
            secondsItem.append(-1)

    for currentTime in secondsItem:
        if not '-1' in str(currentTime):
            allSecondsAdded = allSecondsAdded + currentTime

    averageSeconds = (allSecondsAdded / count)

    avgHours = int(averageSeconds / (60 * 60))
    averageSeconds = averageSeconds % (60 * 60)
    avgMinutes = int(averageSeconds / 60)
    avgSeconds = averageSeconds % 60

    averageTime = str(avgHours) + ":" + str(avgMinutes) + ":" + str(int(avgSeconds))
    return averageTime

# with open('RaceTypes/typesOfRacesWithDistance.csv', newline='') as marathonData:  # Reads the given csv
#     csvReader = csv.reader(marathonData)
#     for raceType in csvReader:
#         raceTypes.append(raceType)

# for player in range(0, len(montrealParticipants)):
#     raceType = montrealParticipants[player][3].upper().replace(" ", "")
#
#     raceEventDetail = [raceEvent for raceEvent in raceTypes if raceEvent[0] == raceType]
#     montrealParticipants[player][3] = raceEventDetail[0][1]

with open('ArrangedByID/editedDataByID.csv',
          newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allRunnersEver.append(participant)


with open('MontrealMarathon/montrealMarathonWithCountPerParticipant.csv',
          newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        montrealParticipants.append(participant)

montrealRacerCategories = []

for player in montrealParticipants:
    allSimilarCategories = [category for category in montrealRacerCategories if player[4] == category[0]]
    if len(allSimilarCategories) == 0:
        montrealRacerCategories.append([player[4]])

montrealRacerCategories.sort()

for player in range(0, len(montrealParticipants)):
    if montrealParticipants[player][4] == "F05" or montrealParticipants[player][4] == "F13+":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        if montrealParticipants[player][0] == '1637' or montrealParticipants[player][0] == "179" or \
                        montrealParticipants[player][0] == "890" or montrealParticipants[player][0] == "4049" or \
                        montrealParticipants[player][0] == "4746" or montrealParticipants[player][0] == "4754":
            montrealParticipants[player][4] = "F55-59"

        elif montrealParticipants[player][0] == '2755':
            montrealParticipants[player][4] = "F45-49"

        elif montrealParticipants[player][0] == '3609':
            montrealParticipants[player][4] = "F35-39"

        elif montrealParticipants[player][0] == '6078':
            montrealParticipants[player][4] = "F30-34"
        else:
            print ("Some other guy/girl %s with [%s]" % \
                   (montrealParticipants[player][0], montrealParticipants[player][4]))

    elif montrealParticipants[player][4] == "GARCONS 8" or montrealParticipants[player][4] == "M04" or \
                    montrealParticipants[player][4] == "M05" or montrealParticipants[player][4] == "M06" or \
                    montrealParticipants[player][4] == "M07" or montrealParticipants[player][4] == "M09" or \
                    montrealParticipants[player][4] == "M13+":

        if montrealParticipants[player][0] == '11' or montrealParticipants[player][0] == '17' or\
                montrealParticipants[player][0] == '4956' or montrealParticipants[player][0] == '5351' or \
                montrealParticipants[player][0] == '136' or montrealParticipants[player][0] == '962' or \
                montrealParticipants[player][0] == '1999' or montrealParticipants[player][0] == '7141' or \
                montrealParticipants[player][0] == '5030' or montrealParticipants[player][0] == '3612':
            montrealParticipants[player][4] = "M35-39"

        elif montrealParticipants[player][0] == '6264' or montrealParticipants[player][0] == '6740' or \
                montrealParticipants[player][0] == '7746' or montrealParticipants[player][0] == '3009' or \
                montrealParticipants[player][0] == '3910' or montrealParticipants[player][0] == '5248' or \
                montrealParticipants[player][0] == '6892':
            montrealParticipants[player][4] = "M30-34"

        elif montrealParticipants[player][0] == '6134' or montrealParticipants[player][0] == '700' or \
                montrealParticipants[player][0] == '5' or montrealParticipants[player][0] == '3060':
            montrealParticipants[player][4] = "M45-49"

        elif montrealParticipants[player][0] == '1529' or montrealParticipants[player][0] == '5005' or \
                montrealParticipants[player][0] == '566' or montrealParticipants[player][0] == '2315' or \
                montrealParticipants[player][0] == '4628' or montrealParticipants[player][0] == '3803' or \
                montrealParticipants[player][0] == '8261':
            montrealParticipants[player][4] = "M40-44"

        elif montrealParticipants[player][0] == '7889':
            montrealParticipants[player][4] = "M18-24"

        elif montrealParticipants[player][0] == "311":
            montrealParticipants[player][4] = "M18-24"
        else:
            print("Some other guy/girl %s with [%s]" % \
                  (montrealParticipants[player][0], montrealParticipants[player][4]))

    elif montrealParticipants[player][4] == "M---11":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        montrealParticipants[player][4] = "M60-64"

    elif montrealParticipants[player][4] == "M08":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        if montrealParticipants[player][0] == '7182':
            montrealParticipants[player][4] = "M35-39"

    elif montrealParticipants[player][4] == "M11-":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        montrealParticipants[player][4] = "M30-34"

    elif montrealParticipants[player][4] == "M70+":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        montrealParticipants[player][4] = "M70-79"


    elif montrealParticipants[player][4] == "NO AGE" or montrealParticipants[player][4] == "NOAGE":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        if montrealParticipants[player][0] == '5332' or montrealParticipants[player][0] == "1154":
            montrealParticipants[player][4] = "F25-29"

        elif montrealParticipants[player][0] == '5296':
            montrealParticipants[player][4] = "F30-34"

        elif montrealParticipants[player][0] == "3223" or montrealParticipants[player][0] == "3661":
            montrealParticipants[player][4] = "F45-49"

        elif montrealParticipants[player][0] == "8418" or montrealParticipants[player][0] == "4862":
            montrealParticipants[player][4] = "M35-39"
        else:
            print("Some other guy/girl %s with [%s]" % \
                  (montrealParticipants[player][0], montrealParticipants[player][4]))

    elif montrealParticipants[player][4] == "U0-0":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        if montrealParticipants[player][0] == '6880':
            montrealParticipants[player][4] = "F25-29"

        elif montrealParticipants[player][0] == "447":
            montrealParticipants[player][4] = "M18-24"
        else:
            print("Some other guy/girl %s with [%s]" % \
                  (montrealParticipants[player][0], montrealParticipants[player][4]))

    elif montrealParticipants[player][4] == "F70+":
        # printPlayerOtherInfo(montrealParticipants[player][0], allRunnersEver)
        if montrealParticipants[player][0] == '1076' or montrealParticipants[player][0] == '4382':
            montrealParticipants[player][4] = "F70-79"
        else:
            print("Some other guy/girl %s with [%s]" % \
                  (montrealParticipants[player][0], montrealParticipants[player][4]))

updatedParticipantsWithout2015 = []
only2015Participants = []

# for entry in montrealParticipants:
#     updatedParticipantsWithout2015.append(entry)

for index in range(0, len(montrealParticipants)):
    currentEntry = montrealParticipants[index][:]
    entryFor2015 = currentEntry[:]
    yearList = re.sub("[\[\]' ]", "", currentEntry[1]).split(",")
    distanceList = re.sub("[\[\]' ]", "", currentEntry[2]).split(",")
    timeList = re.sub("[\[\]' ]", "", currentEntry[3]).split(",")

    totalMontrealMarathons = currentEntry[5]
    totalRaces = currentEntry[7]

    if '2015' in yearList:
        if len(yearList) > 1:
            entryFor2015[1] = [yearList[0]]
            entryFor2015[2] = [distanceList[0]]
            entryFor2015[3] = [timeList[0]]

            del (yearList[0])
            del (distanceList[0])
            del (timeList[0])

            averageTime = getAverageTime(timeList, distanceList, len(yearList))

            currentEntry[1] = yearList
            currentEntry[2] = distanceList
            currentEntry[3] = timeList
            currentEntry[5] = int(totalMontrealMarathons) - 1
            currentEntry[6] = averageTime
            currentEntry[7] = int(totalRaces) - 1
            updatedParticipantsWithout2015.append(currentEntry)

            entryFor2015[6] = averageTime             #  Average time from previous Races
            only2015Participants.append(entryFor2015)
        else:
            # omits this entry of 2015
            only2015Participants.append(currentEntry)
            pass
    else:
        updatedParticipantsWithout2015.append(currentEntry)


writeToCSV("MontrealMarathon/montrealMarathonFinalData", montrealParticipants)
writeToCSV("MontrealMarathon/montrealMarathonFinalDataWithout2015", updatedParticipantsWithout2015)
writeToCSV("MontrealMarathon/montrealMarathonFinal2015OnlyData", only2015Participants)
writeToCSV("MontrealMarathon/montrealRacerCategories", montrealRacerCategories)


# ['768', "['2015']", "MARATHONOASISROCK'N'ROLLDEMONTREAL", '40', "['-1']", '', '1', '-1', '1']

# 1637 - F55-59   (F13+)
# 2755 - F45-49	(F05)
# 3609 - F35-39	(F13+)
# 6078 - F30-34	(F13+)
# ----------------------
# 179 - F55-59	(F13+)
# 890  - F55-59	(F13+)
# 4049  - F55-59	(F13+)
# 4746  - F55-59	(F13+)
# 4754  - F55-59	(F13+)
# ======================
#
# 11 - M35-39	(M13+)
# 17 - M35-39	(M13+)
# 700 - M45-49 (M13+)
# 1529 - M40-44 (M13+)
# 3009 - M30-34 (M13+)
# 4956 - M35-39 (M13+)
# 5005 - M40-44 (M13+)
# 5351 -	M35-39	(M13+)
# 6134 - M45-49 (M13+)
# 6264 - M30-34 (M13+)
# 6740 - M30-34 (M13+)
# 7746 - M30-34 (M13+)
# 7889 - M18-24 (M13+)
# ---------------------
# 311 - M18-24 (Similar timing as 7889 in same year)
# 3910 - M30-34 (Similar timing as 6740)
# 5248 - M30-34 (Similar timing as 6740)
# 6892 - M30-34 (Similar timing as 6740)
# 136 - M35-39 (Same timing as 7182 in same year)
# 962 - M35-39 (Same timing as 7182 in same year)
# 1999 - M35-39 (Same timing as 7182 in same year)
# 7141 - M35-39 (Same timing as 7182 in same year)
# 5030 - M35-39 (Similar timing as 11)
# 3612 - M35-39 (Similar timing as 4956)
# 566 - M40-44 (Similar timing as 5005)
# 2315 - M40-44 (Similar timing as 5005)
# 4628 - M40-44 (Similar timing as 5005)
# 3803 - M40-44 (Similar timing as 1529)
# 8261 - M40-44 (Simlar timing to 5082)
# 5 - 	M45-49	(Close to timing of 6134)
# 3060 - 	M45-49	(Close to timing of 6134)
# =====================
#
# 7182 - M35-39 (M08)
# ---------------------
# =====================
#
# 1120 - M70-79 (M70+)
# 5051 - M70-79 (M70+)
# ---------------------
# 1006 - M70-79 (M70+)
# 2037 - M70-79 (M70+)
# 3600 - M70-79 (M70+)
# 4739 - M70-79 (M70+)
# 5525 - M70-79 (M70+)
# 5815 - M70-79 (M70+)
# 6577 - M70-79 (M70+)
# 8505 - M70-79 (M70+)
# =====================
#
# 5332 - F25-29 (NOAGE)
# ---------------------
# 1154 - F25-29 (Same as 5113 in same year)
# 3223 - F45-49 (Same as 905 and 5747)
# 3661 - F45-49 (Same timing as 2013)
# 4862 - M35-39 (Same timing as 8355)
# 5296 - F30-34 (Same timing as 3930)
# 8418 - M35-39 (Close to 1660 in same year)
# =====================
#
# 6880 - F25-29 (U0-0)
# ---------------------
# 447 - M18-24 (Same timing as 8234 in same year)
# =====================
#
# 1076 - F70-79 (F70+)
# 4382 - F70-79 (F70+)
# ---------------------
# ============================================================

# 0 - RunnerID
# 1 - Years he participated in MontrealMarathon
# --------------------------------------
# 2 - EventName (MontrealMarathon)
# --------------------------------------
# 2 - EventType (Distance)
# 3 - FinishTimes of Previous Years
# 4 - Category
# 5 - Number of times participated in Marathon
# 6 - Average Finishtime
# 7 - No of all Racing Events in the past 4 years
# ============================================================

# 12 – 14
# 15 – 17
# 18 – 24
# 25 – 29
# 30 – 34
# 35 – 39
# 40 – 44
# 45 – 49
# 50 – 54
# 55 – 59
# 60 – 64
# 65 – 69
# 70-79
# 80

