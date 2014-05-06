# -*- coding:utf8 -*-
def deco_functionNeedDoc(func):
    def _deco():
        if func.__doc__ == None :
            print func, "has no __doc__, it's a bad habit."
        else:
            print func, ':', func.__doc__, '.'
            
            
        ret = func()
        print "after called"
        return ret
    return _deco

@deco_functionNeedDoc
def f():
    print 'f() Do something'
    return "f"

@deco_functionNeedDoc
def g():
    'I have a __doc__'
    print 'g() Do something'
    return "g"

    
if __name__=="__main__":
    a = f()
    print "a:",repr(a)
    # g()