import sys
import csv
import itertools

editedData = []
headerRecord = []
eventsOf2012 = []
eventsOf2013 = []
eventsOf2014 = []
eventsOf2015 = []
eventsOf2016 = []
allEvents = []
uniqueEventsWithTypes = []

firstRow = 1
def writeToCSV (csvFileName, dataList):
    csvFileNameWithExtension = csvFileName + '.csv'
    with open(csvFileNameWithExtension, 'w', newline='') as fp:
        csvWriter = csv.writer(fp, delimiter=',')
        csvWriter.writerows(dataList)

with open('Project1_data.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)


    # ====================================================================
    #     Skimming through the entries to vertically arrange every race
    # ====================================================================
    for runnerInfo in csvReader:
        if not firstRow == 1:
            rowLength = len(runnerInfo)                             # Get the length of the row to see how many columns it has

            if not ((rowLength - 1) % 5) == 0:
                print ("Following runner instance has missing features for atleast one event: ")
                print ("            %s.", runnerInfo)
                print ("It has %d number of columns: ", rowLength)
                sys.exit(0)

            runnerInstances = (rowLength - 1) // 5                   # Number of different races for this specific runner

            if (runnerInstances == 0):
                print ("Player with ID: %d has no data given for him", runnerInfo[0])
                sys.exit(0)

            if (runnerInstances > 1):
                for instance in range(0,runnerInstances):
                    instanceStartColumn = (instance * 5) + 1
                    instanceEndColumn = (instance * 5) + 5

                    runnerCurrentInstance = []
                    runnerCurrentInstance.append(runnerInfo[0])
                    runnerCurrentInstance.extend(runnerInfo[instanceStartColumn:instanceEndColumn + 1])

                    for item in range(0, len(runnerCurrentInstance)):
                        if not isinstance(runnerCurrentInstance[item], int):
                            runnerCurrentInstance[item] = runnerCurrentInstance[item].replace(" ", "")

                    runnerCurrentInstance[3] = runnerCurrentInstance[3].upper()
                    editedData.append(runnerCurrentInstance)
            else:
                editedData.append(runnerInfo)

        else:
            headerRecord = runnerInfo[0:6]
            editedData.append(headerRecord)
            firstRow = 0

# ====================================================================
#     Separate races by years in which they were run in
# ====================================================================
for eventInstance in editedData:
    eventDate = eventInstance[1]
    eventDateList = eventDate.split("-")

    if len(eventDateList) == 3:
        eventYear = eventDateList[0]
        eventMonth = eventDateList[1]
        eventDay = eventDateList[2]

        if eventYear == "2016":
            if len(eventsOf2016) > 0:
                previousEvent = eventsOf2016[-1]
                if previousEvent[0] != "PARTICIPANT ID" and previousEvent[0] != eventInstance[0]:
                    eventsOf2016.append([])

            eventsOf2016.append(eventInstance)

        if eventYear == "2015":
            if len(eventsOf2015) > 0:
                previousEvent = eventsOf2015[-1]
                if previousEvent[0] != "PARTICIPANT ID" and previousEvent[0] != eventInstance[0]:
                    eventsOf2015.append([])

            eventsOf2015.append(eventInstance)

        if eventYear == "2014":
            if len(eventsOf2014) > 0:
                previousEvent = eventsOf2014[-1]
                if previousEvent[0] != "PARTICIPANT ID" and previousEvent[0] != eventInstance[0]:
                    eventsOf2014.append([])

            eventsOf2014.append(eventInstance)

        if eventYear == "2013":
            if len(eventsOf2013) > 0:
                previousEvent = eventsOf2013[-1]
                if previousEvent[0] != "PARTICIPANT ID" and previousEvent[0] != eventInstance[0]:
                    eventsOf2013.append([])

            eventsOf2013.append(eventInstance)

        if eventYear == "2012":
            if len(eventsOf2012) > 0:
                previousEvent = eventsOf2012[-1]
                if previousEvent[0] != "PARTICIPANT ID" and previousEvent[0] != eventInstance[0]:
                    eventsOf2012.append([])

            eventsOf2012.append(eventInstance)

        newEvent = [eventInstance[1], eventInstance[2], eventInstance[3]]
        allEvents.append(newEvent)
    else:
        if eventDateList[0] != "EVENT DATE":
            print ("This Event has a different Address Format: ", eventInstance)
            sys.exit(0)

# ====================================================================
#     Get all the distinct events in the entire data-set
# ====================================================================
eventIDCount = 0
for event in allEvents:
    if not event in uniqueEventsWithTypes:
        uniqueEventsWithTypes.append(event)

del uniqueEventsWithTypes[0]
uniqueEventsWithTypes.sort(key=lambda elem: (elem[0], elem[1]))

allUniqueEventsAlone = []
distinctEventsWithDate = []

for eventWithType in uniqueEventsWithTypes:
    allUniqueEventsAlone.append([eventWithType[0], eventWithType[1]])

for event in allUniqueEventsAlone:
    event[0] = event[0].upper()
    event[0] = event[0].replace(" ", "")

    if not event in distinctEventsWithDate:
        distinctEventsWithDate.append(event)

distinctEventsWithDate.sort(key=lambda elem: (elem[0], elem[1]))

for count in range(0, len(distinctEventsWithDate)):
    distinctEventsWithDate[count][1] = distinctEventsWithDate[count][1].upper()

# ====================================================================
#     Get all the distinct events without the date information
# ====================================================================
distinctEventWithoutDate = []
for distinctEvent in distinctEventsWithDate:
    if [distinctEvent[1]] not in distinctEventWithoutDate:
        distinctEventWithoutDate.append([distinctEvent[1]])

distinctEventWithoutDate.sort()

# ====================================================================
#     Assign event Ids for each event
# ====================================================================
count = 0
eventListEventID = []
previousEvent = []
for distinctDateEventPair in distinctEventsWithDate:
    countLen = len(str(count))
    appendingZeroes = 5 - countLen

    if len(previousEvent) > 0 and (previousEvent[1] == 'MARATHON OASIS DE MONTREAL' or
                                           previousEvent[1] == "MARATHON OASIS ROCK 'N' ROLL DE MONTREAL"):
        eventId = previousEvent[2]
    else:
        eventId = distinctDateEventPair[0].replace("-", "") + str(str(0) * appendingZeroes) + str(count)
        count = count + 1

    newEvent_IDPair = []
    newEvent_IDPair.append(distinctDateEventPair[0])
    newEvent_IDPair.append(distinctDateEventPair[1])
    newEvent_IDPair.append(eventId)

    eventListEventID.append(newEvent_IDPair)
    previousEvent = newEvent_IDPair

# ====================================================================
#           Get the list of all race types available
# ====================================================================
allTypesOfTheRaces = []
for type in uniqueEventsWithTypes:
    if type[2].upper().replace(" ", "") not in allTypesOfTheRaces:
        allTypesOfTheRaces.append([type[2].upper().replace(" ", "")])

allTypesOfTheRaces.sort()

uniqueTypesOfTheRaces = []
for raceType in allTypesOfTheRaces:
    if raceType not in uniqueTypesOfTheRaces:
        uniqueTypesOfTheRaces.append(raceType)

# ====================================================================
#       Function to check if a given character is an int
# ====================================================================
def representsAnInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# ====================================================================
#       Sssign numerical values to different race-types
# ====================================================================
raceTypeInKiloMeters = []
for uniqueType in uniqueTypesOfTheRaces:
    newTypeWithKilometers = []
    newTypeWithKilometers.append(uniqueType[0])

    if '1/2' in uniqueType[0]:
        newTypeWithKilometers.append(20)
    else:
        splitRaceType = ["".join(x) for _, x in itertools.groupby(uniqueType[0], key=str.isdigit)]
        numberEntryOnly = []
        for entry in splitRaceType:
            if representsAnInt(entry):
                numberEntryOnly.append(int(entry))

        if len(numberEntryOnly) > 0:
            # print (numberEntryOnly)
            if numberEntryOnly[0] >= 35:
                newTypeWithKilometers.append(40)
            elif numberEntryOnly[0] >= 15:
                newTypeWithKilometers.append(20)
            elif numberEntryOnly[0] >= 7.5:
                newTypeWithKilometers.append(10)
            elif numberEntryOnly[0] >= 2.5:
                newTypeWithKilometers.append(5)
            else:
                newTypeWithKilometers.append(1)
        else:
            if ('MARATHON' in splitRaceType[0]) and (('HALF' in splitRaceType[0]) or ('DEMI' in splitRaceType[0])):
                newTypeWithKilometers.append(20)
            else:
                newTypeWithKilometers.append(40)
    raceTypeInKiloMeters.append(newTypeWithKilometers)

# ========================================================================
#       Fetch all the different types of runner categories in the data
# ========================================================================
allRaceCategories = []
itercars = iter(editedData)
next(itercars)

for instance in itercars:
    allRaceCategories.append([instance[5]])

allRaceCategories.sort()
uniqueRaceCategories = []

for category in allRaceCategories:
    if not category in uniqueRaceCategories:
        uniqueRaceCategories.append(category)

for category in uniqueRaceCategories:
    splitCategory = ["".join(x) for _, x in itertools.groupby(category[0], key=str.isdigit)]


# ========================================================================
#       Write all mined data into seperate files for later analysis
# ========================================================================
writeToCSV("ArrangedByID/editedDataByID", editedData)
writeToCSV("ArrangedByYear/editedDataFor2016", eventsOf2016)
writeToCSV("ArrangedByYear/editedDataFor2015", eventsOf2015)
writeToCSV("ArrangedByYear/editedDataFor2014", eventsOf2014)
writeToCSV("ArrangedByYear/editedDataFor2013", eventsOf2013)
writeToCSV("ArrangedByYear/editedDataFor2012", eventsOf2012)
writeToCSV("RaceTypes/uniqueEventsWithTypes", uniqueEventsWithTypes)
writeToCSV("RaceTypes/uniqueEventsOnlyWithDate", distinctEventsWithDate)
writeToCSV("RaceTypes/uniqueEventsOnly", distinctEventWithoutDate)
writeToCSV("RaceTypes/uniqueEventsWithID", eventListEventID)
writeToCSV("RaceTypes/typesOfRaces", uniqueTypesOfTheRaces)
writeToCSV("RaceTypes/typesOfRacesWithDistance", raceTypeInKiloMeters)
writeToCSV("RaceTypes/allCatergories", allRaceCategories)
writeToCSV("RaceTypes/uniqueCatergories", uniqueRaceCategories)


