x = int(input())
y = input()
y1 = int(y[2])*x
y2 = int(y[1])*x
y3 = int(y[0])*x
y4= [y1,y2,y3]

for i in range(3) :
    print(y4[i])
print(y4[0]+y4[1]*10+y4[2]*100)
