"""
静态方法：
    1.与类方法的区分在于装饰器名称不一样，没有cls简写
    2.类中的静态方法不必传递参数（cls，self）
    3.也只能访问类的属性和方法，不能访问对象的属性和方法
    4.加载时机同类方法

总结：
    类方法 静态方法
不同：
    1.装饰器不同
    2.类方法是有参数的，静态方法不没有参数

相同：
    1.只能访问类属性和方法，对象时无法访问的
    2.都可以通过类名调用访问
    3.都可以在没有对象之前使用，因为不依赖于对象

普通方法于两者的区别：
不同：
    1.没有装饰器
    2.依赖于对象，因为每个普通方法都有一个self
    3.self表示对象本身
    4。只有创建了对象才可以调用普通方法，否则无法使用

"""
class Person:
    #类属性
    __age = 18  #成为私有，外界无法访问

    def __init__(self,name):
        self.name = name

    def show(self):
        print('-------->')

    @classmethod
    def updata_age(cls):
        cls.__age = 20  #使用类方法修改私有化类属性
        print('----------类方法')

    @classmethod
    def show_age(cls):       #使用类方法来查看类属性是否修改成功
        print('-------->更新后的age：',cls.__age)

    @staticmethod
    def test():
        print('---------->静态方法')
        #print(self.name)  语法错误，因为根本静态方法中self参数
        print(Person.__age)


Person.updata_age()   #访问类方法
Person.show_age()     #访问类方法

#静态方法调用
Person.test()
