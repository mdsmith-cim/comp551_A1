import sys
import csv

montrealMarathon = []
allRunnersGiven = []

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

def find_listcomp(allTheData, findItem):
    return [runner for runner in allTheData if runner[0] == findItem]

def getAverageTime(listOfTimes, count):
    totalHours = 0
    totalMinutes = 0
    totalSeconds = 0

    for time in listOfTimes:
        if not '-1' in time:
            dataSplit = time.split(":")
            hours = int(dataSplit[0])
            minutes = int(dataSplit[1])
            seconds = int(dataSplit[2])

            totalHours = totalHours + hours
            totalMinutes = totalMinutes + minutes
            totalSeconds = totalSeconds + seconds

            if totalSeconds > 60:
                additionalMinutes = int(totalSeconds / 60)
                totalSeconds = totalSeconds % 60
                totalMinutes = totalMinutes + additionalMinutes

            if totalMinutes > 60:
                additionalHours = int(totalMinutes / 60)
                totalMinutes = totalMinutes % 60
                totalHours = totalHours + additionalHours

    allInSeconds = (totalHours * 60 * 60) + (totalMinutes * 60) + totalSeconds
    averageSeconds = allInSeconds / count

    avgHours = int(averageSeconds / (60 * 60))
    averageSeconds = averageSeconds % (60 * 60)
    avgMinutes = int(averageSeconds / 60)
    avgSeconds = averageSeconds % 60

    averageTime = str(avgHours) + ":" + str(avgMinutes) + ":" + str(int(avgSeconds))
    return averageTime

with open('ArrangedByID/editedDataByID.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        allRunnersGiven.append(participant)
        raceName = participant[2].upper().replace(" ", "")

        if ('MONTREAL' in raceName or 'MONTRÉAL' in raceName) and 'OASIS' in raceName:
            participant[2] = raceName
            montrealMarathon.append(participant)
            # print (participant)

montrealMarathonParticipants = []
previousID = -1

for entry in montrealMarathon:
    if entry[0] == previousID:
        montrealMarathonParticipants[-1][6] = int(montrealMarathonParticipants[-1][6]) + 1

        date = entry[1]
        year = date.split("-")[0]
        if not year in montrealMarathonParticipants[-1][1]:
            montrealMarathonParticipants[-1][1].extend([year])
            montrealMarathonParticipants[-1][4].extend([entry[4]])
            noOfYears = len(montrealMarathonParticipants[-1][1])
            averageTime = getAverageTime(montrealMarathonParticipants[-1][4], noOfYears)
            montrealMarathonParticipants[-1][7] = averageTime
    else:
        newEntry = []
        newEntry.extend(entry)
        newEntry.extend("1")            # Count of how mant Marathons
        newEntry.extend([entry[4]])            # Average Time

        date = newEntry[1]
        year = date.split("-")[0]
        newEntry[1] = [year]
        newEntry[4] = [newEntry[4]]

        montrealMarathonParticipants.append(newEntry)
    previousID = entry[0]

for entry in range (0, len(montrealMarathonParticipants)):
    # totalCountOfRaces = 0
    runnerId = montrealMarathonParticipants[entry][0]
    totalCountOfRaces = [raceEvent for raceEvent in allRunnersGiven if raceEvent[0] == runnerId]
    # print (runnerId + ":" + str(len(totalCountOfRaces)))

    # for item in range(0, len(allRunnersGiven)):
    #     if allRunnersGiven[item][0] == runnerId:
    #         totalCountOfRaces = totalCountOfRaces + 1
    #
    montrealMarathonParticipants[entry].append(len(totalCountOfRaces))
    print(montrealMarathonParticipants[entry])


writeToCSV("MontrealMarathon/montrealMarathon", montrealMarathon)
writeToCSV("MontrealMarathon/montrealMarathonWithCountPerParticipant", montrealMarathonParticipants)





# with open('RaceTypes/uniqueEventsWithID.csv', newline='') as marathonData:     # Reads the given csv
#     csvReader = csv.reader(marathonData)
#
#     for event in csvReader:
#         eventName = event[1].upper().replace(" ", "")
#
#         if 'MONTREAL' in eventName and 'OASIS' in eventName:
#             print (eventName)
