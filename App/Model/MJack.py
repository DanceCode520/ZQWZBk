from App.Model.models import *
import time
import json, datetime


# 时间编码
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)

class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d %H:%M:%S')


# 计算个人所得税及工资
# 单位===养老：0.18  医疗：0.08，失业：0.005，工商：0.006，生育：0.012，单位合计是28.3%。
# 个人===养老：0.08，医疗：0.02，失业：0.005 个人合计：0.105。
def getSalary(social_security_base, provident_fund_base, perSalary):
    costList = ['养老保险金', '医疗保险金', '失业保险金', '工伤保险金', '生育保险金', '住房公积金', '个人所得税',
                '共计支出', '税后月薪', '扣除单位社保']
    payPercent = [[0.08, 0.18], [0.02, 0.08], [0.005, 0.005], [0.00, 0.006], [0.00, 0.012], [0.10, 0.10], [0.00, 0.00]]
    allCost = []
    for i in range(len(costList)):
        sal = Salary()
        sal.name = costList[i]
        if i < len(costList) - 3:
            if costList[i] != "住房公积金":
                sal.perPayment = float('%.2f' % float(social_security_base * payPercent[i][0]))
                sal.comPayment = float('%.2f' % float(social_security_base * payPercent[i][1]))
            else:
                sal.perPayment = float('%.2f' % float(provident_fund_base * payPercent[i][0]))
                sal.comPayment = float('%.2f' % float(provident_fund_base * payPercent[i][1]))
            allCost.append(sal)
            continue
        if i == len(costList) - 3:  # '共计支出'
            sumPerCost = 0
            sumComCost = 0
            for j in range(len(allCost)):
                sumPerCost += allCost[j].perPayment
                sumComCost += allCost[j].comPayment
            sal.perPayment = float('%.2f' % float(sumPerCost))
            sal.comPayment = float('%.2f' % float(sumComCost))
        elif i == len(costList) - 2:  # '税后月薪'
            sal.perPayment = float('%.2f' % float(perSalary - allCost[i - 1].perPayment))
            sal.comPayment = 0.00
        else:
            last = allCost[i - 1]
            lastTwo = allCost[i - 2]
            sal.perPayment = last.perPayment - lastTwo.comPayment
            sal.comPayment = 0.00
        allCost.append(sal)
    return allCost


# 字典转学生对象
def setDicToStudent(dic):
    stu = Student()
    stu.id = dic["id"]
    stu.name = dic["name"]
    stu.age = dic["age"]
    stu.sex = dic["sex"]
    stu.grade = dic["grade"]
    stu.phone_number = dic["phone_number"]
    stu.t_id = dic["t_id"]
    if "teacher" in dic.keys():
        stu.teacher = dic["teacher"]
    stu.bf_score = dic["bf_score"]
    stu.af_score = dic["af_score"]
    stu.school = dic["school"]
    stu.picture = dic["picture"]
    stu.comment = dic["comment"]
    return stu


# 字典转费用对象
def setDicToCost(dic):
    cost = Cost()
    cost.grade1 = dic["grade1"]
    cost.grade2 = dic["grade2"]
    cost.grade3 = dic["grade3"]
    cost.provident_fund_base = dic["provident_fund_base"]
    cost.social_security_base = dic["social_security_base"]
    return cost


# 字典转课程对象
def setDicToCourse(dic):
    cos = Course()
    cos.id = dic.get("id")
    cos.title = dic.get("title")
    cos.fk_tid = dic.get("fk_tid")
    cos.fk_sid = dic.get("fk_sid")
    cos.start_time = dic.get("start_time")
    cos.end_time = dic.get("end_time")
    cos.add_time = dic.get("add_time")
    cos.comment = dic.get("comment")
    if "tname" in dic.keys():
        cos.tname = dic["tname"]
    if "tname" in dic.keys():
        cos.sname = dic["sname"]
    return cos


# 字典转用户对象
def setDicToTeacher(dic):
    teacher = Teacher()
    teacher.id = dic["id"]
    teacher.sex = dic["sex"]
    teacher.name = dic["name"]
    teacher.pwd = dic["pwd"]
    teacher.picture = dic["picture"]
    teacher.phone = dic["phone"]
    teacher.address = dic["address"]
    teacher.birthday = dic["birthday"]
    teacher.signature = dic["signature"]
    teacher.update_time = dic["update_time"]
    teacher.privilege_level = dic["privilege_level"]
    teacher.grade = dic["grade"]
    return teacher


# 设置时间格式
def getDateTime(stamp):
    timeStamp = int(stamp)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime


# 获取初始状态的费用起始和结束时间
def getStartEndTime():
    time_t = time.localtime()
    if time_t.tm_mon != 1:
        start_time = "{}-{}-15".format(time_t.tm_year, (time_t.tm_mon - 1))
        end_time = "{}-{}-15".format(time_t.tm_year, time_t.tm_mon)
    else:
        start_time = "{}-12-15".format(time_t.tm_year - 1)
        end_time = "{}-{}-15".format(time_t.tm_year, time_t.tm_mon)
    return [start_time, end_time]

# 对象转换成json
def objectToJson(obj):
    return json.dumps(obj.__dict__, ensure_ascii=False, cls=DateEnconding)