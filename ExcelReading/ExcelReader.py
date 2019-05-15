from ExcelReading import Class
import datetime

excel = Class.ExcelReader('../Source/课程总表.xls')

for item in excel.seatList:
    avaTime = item.CheckAvalible(datetime.datetime(2019,5,15,18,45))
    if avaTime == -1:
        print("座位被"+item.stuName+"("+item.stuID+")"+"占用中")
    else:
        print("座位空闲，剩余空闲时间"+str(avaTime)+"分钟")
# print(excel.seatList[0].CheckAvalible(datetime.datetime(2019,5,15,9,45)))