#类方法（不依赖于对象，可以独立出对象）
"""
特点：
   1.定义需要依赖装饰器@classmethond
   2.类方法中参数不是一个对象，而是一个类
     print(cls)  #<class '__main__.Dog'>
   3.类方法中只可以使用类属性
   4.类方法不依赖于对象，在对象没有出现之前就可以使用
   5.类方法中可否使用普通方法？
     不可以，因为普通方法的调用依赖于对象，但是类方法先于对象产生

作用：
     因为只能访问类属性和类方法，所有可以在对象创建之前，如果需要一些功能，
     因此可以使用类方法中


"""

class Dog:
    #nickname = 'lili'
    aa = 'lili'

    def __init__(self,nickname):
        self.nickname = nickname

    def run(self): #依赖于对象self存在:只有对象才能调用
        print('{}在院子跑来跑去'.format(self.nickname))

    def eat(self):
        print('玩耍')
        self.run()   #类中方法的调用，通过self.方法名()

    @classmethod
    def test(cls):   #依赖于类存在，没有对象也可以调用
        print('--------->')
        print(cls)   #<class '__main__.Dog'>
        #print(cls.nickname)    #报错
        #print(self.nickname)   #报错

d = Dog('大黄')

d.run()    #调用对象方法run

d.test()    #没有属性test

d.test()

d.eat()
