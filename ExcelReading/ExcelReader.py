from ExcelReading import Class
import datetime

excel = Class.ExcelReader('../Source/课程总表.xls')

for item in excel.seatList:
    avaTime = item.CheckAvalible(datetime.datetime.now())
    if avaTime == -1:
        print("座位被"+item.stuName+"("+item.stuID+")"+"占用中")
    else:
        print("座位空闲，剩余空闲时间"+str(avaTime)+"分钟")

print("Just for Test")