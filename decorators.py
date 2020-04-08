# @outer
# def greet():
#    pass

############################################################################################################
   
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

############################################################################################################