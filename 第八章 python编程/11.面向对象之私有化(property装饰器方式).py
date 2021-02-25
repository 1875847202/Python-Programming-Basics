#在开发中看到的一些私有化处理：装饰器
class Students:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    #私有化之装饰器:先有getxxx
    @property   #加了装饰器可以像访问属性一样访问
    def age(self):
        return self.__age
    #再有set，因为set依赖于get
    @age.setter
    def age(self,age):
        if age > 0 and age < 100:

             self.__age = age
        else:
             print('不在规定范围内')


    # def setAge(self,age):
    #     if age > 0 and age < 100:
    #         self.__age = age
    #     else:
    #         print('错误')
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name,self.__age)

s = Students('peng',12)
s.name = 'lili'
s.age = 400
print(s.age)
print(s.__dir__())
print(s)

# 私有化赋值
# s.setAge(30)
# print(s.getAge())
