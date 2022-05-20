from xlwt import Workbook
from Input.inputUrls import readingUrls
from Input.input import readingInput
from Setup.driverSetup import driverCall
from Calls.makingPageCall import pageCall
from Calls.eventCall import performingEvent
from Calls.finalCall import finalCall
from Setup.networkCalls import gettingGaNetworkCalls
from Calls.gettingCalls import gettingEventCalls
from Validation.validation import validation
from Workbook.workbook import writingData, saveExcelFile

if __name__=="__main__":
    wb = Workbook()
    userInput = readingUrls()
    for i in userInput:
        inputUrl, eventSheet, rulesSheet, resultFile = i
        inputData = readingInput(rulesSheet)
        driver = driverCall()

        driver = pageCall(driver, inputUrl)
        driver = performingEvent(driver, inputUrl, eventSheet)
        driver = finalCall(driver, inputUrl)
        gaCalls = gettingGaNetworkCalls(driver)
        eventCalls = gettingEventCalls(gaCalls, inputData)
        eventObj = validation(eventCalls, inputData)

        sheet = wb.add_sheet(resultFile)
        sheet = writingData(sheet, eventObj)
        output = saveExcelFile(wb)
        print(output)
