class Employee:
    empCount = 0

    def __init__(self, name, salary):
        """初始化函数"""
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("dict:{}".format(self.__dict__))

em1 = Employee('Jack', 23000)
em1.displayCount()
em2 = Employee('zoe', 12000)
em1.age = 20
em1.displayCount()
em2.displayEmployee()
em1.displayEmployee()

