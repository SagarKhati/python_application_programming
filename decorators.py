# @outer
# def greet():
#    pass

##############################################################################
   
#shows the creation of closure function wish using the higher order function outer.
def outer(func):
    def inner():
        print("Accessing :",func.__name__)
        return func()
    return inner
def greet():
   print('Hello!')
wish = outer(greet)
wish()


# shows the creation of decorator function outer, which is used to decorate function greet.
def outer(func):
   def inner():
        print("Accessing :",func.__name__)
        return func()
   return inner
def greet():
   return 'Hello!'
greet = outer(greet) # decorating 'greet'
greet()  # calling new 'greet'


# displays decorating the greet function with decorator function, outer, using @ symbol.
def outer(func):
    def inner():
        print("Accessing :", 
                func.__name__)
        return func()
    return inner
@outer
def greet():
    return 'Hello!'
greet()

##############################################################################


def log(func):
    def inner(msg):
        return "Accessed the function -'{}' with arguments ('{}',) {}".format(func.__name__, msg, '{}')
    return inner
@log
def greet(msg):
    'Greeting Message : ' + msg
res_lst = list()
res_lst.append(greet(str(input())))
print("{}".format(*res_lst))



def log(func):
    def inner(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
                                                                                args,                                                                                kwdargs)
        return str_template + "\n" + str(func(*args, **kwdargs))
    return inner
@log
def average(n1, n2, n3):
    return (n1+n2+n3)/3
res_lst = list()
(a,b,c) = (map(lambda x: float(x.strip()), input().split(',')))
res_lst.append(average(a,b,c))
print("{}".format(*res_lst))



def bold_tag(func):
    def inner(msg):
        return '<b>{}</b>'.format(msg)
    return inner
@bold_tag 
def say(msg):
    return msg
res_lst = list()
res_lst.append(say(input()))
print("{}".format(*res_lst))



def bold_tag(func):    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'        
    return inner
def italic_tag(func):
    def inner(msg):
        return '<i>'+msg+'</i>'
    return inner
@italic_tag
def say(msg):
    return msg
res_lst = list()
res_lst.append(say(input()))
print("{}".format(*res_lst))



def bold_tag(func):
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
    return inner
def italic_tag(func):
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
    return inner
def greet():
    return input()
greet = italic_tag(greet)
res_lst = list()
res_lst.append(greet())
print("{}".format(*res_lst))



def bold_tag(func):    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'        
    return inner
def italic_tag(func):    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'        
    return inner    
@italic_tag
@bold_tag
def greet():
    return input()
res_lst = list()
res_lst.append(greet())
print("{}".format(*res_lst))
        
        
        