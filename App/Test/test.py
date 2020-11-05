from App.DataBase.TeacherMapper import *
from App.Model.models import *
from App.Model.staticData import *

tch = Teacher()
# tch.id = 7
tch.name = "李晓明"
tch.pwd = "new888"
tch.birthday = "2020-05-23"
tch.sex = 1
tch.nation = "汉族new"
tch.address = "new扎旗一中阿尔泰3楼"
tch.update_time = "2018-02-22 08:08:08"
tch.phone = "new123"
tch.picture = "new1.jpg"
tch.grade = "new九年二班&&&七年五班&&&八年六班"
tch.signature = "new我很喜欢学生"

res=Response()
data = [11, 44, 454, 455]
res.suceess(200,"messssg")
