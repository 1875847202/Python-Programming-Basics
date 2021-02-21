#猫类

class Cat:
    type = '猫'

    #通过魔术方法初始化
    def __init__(self,nickname,age,color):
        self.nickname = nickname
        self.age = age
        self.color = color

    #动作：方法
    def eat(self,food):
        print('{}喜欢吃{}'.format(self.nickname,food))

    def catch_mouse(self,color,weight):
        print('{},抓了一只{}kg的，{}的大老鼠！'.format(self.nickname,weight,color))

    def sleep(self,hour):
        if hour < 5:
            print('乖乖！继续睡会吧！')
        else:
            print('赶快起床出去抓老鼠')

    def show(self):
        print('猫的信息：')
        print(self.nickname,self.age,self.color)


#创建对象
cat1 = Cat('花花',2,'灰色')

#通过对象调用方法
cat1.catch_mouse('白色',0.02)

cat1.sleep(8)

cat1.eat('小金鱼')

cat1.show()
