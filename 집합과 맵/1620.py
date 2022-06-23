from sys import stdin as s

N,M=map(int,s.readline().split())

# 리스트와 딕셔너리를 각각 만드는 것이 시간복잡도에 도움이 됨
pokemon=[0 for _ in range(N+1)] # 숫자를 받았을 때 문자를 출력
pokemon_dic={} # 문자열을 받았을 때 숫자를 출력
for i in range(1,N+1):
    each_pok=s.readline().rstrip()
    pokemon[i] = each_pok
    pokemon_dic[each_pok]=i

compare=[s.readline().rstrip() for _ in range(M)]

for i in compare:
    if i.isdigit() == True:
        idx=int(i)
        print(pokemon[int(i)])
    else:
        print(pokemon_dic[i])

    
