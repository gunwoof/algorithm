number = int(input())
texts = [] # 문자열 모음
text_dic={} # 문자를 (단어:단어의 개수) 의 딕셔러니로 받음
count =0 # 그룹 단어의 개수

for i in range(number) :
    texts.append(input())
    text = texts[i] # 문자열 모음 중 하나의 문자열

    for j in range(len(text)) :
        if text[j] not in text_dic.keys():
            text_dic[text[j]] = 1
        elif text[j] in text_dic.keys() and text[j] == (text[j-1]) and text_dic[text[j]] != 0 :
            text_dic[text[j]] += 1
        else : 
            text_dic[(texts[i])[j]] = 0 # 그룹단어가 아니라면 개수를 0으로 만듬
    
    if 0 not in text_dic.values() : 
        count += 1
    text_dic.clear() # 다음 문자열 체크를 위해 사전 비우기

print(count)
    
    

