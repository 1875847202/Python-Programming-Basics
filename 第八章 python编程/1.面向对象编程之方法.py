#类中方法:动作
#种类:普通方法 类方法 静态方法 魔术方法

"""
类的本质是一个模型
而对象则是对模型的一个复制

"""

"""
普通方法格式：
def 方法名(self,参数1，参数2，。。。。)：
     pass


"""

class Phone():
    brand = 'Huawei'
    price = 4999
    type  = 'mate 30'

    #Phone里面的普通方法：call
    def call(self):           #self是把创建出来的对象P1传入(self代表对象)，self是不断发生改变的
        print('self....',self)
        print('正在访问通讯录。。。')
        for person in self.address_book:
            print(person.items())
        print('正在打电话。。。')
        print('留言：',self.note)



#创建对象
p1 = Phone()
#添加属性
p1.note = 'zhangsan 18999778'
p1.address_book = [{'123':'lisai'},{'124':'liuyang'},{'125':'yangfeifei'}]
print(p1,'------1------')
print(p1.brand)
p1.call()   #call(p1)  ---> self.note

print(80*'-')

p2 = Phone()
p2.note = 'lisi 18999898'
print(p2,'------2------')
print(p2.brand)
p2.call()  #call(p1)  ---> self.note       #p2中没有address_book属性，因此会报错


""""
注意：
   当p2对象中没有address_book属性时会报错
   当p1和p2对象都有同一个属性时才正确
"""
