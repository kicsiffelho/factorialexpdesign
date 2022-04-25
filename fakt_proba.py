import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from sympy import *



factor = 2
szint = 2
beallitas = szint**factor
ismetles = 2
meres = 2


# Faktorok alsó és felső szintjei természetes mértékben

x_also_hullam = []
x_felso_hullam = []
for i in range(1,factor+1):
    print("x",i,"a: ",end='',sep="")
    also_hullam = int(input())
    x_also_hullam.append(also_hullam)
    print("x",i,"f: ",end='',sep="")
    felso_hullam = int(input())
    x_felso_hullam.append(felso_hullam)

# print("x_also_hullam:",len(x_also_hullam),len(x_felso_hullam))



# Faktorok alapszintjei

x_also = []
for i in range(factor):
    x_also_elem = (x_also_hullam[i]+x_felso_hullam[i])/2
    x_also.append(x_also_elem)

print("x_also:", x_also)



# Variációs intervallumok

for i in range(len(x_also_hullam)):
    x_intervallum = (np.subtract(x_felso_hullam,x_also_hullam))/2
    
print("intervall:",x_intervallum)



# Faktorok alsó és felső szintjeinek transzformált értékei

x_transzformalt = []
for i in range(factor):
    x_also_transzformalt = (x_also_hullam[i]-x_also[i])/x_intervallum[i]
    x_felso_transzformalt = (x_felso_hullam[i]-x_also[i])/x_intervallum[i]
    x_transzformalt.append(x_also_transzformalt)
    x_transzformalt.append(x_felso_transzformalt)

print(x_transzformalt)


# X értékek táblázat [-1, 1]

if (factor == 1):
    x_elojeles_0 = np.array([1,1])
    x_elojeles_1 = np.array([-1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1]
elif (factor == 2):
    x_elojeles_0 = np.array([1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,
                    x_elojeles_1*x_elojeles_2]
elif (factor == 3):
    x_elojeles_0 = np.array([1,1,1,1,1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1,-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1,-1,-1,1,1])
    x_elojeles_3 = np.array([-1,-1,-1,-1,1,1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,x_elojeles_3,
                    x_elojeles_1*x_elojeles_2,x_elojeles_1*x_elojeles_3,x_elojeles_2*x_elojeles_3,
                        x_elojeles_1*x_elojeles_2*x_elojeles_3]
elif (factor == 4):
    x_elojeles_0 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    x_elojeles_1 = np.array([-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1])
    x_elojeles_2 = np.array([-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1])
    x_elojeles_3 = np.array([-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1])
    x_elojeles_4 = np.array([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1])
    x_elojeles = [x_elojeles_0,x_elojeles_1,x_elojeles_2,x_elojeles_3,x_elojeles_4,
                    x_elojeles_1*x_elojeles_2,x_elojeles_1*x_elojeles_3,x_elojeles_1*x_elojeles_4,
                        x_elojeles_2*x_elojeles_3,x_elojeles_2*x_elojeles_4,x_elojeles_3*x_elojeles_4,
                        x_elojeles_1*x_elojeles_2*x_elojeles_3,x_elojeles_1*x_elojeles_2*x_elojeles_4,
                        x_elojeles_1*x_elojeles_3*x_elojeles_4,x_elojeles_2*x_elojeles_3*x_elojeles_4,
                            x_elojeles_1*x_elojeles_2*x_elojeles_3*x_elojeles_4]
    
    

# print(x_elojeles)



# Az első sorozat mért eredményei

y_k = []
for i in range(ismetles): # factor
    for j in range(2**factor):
        print("y_k",i+1,"(x",j+1,"): ",end='',sep="")
        y_k.append(float(input()))

y_k_sum = []
for i in range(2**factor):
    y_k_sum.append((y_k[i]+y_k[i+(ismetles*factor)])/2)

print(y_k_sum)



# b értékek számítása

b = []
# b.append(sum(y_k_sum)/beallitas)
for i in range(len(y_k_sum)):
    j = np.round(sum(np.multiply(x_elojeles[i],y_k_sum)/beallitas),3)
    b.append(j)

print(b)



# Transzformált koordináta rendszerben a keresett polinom

if (factor == 4):
    print("y = ",b[0] ,"+", b[1],"*x1 +", b[2],"*x2 +", b[3],"*x3 +", b[4],"*x4 +", b[5],"*x1*x2 +", b[6],"*x1*x3 +", b[7],"*x1*x4 +", \
            b[8],"*x2*x3 +", b[9],"*x2*x4 +", b[10],"*x3*x4 +", b[11],"*x1*x2*x3 +", b[12],"*x1*x2*x4 +", \
            b[13],"*x1*x3*x4 +", b[14],"*x2*x3*x4 +", b[15],"*x1*x2*x3*x4")
elif (factor == 3):
    print("y = ", b[0] ,"+", b[1],"*x1 +", b[2],"*x2 +", b[3],"*x3 +", b[4],"*x1*x2 +", b[5],"*x1*x3 +", b[6],"*x2*x3 +", b[7],"*x1*x2*x3")
elif (factor == 2):
    print("y = ", b[0] ,"+", b[1],"*x1 +", b[2],"*x2 +", b[3],"*x1*x2")
elif (factor == 1):
    print("y = ",b[0] ,"+", b[1],"*x1")


# Polinom visszatranszformálása a faktorok természetes mértékére

if (factor == 2):
    print("y =",b[0],b[1]/x_intervallum[0],"*x1","+",(b[1]*(0-x_also[0]))/x_intervallum[0],b[2]/x_intervallum[1],"*x2","+",(b[2]*(0-x_also[1]))/x_intervallum[1])
elif (factor == 3):
    print("y =",b[0],b[1]/x_intervallum[0],"*x1","+",(b[1]*(0-x_also[0]))/x_intervallum[0],b[2]/x_intervallum[1],"*x2","+",(b[2]*(0-x_also[1]))/x_intervallum[1],b[3]/x_intervallum[2],"*x3","+",(b[3]*(0-x_also[2]))/x_intervallum[2])
elif (factor == 4):
    print("y =",b[0],b[1]/x_intervallum[0],"*x1","+",(b[1]*(0-x_also[0]))/x_intervallum[0],b[2]/x_intervallum[1],"*x2","+",(b[2]*(0-x_also[1]))/x_intervallum[1],b[3]/x_intervallum[2],"*x3","+",(b[3]*(0-x_also[2]))/x_intervallum[2],b[4]/x_intervallum[3],"*x4","+",(b[4]*(0-x_also[3]))/x_intervallum[3])


# Ábrázolás

# def fun_z(x1,x2,x3):
#     return b[0] + b[1]*x1 + b[2]*x2 ++ b[3]*x3 b[4]*x1*x2 + b[5]*x1*x3 + b[6]*x2*x3 + b[7]*x1*x2*x3    
# 
# ax = plt.axes(projection="3d")
# 
# x1_data = np.linspace(x_also_hullam[0],x_felso_hullam[0],100)
# x2_data = np.linspace(x_also_hullam[1],x_felso_hullam[1],100)
# x3_data = np.linspace(x_also_hullam[2],x_felso_hullam[2],100)
# 
# X1,X2,X3 = np.meshgrid(x1_data,x2_data,x3_data)
# Z = fun_z(X1,X2,X3)
# 
#  
# ax.plot_wireframe(X1,X2,X3,Z,cmap="binary")
# ## fig = plt.figure()
# ## ax = fig.add_subplot(projection="3d")
# ## ax.plot_wireframe(X,Z,B,color='black')
# # for a,v in enumerate(z):
# #     ax.text(a, v+25, "%d" %v, ha="center")
# ax.set_xlabel("x1(vc)",fontsize = 22)
# ax.set_ylabel("x2(Lf)",fontsize = 22)
# ax.set_zlabel("y",fontsize = 22)
# plt.show() 


def function_y(x1,x2):
    if (factor == 2):
        return b[0] + b[1]*x1 + b[2] *x2 + b[3]*x1*x2
    elif (factor == 3):
        return b[0] + b[1]*x1 + b[2]*x2 + b[3]*x_also_hullam[2] + b[4]*x1*x2 + b[5]*x1*x_also_hullam[2] + b[6]*x2*x_also_hullam[2] + b[7]*x1*x2*x_also_hullam[2]  
    elif (factor == 4):
        return b[0] + b[1]*x1 + b[2]*x2 + b[3]*x_also_hullam[2] + b[4]*x_also_hullam[3] + b[5]*x1*x2 + b[6]*x1*x_also_hullam[2] + b[7]*x1*x_also_hullam[3] + \
            b[8]*x2*x_also_hullam[2] + b[9]*x2*x_also_hullam[3] + b[10]*x_also_hullam[2]*x_also_hullam[3] + b[11]*x1*x2*x_also_hullam[2] + b[12]*x1*x2*x_also_hullam[3] + \
            b[13]*x1*x_also_hullam[2]+x_also_hullam[3] + b[14]*x2*x_also_hullam[2]*x_also_hullam[3] + b[15]*x1*x2*x_also_hullam[2]*x_also_hullam[3]
        


ax = plt.axes(projection="3d")


x1_data = np.linspace(x_also_hullam[0],x_felso_hullam[0],100)
x2_data = np.linspace(x_also_hullam[1],x_felso_hullam[1],100)


X1,X2 = np.meshgrid(x1_data,x2_data)
Y = function_y(X1,X2)

 
ax.plot_wireframe(X1,X2,Y,cmap="binary")
## fig = plt.figure()
## ax = fig.add_subplot(projection="3d")
## ax.plot_wireframe(X,Z,B,color='black')
# for a,v in enumerate(z):
#     ax.text(a, v+25, "%d" %v, ha="center")
ax.set_xlabel("x1(vc)",fontsize = 22)
ax.set_ylabel("x2(Lf)",fontsize = 22)
ax.set_zlabel("y",fontsize = 22)
plt.show() 