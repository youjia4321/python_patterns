class B(object):
    instant = None
    flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instant is None:
            cls.instant = object.__new__(cls)
            # cls.instant = super().__new__(cls)
        return cls.instant

    def __init__(self):
        if not B.flag:
            return
        self.name = '张三'
        B.flag = False
        print('B已经被初始化了')

d = B()
print('d对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(d), id(B)))
e = B()
print('e对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(e), id(B)))
f = B()
print('f对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(f), id(B)))
