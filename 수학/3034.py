import math as m

number, w, h = map(int,input().split())
match = []
answer = []

for i in range(number) :
    match.append(int(input())) 
    if match[i] <= max(w,h) or match[i] <= m.sqrt(w**2+h**2) :
        answer.append("DA")
    else :
        answer.append("NE") 
    
for i in range(number) :
    print(answer[i])


