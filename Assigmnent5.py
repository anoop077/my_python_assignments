'''
#Ques1
x=[input("Enter a num: ") for i in range(10)]

'''



'''
#Ques2
while True:
    print("An Infinite Loop never ends")

'''



'''
#Ques3
l=[ ]
n=int(input("Enter a num: "))
for i in range(n):
    m=int(input("Enter number for list: "))
    n=m*m
    l.append(n)
print("the square of the elements",l)
       

'''



'''
#Ques4
l=['a',2.3,1,'n',6.5,2,'o','o',3,'p',1.3]
m=[]
n=[]
o=[]
for x in range(0,len(l)):
    if type(l[x])==float:
        m.append(l[x])
    elif type(l[x])==int:
        n.append(l[x])
    else:
        o.append(l[x])
print("Float list",m,"\nInteger list",n,"\nString list",o)

'''



'''
#Ques5
a=[]
b=[]
for i in range(0,101):
    if i % 2==0:
        a.append(i)
    else:
        b.append(i)
print("Even numbers are: ",a,"\nOdd numbers are: ",b)


'''



'''
#Ques6
for x in range(5):
    print("*"*x)

'''



'''
#Ques7
n=[input("Enter the names: ") for i in range(5)]
m=[input("Enter the profession: ") for j in range(5)]
d={}
for i in n:
    for x in m:
        d[i]=x
print("Dictionary is: ",d)

'''



'''
#Ques8
l=[int(input("Enter the no of a list: ")) for i in range(10)]
n=int(input("Enter a num to be searched: "))
if n in l:
    l.remove(n)
    print("The list after removing the desired element: ",l)
else:
    print("Element not found.")
    

'''
