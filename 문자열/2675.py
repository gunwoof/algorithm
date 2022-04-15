n = int(input())

for i in range(n) :
    R, S = input().split()
    R = int(R)
    
    rep = []
    for j in range(len(S)):
        rep.append(S[j]*R)
        
    for j in range(len(S)):
        if j != len(S)-1:
            print(rep[j],end="")
        else :
            print(rep[j])
    
    
