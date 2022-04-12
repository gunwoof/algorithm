n = int(input())
text =[]
for i in range(n) :
    text = input().split()
    
    for j in range(len(text)) :
        text[j] = "".join(list(reversed(text[j]))) 
    
    print(" ".join(text))
    text.clear()


# 누군가의 깔끔한 코드
'''N = int(input())

for i in range(N) :
  sentence = list(input().split())

  for j in sentence :
    print(''.join(j[::-1]) + " ", end="")
  print()'''

   
