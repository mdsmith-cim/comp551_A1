import csv

with open('uniqueEventsOnlyWithDate.csv', newline='') as marathonData:     # Reads the given csv
    csvReader = csv.reader(marathonData)
    distinctEventsWithDate = csvReader

    previousEvent = None
    for event in distinctEventsWithDate:
        # print (event)
        if not previousEvent == None:
            if event[0] == previousEvent[0] and event[1][:6] in previousEvent[1][:6]:
                print (previousEvent)
                print (event)
                print ("====================")

            previousEvent = event
        else:
            previousEvent = event

# ['2013-09-22', 'MARATHON OASIS DE MONTREAL']
# ['2013-09-22', 'MARATHONOASISDEMONTREAL']


# ['2015-09-20', "MARATHON OASIS ROCK 'N' ROLL DE MONTREAL"]
# ['2015-09-20', "MARATHONOASISROCK'N'ROLLDEMONTREAL"]