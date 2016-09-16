import sys
import csv
import xlwt

editedData = []
headerRecord = []
eventsOf2012 = []
eventsOf2013 = []
eventsOf2014 = []
eventsOf2015 = []
eventsOf2016 = []
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
    eventYear = eventDateList[0]

    if eventYear == "2016":
        eventsOf2016.append(eventInstance)

    if eventYear == "2015":
        eventsOf2015.append(eventInstance)

    if eventYear == "2014":
        eventsOf2014.append(eventInstance)

    if eventYear == "2013":
        eventsOf2013.append(eventInstance)

    if eventYear == "2012":
        eventsOf2012.append(eventInstance)

writeToCSV("editedDataByID", editedData)
writeToCSV("editedDataFor2016", eventsOf2016)
writeToCSV("editedDataFor2015", eventsOf2015)
writeToCSV("editedDataFor2014", eventsOf2014)
writeToCSV("editedDataFor2013", eventsOf2013)
writeToCSV("editedDataFor2012", eventsOf2012)