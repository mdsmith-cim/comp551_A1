import csv
import re

allRunnersEver = []
runningData2016 = []
runningData2015 = []
runningData2014 = []
runningData2013 = []
runningData2012 = []
montrealMarathonData = []

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allRunnersEver.append(participant)

with open('MontrealMarathon/montrealMarathonFinalData.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        montrealMarathonData.append(participant)

with open('ArrangedByYear/editedDataFor2016.csv',newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        if len(participant) == 0:
            pass
        else:
            runningData2016.append(participant)

with open('ArrangedByYear/editedDataFor2015.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        if len(participant) == 0:
            pass
        else:
            runningData2015.append(participant)

with open('ArrangedByYear/editedDataFor2014.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        if len(participant) == 0:
            pass
        else:
            runningData2014.append(participant)

with open('ArrangedByYear/editedDataFor2013.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        if len(participant) == 0:
            pass
        else:
            runningData2013.append(participant)

with open('ArrangedByYear/editedDataFor2012.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        if len(participant) == 0:
            pass
        else:
            runningData2012.append(participant)

def convertTimeToSeconds(time):
    if not '-1' in time:
        dataSplit = time.split(":")
        hours = int(dataSplit[0])
        minutes = int(dataSplit[1])
        seconds = int(dataSplit[2])
        convertedToSeconds = ((hours * 60 * 60) + (minutes * 60) + (seconds))
        return convertedToSeconds
    else:
        return -1

def getMarathonersInYear(allRacesList):
    marathonersInYear = []
    for participant in range(0, len(allRacesList)):
        allRacesList[participant][2] = allRacesList[participant][2].upper().replace(" ", "")
        if ('MARATHON' in allRacesList[participant][3] and
                    'HALF' not in allRacesList[participant][3] and 'DEMI' not in allRacesList[participant][3])\
                and 'MONTREAL' not in allRacesList[participant][2] \
                     and 'MONTRÉAL' not in allRacesList[participant][2] and 'OASIS' not in allRacesList[participant][2]:
            allRacesList[participant][3] = allRacesList[participant][3].upper()
            allRacesList[participant][4] = convertTimeToSeconds(allRacesList[participant][4])
            marathonersInYear.append(allRacesList[participant])
    return marathonersInYear

print("Fetching external marathon details every year per participant......")
marathonsOnlyIn2016 = getMarathonersInYear(runningData2016)
marathonsOnlyIn2015 = getMarathonersInYear(runningData2015)
marathonsOnlyIn2014 = getMarathonersInYear(runningData2014)
marathonsOnlyIn2013 = getMarathonersInYear(runningData2013)
marathonsOnlyIn2012 = getMarathonersInYear(runningData2012)

print("Writing external marathon details per year per participant......")
writeToCSV("ArrangedByYear/otherMarathonsOnlyIn2016", marathonsOnlyIn2016)
writeToCSV("ArrangedByYear/otherMarathonsOnlyIn2015", marathonsOnlyIn2015)
writeToCSV("ArrangedByYear/otherMarathonsOnlyIn2014", marathonsOnlyIn2014)
writeToCSV("ArrangedByYear/otherMarathonsOnlyIn2013", marathonsOnlyIn2013)
writeToCSV("ArrangedByYear/otherMarathonsOnlyIn2012", marathonsOnlyIn2012)


def getAverageMarathonRuntime(runner):
    playerId = runner[0]
    montrealMarathonYears = runner[1]
    montrealMarathonRuntimes = runner[3]

    raceTimesIn2012 = []
    raceTimesIn2013 = []
    raceTimesIn2014 = []
    raceTimesIn2015 = []
    raceTimesIn2016 = []

    timeAverage2012 = 0
    timeAverage2013 = 0
    timeAverage2014 = 0
    timeAverage2015 = 0
    timeAverage2016 = 0

    racesIn2016 = [event for event in marathonsOnlyIn2016 if playerId == int(event[0])]
    racesIn2015 = [event for event in marathonsOnlyIn2015 if playerId == int(event[0])]
    racesIn2014 = [event for event in marathonsOnlyIn2014 if playerId == int(event[0])]
    racesIn2013 = [event for event in marathonsOnlyIn2013 if playerId == int(event[0])]
    racesIn2012 = [event for event in marathonsOnlyIn2012 if playerId == int(event[0])]

    if len(racesIn2016) > 0:
        for race in racesIn2016:
            raceTimesIn2016.append(race[4])

    if len(racesIn2015) > 0:
        for race in racesIn2015:
            raceTimesIn2015.append(race[4])

    if len(racesIn2014) > 0:
        for race in racesIn2014:
            raceTimesIn2014.append(race[4])

    if len(racesIn2013) > 0:
        for race in racesIn2013:
            raceTimesIn2013.append(race[4])

    if len(racesIn2012) > 0:
        for race in racesIn2012:
            raceTimesIn2012.append(race[4])

# ===========================================================

    totalTime2012 = 0
    totalCount2012 = len(raceTimesIn2012)

    if totalCount2012 > 0:
        for time in raceTimesIn2012:
            if time == -1:
                totalCount2012 = totalCount2012 - 1
            else:
                totalTime2012 = totalTime2012 + time

    if 2012 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2012)
        totalTime2012 = totalTime2012 + montrealMarathonRuntimes[indexOfTime]
        totalCount2012 = totalCount2012 + 1

    if not totalCount2012 == 0:
        timeAverage2012 = totalTime2012 / totalCount2012

# ===========================================================

    totalTime2013 = 0
    totalCount2013 = len(raceTimesIn2013)

    if totalCount2013 > 0:
        for time in raceTimesIn2013:
            if time == -1:
                totalCount2013 = totalCount2013 - 1
            else:
                totalTime2013 = totalTime2013 + time

    if 2013 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2013)
        totalTime2013 = totalTime2013 + montrealMarathonRuntimes[indexOfTime]
        totalCount2013 = totalCount2013 + 1

    if not (totalCount2013 + totalCount2013) == 0:
        timeAverage2013 = (totalTime2012 + totalTime2013) / (totalCount2012 + totalCount2013)

# ===========================================================

    totalTime2014 = 0
    totalCount2014 = len(raceTimesIn2014)

    if totalCount2014 > 0:
        for time in raceTimesIn2014:
            if time == -1:
                totalCount2014 = totalCount2014 - 1
            else:
                totalTime2014 = totalTime2014 + time

    if 2014 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2014)
        totalTime2014 = totalTime2014 + montrealMarathonRuntimes[indexOfTime]
        totalCount2014 = totalCount2014 + 1

    if not (totalCount2012 + totalCount2013 + totalCount2014) == 0:
        timeAverage2014 = (totalTime2012 + totalTime2013 + totalTime2014) / (totalCount2012 + totalCount2013 + totalCount2014)

# ===========================================================

    totalTime2015 = 0
    totalCount2015 = len(raceTimesIn2015)

    if totalCount2015 > 0:
        for time in raceTimesIn2015:
            if time == -1:
                totalCount2015 = totalCount2015 - 1
            else:
                totalTime2015 = totalTime2015 + time

    if 2015 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2015)
        totalTime2015 = totalTime2015 + montrealMarathonRuntimes[indexOfTime]
        totalCount2015 = totalCount2015 + 1

    if not (totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015) == 0:
        timeAverage2015 = (totalTime2012 + totalTime2013 + totalTime2014 + totalTime2015) / (totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015)

# ===========================================================

    totalTime2016 = 0
    totalCount2016 = len(raceTimesIn2016)

    if totalCount2016 > 0:
        for time in raceTimesIn2016:
            if time == -1:
                totalCount2016 = totalCount2016 - 1
            else:
                totalTime2016 = totalTime2016 + time

    if not (totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015 + totalCount2016) == 0:
        timeAverage2016 = (totalTime2012 + totalTime2013 + totalTime2014 + totalTime2015 + totalTime2016) / (totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015 + totalCount2016)

# ===========================================================
    montreal_2012_time = 0
    montreal_2013_time = 0
    montreal_2014_time = 0
    montreal_2015_time = 0
    montreal_2016_time = 0

    raceCount_2012 = totalCount2012
    raceCount_2013 = totalCount2013
    raceCount_2014 = totalCount2014
    raceCount_2015 = totalCount2015
    raceCount_2016 = totalCount2016

    time_2012 = 0
    time_2013 = 0
    time_2014 = 0
    time_2015 = 0
    time_2016 = 0

    if 2012 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2012)
        montreal_2012_time = montrealMarathonRuntimes[indexOfTime]
        raceCount_2012 = totalCount2012 - 1

    if not (raceCount_2012 + totalCount2013 + totalCount2014 + totalCount2015 + totalCount2016) == 0:
        time_2012 = (
                        (totalTime2012 - montreal_2012_time) + totalTime2013 + totalTime2014 + totalTime2015 + totalTime2016) / (
                        raceCount_2012 + totalCount2013 + totalCount2014 + totalCount2015 + totalCount2016
                    )

    if 2013 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2013)
        montreal_2013_time = montrealMarathonRuntimes[indexOfTime]
        raceCount_2013 = totalCount2013 - 1

    if not (totalCount2012 + raceCount_2013 + totalCount2014 + totalCount2015 + totalCount2016) == 0:
        time_2013 = (
                        totalTime2012 + (totalTime2013 - montreal_2013_time) + totalTime2014 + totalTime2015 + totalTime2016) / (
                        totalCount2012 + raceCount_2013 + totalCount2014 + totalCount2015 + totalCount2016
                    )

    if 2014 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2014)
        montreal_2014_time = montrealMarathonRuntimes[indexOfTime]
        raceCount_2014 = totalCount2014 - 1

    if not (totalCount2012 + totalCount2013 + raceCount_2014 + totalCount2015 + totalCount2016) == 0:
        time_2014 = (
                        totalTime2012 + totalTime2013 + (totalTime2014 - montreal_2014_time) + totalTime2015 + totalTime2016) / (
                        totalCount2012 + totalCount2013 + raceCount_2014 + totalCount2015 + totalCount2016
                    )

    if 2015 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2015)
        montreal_2015_time = montrealMarathonRuntimes[indexOfTime]
        raceCount_2015 = totalCount2015 - 1

    if not (totalCount2012 + totalCount2013 + totalCount2014 + raceCount_2015 + totalCount2016) == 0:
        time_2015 = (
                        totalTime2012 + totalTime2013 + totalTime2014 + (totalTime2015 - montreal_2015_time) + totalTime2016) / (
                        totalCount2012 + totalCount2013 + totalCount2014 + raceCount_2015 + totalCount2016
                    )

    if 2016 in montrealMarathonYears:
        indexOfTime = montrealMarathonYears.index(2016)
        montreal_2016_time = montrealMarathonRuntimes[indexOfTime]
        raceCount_2016 = totalCount2016 - 1

    if not (totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015 + raceCount_2016) == 0:
        time_2016 = (
                        totalTime2012  + totalTime2013 + totalTime2014 + totalTime2015 + (totalTime2016 - montreal_2016_time)) / (
                        totalCount2012 + totalCount2013 + totalCount2014 + totalCount2015 + raceCount_2016
                    )

    yearTimeList = []
    yearTimeList.append(int(time_2012))
    yearTimeList.append(int(time_2013))
    yearTimeList.append(int(time_2014))
    yearTimeList.append(int(time_2015))
    yearTimeList.append(int(time_2016))

    timeAverageList = []
    timeAverageList.append(int(timeAverage2014))
    timeAverageList.append(int(timeAverage2015))
    timeAverageList.append(int(timeAverage2016))
    timeAverageList.append(yearTimeList)

    # if playerId == 8708:
    # # print(playerId)
    #     print(montrealMarathonYears)
    #     print(montrealMarathonRuntimes)
    #     print(raceTimesIn2012)
    #     print(raceTimesIn2013)
    #     print(raceTimesIn2014)
    #     print(raceTimesIn2015)
    #     print(raceTimesIn2016)
    #     print(timeAverageList)
    #     print("==================================")
    # print("+ " + str(playerId))
    return timeAverageList
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getListOfRaceCountsPerYear(runner):
    playerId = runner[0]

    runsIn2016 = 0
    runsIn2015 = 0
    runsIn2014 = 0
    runsIn2013 = 0
    runsIn2012 = 0

    allRunsByPlayer = [run for run in allRunnersEver if int(run[0]) == playerId]

    for run in allRunsByPlayer:
        runYear = run[1].split("-")[0]

        if runYear == "2016":
            runsIn2016 = runsIn2016 + 1
        elif runYear == "2015":
            runsIn2015 = runsIn2015 + 1
        elif runYear == "2014":
            runsIn2014 = runsIn2014 + 1
        elif runYear == "2013":
            runsIn2013 = runsIn2013 + 1
        elif runYear == "2012":
            runsIn2012 = runsIn2012 + 1

    # runsIn2016 = [run for run in allRunnersEver if (int(run[0]) == playerId and run[1].split("-")[0] == "2016")]
    # runsIn2015 = [run for run in allRunnersEver if (int(run[0]) == playerId and run[1].split("-")[0] == "2015")]
    # runsIn2014 = [run for run in allRunnersEver if (int(run[0]) == playerId and run[1].split("-")[0] == "2014")]
    # runsIn2013 = [run for run in allRunnersEver if (int(run[0]) == playerId and run[1].split("-")[0] == "2013")]
    # runsIn2012 = [run for run in allRunnersEver if (int(run[0]) == playerId and run[1].split("-")[0] == "2012")]

    previousRunCounts = []
    previousRunCounts.append(runsIn2016)
    previousRunCounts.append(runsIn2015)
    previousRunCounts.append(runsIn2014)
    previousRunCounts.append(runsIn2013)
    previousRunCounts.append(runsIn2012)
    print("* " + str(playerId))
    return previousRunCounts


print("Aggregating all required details into one list.......")
formattedMontrealRaceWithAllInfo = []
for index in range(0, len(montrealMarathonData)):
    deleteEntry = False
    newDistanceList = []
    newYearList = []
    newTimeList = []

    currentEntry = montrealMarathonData[index]
    yearList = re.sub("[\[\]' ]", "", currentEntry[1]).split(",")
    distanceList = re.sub("[\[\]' ]", "", currentEntry[2]).split(",")
    timeList = re.sub("[\[\]' ]", "", currentEntry[3]).split(",")
    ageCategory = currentEntry[4]
    noOfAllRaces = currentEntry[7]

    for item in range(0, len(distanceList)):
        if distanceList[item] == '40':
            newDistanceList.append(int(distanceList[item]))
            newYearList.append(int(yearList[item]))
            # newTimeList.append(timeList[item])
            newTimeList.append(convertTimeToSeconds(timeList[item]))

    if len(newDistanceList) > 0:
        newFullEntry = []
        newFullEntry.append(int(currentEntry[0]))
        newFullEntry.append(newYearList)
        newFullEntry.append(newDistanceList)
        newFullEntry.append(newTimeList)
        newFullEntry.append(len(newTimeList))
        newFullEntry.append(int(noOfAllRaces))

        ageCategory = re.sub("[MF]", "", ageCategory)
        categoryThresholds = ageCategory.split("-")

        if '80' in ageCategory:
            ageCategory = int(ageCategory.replace("+",""))
        elif currentEntry[0] == '768':
            pass
        else:
            ageCategory = (int(categoryThresholds[0]) + int(categoryThresholds[1])) / 2

        averageMarathonFinishTimes = getAverageMarathonRuntime(newFullEntry)
        noOfRacesPerYearList = getListOfRaceCountsPerYear(newFullEntry)

        newFullEntry.append(averageMarathonFinishTimes)
        newFullEntry.append(noOfRacesPerYearList)
        newFullEntry.append(ageCategory)
        formattedMontrealRaceWithAllInfo.append(newFullEntry)

#
for item in formattedMontrealRaceWithAllInfo:
    print (item)

writeToCSV("ArrangedByID/FormattedAllInfo", formattedMontrealRaceWithAllInfo)




