# TokenIssuer is a coroutine function, which uses yield to accept name as input.
def TokenIssuer():
    tokenId = 0
    while True:
        name = yield
        tokenId += 1
        print('Token number of', name, ':', tokenId)
t = TokenIssuer()
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
# Execution of coroutine function begins only when next is called on coroutine t.
# This results in the execution of all the statements till a yield statement is encountered.
# Further execution of function resumes when an input is passed using send, and processes all statements till next yield statement.




def TokenIssuer(tokenId=0):
    try:
       while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()
# the coroutine function TokenIssuer takes an argument, which is used to set a starting number for tokens.
# When coroutine t is closed, statements under GeneratorExit block are executed.




# As seen in Example1 and Example2, passing input to coroutine is possible only after the first next function call.
# Many programmers may forget to do so, which results in error.
# Such a scenario can be avoided using a decorator as shown in Example 3.
def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
@coroutine_decorator
def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()
# coroutine_decorator takes care of calling next on the created coroutine t.





def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, 3.0*x^2 + 4.0, with x being {} equals {}".format(x, a*(x**2)+b))

a = float(input())
b = float(input())
equation1 = linear_equation(a, b)
next(equation1)
equation1.send(6)
    



def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper

@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, 3.0*x^2 + 4.0, with x being {} equals {}".format(x, a*(x**2)+b))

a = float(input())
b = float(input())
equation1 = linear_equation(a, b)
equation1.send(6)





def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, {}*x^2 + {}, with x being {} equals {}".format(a, b, x, a*(x**2)+b))

@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)

def main(x):
    n = numberParser()
    n.send(x)
    
x = float(input())
res = main(x);
    


    
    








