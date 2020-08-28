# @author Yu Tongxin
# @data 2020-08-28
import re
import xlwt
import os

def read_log():
    value = []
    value.append(["date", "type", "info"])
    with open("Apache_log/Apache_2k.log", "r") as log:
        for line in log:
            value.append(extract_data(line))
    book_name_xls = 'Apache_log.xls'
    sheet_name_xls = 'apache_log'
    if os.path.exists(book_name_xls):
        os.remove(book_name_xls)

    write_excel_xls(book_name_xls, sheet_name_xls, value)


def extract_data(line):
    list = []
    matchObj = re.match(r'(\[.*\]) (\[.*\]) (.*)', line, re.M | re.I)
    if matchObj:
        date = matchObj.group(1).strip().replace("[", "").replace("]", "")
        type = matchObj.group(2).strip().replace("[", "").replace("]", "")
        info = matchObj.group(3)
        list.append(date)
        list.append(type)
        list.append(info)
        return list
    else:
        print("No match!!")

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

read_log()
