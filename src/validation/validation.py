from src.validation_functions.validateFunctions import dataFormatValidation, dataTypeValidation, dataValueValidation


def creatingEventObjForEmptyList(i, inputData):
    properties = inputData[i].keys()
    tempEventObj = {}
    for k in properties:
        requirement = inputData[i][k]['requirement']
        problemType = inputData[i][k]['problemType']
        capturedValue = 'NA'
        expectedValue = inputData[i][k]['expectedValue']

        tempPropertyObj = creatingPropertyObj(requirement, problemType, capturedValue, expectedValue)
        tempEventObj[k] = tempPropertyObj
    return tempEventObj


def creatingPropertyObj(requirement, problemType, capturedValue, expectedValue):
    tempPropertyObj = {}
    errorValue = 'No Error/'
    typeError = ''
    # If property was needed but not captured
    if (requirement == 'R' and capturedValue == 'NA'):
        errorValue, typeError = 'Error', 'Value Not Found'
    # If we have to check data type
    elif (problemType == 'Data Type'):
        errorValue, typeError = dataTypeValidation(capturedValue, expectedValue)
    # or else we have to check data value
    elif (problemType == 'Data Value'):
        errorValue, typeError = dataValueValidation(capturedValue, expectedValue)
    # or else we have to check data format
    elif (problemType == 'Data Format'):
        errorValue, typeError = dataFormatValidation(capturedValue, expectedValue)
    tempPropertyObj['errorCheck'] = errorValue + '/' + typeError
    tempPropertyObj['capturedValue'] = capturedValue
    tempPropertyObj['expectedValue'] = expectedValue
    return tempPropertyObj


def creatingEventObj(i, j, inputData):
    properties = inputData[i].keys()
    tempEventObj = {}
    for k in properties:
        requirement = inputData[i][k]['requirement']
        problemType = inputData[i][k]['problemType']
        capturedValue = j[k][0]
        expectedValue = inputData[i][k]['expectedValue']

        tempPropertyObj = creatingPropertyObj(requirement, problemType, capturedValue, expectedValue)
        tempEventObj[k] = tempPropertyObj
    return tempEventObj


def validation(eventCall, inputData):
    # final object that will be written into the Excel sheet
    eventObj = {}
    # For each event in eventCall that user specified
    for i in eventCall:
        tempEventList = []
        if (len(eventCall[i]) == 0):
            tempEventObj = creatingEventObjForEmptyList(i, inputData)
            tempEventList.append(tempEventObj)
        else:
            for j in eventCall[i]:
                tempEventObj = creatingEventObj(i, j, inputData)
                tempEventList.append(tempEventObj)
        eventObj[i] = tempEventList
    return eventObj
