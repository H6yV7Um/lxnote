class Bird(object):
    num=30
    def mm(self):
        print("miao~~")
    
class Chicken(Bird):
    fly=False
    def __init__(self):
        self.age=20
        self.color="red"
    def isAdult(self):
        if self.age>2:
            return True
        else:
            return False
    adult=property(isAdult)
    
pp=Chicken()


bb=Bird()
AA=333
#bb.mm()
#pp.mm()

def xxx():
    "Lx haahha"
    a=333
    print("pppp")
    print(locals())
    print(globals())
if __name__=='__main__':
    print(hasattr(pp,'age'))
    print(hasattr(pp,'isAdult'))
    print(getattr(pp,'mm'))
    print(dir('__main__'))
    xxx()
