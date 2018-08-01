import numpy as np

a  = np.fromfunction(lambda x,y: x+y,(5,5),dtype='int32')
print(" a:\n{0}\n".format(a))

b = np.eye(6,6) + np.eye(6,6,k=1) + np.eye(6,6,k=-1)
b = b.astype(dtype='bool')
print(" b:\n{0}\n".format(b))
