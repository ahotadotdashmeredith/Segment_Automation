import pandas as pd
from pathlib import Path


def readingPropertyRules(df, start, end, k):
    tempPropertyObj = {}
    for i in range(start, end):
        property = df[df.columns[k]][i]
        tempObj = {'requirement': df.iloc[i][k+1], 'problemType': df.iloc[i][k+2]}
        if (tempObj['problemType'] == 'Data Type'):
            tempObj['expectedValue'] = df.iloc[i][k+3]
        elif (tempObj['problemType'] == 'Data Value'):
            tempObj['expectedValue'] = df.iloc[i][k+4]
        else:
            tempObj['expectedValue'] = df.iloc[i][k+5]
        tempPropertyObj[property] = tempObj
    return tempPropertyObj


def readingInputSheet(sheetName, parPath):
    df = readSheetAsDf(sheetName, parPath)
    tempPropertyObj = readingPropertyRules(df, 0, len(df), 0)
    return tempPropertyObj


def readSheetAsDf(sheetName, parPath, relPath='Files\\InputRules\\Rules.xlsx'):
    path = (parPath/relPath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    return df


def creatingListIndex(sheetName, parPath):
    df = readSheetAsDf(sheetName, parPath)
    #list giving information as to how many parameters each event has in the input-Rules file
    eventParametersIndex = []
    for i in range(len(df[df.columns[0]])):
        if(str(df[df.columns[0]][i])=='nan'):
            continue
        else:
            eventParametersIndex.append(i)
    return df, eventParametersIndex


def readingMainSheetData(df, eventParametersIndex):
    inputData = {}
    for i in range(0, len(eventParametersIndex)):
        eventType = df[df.columns[0]][eventParametersIndex[i]]
        finalPropertyIndex = 0
        if (i == len(eventParametersIndex) - 1):
            finalPropertyIndex = df[df.columns[1]].count()
        else:
            finalPropertyIndex = eventParametersIndex[i + 1]
        tempPropertyObj = readingPropertyRules(df, eventParametersIndex[i], finalPropertyIndex, 1)
        inputData[eventType] = tempPropertyObj
    return inputData


def readingGeneralSheetData(inputData, parPath):
    sheetInput = readingInputSheet('GENERAL', parPath)
    tempPageviewObj = inputData.get('pageview')
    for i,j in sheetInput.items():
        tempPageviewObj[i] = j
    inputData['pageview'] = tempPageviewObj
    return inputData


def readingVideoSheetData(inputData, parPath):
    sheetInput = readingInputSheet('GENERALVIDEO', parPath)
    inputData['jumpstartPlayer'] = sheetInput
    return inputData


def readingInput(sheetName, parPath, viewType):
    # Reading data from intended sheet
    df, eventParametersIndex = creatingListIndex(sheetName, parPath)
    inputData = readingMainSheetData(df, eventParametersIndex)
    # Adding data from General sheet
    inputData = readingGeneralSheetData(inputData, parPath)
    # Adding data from GENERALVIDEO sheet if page contains video
    if (viewType=='Video'):
        inputData = readingVideoSheetData(inputData, parPath)
    return inputData


if __name__=='__main__':
    parPath = Path.cwd().parent
    print(readingInput('BIO', parPath, 'Video'))
