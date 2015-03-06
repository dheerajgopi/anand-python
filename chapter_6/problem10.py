import time

def fib(n):
   if n is 0 or n is 1:
      return 1
   else:
      return fib(n-1)+fib(n-2)

def profile(fun):
   def g(x):
      t=0
      start=time.time()
      v=fun(x)
      t=time.time()-start
      return str(t)+'  seconds'
   return g

a = profile(fib)
print a(7)
