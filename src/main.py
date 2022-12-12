from xlwt import Workbook
from src.Input.urls import readingUrls
from src.Input.rules import readingInput
from src.Setup.driverSetup import driverCall
from src.Calls.makingPageCall import pageCall
from src.Calls.eventCall import performingEvent
from src.Calls.finalCall import finalCall
from src.Setup.networkCalls import gettingGaNetworkCalls
from src.Calls.gettingCalls import gettingEventCalls
from src.Validation.validation import validation
from src.Workbook.workbook import writingData, saveExcelFile
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
        driver = finalCall(driver, inputUrl)
        gaCalls = gettingGaNetworkCalls(driver)
        eventCalls = gettingEventCalls(gaCalls, inputData)
        eventObj = validation(eventCalls, inputData)
        sheet = wb.add_sheet(resultSheet)
        sheet = writingData(sheet, eventObj)
        output = saveExcelFile(wb, parPath)
        print(output)
