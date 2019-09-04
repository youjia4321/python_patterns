def user_info(func):
    def wapper(self, *args, **kwargs):
        print("显示用户信息:")
        user = func(self, *args, **kwargs)
        return user
    return wapper


class Person(object):
    _objects = {}

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @user_info
    def get_info(self):
        self._objects['姓名'] = self.name
        self._objects['年龄'] = self.age
        self._objects['性别'] = self.sex
        return self._objects
    
    def __str__(self):
        self._objects['姓名'] = self.name
        self._objects['年龄'] = self.age
        self._objects['性别'] = self.sex
        return str(self._objects)

if __name__ == "__main__":
    user = Person("youjia", "12", "male")
    print(user)
    print("#"*60)
    print(user.get_info())