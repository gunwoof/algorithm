from sys import stdin as s

n=list(map(int,s.readline().split()))

rec_min=[]
rec_min.append(n[0])
rec_min.append(n[1])
rec_min.append(n[2]-n[0])
rec_min.append(n[3]-n[1])

print(min(rec_min))



    