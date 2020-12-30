# coding=utf-8
from datetime import datetime
import xlrd

data = xlrd.open_workbook("刷卡记录表.xlsx")
table = data.sheet_by_name("Sheet0")
rowNum = table.nrows
colNum = table.ncols
sheet0 = data.sheet_by_index(0)
i = rowNum
end = sheet0.cell(1,0).value
begin = sheet0.cell(5,0).value
begin = datetime.strptime(begin, '%Y-%m-%d %H:%M:%S')
begin = format(begin, '%H%S')
end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
end = format(end, '%H%S')
# end = datetime.strptime(end, '%H:%M')
# begin = format(begin, '%H,%M')
# du = (end - begin)
print(begin)
print(end)
a = int(begin)
b = int(end)
c = 830
d = 1730
print(c - a)
print(d - b)
# if du > 0:
#     print('ok')
# else:
# print(du)
