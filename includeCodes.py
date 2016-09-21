import csv

montrealParticipants = []
raceTypes = []


def writeToCSV(csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)


with open('RaceTypes/typesOfRacesWithDistance.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for raceType in csvReader:
        raceTypes.append(raceType)

with open('MontrealMarathon/montrealMarathonWithCountPerParticipant.csv',
          newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        montrealParticipants.append(participant)

for player in range(0, len(montrealParticipants)):
    raceType = montrealParticipants[player][3].upper().replace(" ", "")

    raceEventDetail = [raceEvent for raceEvent in raceTypes if raceEvent[0] == raceType]
    montrealParticipants[player][3] = raceEventDetail[0][1]

montrealRacerCategories = []

for player in montrealParticipants:
    allSimilarCategories = [category for category in montrealRacerCategories if player[5] == category[0]]
    if len(allSimilarCategories) == 0:
        montrealRacerCategories.append([player[5]])

montrealRacerCategories.sort()

for player in range(0, len(montrealParticipants)):
    if montrealParticipants[player][5] == "F05" or montrealParticipants[player][5] == "F13+":
        montrealParticipants[player][5] = "F12-14"

    elif montrealParticipants[player][5] == "GARCONS 8" or montrealParticipants[player][5] == "M04" or \
                    montrealParticipants[player][5] == "M05" or montrealParticipants[player][5] == "M06" or \
                    montrealParticipants[player][5] == "M07" or montrealParticipants[player][5] == "M09" or \
                    montrealParticipants[player][5] == "M13+":
        montrealParticipants[player][5] = "M12-14"

    elif montrealParticipants[player][5] == "M---11":
        montrealParticipants[player][5] = "M60-64"

    elif montrealParticipants[player][5] == "M08":
        montrealParticipants[player][5] = "M35-39"

    elif montrealParticipants[player][5] == "M11-":
        montrealParticipants[player][5] = "M30-34"

    elif montrealParticipants[player][5] == "M70+":
        montrealParticipants[player][5] = "M70-79"

    elif montrealParticipants[player][5] == "NO AGE" or montrealParticipants[player][5] == "NOAGE":
        montrealParticipants[player][5] = "M45-49"

    elif montrealParticipants[player][5] == "U0-0":
        montrealParticipants[player][5] = "M40-44"

    elif montrealParticipants[player][5] == "F70+":
        montrealParticipants[player][5] = "F70-79"

# ['768', "['2015']", "MARATHONOASISROCK'N'ROLLDEMONTREAL", '40', "['-1']", '', '1', '-1', '1']

# F05, -        F12-14
# F13+, -       F12-14
# GARCONS 8, -  M12-14
# M---11, -     M60-64
# M04, -        M12-14
# M05, -        M12-14
# M06, -        M12-14
# M07, -        M12-14
# M08,  -       M35-39
# M09, -        M12-14
# M11-, -       M30-34
# M13+, -       M12-14
# M70+, -       M70-79
# NO AGE, -     M45-49
# NOAGE, -      M45-49
# U0-0, -       M40-44
# F70+ -        F70-79

# 0 - RunnerID
# 1 - Years he participated in MontrealMarathon
# 2 - EventName (MontrealMarathon)
# 3 - EventType (Distance)
# 4 - Times of Previous Years
# 5 - Category
# 6 - Number of times participated in Marathon
# 7 - Average Finishtime
# 8 - No of all Racing Events in the past 4 years


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


writeToCSV("MontrealMarathon/montrealMarathonFinalData", montrealParticipants)
writeToCSV("MontrealMarathon/montrealRacerCategories", montrealRacerCategories)
