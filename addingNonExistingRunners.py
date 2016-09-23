import csv

idSplitIntoRowsData = []
allTheInfo = []
nonExistantPlayers = []

Y1TrainingSet = []
Y1TestSet = []
Y2TrainingSet = []
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

with open('FinalDataSets/DataSetOn23rd/Y1TrainSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y1TrainingSet.append(participant)

with open('FinalDataSets/DataSetOn23rd/Y1TestSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y1TestSet.append(participant)

with open('FinalDataSets/DataSetOn23rd/Y2TrainingSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y2TrainingSet.append(participant)

with open('FinalDataSets/DataSetOn23rd/Y2TestSet.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        Y2TestSet.append(participant)

with open('FinalDataSets/IdsNotListed.csv', newline='') as marathonData:  # Reads the given csv
    csvReader = csv.reader(marathonData)
    for participant in csvReader:
        nonExistantPlayers.append(participant)



# writeToCSV("FinalDataSets/DataSetOn23rd/Y1TestSet_Extended", Y1TestSet_Extended)
# writeToCSV("FinalDataSets/DataSetOn23rd/Y2TestSet_Extended", Y2TestSet_Extended)


