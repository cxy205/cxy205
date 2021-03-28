#只能解决有解，且无自由变量的方程组
import numpy as np

m=int(input("请输入矩阵行数："))
n=int(input("请输入矩阵列数："))

mat=np.mat(np.zeros((m,n)))
mat1=np.mat(np.zeros((1,n-1)))

print("请输入矩阵：")#输入增广矩阵

for i in range(m):
    mat[i]=input().split(" ")
    
print("原矩阵:")
print(mat)

 #应先判断正在处理的行的主元位置系数是否为0，若为0，则进行上下行交换
for i in range(m):
    if mat[i,i]==0 and i!=m-1:
        mat[i],mat[i+1]=mat[i+1],mat[i]
        
    if mat[i,i]==0 and i==m-1:
        print("存在自由变量")
        break

    a=mat[i,i]3
    for j in range(i,n):
        mat[i,j]=mat[i,j]/a
    for k in range(i+1,m):
        a=mat[k,i]
        for p in range(i,n):
            mat[k,p]=mat[k,p]-mat[i,p]*a 
            
print("最简阶梯矩阵：")            
print(mat)
 
for i in range(m-1,-1,-1):
    if i==m-1:
        mat1[0,i]=mat[i,n-1]
    else:
        b=0
        for j in range(n-2,i-1,-1):
            b=b+mat[i,j]*mat1[0,j]
        mat1[0,i]=(mat[i,n-1]-b)/mat[i,i]
print("解：")
print(mat1)
#mat1中解的顺序从左到右依次为x1到xm

