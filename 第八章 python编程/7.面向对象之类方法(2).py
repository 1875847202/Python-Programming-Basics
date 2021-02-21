#补充类方法：仅仅能操作类，不依赖于对象

class Person:
    #类属性
    __age = 18  #成为私有，外界无法访问

    def show(self):
        print('-------->')

    @classmethod
    def updata_age(cls):
        cls.__age = 20  #使用类方法修改私有化类属性
        print('----------类方法')

    @classmethod
    def show_age(cls):       #使用类方法来查看类属性是否修改成功
        print('-------->更新后的age：',cls.__age)

Person.updata_age()   #访问类方法
Person.show_age()     #访问类方法
