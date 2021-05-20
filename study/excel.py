import xlrd

book = xlrd.open_workbook('ztky_centers_aging (1).xlsx')
# print(f"包含表单数量 {book.nsheets}")
# print(f"表单的名分别为: {book.sheet_names()}")
#
# sheet = book.sheet_by_index(0)
# # a = book.sheet_by_name('Sheet1')
# # print(a)
#
# print(f"表单名：{sheet.name} ")
# print(f"表单索引：{sheet.number}")
# print(f"表单行数：{sheet.nrows}")
# print(f"表单列数：{sheet.ncols}")
# # 读取一个数据
# print(f"单元格A1内容是: {sheet.cell_value(rowx=1, colx=1)}")
# # 读取一行的数据
# print(f"第一行内容是: {sheet.row_values(rowx=0)}")
# #读取一列的数据
# print(f"第一列内容是: {sheet.col_values(colx=1)}")


print('''\n计算时效总和''')
sheet = book.sheet_by_name('Sheet1')
values = sheet.col_values(colx=2)
# print(f"第一列内容是: {sheet.col_values(colx=2)}")
incomes = values[1:]
print(f'总时效合为：{sum(incomes)}')


