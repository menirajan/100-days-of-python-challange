
# usual  parameters 
def fun(x):
     return x*2
call = fun(5)
print(call)


#optional parameters
def fun2(x=3): # here variable with value defined value is optional parameters
    return x**5
call2 = fun2() # no need to pass value from here , if we pass value from here it will use this value as the primary value.
print(call2)

# example 1
def name (name, times=5):
    print(name*times)

name('nirajan ')
