#类中方法：魔术方法

#init方法：让对象属性达到统一

class Phone():

    #魔术方法之一： __名字__()
    def __init__(self):  #init初始化,模板的统一化，使得两个对象都有相同的属性
        self.brand = 'xiaomi'  #self表示当前创建的对象的地址（动态地给self空间中添加了两个属性）
        self.price = 4999

    def call(self):                 #self是不断发生变化的
        print('---------->call')
        print('价格：',self.price)   #不能保证每个self中都存在price

p = Phone()
p.call()

p1 = Phone()
p1.call()
"""
    1.找有没有一块空间是Phone
    2.利用Phone类，向内存申请一块Phone一样的空间。
    3.去Phone中找有没有__init__，如果没有则执行将
      开辟内存给对象名p
    4.如果有__init__，则会进入init方法执行里面的动作 
      接下来将申请的内存地址赋值给对象p
"""

# p.price = 1000
# p.call()    #p.call()  p对象
#
# p1 = Phone()
# p1.call()
