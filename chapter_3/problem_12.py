import inspect

def mypydoc():
    mod = __import__('os')
    dir_list = dir(mod)
    print '\n-----FUNCTIONS-----\n'
    
    for item in dir_list:
        fun = getattr(mod, str(item)) # 'getattr' returns a 'item' function object in module 'mod'

        if inspect.isfunction(fun): # checks if the function object is actually a function(C-functions cant be detected)
            print item

print mypydoc()
