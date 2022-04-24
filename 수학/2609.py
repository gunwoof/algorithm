from sys import stdin as s

n,m = map(int,s.readline().split())
gcf=0 # 최대 공약수
lcm=0 # 최소 공배수

for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0 :  
        gcf=i

for i in range(min(n,m),n*m+1):
    if i%n==0 and i%m==0:
        lcm=i
        break

print(gcf)
print(lcm)