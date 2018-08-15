'''
#Ques1
def area():
    PI=3.14
    r=float(input("Enter the radius: "))
    area=PI*r*r
    print("Area of the circle is: ",area)
    

'''


'''
#Ques2
def perfect(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum=sum+x
        return sum==n
#Incomplete....!!
#Incorrect....!!

'''


'''
#Ques3
def table(n, t=1):
    if t==11:
        return
    print(str(12)+"*"+str(t)+"="+str(n*t))
    table(n, t+1)
    

'''


'''
#Ques4
def power(b,e):
    if(e==1):
        return(b)
    elif(e!=1):
        return(b*power(b,e-1))
'''


'''
#Ques5
def fact(n):
    d=dict()
    d={"Factorials stored in a dictionary {}".format(n)}
    print(d)
    if(n<=1):
        return 1
    else:
        return(n*fact(n-1))

'''
