from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

# f = int(input("Faktorok száma: "))
# p = int(input("Kísérleti beállítások szinjeinek száma: "))
# # n = int(input("Független beállítások száma: "))
# m = int(input("Ismétlések száma: "))
# meresek = int(input("Mérések száma: "))
f = 2
p = 2
n = p**2
m = 2
meresek = m*n

x1_values = [30,40]
x2_values = [4,8]

base_x1_values = (np.sum(x1_values))/f
base_x2_values = (np.sum(x2_values))/f

for x1 in range(len(x1_values)):
    delta_x1 = x1_values[x1] - x1_values[x1-1]


for x2 in range(len(x2_values)):
    delta_x2 = x2_values[x2] - x2_values[x2-1]

delta_x1 = delta_x1/2
delta_x2 = delta_x2/2

print("x2:",x1_values)
print("x1:",x2_values)
print("alapszint x1:",base_x1_values)
print("alapszint x2:",base_x2_values)
print("delta_x1:",delta_x1)
print("delta_x2:",delta_x2)

x1a = round((x1_values[0] - base_x1_values)/delta_x1)
x1f = round((x1_values[1] - base_x1_values)/delta_x1)
x2a = round((x2_values[0] - base_x2_values)/delta_x2)
x2f = round((x2_values[1] - base_x2_values)/delta_x2)

print("x1a:",x1a,"x1f:",x1f,"x2a:",x2a,"x2f:",x2f)

x1_m = [-1,1,-1,1]
x2_m = [-1,-1,1,1]
x1x2 = np.multiply(x1_m,x2_m)
print("x1x2:",x1x2)

y_k1 = [27.0,15.9,22.1,13.4]
y_k2 = [28.0,17.1,22.9,13.6]
y_k = []
for y in range(len(y_k1)):
    y_k.append((y_k1[y]+y_k2[y])/2)

print("y_k:",y_k)

ones = [1,1,1,1]
x_values = [ones,x1_m,x2_m,x1x2]
b = []
for j in range(len(x_values)):
    j = np.round(sum(np.multiply(y_k, x_values[j]))/n,3)
    b.append(j)

print("b:",b)
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

# SZÓRÁS
s = []
for q in range(len(y_k1)):
    szoras = round(((y_k1[q]-y_k[q])**2 + (y_k2[q]-y_k[q])**2)/(m-1),4)
    s.append(szoras)
print("s:",s)

s_y = 0
s_count = 0
for o in range(len(s)):
    s_count += s[o]
s_y = s_count/n
print("s_y:",s_y)

# Válaszfüggvény y = 2.825 - 1.275*x1 + 0.7*x2s
z = []
for k in range(len(x1_m)):
    z.append(round(b[0]+b[1]*x1_m[k]+b[2]*x2_m[k],3)) 

print("y:",z)

s_ad = []
for w in range(len(y_k)):
    ad = (z[w]-y_k[w])**2
    s_ad.append(ad)
print("s_ad:",s_ad)

s_ad2 = sum(s_ad)/(n-f-1)
print("s_ad2:",s_ad2)
ff = round(s_ad2/s_y,4)
print("F:",ff)

# x = x1_m
# y = x2_m
# z = y_k
# print(z)

def function_z(x,y):
     return b[0] + b[1]*x + b[2] *y + b[3]*x*y


ax = plt.axes(projection="3d")


x_data = np.linspace(x1_values[0],x1_values[1],100)
y_data = np.linspace(x2_values[0],x2_values[1],100)


X,Y = np.meshgrid(x_data,y_data)
Z = function_z(X,Y)

 
ax.plot_wireframe(X,Y,Z,cmap="binary")
## fig = plt.figure()
## ax = fig.add_subplot(projection="3d")
## ax.plot_wireframe(X,Z,B,color='black')
# for a,v in enumerate(z):
#     ax.text(a, v+25, "%d" %v, ha="center")
ax.set_xlabel("x1(vc)",fontsize = 22)
ax.set_ylabel("x2(Lf)",fontsize = 22)
ax.set_zlabel("y",fontsize = 22)
plt.show()