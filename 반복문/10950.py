count = int(input())
x=[]
y=[]
for i in range(count) :
    a,b = map(int,input().split())
    x.append(a) 
    y.append(b) 

for i in range(count) :
    print(x[i]+y[i])
