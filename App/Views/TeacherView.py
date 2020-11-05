from flask import Blueprint, render_template, request, session, redirect, url_for
from App.DataBase.TeacherMapper import *
from App.Model.staticData import *

teacher = Blueprint("teacher", __name__)


# 用户信息验证及显示
@teacher.route('/info', methods=['GET', 'POST'])
def bkControl():
    if request.method == 'POST':
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        if isLoginRight(phone, pwd):
            user = getTeacherTeacherDataById(phone)
            session["phone"] = user.phone
            session["picture"] = user.picture
            return render_template('backBase.html', user=user)
        return render_template("register.html", allClass=getAllClasses())
    else:
        if session["nickname"]:
            user = getTeacherTeacherDataById(session["uid"])
            return render_template('backBase.html', user=user)


# 获取用户信息
@teacher.route("/getInfo/<int:phone>")
def getUserInfo(phone):
    return getTeacherTeacherDataById(phone)


# 修改用户信息
@teacher.route("/updateInfo", methods=["GET", "POST"])
def updateUserInfo():
    user = MJ.setDicToTeacher(request.json)
    return updateTeacherData(user)


# 修改用户密码
@teacher.route("/updatePwd", methods=["GET", "POST"])
def updateUserPasswd():
    uid = request.json.get("uid")
    pwd = request.json.get("pwd")
    return updateTeacherPwd(uid, pwd)

@teacher.route("delete/<int:id>")
def deleteUserInfo(id):
    return deleteTeacherData(id)

