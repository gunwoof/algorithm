x,y = map(int,input().split())
z=[]
if x !=0 and y!= 0 :
        z.append(x+y)

while x !=0 and y!= 0 :
    x,y = map(int,input().split())
    if x !=0 and y!= 0 :
        z.append(x+y)

for i in range(len(z)) :
    print(z[i])


# 누군가의 깔끔한 코드
'''while True:
  num1,num2=map(int,input().split())
  if num1==0 and num2==0:
    break
  print("{}".format(num1+num2))'''