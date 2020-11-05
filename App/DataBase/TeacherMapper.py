import pymysql
import json, App.Model.MJack as MJ
from App.Model.models import *
import datetime


class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d %H:%M:%S')


# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="michael88", database="zqwz")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


# 用户表信息修改
# 查询用户信息
def getTeacherTeacherDataById(phone):
    db.ping(reconnect=True)
    sql = "select * from teacher where phone={} and isdel={}".format(phone, 0)
    res = Response()
    try:
        cursor.execute(sql)
        res.successWithData(200, "success", cursor.fetchone())
    except:
        res.suceess(500, "error")
    return MJ.objectToJson(res)


# 查询用户信息
def getTeacherDataByIdJson(id):
    db.ping(reconnect=True)
    sql = "select * from teacher where id={}".format(id)
    res = Response()
    try:
        cursor.execute(sql)
        res.successWithData(200, "success", cursor.fetchone())
    except:
        res.suceess(500, "error")
    return MJ.objectToJson(res)


# 验证用户登录信息
def isLoginRight(phone, password):
    db.ping(reconnect=True)
    sql = "select count(id) from teacher where phone={} and pwd='{}'".format(phone, password)
    res = Response()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result['count(id)']:
            success = True
            res.suceess(200, "success")
    except:
        res.suceess(500, "success")
    return MJ.objectToJson(res)


# 更新用户信息
def updateTeacherData(tch):
    db.ping(reconnect=True)
    sql = "update teacher set name ='{}',pwd ='{}',birthday = '{}',sex ={}" \
          ",address ='{}',nation = '{}',update_time ='{}',signature = '{}'" \
          ",privilege_level={},phone='{}',picture='{}',grade='{}' where id={}".format(
        tch.name, tch.pwd, tch.birthday, tch.sex, tch.address, tch.nation, tch.update_time, tch.signature,
        tch.privilege_level, tch.phone, tch.picture, tch.grade, tch.id)
    res = Response()
    try:
        cursor.execute(sql)
        db.commit()
        res.suceess(200, "success")
    except:
        res.suceess(500, "success")
    return MJ.objectToJson(res)


# 修改用户密码
def updateTeacherPwd(phone, pwd):
    db.ping(reconnect=True)
    sql = "update teacher set pwd='{}' where phone={}".format(pwd, phone)
    res = Response()
    try:
        cursor.execute(sql)
        db.commit()
        res.suceess(200, "success")
    except:
        res.suceess(500, "success")
    return MJ.objectToJson(res)


# 增加用户信息
def insertTeacherData(tch):
    db.ping(reconnect=True)
    sql = "insert into teacher(name,pwd,birthday,sex,signature,address,update_time," \
          "privilege_level,phone,picture,grade,nation) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        tch.name, tch.pwd, tch.birthday, tch.sex, tch.signature, tch.address, tch.update_time,
        tch.privilege_level, tch.phone, tch.picture, tch.grade, tch.nation)
    res = Response()
    try:
        cursor.execute(sql)
        db.commit()
        res.suceess(200, "success")
    except:
        res.suceess(500, "success")
    return MJ.objectToJson(res)


# 删除教师信息
def deleteTeacherData(tid):
    db.ping(reconnect=True)
    sql = "update teacher set isdel={} where id={}".format(1, tid)
    res = Response()
    try:
        cursor.execute(sql)
        db.commit()
        res.suceess(200, "success")
    except:
        res.suceess(500, "success")
    return MJ.objectToJson(res)
