from sys import stdin as s

ABC=list(map(int,s.readline().split()))

if ABC[1]>=ABC[2]:
    print(-1)
    exit()

BEpoint=ABC[0]//(ABC[2]-ABC[1])+1
print(BEpoint)
