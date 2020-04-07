# Function as a Data

def greet():
    return 'Hello Everyone!'
print(greet())
wish = greet        # 'greet' function assigned to variable 'wish'
print(type(wish))   
print(wish())


##########################################################################################################


# Function as an Argument

def add(x, y):
    return x + y
def sub(x, y):
   return x - y
def prod(x, y):
    return x * y
def do(func, x, y):
   return func(x, y)
print(do(add, 12, 4))  # 'add' as arg
print(do(sub, 12, 4))  # 'sub' as arg
print(do(prod, 12, 4))  # 'prod' as arg


#########################################################################################################


# Returning a Function

def outer():
    def inner():
        s = 'Hello world!'
        return s                    
    return inner()    
print(outer())


#########################################################################################################


def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner   # Removed '()' to return 'inner' function itself    
print(outer()) #returns 'inner' function
func = outer() 
print(type(func))
print(func()) # calling 'inner' function


#########################################################################################################


# Closures

def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple
c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))


#########################################################################################################


#Write detecter implementation
def detecter(element):
    #Write isIn implementation    
    def isIn(sequence):
        if element in sequence:
            return True
        else:
            return False
    return isIn
#Write closure function implementation for detect30 and detect45
detect30 = detecter(30)
detect45 = detecter(45)

func_lst = [detect30, detect45]
res_lst = list()
lst = list(map(lambda x: int(x.strip()), input().split(',')))
for func in func_lst:
    res_lst.append(func(lst))
print("{}\n{}".format(*res_lst))
        
        
##########################################################################################################        

        
# Add the factory function implementation here
def factory(n = 0):
    def current():
        return n
    def counter():
        return n+1
    return current, counter

f_current, f_counter = factory(int(input()))

func_lst = [f_current, f_counter]
res_lst = list()
for func in func_lst:
    res_lst.append(func())
print("{}\n{}".format(*res_lst))        

