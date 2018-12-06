#Homework 1
#Tarik Dahnoun
#left midpoint trapezoid integral functions
import numpy as np

xi=-1.
xf=1.
nts1=2
nts2=2
nts3=2

def function(x):
    return np.cos(x**2-x)

def left_endpoints(nts):
    x=np.linspace(xi,xf,nts)
    dx=x[1]-x[0]
    
    y=np.zeros(nts)
    for i in range(0,nts-1):
        y=function(x)*dx
    y.tolist()
    I=sum(y)
    return I
    
A=left_endpoints(nts1)
# print A

##############################################################

def midpoint(nts):    
    x=np.linspace(xi,xf,nts)
    dx=x[1]-x[0]
    
    y=np.zeros(nts)
    for i in range(0,nts-1):
        y[i]=function(x[i]+dx/2)*dx
    y.tolist()
    I=sum(y)
    return I
    
B=midpoint(nts2)
# print B

##############################################################

def trapezoid(nts):
    x=np.linspace(xi,xf,nts)
    dx=x[1]-x[0]
    
    y=np.zeros(nts)
    for i in range(0,nts-1):
        y[i]=((function(x[i])+function(x[i+1]))/2)*dx
    y.tolist()
    I=sum(y)
    return I
    
C=trapezoid(nts3)
# print C

##############################################################

def wolfram():
    return 1.55547
    
D=wolfram()


#Assume the number from wolfram is perfect:


while abs(A-D)>=.002: #plus or minus 10^-4
    nts1=nts1+1
    A=left_endpoints(nts1)
print "Using the left endpoint method, it takes",nts1,"to be accurate to .002"
print "The value of the integral is approximately",A
print
while abs(B-D)>=.002: #plus or minus 10^-4
    nts2=nts2+1
    B=midpoint(nts2)
print "Using the midpoint method, it takes",nts2,"to be accurate to .002"
print "The value of the integral is approximately",B
print
while abs(C-D)>=.002: #plus or minus 10^-4
    nts3=nts3+1
    C=trapezoid(nts3)
print "Using the trapezoid method, it takes",nts3,"to be accurate to .002"
print "The value of the integral is approximately",A    
    
    