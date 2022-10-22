import provider as pr
from datetime import date



def append_student():
        wb=pr.work_book()
        sheet = wb['Ученики']
        i=pr.empty_line('Ученики')
        sheet.cell(row=i, column=1).value=i-1
        sheet.cell(row=i, column=2).value=a
        wb.save(filename ='Классный журнал 7а.xlsx')
        wb.close()