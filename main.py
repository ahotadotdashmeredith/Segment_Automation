from xlwt import Workbook
from Input.urls import readingUrls
from Input.rules import readingInput
from Setup.driverSetup import driverCall
from Calls.makingPageCall import pageCall
from Calls.eventCall import performingEvent
from Calls.finalCall import finalCall
from Setup.networkCalls import gettingGaNetworkCalls
from Calls.gettingCalls import gettingEventCalls
from Validation.validation import validation
from Workbook.workbook import writingData, saveExcelFile
from pathlib import Path


if __name__ == "__main__":
    parPath = Path.cwd()
    wb = Workbook()
    userInput = readingUrls('Sheet1', parPath)
    for i in userInput:
        inputUrl, brand, rulesSheet, viewType, resultSheet = i
        inputData = readingInput(rulesSheet, parPath, viewType)
        driver = driverCall()
        driver = pageCall(driver, inputUrl)
        driver = performingEvent(driver, inputUrl, rulesSheet, viewType, parPath)
        # driver = finalCall(driver, inputUrl)
        gaCalls = gettingGaNetworkCalls(driver)
        eventCalls = gettingEventCalls(gaCalls, inputData)
        eventObj = validation(eventCalls, inputData)
        sheet = wb.add_sheet(resultSheet)
        sheet = writingData(sheet, eventObj)
        output = saveExcelFile(wb, parPath)
        print(output)
