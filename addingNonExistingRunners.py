import csv
import re

idSplitIntoRowsData = []
allTheInfo = []
nonExistantPlayers = []

dataOfEveryone = []

# Y1TrainingSet = []
Y1TestSet = []
# Y2TrainingSet = []
Y2TestSet = []

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        idSplitIntoRowsData.append(participant)

with open('ArrangedByID/FormattedAllInfo.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allTheInfo.append(participant)

with open('MontrealMarathon/montrealMarathonFinalData.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        dataOfEveryone.append(participant)

# with open('FinalDataSets/DataSetOn23rd/Y1TrainSet.csv', newline='') as marathonData:  # Reads the given csv
#     csvReader = csv.reader(marathonData)
#     for participant in csvReader:
#         Y1TrainingSet.append(participant)

with open('FinalDataSets/DataSetOn23rd/Y1TestSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y1TestSet.append(participant)

# with open('FinalDataSets/DataSetOn23rd/Y2TrainingSet.csv', newline='') as marathonData:  # Reads the given csv
#     csvReader = csv.reader(marathonData)
#     for participant in csvReader:
#         Y2TrainingSet.append(participant)

with open('FinalDataSets/DataSetOn23rd/Y2TestSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y2TestSet.append(participant)

# with open('FinalDataSets/IdsNotListed.csv', newline='') as marathonData:  # Reads the given csv
#     csvReader = csv.reader(marathonData)
#     for participant in csvReader:
#         nonExistantPlayers.append(participant)

ageGroupAverageTill2014 = []

def getMeanForAgeGroup(ageGroup):
    alreadyExists = [event for event in ageGroupAverageTill2014 if event[0] == ageGroup]

    if len(alreadyExists) > 0:
        ageGroupAverage = alreadyExists[0][1]
    else:
        ageGropuList = [event for event in allTheInfo if event[8] == str(ageGroup)]
        totalTime = 0
        itemCount = 0

        for person in ageGropuList:
            yearList = re.sub("[\[\] ]", "", person[1]).split(",")
            timeList = re.sub("[\[\] ]", "", person[3]).split(",")

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

def getAverageMarathonRuntime(playerId):
    averageRuntimeForRunner = 0
    totalTime = 0
    totalRaces = 0

    runnerInfo = [info for info in idSplitIntoRowsData if info[0] == playerId]

    for item in range(0, len(runnerInfo)):
        raceType = runnerInfo[item][3].upper().replace(" ", "")
        raceTime = runnerInfo[item][4]
        raceTimeSplit = raceTime.split(":")

        if ('MARATHON' in raceType and 'HALF' not in raceType and 'DEMI' not in raceType and not '00' in raceTimeSplit[0]):
            if not '-1' in  raceTimeSplit:
                raceTimeSeconds = (int(raceTimeSplit[0]) * 3600) + (int(raceTimeSplit[1]) * 60) + int(raceTimeSplit[2])
                totalTime = totalTime + raceTimeSeconds
                totalRaces = totalRaces + 1

    if not totalRaces == 0:
        averageRuntimeForRunner = (totalTime / totalRaces)
    return averageRuntimeForRunner


Y1TestSet_Extended = []
Y2TestSet_Extended = []

for count in range(0, 8711):
    runnerInfo = [info for info in Y1TestSet if int(info[0]) == count]
    runnerInfo2 = [info for info in Y2TestSet if int(info[0]) == count]

    if len(runnerInfo) == 1:
        Y1TestSet_Extended.append(runnerInfo[0])
        Y2TestSet_Extended.append(runnerInfo2[0])
        pass
    else:
        newY1Info = []
        newY2Info = []

        playerId = str(count)
        noOfMontrealMarathons = str(0)

        runnerInfo = [info for info in dataOfEveryone if int(info[0]) == count]
        noOfAllRaces = runnerInfo[0][7]
        category = runnerInfo[0][4]

        ageCategory = re.sub("[MF]", "", category)
        categoryThresholds = ageCategory.split("-")

        if '80' in ageCategory:
            ageCategory = int(ageCategory.replace("+", ""))
        else:
            ageCategory = (int(categoryThresholds[0]) + int(categoryThresholds[1])) / 2

        averageTimesInMarathon = getAverageMarathonRuntime(playerId)

        if averageTimesInMarathon == 0:
            averageTimesInMarathon = getMeanForAgeGroup(ageCategory)
            # print(averageTimesInMarathon)
        newY1Info.append(playerId)
        newY1Info.append(noOfMontrealMarathons)
        newY1Info.append(noOfAllRaces)
        newY1Info.append(str(ageCategory))

        newY2Info.append(playerId)
        newY2Info.append(averageTimesInMarathon)         #average
        newY2Info.append(noOfAllRaces)
        newY2Info.append(str(ageCategory))

        Y1TestSet_Extended.append(newY1Info)
        Y2TestSet_Extended.append(newY2Info)

# total = 0
# for item in Y1TestSet_Extended:
#     print(item)
#     total = total + 1
#
# print (total)

writeToCSV("FinalDataSets/DataSetOn23rd/Y1TestSet_Extended", Y1TestSet_Extended)
writeToCSV("FinalDataSets/DataSetOn23rd/Y2TestSet_Extended", Y2TestSet_Extended)


