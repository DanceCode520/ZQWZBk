classes = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
grades = ["七", "八", "九"]

def getAllClasses():
    allClasses = []
    for i in grades:
        for j in classes:
            myclass = i + "年" + j + "班"
            allClasses.append(myclass)
    return allClasses
