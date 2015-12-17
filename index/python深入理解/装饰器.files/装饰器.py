
def simple(*args):
    for arg in args:
        print(arg,end=" ")

def logit(func):
    def wrapper(*args, **kwargs):
        print("\n")
        print('function %s called with args %s' % (func, args),end="\n")
        func(*args, **kwargs)
    wrapper.__name__=func.__name__
    return wrapper

@logit
def simple2(*args):
    for arg in args:
        print(arg,end=" ")
        
simple(1,2,3,4)
simple=logit(simple)

simple(1,2,3,4)
simple2(1,2,3,4)
