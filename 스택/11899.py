# 스택에 '('다음 ')'나오면 삭제
# 남은거 카운트

from sys import stdin as s

door=list(s.readline().strip())
stack=[]
for i in door:
    stack.append(i)
    if len(stack) >=2 and stack[-2]=='(' and stack[-1] ==')':
        stack.pop()
        stack.pop()

print(len(stack))
