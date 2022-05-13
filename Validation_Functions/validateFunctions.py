import re

def dataTypeValidation(capturedValue, expectedValue):
    #If data type matches
    if (expectedValue == type(capturedValue).__name__):
        return "No Error", ''
    #if data type doesn't match
    else:
        return "Error", 'Data Type Mismatch'



def dataValueValidation(capturedValue, expectedValue):
    #If data value matches
    if (capturedValue == expectedValue):
        return "No Error", ''
    #If data value doesn't match
    else:
        return "Error", 'Incorrect Value'



def dataFormatValidation(capturedValue, expectedValue):
    print(capturedValue)
    print(expectedValue)
    #The format is correct i.e. string matches
    if re.fullmatch(expectedValue, str(capturedValue)) is not None:
        return "No Error", ''
    #the parameter value does not match the format
    else:
        return "Error", 'Format Mismatch'