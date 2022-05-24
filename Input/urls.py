import pandas as pd
from pathlib import Path

def readingUrls(sheetName, parPath, relPath='Files\\Urls\\InputUrls.xlsx'):
    path = (parPath/relPath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    userInput = []

    for i in range(1, len(df)):
        url = str(df['Urls'][i])
        brand = str(df['brand'][i])
        pageType = str(df['pageType'][i])
        if(str(df['viewType'][i])=='nan'):
            viewType=''
        else:
            viewType = str(df['viewType'][i])

        brand = brand
        file = pageType+viewType
        resultFile = brand+pageType+viewType
        input = (url, brand, file, resultFile)
        userInput.append(input)

    return userInput

if __name__=="__main__":
    userInput = readingUrls('Sheet1')
    print(userInput)


