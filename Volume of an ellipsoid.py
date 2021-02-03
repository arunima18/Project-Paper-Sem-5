# Project question 2: Volume of an ellipsoid
import random
import math
import matplotlib.pyplot as plt


# Function to calculate the volume of an ellipsoid
def Vol_Ellipsoid(a, b, c, N):
    A = []
    B = []
    C = []
    ellipsoid_point = 0
    cuboid_point = 0
    i = 1
    while i <= N:
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        z = random.uniform(-c, c)
        # Check whether the points lie inside the ellipsoid
        z = (x ** 2 / a ** 2) + (y ** 2 / b ** 2) + (z ** 2 / c ** 2)
        if z <= 1:
            ellipsoid_point = ellipsoid_point + 1
            A.append(x)
            B.append(y)
            C.append(z)

        cuboid_point = cuboid_point + 1
        i = i + 1

    Volume = (8 * a * b * c * ellipsoid_point) / cuboid_point
    return Volume, A, B, C


# For the calculation of Fractional Error, T is no. of trails, analytical volume=12.57
def Error(a, b, c, n):      #n is the number of random points
    E = []
    N = []
    V = []
    i = 1
    while i <= 500:         #total of 500 trails of interval 100, going upto 50000 points
        v, A, B, C = Vol_Ellipsoid(a, b, c, i * n)
        e = (v - 12.57) / v
        E.append(e)
        N.append(i * 100)
        V.append(v)
        i = i + 1
    return E, N, V


# Main function
E, N, V = Error(1, 1.5, 2, 100)

#For 3D plot of the Ellipsoid 
V,A,B,C=Vol_Ellipsoid(1,1.5,2,40000)
print("Volume of an ellipsoid with a=1 unit, b=1.5 unit, c=2 unit and N=40000 random points is: ")
print(V)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(A,B,C, c = 'b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("3 dimensional plot of the Ellipsoid obtained for N=40000 random points")
plt.show()



#######################################################################################################################
'''
C:\pythonProject7\Scripts\python.exe "C:/Users/Arunima Das/PycharmProjects/pythonProject7/main.py"
Volume of an ellipsoid with a=1 unit, b=1.5 unit, c=2 unit and N=40000 random points is: 
12.591

Process finished with exit code 0 '''

















 
