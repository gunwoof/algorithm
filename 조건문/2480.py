number = input("").split()
x = int(number[0])
y = int(number[1])
z = int(number[2])
dice = [x,y,z]

max = 0
if x == y == z :
    print(10000+x*1000)
elif x == y and y != z :
    print(1000+x*100)
elif x != y and y == z :
    print(1000+y*100)
elif z == x and x!= y :
    print(1000+z*100)
else :
    for i in range(3) :
        if dice[i] > max :
            max = dice[i]
    print(max*100)


# 누군가의 깔끔한 코드
'''a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a == b == c:
  print(10000 + a * 1000)
elif a == b:
  print(1000 + a * 100)
elif a == c:
  print(1000 + a*100)
elif b == c:
  print(1000 + b*100)  
else:
  print(max(a,b,c) * 100)'''