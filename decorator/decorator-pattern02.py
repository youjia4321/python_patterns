def dec_out():
    print("运行了dec_out")
    def dec_in(fn):
        print("运行了dec_in")
        return fn
    return dec_in

@dec_out()
def my_fn(a):
    return "函数返回值为"+str(a)

print(my_fn('123'))