"""
json数据格式：对象数组[{},{},{}...]
注意点：
1.json格式必须为双引号
2.json读取：data[0].get('str') json的索引从0开始
"""

# CSV文件的存储：特定字符分隔的纯文本
import csv

with open('data.csv','w',encoding = 'utf-8') as f:
# delimiter修改列与列之间的分隔符
# with open('data.csv','w',delimitr = ' ',encoding = 'utf-8') as f: # 已空格作为分隔符

    # 类似于pyquery，xpath的初始化对象
    writer = csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','chd',18])
    writer.writerow(['1002','whx',21])
    writer.writerow(['1003','sgx',20])
  
# CSV文件的读取
with open('data_test.csv','r',encoding = 'utf-8') as f:
    reader = csv.read(f)
    for row in reader:
        print(row)
        
        
# pandas读取文件
import pandas as pd

f = pd.read_csv('data.csv')
    print(f)
