import re
import xlrd
from interval import Interval
from ExcelReading import Utils
import datetime


class ExcelReader:

    def __init__(self, excelPath):
        self.path = excelPath
        self.workbook = xlrd.open_workbook(excelPath)
        self._InputSchedule(self.workbook)
        self._InputSeat(self.workbook)

    def _InputSchedule(self, workbook):
        Courselist = []
        Data_sheet = workbook.sheet_by_index(0)
        rowNum = Data_sheet.nrows
        colNum = Data_sheet.ncols
        for i in range(4, rowNum):
            rowList = []
            for j in range(colNum):
                rowList.append(Data_sheet.cell_value(i, j))
            Courselist.append(Class(rowList))
        self.courseList = Courselist

    def _InputSeat(self, workbook):
        SeatList = []
        Data_sheet = workbook.sheet_by_index(1)
        rowNum = Data_sheet.nrows
        colNum = Data_sheet.ncols
        for i in range(0, rowNum):
            rowList = []
            for j in range(colNum):
                rowList.append(Data_sheet.cell_value(i, j))
            SeatList.append(Seat(rowList))
        self.seatList = SeatList
        for item in self.seatList:
            item.GetClassInfo(self.courseList)


class Class:

    def __init__(self, infoList):
        self.classIndex = re.sub(r"[\u4e00-\u9fa5]", "", infoList[0])
        del infoList[0]
        courseList = []
        for i in range(len(infoList)):
            if infoList[i] != "":
                courseInfoList = infoList[i].split("\n")
                for j in range(int(len(courseInfoList) / 5)):
                    list = courseInfoList[j * 5:5 * j + 5]
                    course = Course(list, self._GetDayOfWeeks(i))
                    courseList.append(course)
        self.courseList = courseList

    def _GetDayOfWeeks(self, i):
        if i in Interval(0, 5):
            return 0
        if i in Interval(5, 10):
            return 1
        if i in Interval(10, 15):
            return 2
        if i in Interval(15, 20):
            return 3
        if i in Interval(20, 25):
            return 4

    def isHavingClass(self, time):
        for i in range(len(self.courseList)):

            if self.courseList[i].isHavingClass(time) != -1:
                takeUp = self.courseList[i].isHavingClass(time)
                if self.courseList[i + 1].isHavingClass(time + datetime.timedelta(hours=2)) != -1:
                    takeUp += 120
                return takeUp

        return -1


class Course:

    def __init__(self, stringList, dayOfWeek):
        self.dayOfWeek = dayOfWeek
        self.courseName = stringList[0]
        self.teacherName = stringList[1]
        self.courseIndex = stringList[2]
        self.forCheck = stringList[4]
        if stringList[4].find("单周") != -1:
            self.weekType = Utils.WeekType.ODD
        elif stringList[4].find("双周") != -1:
            self.weekType = Utils.WeekType.EVEN
        else:
            self.weekType = Utils.WeekType.NORMAL
        wnl = stringList[4].split("][")
        self._DispatchWeeks(wnl[0].replace('[', ''))
        self._DispatchLessons(wnl[1].replace(']', ''))

    def _DispatchWeeks(self, string):
        weeklist = []
        substring = re.sub(r"[\u4e00-\u9fa5]", "", string)
        if substring.isnumeric():
            weeklist.append(int(substring))
        weekliststr = substring.split(",")
        for week in weekliststr:
            matchObj = re.match(r'([0-9]+)-([0-9]+)', week, re.M | re.I)
            if matchObj != None:
                for index in range(int(matchObj.group(1)), int(matchObj.group(2)) + 1):
                    weeklist.append(index)
            elif week.isnumeric():
                weeklist.append(int(week))

        if self.weekType == Utils.WeekType.ODD:
            for i in weeklist:
                if i % 2 == 0:
                    weeklist.remove(i)
        if self.weekType == Utils.WeekType.EVEN:
            for i in weeklist:
                if i % 2 != 0:
                    weeklist.remove(i)
        self.weeks = weeklist

    def _DispatchLessons(self, string):
        lesson = []
        matchObj = re.match(r'([0-9]+)-([0-9]+)', string, re.M | re.I)
        if matchObj != None:
            self.classTime = Utils.ClassTime(int(matchObj.group(1)), int(matchObj.group(2)))

    # 这里改成返回-1和占用时间
    def isHavingClass(self, time):
        if time.date().weekday() != self.dayOfWeek:
            return -1
        for i in self.weeks:
            if time.date().isocalendar()[1] - 10 == i:
                if time.time() >= self.classTime.start and time.time() <= self.classTime.end:
                    return int((datetime.datetime.combine(time.date(), self.classTime.end) - time).seconds / 60)
                else:
                    return -1;
        return -1;


class Seat:

    def __init__(self, stringList):
        stuID = stringList[0]
        if isinstance(stuID, float):
            self.stuID = str(stuID)[:-2]
        else:
            self.stuID = stuID
        self.stuName = stringList[1]
        self.scheduleList = stringList[2:len(stringList)]

    # 如果返回-1则座位拥有者没有课，需要预留。
    # 如果为时间差值，则为剩余空闲时间
    def CheckAvalible(self, datetime):
        return self.classObj.isHavingClass(datetime)

    def GetClassInfo(self, classList):
        classId = str(self.stuID)[:-2]
        for classItem in classList:
            if classItem.classIndex == classId:
                self.classObj = classItem
