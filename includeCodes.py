import csv

montrealParticipants = []
raceTypes = []

def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

with open('RaceTypes/typesOfRacesWithDistance.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)
    for raceType in csvReader:
        raceTypes.append(raceType)

with open('MontrealMarathon/montrealMarathonWithCountPerParticipant.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        montrealParticipants.append(participant)

for player in range (0, len(montrealParticipants)):
    raceType = montrealParticipants[player][3].upper().replace(" ", "")

    raceEventDetail = [raceEvent for raceEvent in raceTypes if raceEvent[0] == raceType]
    montrealParticipants[player][3] = raceEventDetail[0][1]

# for player in montrealParticipants:
#     print(player)


writeToCSV("MontrealMarathon/montrealMarathonFinalData", montrealParticipants)



