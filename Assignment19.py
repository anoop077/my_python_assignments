#Question1
'''
import pandas as pd
d1={'Name':['shubham'],'eamil':["shubhamguleria20@gmail.com"],'age':[23]}
d2={'Name':['abhinab'],'eamil':["abhinabthakur@gmail.com"],'age':[43]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)


f=pd.concat([df1,df2])
print(f)
'''
#Question2
'''
import numpy as np
import pandas as pd
f=pd.read_csv("C:\\Users\\Anup\Desktop\\weather.csv",index_col=0)
print(f.head(5))
a=f.head(10)
print(np.mean(a))
print(np.median(a))
b=f.tail(5)
g=b.MinTemp
print(np.mean(g))
print(np.median(g))
'''
