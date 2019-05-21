import xlrd
 
# 打开Excel文件读取数据
workbook = xlrd.open_workbook('test.xls')
 
# 打印所有的sheet列出所有的sheet名字
print(workbook.sheet_names())
 
# 根据sheet索引或者名称获取sheet内容
Data_sheet = workbook.sheets()[0]
# Data_sheet = workbook.sheet_by_index(1) 
# Data_sheet = workbook.sheet_by_name(u'pyTest') 
 
# 获取sheet名称、行数和列数
sheet_name = Data_sheet.name
rows_num = Data_sheet.nrows
cols_num = Data_sheet.ncols
print(sheet_name,rows_num,cols_num)
 
 
# 获取整行和整列的值（列表）   
first_row = Data_sheet.row_values(0) #获取第一行内容 
first_col = Data_sheet.col_values(1) #获取第二列内容 
print(first_row,first_col)
 
# 获取单元格内容的数据类型
# 相当于在一个二维矩阵中取值
# （row,col）-->(行,列)
cell_A1 = Data_sheet.cell(0,0).value # 第一行第一列坐标A1的单元格数据
cell_B1 = Data_sheet.cell(0,1).value # 第一行第三列坐标C1的单元格数据
 
cell_B2 = Data_sheet.row(1)[1].value # 第2行第2列
cell_C2 = Data_sheet.col(2)[1].value # 第3列第2行
print(cell_A1,cell_B1,cell_B2,cell_C2)


# 检查单元格的数据类型
# ctype的取值含义
# ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
cell_ctype = Data_sheet.cell(1,2).ctype
print(cell_ctype)
 