from sys import stdin as s

L=int(s.readline())
string=s.readline().rstrip()
hash_sum=0

for i in range(L):
    ai=ord(string[i])-ord("a")+1
    hash_sum += ai*(31**i)
    

print(hash_sum%1234567891)
