# Camila Sandoval
# BIM A+ 3
# Assignment 03 - Polygon

import math
print ('POLYGON PROGRAM')

columns = 2 # X and Y coordinates
rows = int(input("Number of sides: "))
p = [[0 for x in range(columns)] for y in range(rows)] 

for a in range(0,rows):
    print ('Point ',a+1,': ')
    print('(insert x then y)')
    for b in range(0,columns):
        p[a][b] = float(input())

print('-' * 30)
print(f"{'Point':>6} {'X':>6} {'Y':>11}")
print('-' * 30)

for c in range(0,rows):
    print(f"{c+1:4.0f} {p[c][0]:10.2f} {p[c][1]:11.2f}")

print('-' * 30)

Ax = 0 # Area
Sx = 0 # Static moment in X
Sy = 0 # Static moment in Y
Ix = 0 # Axial inertia moment in X
Iy = 0 # Axial inertia moment in Y
Ixy = 0 # Axial inertia moment in XY
for d in range(0,rows-1):
    Ax = Ax + (p[d+1][0] + p[d][0]) * (p[d+1][1]-p[d][1])
    Sx = Sx + (p[d+1][0] - p[d][0]) * (pow(p[d+1][1],2) + (p[d+1][1]*p[d][1]) + pow(p[d][1],2))
    Sy = Sy + (p[d+1][1] - p[d][1]) * (pow(p[d+1][0],2) + (p[d+1][0]*p[d][0]) + pow(p[d][0],2))
    Ix = Ix + (p[d+1][0] - p[d][0]) * (pow(p[d+1][1],3) + (pow(p[d+1][1],2) * p[d][1]) + (p[d+1][1] * pow(p[d][1],2)) + pow(p[d][1],3))
    Iy = Iy + (p[d+1][1] - p[d][1]) * (pow(p[d+1][0],3) + (pow(p[d+1][0],2) * p[d][0]) + (p[d+1][0] * pow(p[d][0],2)) + pow(p[d][0],3))
    Ixy = Ixy + ((p[d+1][1] - p[d][1]) * ((p[d+1][1] * ((3 * pow(p[d+1][0],2)) + (2 * p[d+1][0] * p[d][0]) + pow(p[d][0],2))) + (p[d][1] * ((3 * pow(p[d][0],2)) + (2 * p[d+1][0] * p[d][0]) + pow(p[d+1][0],2)))))
Ax = Ax/2
Sx = abs(Sx/6)
Sy = abs(Sy/6)
Ix = abs(Ix/12)
Iy = abs(Iy/12)
Ixy = -Ixy/24
Xt = Sy/Ax # Cross-sectioal center coordinate in X
Yt = Sx/Ax # Cross-sectioal center coordinate in Y
Ixt = Ix - (Yt**2 * Ax) # Moment in X
Iyt = Iy - (Xt**2 * Ax) # Moment in Y
Ixyt = Ixy + (Xt * Yt * Ax) # Moment in XY

print ('Geometric characteristics')
print(f"{'Polygon Area,                            Ax= '}{Ax:6.2f}")
print(f"{'Static moment in X,                      Sx= '}{Sx:6.2f}")
print(f"{'Static moment in Y,                      Sy= '}{Sy:6.2f}")
print(f"{'Axial inertia moment in X,               Ix= '}{Ix:6.2f}")
print(f"{'Axial inertia moment in Y,               Iy= '}{Iy:6.2f}")
print(f"{'Axial inertia moment in XY,             Ixy= '}{Ixy:6.2f}")
print(f"{'Cross-sectioal center coordinate in X,   Xt= '}{Xt:6.2f}")
print(f"{'Cross-sectioal center coordinate in Y,   Yt= '}{Yt:6.2f}")
print(f"{'Moment in X,                            Ixt= '}{Ixt:6.2f}")
print(f"{'Moment in Y,                            Iyt= '}{Iyt:6.2f}")
print(f"{'Moment in XY,                          Ixyt= '}{Ixyt:6.2f}")