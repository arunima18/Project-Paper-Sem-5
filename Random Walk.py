# Project Qn 1  - Random Walk : for 100 Random Walks 

import random
import math


# Funtion of a single random walk
def RandomWalk_(S):
    A = [0 for i in range(S)]
    B = [0 for i in range(S)]

    for i in range(S):
        t = random.uniform(0, 6.28)     #A random angle in [0,6.28]
        A[i] = A[i - 1] + math.cos(t)   #x displacement
        B[i] = B[i - 1] + math.sin(t)   #y displacement

    return A, B


# Radial Distance at the end of a Random Walk 
def RadDis_(A, B):
    x = A.pop()
    y = B.pop()

    r = (x ** 2 + y ** 2) ** 0.5

    A.append(x)
    B.append(y)

    return r


# Average distance in x and y directions for one walk 
def Avg(A, B, S):
    d1 = 0
    d2 = 0
    i = 1

    while i < S:
        d1 = d1 + (A[i] - A[i - 1])     #distance in x direction 
        d2 = d2 + (B[i] - B[i - 1])     #distance in y direction 
        i = i + 1

    return d1 / S, d2 / S               #Dividing by number of steps S to get average 



# Function for 100 Random walks for number of steps 'S'
def RW_100(S):
    Avgx = [0 for i in range(100)]      #This matrix saves the average x displacement for 100 walks of 'S' steps
    Avgy = [0 for i in range(100)]      #This matrix saves the average y displacement for 100 walks of 'S' steps
    Radial = [0 for i in range(100)]    #This matrix saves the radial distance for 100 walks of 'S' steps

    i = 1
    while i <= 100:
        X, Y = RandomWalk_(S)
        x1, x2 = Avg(X, Y, S)
        Avgx[i - 1] = x1
        Avgy[i - 1] = x2
        Radial[i - 1] = RadDis_(X, Y)
        i = i + 1

    return Avgx, Avgy, Radial


#Function for calculating RMS value for 100 walks of 'S' steps
def RMS_(R,S):                          #R is the matrix that saves the 100 radial distances for 100 walks of 'S' steps
    j=0
    sum=0
    while j<100:
        sum = sum + (R[j])**2
        j=j+1
    rms = (sum/100)**0.5                #Calculating the RMS distance for 100 walks with 'S' steps
    return rms





# main Function

print('For N=3000-')
A1, B1 = RandomWalk_(3000)
r1 = RadDis_(A1,B1)
print('The radial distance covered is: ')
print(r1)
d11,d21=Avg(A1,B1,3000)
print('The average distance in the x direction is:')
print(d11)
print('The average distance in th y direction is:')
print(d21)
P1,P2,P3=RW_100(3000)
rms1=RMS_(P3,3000)
print('The RMS distance for N=3000 is: ')
print(rms1)


print('For N=2000-')
A2, B2 = RandomWalk_(2000)
r2 = RadDis_(A2,B2)
print('The radial distance covered is: ')
print(r2)
d12,d22=Avg(A2,B2,2000)
print('The average distance in the x direction is:')
print(d12)
print('The average distance in th y direction is:')
print(d22)
Q1,Q2,Q3=RW_100(2000)

rms2=RMS_(Q3,2000)
print('The RMS distance for N=2000 is: ')
print(rms2)



print('For N=1000-')
A3, B3 = RandomWalk_(1000)
r3 = RadDis_(A3,B3)
print('The radial distance covered is: ')
print(r3)
d13,d23=Avg(A3,B3,1000)
print('The average distance in the x direction is:')
print(d13)
print('The average distance in th y direction is:')
print(d23)
R1,R2,R3=RW_100(1000)

rms3=RMS_(R3,1000)
print('The RMS distance for N=1000 is: ')
print(rms3)



print('For N=500-')
A4, B4 = RandomWalk_(500)
r4 = RadDis_(A4,B4)
print('The radial distance covered is: ')
print(r4)
d14,d24=Avg(A4,B4,500)
print('The average distance in the x direction is:')
print(d14)
print('The average distance in th y direction is:')
print(d24)
L1,L2,L3=RW_100(500)
rms4=RMS_(L3,500)
print('The RMS distance for N=500 is: ')
print(rms4)



print('For N=250-')
A5, B5 = RandomWalk_(250)
r5 = RadDis_(A5,B5)
print('The radial distance covered is: ')
print(r5)
d15,d25=Avg(A5,B5,250)
print('The average distance in the x direction is:')
print(d15)
print('The average distance in th y direction is:')
print(d25)
K1,K2,K3=RW_100(250)

rms5=RMS_(K3,250)
print('The RMS distance for N=250 is: ')
print(rms5)