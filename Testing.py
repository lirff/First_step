from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "New Title"
wb.save('First.xlsx')
ws1 = wb.create_sheet('Ws1')
wb.save('Sec.xlsx')
