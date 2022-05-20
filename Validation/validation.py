from Validation_Functions.validateFunctions import dataFormatValidation, dataTypeValidation, dataValueValidation


def validation(eventCall, inputData):
    #final object that will be written into the excel sheet
    eventObj = {}

    #variable later used for concatenation
    valueNotFound = 'Value Not Found'

    #For each event in input file that user specified
    for i in inputData:

        #object that will contain error, expected and captured value for each event
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

            #If property was needed but not captured
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

    return eventObj