#__str__
#触发时机：打印对象名，自动触发调用__str__里面的的内容
#注意：一定在这个方法里添加return，return后面就是打印对象看到的的内容

# class Person:
#     def __init__(self,name):
#         self.name = name
#
#
# p = Person('tonm')
# print(p)           #这样打印出来的只是一个地址


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：'+self.name+',年龄：'+str(self.age)+''

p = Person('tom',10)
print(p)

p1 = Person('jabjdj',12)
print(p1)

#单纯打印对象名称，结果是一个地址，地址对于开发者没有太大意义
#如果想在打印对象名的时候给开发者更多的信息量

"""
总结：魔术方法
重点：
   __init__(构造方法：创建完空间之后调用的第一个方法),
   __str__(打印对象使得开发者了解更多的信息)
"""
