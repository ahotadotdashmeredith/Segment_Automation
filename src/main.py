from xlwt import Workbook
from src.input.urls import readingUrls
from src.input.rules import readingInput
from src.setup.driverSetup import driverCall
from src.calls.makingPageCall import pageCall
from src.calls.eventCall import performingEvent
from src.calls.finalCall import finalCall
from src.setup.networkCalls import gettingGaNetworkCalls
from src.calls.gettingCalls import gettingEventCalls
from src.validation.validation import validation
from src.workbook.workbook import writingData, saveExcelFile
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
