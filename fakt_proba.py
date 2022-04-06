import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


factor = 3
szint = 2
beallitas = szint**factor
ismetles = 2
meres = 2


# Faktorok alsó és felső szintjei természetes mértékben

x_also_hullam = []
x_felso_hullam = []
for i in range(1,factor+1):
    print("x",i,"a: ")
    also_hullam = int(input())
    x_also_hullam.append(also_hullam)
    print("x",i,"f: ")
    felso_hullam = int(input())
    x_felso_hullam.append(felso_hullam)

# print("x_also_hullam:",len(x_also_hullam),len(x_felso_hullam))



# Faktorok alapszintjei

x_also = []
for i in range(factor):
    x_also_elem = (x_also_hullam[i]+x_felso_hullam[i])/2
    x_also.append(x_also_elem)

# print("x_also:", len(x_also))



# Variációs intervallumok

for i in range(len(x_also_hullam)):
    x_intervallum = (np.subtract(x_felso_hullam,x_also_hullam))/2
    
#print("intervall:",len(x_intervallum))



# Faktorok alsó és felső szintjeinek transzformált értékei

x_transzformalt = []
for i in range(factor):
    x_also_transzformalt = (x_also_hullam[i]-x_also[i])/x_intervallum[i]
    x_felso_transzformalt = (x_felso_hullam[i]-x_also[i])/x_intervallum[i]
    x_transzformalt.append(x_also_transzformalt)
    x_transzformalt.append(x_felso_transzformalt)

#print(x_transzformalt)

if (factor == 4):
    print()
elif (factor == 3):
    print("y = b0 + b1 * x1 + b2 * x2 + b12 * x12 + b23 * x23 + b13 * x13 + b123 * x123")
elif (factor == 2):
    print("y = b0 + b1 * x1 + b2 * x2 + b12 * x12")
elif (factor == 1):
    print("y = b0 + b1 * x1")
