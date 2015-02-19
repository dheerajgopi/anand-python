import inspect

def mypydoc():
    mod = __import__('math')
    dir_list = dir(mod)
    print '\n-----FUNCTIONS-----\n'
    
    for item in dir_list:
        print item

mypydoc()
