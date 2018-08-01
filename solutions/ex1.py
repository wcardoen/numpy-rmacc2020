import numpy as np
# Exercise 1.a.::
print("Exercise 1.a::")
ex = [i for i in range(1,11)]
lst = [2**i for i in ex]
print("1D array:\n{0}\n".format(np.array(lst)))

# Exercise 1.b::
print("Exercise 1.b::")
start = 2.
end   = 3.
npoints = 5 
dx= (end - start)/float(npoints-1)

pt = [ start+i*dx for i in range(npoints)]
lst = [10**item for item in pt]
print("{0}".format(np.array(lst)))
print("{0}\n".format(np.logspace(start,end,npoints)))

# Exercise 1.c::
print("Exercise 1.c::")
lst= range(30,0,-1)
print("{0}\n".format(np.array(lst).reshape((5,6))))
