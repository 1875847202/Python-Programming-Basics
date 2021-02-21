class Person():
    name = '张三'

    def __init__(self,name1,age1):
        self.name = name1
        self.age = age1

    def eat(self):
        print('{} 正在吃红烧肉！'.format(self.name))
        print('今年{}岁'.format(self.age))

    def run(self):
        print('{},今年{}岁'.format(self.name,self.age))

p = Person('lisi',20)
p.eat()
p.run()

print(60*'--')


p1 = Person('zhaoliu',34)
p1.eat()
"""
访问原则：先找模型内部，然后找对象自己

"""
