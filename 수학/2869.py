from sys import stdin as s

A,B,V = map(int,s.readline().split())
height = 0
cnt=0

cnt = (V-B)/(A-B)
if (V-B)%(A-B) !=0:
    cnt=int(cnt+1)
else :
    cnt = int(cnt)
    
print(cnt)