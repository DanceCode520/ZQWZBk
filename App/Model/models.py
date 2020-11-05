# 学生类
class Student:
    id = 0  # 学生id
    name = ''  # 学生姓名
    age = 0  # 学生年龄
    sex = 0  # 学生性别：0女 1男
    grade = 1  # 学生年级
    t_id = 1  # 学生班任id
    teacher = ""  # 学生班任姓名
    bf_score = 0  # 补课前成绩
    af_score = 0  # 补课后成绩
    school = ''  # 所在学校
    picture = ''  # 学生照片
    phone_number = ''  # 学生电话
    comment = ''  # 备注信息


# 课程类
class Course:
    id = 0  # 课程id
    title = ''  # 课程名称
    start_time = ''  # 开始时间
    end_time = ''  # 结束时间
    add_time = ''  # 添加时间
    fk_tid = 1  # 教师id
    fk_sid = 1  # 学生id
    tname = ""  # 教师姓名
    sname = ""  # 学生姓名
    comment = ''  # 课程备注


# 薪水类
class Salary:
    name = ''  # 费用名称
    perPayment = 0  # 个人缴纳数目
    comPayment = 0  # 公司缴纳数目


# 费用类
class Cost:
    grade1 = 80  # 高一费用
    grade2 = 80  # 高二费用
    grade3 = 80  # 高三费用
    provident_fund_base = 8000  # 公积金缴纳基数
    social_security_base = 8000  # 社保缴纳基数


# 教师类
class Teacher:
    id = 1  # id
    name = ""  # 姓名
    pwd = ""  # 登录密码
    birthday = ""  # 生日
    sex = 0  # 性别
    address = ""  # 住址
    nation = ""  # 民族
    update_time = ""  # 上次更新时间
    signature = ""  # 个性签名
    privilege_level = 1  # 用户权限等级
    phone = ""  # 手机号码
    picture = ""  # 用户图片
    grade = ""  # 教师所教年级


# 上传文件类
class File:
    id = 1  # 文件id
    name = ""  # 文件名称
    size = "0M"  # 文件大小
    create_time = ""  # 创建时间
    id_del = 0  # 是否删除
    t_id = 1  # 教师id
    subject = "数学"  # 所属科目


# 返回信息类
class Response:
    code = 200
    message = "success"
    data = []

    def successWithData(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def suceess(self, code, message):
        self.code = code
        self.message = message
