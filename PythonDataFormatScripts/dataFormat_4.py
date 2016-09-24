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

# ===================================================================================
#   Load the data set consisting of  all information regarding every specific runner
# ===================================================================================
with open('ArrangedByID/FormattedAllInfo.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allTheInfo.append(participant)

# ========================================================================
#     Load all the data initially generated from the given data-set
# ========================================================================
with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        idSplitIntoRowsData.append(participant)

# ========================================================================
#     Function to get the Mean Running time for a given Age-Group
# ========================================================================
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


# =======================================================================
#     From the loaded information generate the Training set for Y1 & Y2
#          Consists of data about Montreal Participants until 2014
# =======================================================================
for runner in allTheInfo:
    newY1Info = []
    newY2Info = []
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

    finish_2015Time = 0
    if '2015' in runner[1]:
        finish_2015Time = int(re.sub("[\[\] ]", "", runner[3]).split(",")[0])

    newY1Info.append(playerId)
    newY1Info.append(noOfMontrealMarathons)
    newY1Info.append(noOfAllRaces)
    # newY1Info.append(averageRuntimeInMarathons)
    newY1Info.append(category)
    newY1Info.append(didTheyAttend)

    newY2Info.append(playerId)
    newY2Info.append(averageRuntimeInMarathons)
    newY2Info.append(noOfAllRaces)
    newY2Info.append(category)
    newY2Info.append(finish_2015Time)

    Y1TrainingSet.append(newY1Info)
    if not newY2Info[4] == 0 and not newY2Info[4] == -1:
        Y2TrainingSet.append(newY2Info)

# =======================================================================
#     From the loaded information generate the Testing set for Y1 & Y2
#          Consists of data about Montreal Participants until 2015
# =======================================================================
for runner in allTheInfo:
    newY1Info = []
    newY2Info = []

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
    newY1Info.append(category)

    newY2Info.append(playerId)
    newY2Info.append(averageRuntimeInMarathons)
    newY2Info.append(noOfAllRaces)
    newY2Info.append(category)

    Y1TestSet.append(newY1Info)
    Y2TestSet.append(newY2Info)

# ============================================================================================
#       Get a list of all other players who hadn't participated in the Montreal Marathon ever
#             and hence left out in the above formulated two sets
# ============================================================================================
nonExistantPlayers = []
for runner in idSplitIntoRowsData:
    newY2Info = []
    runnerId = runner[0]
    runnerInfo = [event for event in allTheInfo if event[0] == runnerId]
    if len(runnerInfo) == 0:
        if not [runnerId] in nonExistantPlayers:
            nonExistantPlayers.append([runnerId])


# ========================================================================
#       Write all mined data into seperate files for later analysis
# ========================================================================
writeToCSV("FinalDataSets/DataSetOn23rd/Y1TrainSet", Y1TrainingSet)
writeToCSV("FinalDataSets/DataSetOn23rd/Y1TestSet", Y1TestSet)
writeToCSV("FinalDataSets/DataSetOn23rd/Y2TrainingSet", Y2TrainingSet)
writeToCSV("FinalDataSets/DataSetOn23rd/Y2TestSet", Y2TestSet)
writeToCSV("FinalDataSets/IdsNotListed", nonExistantPlayers)


# ========================================================================
#       Indexs of each data-item in the List of player information
# ========================================================================
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