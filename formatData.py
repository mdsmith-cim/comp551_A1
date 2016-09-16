import sys
import csv
import re

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

    for runnerInfo in csvReader:
        if not firstRow == 1:
            #print(runnerInfo)
            rowLength = len(runnerInfo)                             # Get the length of the row to see how many columns it has

            if not ((rowLength - 1) % 5) == 0:
                print ("Following runner instance has missing features for atleast one event: ")
                print ("            %s.", runnerInfo)
                print ("It has %d number of columns: ", rowLength)
                sys.exit(0)

            runnerInstances = (rowLength - 1) // 5                   # Number of different races for this specific runner
            #print(runnerInstances)

            if (runnerInstances == 0):
                print ("Player with ID: %d has no data given for him", runnerInfo[0])
                sys.exit(0)

            if (runnerInstances > 1):
                #print(runnerInstances)
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
                    # print (runnerCurrentInstance)
            else:
                editedData.append(runnerInfo)

        else:
            headerRecord = runnerInfo[0:6]
            editedData.append(headerRecord)
            firstRow = 0

    # Print All the Data
    # for runnerInfo in editedData:
    #     print(runnerInfo)

    #print (len(editedData))

for eventInstance in editedData:
    eventDate = eventInstance[1]
    eventDateList = eventDate.split("-")

    if len(eventDateList) == 3:
        eventYear = eventDateList[0]
        eventMonth = eventDateList[1]
        eventDay = eventDateList[2]
        eventInstance[1] = eventMonth + "-" + eventDay

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

        newEvent = [eventInstance[2], eventInstance[3]]
        allEvents.append(newEvent)
    else:
        # print (eventDateList[0])
        if eventDateList[0] != "EVENT DATE":
            print ("This Event has a different Address Format: ", eventInstance)
            sys.exit(0)

for event in allEvents:
    if not event in uniqueEventsWithTypes:
        uniqueEventsWithTypes.append(event)

del uniqueEventsWithTypes[0]
uniqueEventsWithTypes.sort()

allUniqueEventsAlone = []
distinctEventsAlone = []

for eventWithType in uniqueEventsWithTypes:
    allUniqueEventsAlone.append([eventWithType[0]])

for event in allUniqueEventsAlone:
    event[0] = event[0].upper()
    event[0] = event[0].replace(" ", "")

    if not event in distinctEventsAlone:
        distinctEventsAlone.append(event)
        # print(event)


writeToCSV("ArrangedByID/editedDataByID", editedData)
writeToCSV("ArrangedByYear/editedDataFor2016", eventsOf2016)
writeToCSV("ArrangedByYear/editedDataFor2015", eventsOf2015)
writeToCSV("ArrangedByYear/editedDataFor2014", eventsOf2014)
writeToCSV("ArrangedByYear/editedDataFor2013", eventsOf2013)
writeToCSV("ArrangedByYear/editedDataFor2012", eventsOf2012)
writeToCSV("uniqueEventsWithTypes", uniqueEventsWithTypes)
writeToCSV("uniqueEventsOnly", distinctEventsAlone)


