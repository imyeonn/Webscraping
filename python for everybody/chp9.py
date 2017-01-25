# chp 1~ 9 내용 다 포함

# 파일 입력받기
name = raw_input("Enter file:")
# 파일 읽기용으로 열기
handle = open(name, 'r')
# 파일 전체 읽어들이기
text = handle.read()
# 파일 전체를 단어별로 자르기(words: list, text: string)
words = text.split()

# 딕셔너리 설정하고 단어별 숫자세기(word; count 형태)
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

# 빈도 수 가장 큰 단어 찾기
bigcount = None
bigword = None
# 아까 저장해둔 counts 하나씩 확인(츅츅츅)
for word.count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# 가장 큰 거 찾으면 for 나옴
print bigword, bigcount
