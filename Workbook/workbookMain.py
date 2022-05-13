import xlwt as xw
# from workbookRules import wb
import sys
sys.path.insert(1, 'C:\\Users\\ahota\\PycharmProjects\\GA\\Validation')
from Validation.validation import eventObj
from xlwt import Workbook


wb = Workbook()
sheet1 = wb.add_sheet('Event Info')
columns = ['Event', 'Property Names', 'Error Check', 'Captured Value', 'Expected value']
parameters = list(eventObj.keys())


#Writing the headings column
for i in range(len(columns)):
    if(i==len(columns)-1):
        sheet1.col(i).width = 14000
    else:
        sheet1.col(i).width = 7000
    sheet1.write(0, i, columns[i], xw.easyxf('font: bold 1'))


#Writing the data
i = 2
eventIndex = 0
while eventIndex<len(parameters):
    sheet1.write(i, 0, parameters[eventIndex])
    propertyList = list(eventObj[parameters[eventIndex]].keys())
    for j in propertyList:
        #property
        sheet1.write(i, 1, j)
        #error Check
        if(eventObj[parameters[eventIndex]][j]['errorCheck'].startswith('E')):
            sheet1.write(i, 2, eventObj[parameters[eventIndex]][j]['errorCheck'], xw.easyxf('pattern: pattern solid, fore_colour red;'))
        else:
            sheet1.write(i, 2, eventObj[parameters[eventIndex]][j]['errorCheck'])
        #Captured Value
        sheet1.write(i, 3, eventObj[parameters[eventIndex]][j]['capturedValue'])
        #Expected Value
        sheet1.write(i, 4, eventObj[parameters[eventIndex]][j]['expectedValue'])
        i = i + 1
    eventIndex = eventIndex+1

wb.save('C:\\Users\\ahota\\Documents\\Work\\Selenium\\GA\\Result\\health_article_event_Result.xls')
