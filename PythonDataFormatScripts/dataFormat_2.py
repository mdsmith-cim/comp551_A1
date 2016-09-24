import csv

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)


# ========================================================================
#     Function to get the average time given the times & distances run
# ========================================================================
def getAverageTime(listOfTimes, listOfDistances, count):
    allSecondsAdded = 0
    secondsItem = []

    for item in range(0, len(listOfTimes)):
        distanceRan = int(listOfDistances[item])
        distanceMultiple = 40 / distanceRan

        if not distanceMultiple == 1:
            distanceMultiple = distanceMultiple * 1.15

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

montrealMarathon = []
allRunnersGiven = []
montrealMarathonParticipants = []
raceTypes = []
previousID = -1

# ========================================================================
#     Function to get the race event type fiven its name
# ========================================================================
def getRaceType(raceEventName):
    raceType = raceEventName.upper().replace(" ", "")
    raceEventDetail = [raceEvent for raceEvent in raceTypes if raceEvent[0] == raceType]
    return raceEventDetail[0][1]

# ========================================================================
#     Load all race types information from previously created files
# ========================================================================
with open('RaceTypes/typesOfRacesWithDistance.csv', newline='') as marathonData:  # Reads the given csv
    print ("Loading types of different races with their distances......")
    csvReader = csv.reader(marathonData)
    for raceType in csvReader:
        raceTypes.append(raceType)

# ========================================================================
#  Extract only the Montreal Marathon related data from the formatted list
# ========================================================================
print("Loading all the information about all runners from dataset [editedDataByID.csv] and "
          "extracting only the MontrealMarathon events.....")
with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allRunnersGiven.append(participant)
        raceName = participant[2].upper().replace(" ", "")

        if ('MONTREAL' in raceName or 'MONTRÉAL' in raceName) and 'OASIS' in raceName:
            participant[2] = raceName
            montrealMarathon.append(participant)

# ========================================================================
#  Aggregate MontrealMarathon data of same runner over several years together
# ========================================================================
print("Formatting the loaded data on MontrealRunners to aggregate details about same runners over several years.....")
for entry in montrealMarathon:
    if entry[0] == previousID:
        montrealMarathonParticipants[-1][6] = int(montrealMarathonParticipants[-1][6]) + 1

        date = entry[1]
        year = date.split("-")[0]
        if not year in montrealMarathonParticipants[-1][1]:
            montrealMarathonParticipants[-1][1].extend([year])

            raceTypeInDistance = getRaceType(entry[3])
            montrealMarathonParticipants[-1][3].extend([raceTypeInDistance])
            montrealMarathonParticipants[-1][4].extend([entry[4]])
            noOfYears = len(montrealMarathonParticipants[-1][1])

            if '-1' in montrealMarathonParticipants[-1][4]:
                notFinishedTimes = montrealMarathonParticipants[-1][4].count('-1')
                noOfYears = noOfYears - notFinishedTimes

            if noOfYears > 0:
                previousRaceDistances = montrealMarathonParticipants[-1][3]
                previousRaceTimes = montrealMarathonParticipants[-1][4]
                averageTime = getAverageTime(previousRaceTimes, previousRaceDistances, noOfYears)
                montrealMarathonParticipants[-1][7] = averageTime
    else:
        newEntry = []
        newEntry.extend(entry)
        newEntry.extend("1")            # Count of how mant Marathons
        raceTypeInDistance = getRaceType(entry[3])
        if not entry[4] == '-1':
            newEntry.extend([entry[4]])            # Average Time
        else:
            newEntry.extend(['-1'])

        date = newEntry[1]
        year = date.split("-")[0]
        newEntry[1] = [year]
        newEntry[3] = [raceTypeInDistance]
        newEntry[4] = [newEntry[4]]

        montrealMarathonParticipants.append(newEntry)
    previousID = entry[0]

# ================================================================================
#  Totalling all previous races (including the ones other than MontrealMarathon)
#           for each specif runner.....
# ================================================================================
print("Adding total count of all previous races (including the ones other than MontrealMarathon) to the dataset....")
for entry in range (0, len(montrealMarathonParticipants)):
    runnerId = montrealMarathonParticipants[entry][0]
    totalCountOfRaces = [raceEvent for raceEvent in allRunnersGiven if raceEvent[0] == runnerId]
    montrealMarathonParticipants[entry].append(len(totalCountOfRaces))

# =================================================================================
#  Delete the common column "EventName" for all entries which is MontrealMarathon
# =================================================================================
print("Deleting the common column for all entries which is event-name equalling to Montreal Marathon....")
for entry in montrealMarathonParticipants:
    del entry[2]
    print(entry)

# ========================================================================
#       Write all mined data into seperate files for later analysis
# ========================================================================
writeToCSV("MontrealMarathon/montrealMarathon", montrealMarathon)
writeToCSV("MontrealMarathon/montrealMarathonWithCountPerParticipant", montrealMarathonParticipants)
writeToCSV("MontrealMarathon/NoTimeMultiplication/montrealMarathonWithCountPerParticipant_NoMul", montrealMarathonParticipants)
