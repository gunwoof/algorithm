from sys import stdin as s

p_s=list(map(int,s.readline().split()))
p_s_dic={}

for i in range(p_s[0]):
    site,password=s.readline().split()
    
    p_s_dic[site]=password

key_s=[s.readline().strip() for _ in range(p_s[1])]

for i in key_s:
    print(p_s_dic[i])   




    