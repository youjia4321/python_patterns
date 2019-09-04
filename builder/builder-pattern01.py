'''
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现

一个例子更能很好的理解以上的内容：
1. 有一个接口类，定义创建对象的方法。一个指挥员类，接受创造者对象为参数。两个创造者类，创建对象方法相同，内部创建可自定义
2.一个指挥员，两个创造者(瘦子 胖子)，指挥员可以指定由哪个创造者来创造
'''

from abc import ABCMeta, abstractmethod

class Builder():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Person(Builder):
    def __init__(self, name):
        self.name = name

    def draw_left_arm(self):
        print('画%s的左手' % self.name)

    def draw_right_arm(self):
        print('画%s的右手' % self.name)

    def draw_left_foot(self):
        print('画%s的左脚' % self.name)

    def draw_right_foot(self):
        print('画%s的右脚' % self.name)

    def draw_head(self):
        print('画%s的大头' % self.name)

    def draw_body(self):
        print('画%s的身体' % self.name)


class Director():
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()


if __name__=='__main__':
    person = Person("瘦子")
    _person = Person("胖子")
    director=Director(person)
    _director=Director(_person)
    director.draw()
    _director.draw()