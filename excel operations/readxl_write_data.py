import openpyxl
#path for excel file
path="D:\Study material\MS\selenium testing codes\excel operations\practice book.xlsx"

workbook=openpyxl.load_workbook(path)
#to select active sheet from excel file
sheet=workbook.get_sheet_by_name("Sheet1") #workbook.get_sheet_by_name("sheet1")


#to write data in each cell
for r in range(1,5):
    for c in range(1, 4):
        sheet.cell(row=r,column=c).value="sandesh"
#to save excel file
workbook.save(path)
