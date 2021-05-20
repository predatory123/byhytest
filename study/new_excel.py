import xlwt

name2Age = {
    '张飞' :  38,
    '赵云' :  27,
    '许褚' :  36,
    '典韦' :  38,
    '关羽' :  39,
    '黄忠' :  49,
    '徐晃' :  43,
    '马超' :  23,
}

# 创建一个新的Workbook对象
book = xlwt.Workbook()

# 增加一个名为“年龄”的表
sh = book.add_sheet('年龄表')

# 写入内容
row = 1

for name,age in name2Age.items():
    sh.write(row,0,name)
    sh.write(row,1,age)
    row += 1

# 保存文件
book.save('年龄表.xls')