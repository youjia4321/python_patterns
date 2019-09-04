'''
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，
很实用，能大大降低耗时，提高性能，因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
'''

import copy
from collections import OrderedDict

class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register(self, identifier, obj):
        """Register an object"""
        self._objects[identifier] = obj

    def unregister(self, identifier):
        """Unregister an object"""
        del self._objects[identifier]

    def clone(self, identifier, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        found = self._objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attrs)
        return obj


class Person(object):
    def __init__(self, **info):
        self.__dict__.update(info)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


def main():
    student1 = Person(姓名='dkc', 年龄=24, 性别='male', 婚姻状况='否', 电话='086-123127374')
    prototype = Prototype()
    cid = 'k1&student'
    prototype.register(cid, student1)
    student2 = prototype.clone(cid, 是否优秀学生="yes", edtion=2)
    for i in (student1, student2):
        print(i)
    
    print("ID b1 : {} != ID b2 : {}".format(id(student1), id(student2)))

if __name__ == '__main__':
    main()
