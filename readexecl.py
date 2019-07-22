#read execl
import logging
import xlrd
def test():
    readbook = xlrd.open_workbook(r'C:\Users\user\Desktop\20190515\20190418case.xls')

    sheet = readbook.sheet_by_index(0)
    lng = sheet.cell(1, 3).value

    logging.info(sheet)
    logging.info(lng)
    return sheet



