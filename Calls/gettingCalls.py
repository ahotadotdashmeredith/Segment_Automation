def formattingGaCalls(gaCalls):
    # dict that will contain all events captured from network calls in event type format
    allCalls = {}
    pageDone = False
    for i in gaCalls:
        try:
            if (i['t'] == ['pageview'] and pageDone==False):
                allCalls['pageview'] = i
                pageDone = True
            elif(i['t']==['event']):
                allCalls[i['ec'][0]] = i
        except:
            pass
    return allCalls


def gettingEventCalls(gaCalls, inputData):
    allCalls = formattingGaCalls(gaCalls)

    # dict containing all events that we want to validate i.e. user entered in input file, in the same event type format
    eventCalls = {}
    #for each event in input
    for inputParameter, inputParameterPropertiesObj in inputData.items():
        # Code for checking if desired event was captured or not
        try:
            print(inputParameter)
            print(allCalls[inputParameter])
        # If the desired event was not captured
        except:
             allCalls[inputParameter] = {}

        #this object will store the value of each property for the input parameter
        tempObj = {}
        #Looping through all the properties of a input parameter
        for property, propertyConditionsObj in inputParameterPropertiesObj.items():
            #If property was not found
            try:
                tempObj[property] = allCalls[inputParameter][property]
            except:
                tempObj[property] = ['NA']
        #Storing the value in eventCall dict
        eventCalls[inputParameter] = tempObj

    return eventCalls




