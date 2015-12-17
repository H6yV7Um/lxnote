def pp():
    n=3
    def nnn(num):
        return num**n
    return nnn

f=pp()
del pp

def mmm():
    print(123)

f2=mmm

print("-----------------闭包函数:")
print(f.__closure__)
print(type(f.__closure__[0]))
print(f.__closure__[0].cell_contents)
print("-----------------普通函数:")
print(f2.__closure__)

