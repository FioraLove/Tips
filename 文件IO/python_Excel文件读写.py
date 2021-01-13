"""
CSV文件读写：CSV模块，pandas模块

Excel文件读写：xlrd与xlwt模块；openpyxl模块；pandas模块 
"""

"""
我们在python中引入openpyxl模块来操控excel文件。一个以.xlsx为扩张名的excel文件打开后叫工作簿workbook，
每个工作簿可以包括多张表单worksheet，正在操作的这张表单被认为是活跃的active sheet。每张表单有行和列，行号1、2、3…，列号A、B、C...。在
某一个特定行和特定列的小格子叫单元格cell。

python程序从excel文件中读数据基本遵循以下步骤：
　　1、import openpyxl
　　2、调用openpyxl模块下的load_workbook(‘你的文件名.xlsx’)函数打开excel文件，得到一个工作簿(workbook)对象wb
　　3、通过wb.active或wb的方法函数get_sheet_by_name(‘你想要访问的表单名称’)得到表单对象ws

　　4、通过索引获取单元格：ws[‘B2’]
     　　通过表单的方法函数cell（）获取单元格：ws.cell(row=1, column=2)
    　　 通过单元格的属性value，row，column，coordinate对单元格进行多方向立体式访问
　　5、行对象ws[10]，列对象[‘C’]，行切片ws[5:10]、列切片ws[‘C:D’]，单元格左上角和右下角左边共同划定表单指定区域ws['A1':'C3']
　　6、ws.max_row和ws.max_column给出数据用到的最大行和列
　　7、from openpyxl.utils import get_column_letter, column_index_from_string引进来的两个函数实现excel表格列字母和数字的转换
"""
