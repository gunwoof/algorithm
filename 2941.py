croAlpa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

problem = input()
cnt = 0

for i in range(len(problem)) :
    onstr2="".join(problem[i:i+2])
    onstr3="".join(problem[i:i+3])
    
    if "".join(problem[i-1:i+2]) in croAlpa or "".join(problem[i-1:i+1]) in croAlpa : # "dz=" 넘기기용
        continue
    elif onstr2 in croAlpa or onstr3 in croAlpa :
        cnt += 1
    else :
        cnt += 1
          
print(cnt)


# 누군가의 깔끔한 코드
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha = input()
for t in a: 
    alpha = alpha.replace(t, '*')
print(len(alpha))

