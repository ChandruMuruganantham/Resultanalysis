import pandas as pd
import numpy as np
import random
df = pd.read_excel("sk1.xlsx")#,index_col ="rollno")
a2=df.shape
r,c=a2
print("Number of rows in df Dataframe:" ,r)
print("Number of columns in df Dataframe:" ,c)
x=df.values
print(x)
k=3 #int(input("Enter the number of cluster : "))

ccluster={}
for i in range(k):
    ccluster[i]=[]

newcluster={}
for i in range(k):
    newcluster[i]=[]

#print(cluster)
#y = random.sample(range(1,r),k)
y=23,42,52

centroids={}
print("Random Centroids")
for i in range(k): 
    centroids[i]=df.iloc[y[i]]
    #'print(centroids[i])
#print("Euclidean Distance")

for i in range(1,3):
    print("Iteration : " ,i)
    cluster={}
    for i in range(k):
        cluster[i]=[]
    for kr in range(0,r):
        #print("Object : ",kr)
        data=x[kr]
        #print("Values :" ,data)
        euc_dist=[]
        for j in range(k):
            euc_dist.append(round(np.linalg.norm(data-centroids[j]),1))
        cluster[euc_dist.index(min(euc_dist))].append(kr)
        ccluster[euc_dist.index(min(euc_dist))].append(data)
        #print("Euclidean Distance :",euc_dist)  
    print("CLUSTERS")
    #print(cluster)
    cluster.clear()
    #print(newcluster)
    #newcluster.clear()
    
    ncentroids={}
    print("New Centroids")
    for i in range(k):
        ncentroids[i]= np.average(ccluster[i],axis=0)
        ncentroids[i]=np.round(ncentroids[i],2)
    #print(ncentroids)
    cen1=[]
    cen2=[]
    for i in range(0,k):
        cen1.append(centroids[i])
        cen2.append(ncentroids[i])  
    #print("cen1:",cen1)
    #print("cen2:",cen2)
    #print(len(cen1))
    #print(len(cen2))
    c=[round(x1-x2,2) for x1,x2 in zip(cen1,cen2)]
    d=[abs(x) for x in c]
    print(d)
    if d[0] <= 0.5: 
        print("Correct Iteration")
        break
    else:
        centroids=ncentroids