from sys import stdin as s

# 단어 뒤집는 함수
def word_reverse(words):
    words=words.split()
    for i in range(len(words)):
        words[i]=(words[i])[::-1]
    
    words=" ".join(words)
    return words


# 태그와 단어 구분(문자열 -> 리스트)
S=s.readline().strip().replace('<','|<').replace('>','>|').split('|')

S_processing=[]
for i in range(len(S)):
    if S[i] != '': # 빈 문자열 제거
        if S[i][0] == '<': # 태그는 뒤집지 않고 넣기
            S_processing.append(S[i])
        else : # 단어는 뒤집고 넣기
            S[i]=word_reverse(S[i])
            S_processing.append(S[i])

# 리스트->문자열로 바꿈
S_processing="".join(S_processing)
print(S_processing)