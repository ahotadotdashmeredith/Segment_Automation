import pandas as pd
from pathlib import Path

def readInputGeneralExcelSheet(parPath, relPath='Files\\InputRules\\Rules.xlsx'):
    sheetName = 'GENERAL'
    path = (parPath/relPath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    return df

def readingInputGeneral(parPath):
    inputData = {}
    df = readInputGeneralExcelSheet(parPath)
    tempPropertyObj = {}
    for i in range(0, len(df)):
        property = df[df.columns[0]][i]
        tempObj = {'requirement': df.iloc[i][1], 'problemType' : df.iloc[i][2]}
        if(tempObj['problemType']=='Data Type'):
            tempObj['expectedValue'] = df.iloc[i][3]
        elif (tempObj['problemType'] == 'Data Value'):
            tempObj['expectedValue'] = df.iloc[i][4]
        else:
            tempObj['expectedValue'] = df.iloc[i][5]
        tempPropertyObj[property] = tempObj

        inputData['pageview'] = tempPropertyObj

    return inputData

def readInputExcelSheet(sheetName, parPath, relPath='Files\\InputRules\\Rules.xlsx'):
    path = (parPath/relPath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    return df


def creatingListIndex(sheetName, parPath):
    df = readInputExcelSheet(sheetName, parPath)
    #list giving information as to how many paramters each event has in the input-Rules file
    eventParametersIndex = []
    for i in range(len(df[df.columns[0]])):
        if(str(df[df.columns[0]][i])=='nan'):
            continue
        else:
            eventParametersIndex.append(i)
    return df, eventParametersIndex


def readingInput(sheetName, parPath):
    df, eventParametersIndex = creatingListIndex(sheetName, parPath)
    inputData = {}
    for i in range(0, len(eventParametersIndex)):
        tempPropertyObj = {}
        eventType = df[df.columns[0]][eventParametersIndex[i]]
        finalPropertyIndex = 0
        if(i==len(eventParametersIndex)-1):
            finalPropertyIndex = df[df.columns[1]].count()
        else:
            finalPropertyIndex = eventParametersIndex[i+1]
        for j in range(eventParametersIndex[i], finalPropertyIndex):
            property = df[df.columns[1]][j]
            tempObj = {'requirement': df.iloc[j][2], 'problemType' : df.iloc[j][3]}
            if(tempObj['problemType']=='Data Type'):
                tempObj['expectedValue'] = df.iloc[j][4]
            elif (tempObj['problemType'] == 'Data Value'):
                tempObj['expectedValue'] = df.iloc[j][5]
            else:
                tempObj['expectedValue'] = df.iloc[j][6]
            tempPropertyObj[property] = tempObj
        inputData[eventType] = tempPropertyObj

    generalInput = readingInputGeneral(parPath)
    tempPageviewObj = inputData.get('pageview')
    for i,j in generalInput['pageview'].items():
        tempPageviewObj[i] = j
    inputData['pageview'] = tempPageviewObj

    return inputData

if __name__=='__main__':
    parPath = Path.cwd().parent
    # userInput = readInputGeneralExcelSheet(parPath)
    # print(userInput)
    # print(readingInputGeneral(parPath))
    print(readingInput('BIO',parPath))