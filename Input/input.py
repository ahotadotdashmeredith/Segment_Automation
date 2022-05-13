import pandas as pd

excel_data = pd.read_excel('C:\\Users\\ahota\\Documents\\Work\\Selenium\\GA\\UserInput\\Health_Article.xlsx')

df = pd.DataFrame(excel_data)
keys = df.keys()

inputUrl = df.iloc[0][0]
inputData = {}
eventParametersIndex = []
chosenEvents = []

for i in range(len(df[df.columns[1]])):
    if(str(df[df.columns[1]][i])=='nan'):
        continue
    else:
        eventParametersIndex.append(i)

for i in range(len(df[df.columns[1]])):
    if(str(df[df.columns[1]][i])=='nan' or str(df[df.columns[1]][i])=='pageview'):
        continue
    else:
        chosenEvents.append(df[df.columns[1]][i])


for i in range(0, len(eventParametersIndex)):
    tempPropertyObj = {}
    eventType = df[df.columns[1]][eventParametersIndex[i]]
    finalPropertyIndex = 0
    if(i==len(eventParametersIndex)-1):
        finalPropertyIndex = df[df.columns[2]].count()
    else:
        finalPropertyIndex = eventParametersIndex[i+1]

    for j in range(eventParametersIndex[i], finalPropertyIndex):

        property = df[df.columns[2]][j]
        tempObj = {'requirement': df.iloc[j][3], 'problemType' : df.iloc[j][4]}
        if(tempObj['problemType']=='Data Type'):
            tempObj['expectedValue'] = df.iloc[j][5]
        elif (tempObj['problemType'] == 'Data Value'):
            tempObj['expectedValue'] = df.iloc[j][6]
        else:
            tempObj['expectedValue'] = df.iloc[j][7]
        tempPropertyObj[property] = tempObj

    inputData[eventType] = tempPropertyObj

print("input Data - ", inputData)
print('input Url', inputUrl)
print(chosenEvents)

