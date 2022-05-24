import xlwt as xw


def writingHeadingColumns(sheet):
    try:
        columns = ['Event', 'Property Names', 'Error Check', 'Captured Value', 'Expected value']
        #Writing the headings column
        for i in range(len(columns)):
            if(i==len(columns)-1):
                sheet.col(i).width = 14000
            else:
                sheet.col(i).width = 7000
            sheet.write(0, i, columns[i], xw.easyxf('font: bold 1'))
    except:
        print("Error in writing headings in excel sheet")
    return sheet


def writingData(sheet, eventObj):
    try :
        sheet = writingHeadingColumns(sheet)
        parameters = list(eventObj.keys())
        #Writing the data
        i = 2
        eventIndex = 0
        while eventIndex<len(parameters):
            sheet.write(i, 0, parameters[eventIndex])
            propertyList = list(eventObj[parameters[eventIndex]].keys())
            for j in propertyList:
                #property
                sheet.write(i, 1, j)
                #error Check
                if(eventObj[parameters[eventIndex]][j]['errorCheck'].startswith('E')):
                    sheet.write(i, 2, eventObj[parameters[eventIndex]][j]['errorCheck'], xw.easyxf('pattern: pattern solid, fore_colour red;'))
                else:
                    sheet.write(i, 2, eventObj[parameters[eventIndex]][j]['errorCheck'])
                #Captured Value
                sheet.write(i, 3, str(eventObj[parameters[eventIndex]][j]['capturedValue']))
                #Expected Value
                sheet.write(i, 4, str(eventObj[parameters[eventIndex]][j]['expectedValue']))
                i = i + 1
            eventIndex = eventIndex+1
    except:
        print('Error in writing data in Excel Sheet')
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


