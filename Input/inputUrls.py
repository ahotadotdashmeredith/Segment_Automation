import pandas as pd


def readingUrls(path='C:\\Users\\ahota\\Documents\\Work\\Selenium\\GA\\Urls\\InputUrls.xlsx'):
    excel_data = pd.read_excel(path)
    df = pd.DataFrame(excel_data)
    url = ''
    pageType = ''
    viewType = ''
    userInput = []

    for i in range(1, len(df)):
        url = str(df['Urls'][i])
        brand = str(df['brand'][i])
        pageType = str(df['pageType'][i])
        if(str(df['viewType'][i])=='nan'):
            viewType=''
        else:
            viewType = str(df['viewType'][i])

        eventFile = brand+pageType+viewType+"Events"
        rulesFile = brand+pageType+viewType+"Rules"
        resultFile = brand+pageType+viewType+"Result"
        input = (url, eventFile, rulesFile, resultFile)
        userInput.append(input)

    return userInput

# if __name__=="__main__":
#     userInput = readingUrls()
#     print(userInput)


