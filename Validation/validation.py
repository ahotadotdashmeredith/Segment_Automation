import sys
from Input.input import inputData

sys.path.insert(1, 'C:\\Users\\ahota\\PycharmProjects\\GA\\Calls')
from Validation_Functions.validateFunctions import dataFormatValidation, dataTypeValidation, dataValueValidation
from Calls.gettingCalls import eventCall

eventObj = {}
valueNotFound = 'Value Not Found'

#For each event in input file that user specified
for i in inputData:
    tempEventObj = {}
    #getting the property and its object for each event from the input file
    for property, propertyObj in inputData[i].items():
        #a temporary object for each property
        tempPropertyObj = {}
        errorValue = 'No Error/'
        typeError = ''

        #the value we captured from network
        tempPropertyObj['capturedValue'] = eventCall[i][property][0]
        #the value we wanted
        tempPropertyObj['expectedValue'] = propertyObj['expectedValue']


        if (propertyObj['requirement'] == 'R' and tempPropertyObj['capturedValue'] == 'NA'):
            errorValue = 'Error'
            typeError = valueNotFound
            tempPropertyObj['errorCheck'] = errorValue + '/' + typeError
            tempEventObj[property] = tempPropertyObj
            continue

        # If we have to check data type
        if (propertyObj['problemType'] == 'Data Type'):
            errorValue, typeError = dataTypeValidation(tempPropertyObj['capturedValue'],
                                                       tempPropertyObj['expectedValue'])

        # or else we have to check data value
        elif (propertyObj['problemType'] == 'Data Value'):
            errorValue, typeError = dataValueValidation(tempPropertyObj['capturedValue'],
                                                        tempPropertyObj['expectedValue'])

        # or else we have to check data format
        elif (propertyObj['problemType'] == 'Data Format'):
            errorValue, typeError = dataFormatValidation(tempPropertyObj['capturedValue'],
                                                         tempPropertyObj['expectedValue'])

        tempPropertyObj['errorCheck'] = errorValue + '/' + typeError

        tempEventObj[property] = tempPropertyObj

    eventObj[i] = tempEventObj

print("eventObj -",eventObj)
