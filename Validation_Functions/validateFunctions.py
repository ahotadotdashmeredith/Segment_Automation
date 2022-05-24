import re

def dataTypeValidation(capturedValue, expectedValue):
    #If value captured is empty
    if(len(capturedValue)==0):
        return "Error", 'Value Empty'
    #If data type matches
    elif (expectedValue == type(capturedValue).__name__):
        return "No Error", ''
    #if data type doesn't match
    else:
        return "Error", 'Data Type Mismatch'



def dataValueValidation(capturedValue, expectedValue):
    #If value captured is empty
    if(len(capturedValue)==0):
        return "Error", 'Value Empty'
    #If data value matches
    elif (str(capturedValue) == str(expectedValue)):
        return "No Error", ''
    #If data value doesn't match
    else:
        return "Error", 'Incorrect Value'



def dataFormatValidation(capturedValue, expectedValue):
    #If value captured is empty
    if(len(capturedValue)==0):
        return "Error", 'Value Empty'
    #The format is correct i.e. string matches
    elif re.fullmatch(str(expectedValue), str(capturedValue)) is not None:
        return "No Error", ''
    #the parameter value does not match the format
    else:
        return "Error", 'Format Mismatch'

if __name__=='__main__':
    print(dataTypeValidation('1000028', 'int'))