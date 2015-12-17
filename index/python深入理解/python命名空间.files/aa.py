g=123

def out():
    print("out:")
    e=12
    g=10
    def aaa():
        def intFun():
            loc=333
            nonlocal e
            e+=4
            return e,loc
        return intFun()
    return aaa()

if __name__=="__main__":
    
    print(out())
    

