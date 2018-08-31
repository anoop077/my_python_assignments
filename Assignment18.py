#Question1
'''
>>> import numpy as np
>>> a=np.random.random((10,1))
>>> np.mean(a)
0.5750048165497816

'''
#Question2
'''
>>> import numpy as np
>>> a=np.random.random((20,1))
>>> print(np.std(a))
0.250265332750936
>>> print(np.var(a))
0.0626327367769367

'''
#Question3
'''
>>> import numpy as np
>>> a=np.random.random((10,20))
>>> b=np.random.random((20,25))
>>> c=np.matmul(a,b)
>>> np.shape(c)
(10, 25)
>>> print(c.sum())
1226.8264103992237

'''
#Question4
'''
>>> import numpy as np
>>> A=np.arange(10).reshape(10,1)
>>> A
array([[0],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8],
       [9]])
>>> A.shape
(10, 1)

'''
