'''
# 1.program number 

def subNumbers(x,y):
    return x-y
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("subtractiom of two numbers is:",subNumbers(a,b))





#2. program  to find first 10 prime numbers

def is_prime(n):
    x=2
    count=0
    while count<n:
        for i in range(2,int (x**.5)+1):
            if x%i==0:
                break
        else:
            print(x)
            count+=1
        x+=1
is_prime(10)         



#3. program to find the sum of first 10 prime numbers

def is_prime(n):
    x=2
    count=0
    sum=0
    while count<n:
        for i in range(2,int (x**.5)+1):
            if x%i==0:
                break
        else:
            sum+=x
            count+=1
        x+=1
    print("sum of first 10 prime numbers is:",sum)
is_prime(10)




#4. A function that takes another function as an argument
def fun(func,arg):
    return func(arg)
def square(x):
    return x**2
res=fun(square,5)
print(res)




# 5.A function that takes another function as an argument
def fun(func, arg):
    return func(arg)
  
def square(x):
    return  x ** 2
x=int(input("enter a number:"))  
# Calling fun and passing square function as an argument  
res = fun(square, x)
print(res)

'''

# 










