from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

# f = int(input("Faktorok száma: "))
# p = int(input("Kísérleti beállítások szinjeinek száma: "))
# n = int(input("Független beállítások száma: "))
# m = int(input('Ismétlések száma: '))
f = 2
p = 2
n = p**2
m = 2
meresek = m*n

x1_values = [80, 120]
x2_values = [0.03, 10.02]

base_x1_values = (np.sum(x1_values))/f
base_x2_values = (np.sum(x2_values))/f

for x1 in range(len(x1_values)):
    delta_x1 = x1_values[x1] - x1_values[x1-1]


for x2 in range(len(x2_values)):
    delta_x2 = x2_values[x2] - x2_values[x2-1]

delta_x1 = delta_x1/2
delta_x2 = delta_x2/2

# print(delta_x1)
# print(delta_x2)
# print(base_x1_values)
# print(base_x2_values)
# print(delta_x1)
# print(delta_x2)

x1a = round((x1_values[0] - base_x1_values)/delta_x1)
x1f = round((x1_values[1] - base_x1_values)/delta_x1)
x2a = round((x2_values[0] - base_x2_values)/delta_x2)
x2f = round((x2_values[1] - base_x2_values)/delta_x2)

# print(x1a, x1f, x2a, x2f)

x1_m = [-1,1,-1,1]
x2_m = [-1,-1,1,1]
x1x2 = np.multiply(x1_m,x2_m)
# print(x1x2)

y_k1 = [3.20,0.90,4.95,2.13]
y_k2 = [3.40,1.00,4.85,2.17]
y_k = []
for y in range(len(y_k1)):
    y_k.append((y_k1[y]+y_k2[y])/2)

# print(y_k)

ones = [1,1,1,1]
x_values = [ones,x1_m,x2_m,x1x2]
b = []
for j in range(len(x_values)):
    j = np.round(sum(np.multiply(y_k, x_values[j]))/n,3)
    b.append(j)

print(b)
# b0 = round(sum(y_k)/n,3)
# b1 = round(sum(np.multiply(y_k, x1_m))/n,3)
# b2 = round(sum(np.multiply(y_k, x2_m))/n,3)
# b12 = round(sum(np.multiply(y_k,x1x2))/n,3)
# print(b0,b1,b2,b12)

# y = b0 + b1*x1 + b2*x2 + b12*x1x2

# for i in range(len(x1_m)):

# x = [0, x1_m,x2_m,x1x2]
# y = b0 + float(x1_m)*b1 + float(x2_m)*b2 + float(b12)*x1x2

# plt.figure(figsize =(6,4))
# plt.scatter(x, y)

# Válaszfüggvény y = 2.825 - 1.275*x1 + 0.7*x2
z = []
for k in range(len(x1_m)):
    z.append(round(b[0]+b[1]*x1_m[k]+b[2]*x2_m[k],3))        

# print(z)

x = x1_m
y = x2_m
# z = y_k
# print(z)


fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111,projection="3d")
ax.plot3D(x,y,z,'r--o')
# for a,v in enumerate(z):
#     ax.text(a, v+25, "%d" %v, ha="center")
ax.set_xlabel("x1(vc)",fontsize = 22)
ax.set_ylabel("x2(Lf)",fontsize = 22)
ax.set_zlabel("y",fontsize = 22)
plt.show()