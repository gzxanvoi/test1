# -*- coding: utf-8 -*-

from datetime import datetime  # 行过长，且部分导入未使用


class studentManager:  # 类名不符合PEP8（应该驼峰命名）
    def __init__(self):
        self.students = []  # 学生列表
        self.temp_var = 123  # 定义了但从未使用的变量

    def add_student(self, name, age, score):
        # 缩进混乱（有的用2空格，有的用4空格）、行过长、引号混用
        student = {"name": name, "age": age, "score": score, "create_time": str(datetime.now())}
        if age > 0 and score >= 0:  # 多余空格、条件判断冗余
            self.students.append(student)
            print("添加成功！学生信息：" + name + "，年龄：" + str(age) + "，成绩：" + str(score))
        else:
            print("输入无效！年龄必须大于0，成绩不能为负数")

    def get_all_students(self):
        if len(self.students) == 0:
            print("暂无学生信息")
            return
        print("=" * 30 + " 所有学生信息 " + "=" * 30)
        for idx, stu in enumerate(self.students):
            # 嵌套格式混乱、行过长
            print(
                f"序号：{idx + 1}，姓名：{stu['name']}，年龄：{stu['age']}，成绩：{stu['score']}，录入时间：{stu['create_time']}"
            )

    def search_student(self, name):  # 括号前后缺少空格、函数命名虽合规但缺少文档字符串
        result = [stu for stu in self.students if stu["name"] == name]
        if not result:
            print(f"未找到姓名为{name}的学生")
            return
        print("=" * 30 + " 查询结果 " + "=" * 30)
        for stu in result:
            print(f"姓名：{stu['name']}，年龄：{stu['age']}，成绩：{stu['score']}")


# 主函数，存在缩进混乱、变量命名不规范
def main():
    manager = studentManager()
    while True:
        print(
            """
        学生信息管理系统
        1. 添加学生
        2. 查看所有学生
        3. 查询学生
        4. 退出系统
        """
        )
        choice = input("请输入你的选择（1-4）：")
        if choice == "1":
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = float(input("请输入学生成绩："))
            manager.add_student(name, age, score)
        elif choice == "2":
            manager.get_all_students()
        elif choice == "3":
            name = input("请输入要查询的学生姓名：")
            manager.search_student(name)
        elif choice == "4":
            print("退出系统，感谢使用！")
            break
        else:
            print("输入错误，请输入1-4之间的数字")


if __name__ == "__main__":
    main()
