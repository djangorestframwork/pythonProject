'''
def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m
for i in (identity(5)):
    pass

import numpy as np
n=np.identity(3)
for i in n:
    print(i)

n=4
identity = [[0]*i + [1] + [0]*(n-i-1) for i in range(n) ]

s=[]
l=[1,2,3,4,5,6,7,8,9]
l2=sorted(l,reverse=True)
a=0
while a<len(l2):
    for i in l2:
        if i is min(l2):
            s.append(i)
            l2.remove(i)
        elif i is max(l2):
            s.append(i)
            l2.remove(i)

print(s)
d=""
k=""
s='y'
while s=='y':
    a=input("enter any character:")
    b=int(input("how many times:"))
    d=d+(a*b)
    k=k+(a+str(b))

    s=input("Enter one more character?y/n:")

print("The given input is:",k)
print("The given output is:",d) '''

'''
v=[8, 2, 3, 12, 16]
a=[]
for i in v:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1

    a.append(c)
    print(a)

c=sorted(list(zip(a,v)),reverse=True)
print(c)
for i,j in c:

    print(j,end=' ') '''
'''
num=input("enter an odd length:")
l=len(num)
for i in range(l):
    for j in range(l):
        if i==j or i+j==l-1:
            print(num[j],end=" ")
        else:
            print(" ",end=" ")
    print() 

word=input("enter the word:")
s=""
for i in word:
    s=i+s
if s==word:
    print("It is a polindrome")
else:
    print("It is not a polindrome") '''

'''
lower=int(input("Enter the starting value:"))
higher=int(input("Enter the ending value:"))

for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num) '''


#
'''
def long(A):
    s=""
    for i in range(len(A)):
        for j in range(len(A),i,-1):
            if len(s)>=j-i:
                break
            elif A[i:j]==A[i:j][::-1]:
                s=A[i:j]
                break
    return s
print(long("greeks")) '''
l = [5, 3, 2, 6, 5, 7]

s = []
l2 = sorted(l, reverse=True)
a = 0
while 0 < len(l2):
    for i in l2:
        if i is min(l2):
            s.append(i)
            l2.remove(i)
        elif i is max(l2):
            s.append(i)
            l2.remove(i)

print(s)


