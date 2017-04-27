#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX
import pickle

class Teacher():
    def __init__(self,name,age,favor,asset=0):
        self.name = name
        self.age = age
        self.favor = favor
        self.asset = 0

    def gain(self,fee):
        self.asset += fee
        print('老师课时费:\t%.2f' % self.asset)
    def accident(self,fee):
        self.asset -= fee
        print('课时费:\t%.2f' % self.asset)
class Courses:
    def __init__(self,courses,fee,teacher):
        self.courses = courses
        self.fee = fee
        self.teacher = teacher
        self.teach_dict = pickle.load(open('teacher.txt', 'rb'))
    def study(self):
        #self.stu = stu
        self.teacher.gain(self.fee)
        self.teach_dict[self.teacher.name].asset = self.teacher.asset
        pickle.dump(self.teach_dict,open('teacher.txt','wb'))
        print('好好学习，天天向上')
        #print(self.stu)

class Student:
    def __init__(self):
        self.course = Courses
        #self.name = name
        self.cour_dict = pickle.load(open('course.txt', 'rb'))
        self.stu_cour = pickle.load(open('student.txt', 'rb'))
    def select_course(self):
        while True:
            print(''.center(100,'-')+'\n这学期已经选择的课程:')
            for item in self.stu_cour:
                print(item)
            print('\n这学期的课程:')
            for item in self.cour_dict:
                print(item)
            opt = input('exit 退出\n请选择需要学习的课程:')
            if 'exit' in opt:
                print(''.center(100,'*')+'\n退出选课')
                return
            elif self.stu_cour.get(opt.strip()):
                print('此课程已经被选')
                continue
            elif not self.cour_dict.get(opt.strip()) or opt == '':
                print('输入错误\n')
                continue
            else:
                self.stu_cour[opt.strip()] = {opt.strip():self.cour_dict[opt.strip()],'score':0}
                # print(self.stu_cour)
                pickle.dump(self.stu_cour, open('student.txt', 'wb'))
    def del_course(self):
        while True:
            print(''.center(100,'=')+'\n这学期已经选择的课程:')
            for item in self.stu_cour:
                print(item)
            opt = input('exit 退出\n请选择需要删除的课程:')
            if 'exit' in opt or opt == '':
                print(''.center(100,'+')+'\n退出课程删除')
                return
            elif self.stu_cour.get(opt.strip()):
                self.stu_cour.pop(opt.strip())
                pickle.dump(self.stu_cour, open('student.txt', 'wb'))
                continue
            else:
                print('输入错误')
    def get_lesson(self):
        while True:
            print(''.center(100, '=') + '\n这学期已经选择的课程:')
            for item in self.stu_cour:
                print(item)
            opt = input('exit 退出\n请选择需要上的课程:')
            if 'exit' in opt or opt == '':
                print(''.center(100, '+') + '\n退出上课')
                return
            elif self.stu_cour.get(opt.strip()):
                self.stu_cour[opt.strip()]['score'] += 10
                print(self.stu_cour[opt.strip()]['score'])
                self.stu_cour[opt.strip()][opt.strip()].study()
                pickle.dump(self.stu_cour, open('student.txt', 'wb'))
                continue
            else:
                print('输入错误')



def Create_teacher():
    while True:
        name = input("Teacher's name:")
        age = input("Teacher's age:")
        favor = input("Teacher's favor:")
        ack = input('exit:退出\n确认添加:\tY/N:')
        if ack.strip() == 'Y':
            t = Teacher(name,age,favor)
            teach_dict = pickle.load(open('teacher.txt','rb'))
            teach_dict[name] = t
            pickle.dump(teach_dict,open('teacher.txt','wb'))
        elif ack.strip() == 'exit':
            return

def Create_course():
    while True:
        course = input('course name:')
        fee = int(input('fee:'))
        teacher = input('teacher:')
        ack = input('exit:退出\n确认添加:\tY/N:')
        if ack.strip() == 'Y':
            tech_dict = pickle.load(open('teacher.txt', 'rb'))
            if tech_dict.get(teacher.strip(),False):
                courses = Courses(course,fee,tech_dict[teacher.strip()])
                cour_dict = pickle.load(open('course.txt','rb'))
                cour_dict[course] = courses
                pickle.dump(cour_dict,open('course.txt','wb'))
            elif ack.strip() == 'exit':
                return



def admin():
    admin_list = [('创建老师',Create_teacher),( '创建课程',Create_course)]
    while True:
        print('管理员入口'.center(50, '+'))
        for num, item in enumerate(admin_list, 1):
            print(num, item[0])
        opt = input('请选择 or 0 退出:')
        opt = int(opt.strip())
        if opt == 0:
            return
        elif opt <= len(admin_list) and opt > 0:
            opt -= 1
            admin_list[opt][1]()
        else:
            print('输入有误')

def student():
    stu = Student()
    stud_list = [('选课',stu.select_course),('上课',stu.get_lesson),('删课',stu.del_course)]
    while True:
        print('选课系统'.center(50, '*'))
        for num, item in enumerate(stud_list, 1):
            print(num, item[0])
        opt = input('请选择 or 0 退出:')
        opt = int(opt.strip())
        if opt == 0:
            return
        elif opt <= len(stud_list) and opt > 0:
            opt -= 1
            stud_list[opt][1]()
        else:
            print('输入有误')

def main():
    main_list = [('管理员入口',admin),('学生入口',student)]
    while True:
        print('选课系统'.center(50,'*'))
        for num,item in enumerate(main_list,1):
            print(num,item[0])
        opt = input('请选择 or 0 退出:')
        opt = int(opt.strip())
        if opt == 0:
            return
        elif opt <= len(main_list) and opt > 0 :
            opt -= 1
            main_list[opt][1]()
        else:
            print('输入有误')


if __name__ == '__main__':
    main()