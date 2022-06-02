def formattingGaCalls(gaCalls):
    # dict that will contain all events captured from network calls in event-list type format
    fmGaCalls = {'pageview': []}
    for i in gaCalls:
        try:
            if (i['t'] == ['event']):
                fmGaCalls[i['ec'][0]] = []
        except:
            pass
    return fmGaCalls


def adddingGaCalls(gaCalls):
    fmGaCalls = formattingGaCalls(gaCalls)
    pageDone = False
    for i in gaCalls:
        try:
            if (i['t'] == ['pageview'] and pageDone is False):
                fmGaCalls.get('pageview').append(i)
                pageDone = True
            elif (i['t'] == ['event']):
                fmGaCalls.get(i['ec'][0]).append(i)
        except:
            pass
    return fmGaCalls


def takingImportantProperties(organizedNetworkCalls, inputEvent, inputEventPropertiesObj):
    # this list will be the value to each event in eventCalls dict
    tempEventList = []
    # Looping through all the properties of an input parameter
    for i in organizedNetworkCalls[inputEvent]:
        # this object will store the value of necessary properties only for each input event
        tempPropertiesObj = {}
        for property in inputEventPropertiesObj:
            try:
                tempPropertiesObj[property] = i[property]
            except:
                tempPropertiesObj[property] = ['NA']
        # In the end, this will contain objects with necessary properties only
        tempEventList.append(tempPropertiesObj)
    return tempEventList


def gettingEventCalls(gaCalls, inputData):
    organizedNetworkCalls = adddingGaCalls(gaCalls)
    # dict containing all events that we want to validate i.e. user entered in input file, in the same event type format
    eventCalls = {}
    # for each event in input
    for inputEvent, inputEventPropertiesObj in inputData.items():
        # Code for checking if desired event was captured or not
        try:
            for i in organizedNetworkCalls[inputEvent]:
                pass
        # If the desired event was not captured
        except:
            organizedNetworkCalls[inputEvent] = []
        # Storing the list in eventCall dict
        eventCalls[inputEvent] = takingImportantProperties(organizedNetworkCalls, inputEvent, inputEventPropertiesObj)
    return eventCalls
