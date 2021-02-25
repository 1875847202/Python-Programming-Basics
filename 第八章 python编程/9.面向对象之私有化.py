#私有化
#封装：1.私有化属性 2.定义共有的set和get方法（把属性和动作都封装到类中）
#__属性：就是将属性私有化，访问范围仅仅限于类中进行修改

"""
   通常是将对象属性私有化:可以提一些要求，加一些限制
   好处：
       1.隐藏属性不被外界修改
       2.也可以修改，通过函数完成
       def setXxx(self):
           筛选赋值内容
           if xxx是否符合条件：
               赋值
           else：
               不赋值
        3.如果想获取一个具体的某一个属性
          使用get函数
             def getXXX(self):
                 return self.__xxx

"""

class Student:
    __age = 59  #类属性

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__score = 59   #私有变量外界无法访问


    #定义公有的set与get
    #set为了赋值
    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('年龄不在正确的范围内')

    #get为了取值
    def getAge(self):
        return '年龄是：{}'.format(self.__age)

    def setName(self,name):
        if len(name) == 6:
            self.__name = name
        else:
            print('姓名不是6位')
    def getName(self):
        return '姓名是：{}'.format(self.__name)



    def __str__(self):
        return '姓名：{}，年龄：{}，成绩：{}'.format(self.__name,self.__age,self.__score)

lili = Student('lili',23)
lili.setAge(25)
lili.setName('yanggs')
print(lili.getName())
print(lili.getAge())
print(lili)


# feifei = Student('feifei',57)
# print(feifei)
