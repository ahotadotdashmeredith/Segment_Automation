import xlwt as xw


def writingHeadingColumns(sheet):
    try:
        columns = ['Event', 'Property Names', 'Error Check', 'Captured Value', 'Expected value']
        # Writing the headings column
        for i in range(len(columns)):
            if (i == len(columns) - 1):
                sheet.col(i).width = 14000
            else:
                sheet.col(i).width = 7000
            sheet.write(0, i, columns[i], xw.easyxf('font: bold 1'))
    except:
        print("Error in writing headings in excel sheet")
    return sheet


def writingProperty(sheet, i, k):
    propertyList = list(k.keys())
    for j in propertyList:
        # property
        sheet.write(i, 1, j)
        # error Check
        if (k[j]['errorCheck'].startswith('E')):
            sheet.write(i, 2, k[j]['errorCheck'], xw.easyxf('pattern: pattern solid, fore_colour red;'))
        else:
            sheet.write(i, 2, k[j]['errorCheck'])
        # Captured Value
        sheet.write(i, 3, str(k[j]['capturedValue']))
        # Expected Value
        sheet.write(i, 4, str(k[j]['expectedValue']))
        i = i + 1
    return sheet, i


def writingEvent(sheet, eventObj, m, baseRow):
    i = baseRow
    sheet.write(i, 0, m)
    eventsList = eventObj[m]
    for k in eventsList:
        sheet, i = writingProperty(sheet, i, k)
    return sheet, i


def writingData(sheet, eventObj):
    sheet = writingHeadingColumns(sheet)
    baseRow = 2
    for m in eventObj:
        sheet, baseRow = writingEvent(sheet, eventObj, m, baseRow)
    return sheet


def saveExcelFile(wb, parPath, relPath='Files\\Result\\Result.xls'):
    output = ''
    try:
        path = (parPath / relPath)
        wb.save(path)
        output = "File Saved"
    except:
        output = "Error in saving file"
    return output
