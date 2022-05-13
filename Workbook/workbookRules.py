import xlwt as xw
import sys
sys.path.insert(1, 'C:\\Users\\ahota\\PycharmProjects\\gaSegment\\Validation')
from Validation.rulesValidation import returnObject
from xlwt import Workbook
wb = Workbook()


sheet1 = wb.add_sheet('Rules Info')
columns = ['Parameters', 'Values/Availability']
parameters = list(returnObject.keys())
values = list(returnObject.values())

#Writing the headings column
for i in range(len(columns)):
    if(i==len(columns)-1):
        sheet1.col(i).width = 14000
    else:
        sheet1.col(i).width = 7000
    sheet1.write(0, i, columns[i], xw.easyxf('font: bold 1'))



#Finally writing Data
m=1
n=0
for i in values:
    for k,v in i.items():
        sheet1.write(m + 1, n, k)
        sheet1.write(m + 1, n + 1, v)
        m = m+1
    m = m+2

wb.save('C:\\Users\\ahota\\Documents\\Work\\Selenium\\Segment\\Result\\people_article_Rules.xls')