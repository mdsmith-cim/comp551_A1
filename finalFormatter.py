import csv
import re

allTheInfo = []
idSplitIntoRowsData = []
ageGroupAverageTill2014 = []

Y1TrainingSet = []
Y1TestSet = []

Y2TrainingSet = []
Y2TestSet = []

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

with open('ArrangedByID/FormattedAllInfo.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allTheInfo.append(participant)

with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        idSplitIntoRowsData.append(participant)


def getMeanForAgeGroup(runner):
    ageGroup = runner[8]
    ageGroupAverage = 0
    alreadyExists = [event for event in ageGroupAverageTill2014 if event[0] == ageGroup]

    if len(alreadyExists) > 0:
        ageGroupAverage = alreadyExists[0][1]
    elif not runner[0] == '768':
        ageGropuList = [event for event in allTheInfo if event[8] == ageGroup]
        totalTime = 0
        itemCount = 0

        for person in ageGropuList:
            yearList = re.sub("[\[\] ]", "", person[1]).split(",")
            timeList = re.sub("[\[\] ]", "", person[3]).split(",")

            if '2015' in yearList:
                for item in range(1, len(yearList)):
                    if not '-1' in timeList[item]:
                        totalTime = totalTime + int(timeList[item])
                        itemCount = itemCount + 1
            else:
                for item in range(0, len(yearList)):
                    if not '-1' in timeList[item]:
                        totalTime = totalTime + int(timeList[item])
                        itemCount = itemCount + 1

        ageGroupAverage = int(totalTime / itemCount)
        newAgeGroupTime = []
        newAgeGroupTime.append(ageGroup)
        newAgeGroupTime.append(ageGroupAverage)
        ageGroupAverageTill2014.append(newAgeGroupTime)
    return ageGroupAverage

for runner in allTheInfo:
    newY1Info = []
    didTheyAttend = -1

    playerId = runner[0]
    noOfMontrealMarathons = int(runner[4])
    noOfAllRaces = int(runner[5])
    averageRuntimeInMarathons = int(re.sub("[\[\] ]","", runner[6]).split(",")[0])
    category = runner[8]


    if '2015' in runner[1]:
        didTheyAttend = 1
        noOfMontrealMarathons = noOfMontrealMarathons - 1
        noOfAllRaces = noOfAllRaces - 1

        if noOfMontrealMarathons == 0 and averageRuntimeInMarathons == 0:
            averageRuntimeInMarathons = getMeanForAgeGroup(runner)
    else:
        didTheyAttend = 0

    if averageRuntimeInMarathons == -1:
        averageRuntimeInMarathons = getMeanForAgeGroup(runner)

    newY1Info.append(playerId)
    newY1Info.append(noOfMontrealMarathons)
    newY1Info.append(noOfAllRaces)
    newY1Info.append(averageRuntimeInMarathons)
    newY1Info.append(category)
    newY1Info.append(didTheyAttend)

    Y1TrainingSet.append(newY1Info)


for runner in allTheInfo:
    newY1Info = []

    playerId = runner[0]
    noOfMontrealMarathons = int(runner[4])
    noOfAllRaces = int(runner[5])
    averageRuntimeInMarathons = int(re.sub("[\[\] ]", "", runner[6]).split(",")[1])
    category = runner[8]

    if averageRuntimeInMarathons == -1:
        averageRuntimeInMarathons = getMeanForAgeGroup(runner)

    newY1Info.append(playerId)
    newY1Info.append(noOfMontrealMarathons)
    newY1Info.append(noOfAllRaces)
    newY1Info.append(averageRuntimeInMarathons)
    newY1Info.append(category)

    Y1TestSet.append(newY1Info)
    # print(newY1Info)

nonExistantPlayers = []

for runner in idSplitIntoRowsData:
    newY2Info = []

    runnerId = runner[0]
    runnerYear = runner[1].split("-")[0]
    runnerEvent = runner[2].replace(" ", "").upper()
    runnerRaceType = runner[3]

    runnerInfo = [event for event in allTheInfo if event[0] == runnerId]
    if len(runnerInfo) == 0:
        if not runnerId in nonExistantPlayers:
            nonExistantPlayers.append([runnerId])
    else:
        if 'MARATHON' in runnerRaceType and 'HALF' not in runnerRaceType and 'DEMI' not in runnerRaceType and not runnerYear == "2016" and not runnerYear == "2015":
            runnerDetailedInfo = runnerInfo[0]

            avgWithoutCurrentYear = re.sub("[\[\] ]", "", runnerDetailedInfo[6]).split(",")
            noOfRacesInCurrentYear = re.sub("[\[\] ]", "", runnerDetailedInfo[7]).split(",")

            if runnerYear == '2012':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[3])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[4])
            elif runnerYear == '2013':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[4])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[3])
            elif runnerYear == '2014':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[5])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[2])
            # elif runnerYear == '2015':
            #     avgWithoutCurrentYear = int(avgWithoutCurrentYear[6])
            #     noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[1])
            # elif runnerYear == '2016':
            #     avgWithoutCurrentYear = int(avgWithoutCurrentYear[7])
            #     noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[0])

            category = runnerDetailedInfo[8]
            finishTime2015 = 0

            if '2015' in runnerDetailedInfo[1]:
                finishTime2015 = int(re.sub("[\[\] ]", "", runnerDetailedInfo[3]).split(",")[0])

            newY2Info.append(int(runnerId))
            newY2Info.append(avgWithoutCurrentYear)
            newY2Info.append(category)
            newY2Info.append(noOfRacesInCurrentYear)
            newY2Info.append(finishTime2015)
            # print(newY2Info)
    Y2TrainingSet.append(newY2Info)


for runner in idSplitIntoRowsData:
    newY2Info = []

    runnerId = runner[0]
    runnerYear = runner[1].split("-")[0]
    runnerEvent = runner[2].replace(" ", "").upper()
    runnerRaceType = runner[3]

    runnerInfo = [event for event in allTheInfo if event[0] == runnerId]
    if len(runnerInfo) == 0:
        if not runnerId in nonExistantPlayers:
            nonExistantPlayers.append(runnerId)
    else:
        if 'MARATHON' in runnerRaceType and 'HALF' not in runnerRaceType and 'DEMI' not in runnerRaceType and not runnerYear == "2016":
            runnerDetailedInfo = runnerInfo[0]

            avgWithoutCurrentYear = re.sub("[\[\] ]", "", runnerDetailedInfo[6]).split(",")
            noOfRacesInCurrentYear = re.sub("[\[\] ]", "", runnerDetailedInfo[7]).split(",")

            if runnerYear == '2012':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[3])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[4])
            elif runnerYear == '2013':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[4])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[3])
            elif runnerYear == '2014':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[5])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[2])
            elif runnerYear == '2015':
                avgWithoutCurrentYear = int(avgWithoutCurrentYear[6])
                noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[1])
            # elif runnerYear == '2016':
            #     avgWithoutCurrentYear = int(avgWithoutCurrentYear[7])
            #     noOfRacesInCurrentYear = int(noOfRacesInCurrentYear[0])

            category = runnerDetailedInfo[8]

            newY2Info.append(int(runnerId))
            newY2Info.append(avgWithoutCurrentYear)
            newY2Info.append(category)
            newY2Info.append(noOfRacesInCurrentYear)
            # print(newY2Info)
    Y2TestSet.append(newY2Info)


writeToCSV("FinalDataSets/Y1TrainSet", Y1TrainingSet)
writeToCSV("FinalDataSets/Y1TestSet", Y1TestSet)
writeToCSV("FinalDataSets/Y2TrainingSet", Y2TrainingSet)
writeToCSV("FinalDataSets/Y2TestSet", Y2TestSet)
writeToCSV("FinalDataSets/IdsNotListed", nonExistantPlayers)

# 0 - PlayerID
# 1 - Montreal Marathon Years
# 2 - Marathon Distances
# 3 - Montreal Marathon RunTimes
# 4 - Total Number of Montreal Marathons Participated
# 5 - Total Number All Races in history
# 6 - ========================
#       0 - Average marathon time till 2014
#       1 - Average marathon time till 2015
#       2 - Average marathon Time till 2016
#        - +++++++++++++++++++++++++
#           3 - Average all marathons except 2012
#           4 - Average all marathons except 2013
#           5 - Average all marathons except 2014
#           6 - Average all marathons except 2015
#           7 - Average all marathons except 2016
#     +++++++++++++++++++++++++
# 7 - =========================
#   0 - No of Races in 2016
#   1 - No of Races in 2015
#   2 - No of Races in 2014
#   3 - No of Races in 2013
#   4 - No of Races in 2012
# =========================
# 8 - Category