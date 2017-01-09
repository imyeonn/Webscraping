# 정규식

# 정규식 이용하기 위해 re 모듈 물러와서 정규식으로 a나 b 찾기
# "ab"가 아닌 "[ab]"인 이유는 [ ] 안에 있는 각각의 문자 중 하나라도 포함되면 골라내는 용이기 때문.
# search  : [ ] 안 글자 중 일부라도 포함되면 찾아줌
# match   : [ ] 안 글자와 완전히 동일한 글자를 찾아줌


import re
r = re.compile("[ab]")
print(r.search("pizza"))
print(r.match("pizza"))
print(r.match("abcd"))


# . : 임의의 한 문자

a = re.compile("a,c")
a.search("abc")

# ? : 바로 앞의 문자가 존재하거나 존재하지 않음

b = re.compile("ab?c")
b.search("ac")
b.search("abc")
b.search("abbc")

# * : 바로 앞의 문자가 존재하지 않거나 갯수에 상관없이 존재

b = re.compile("ab*c")
b.search("ac")
b.search("abc")
b.search("abbc")

# + : 바로 앞의 문자가 한 번 이상 존재

b = re.compile("ab+c")
b.search("ac")
b.search("abc")
b.search("abbc")

# ^ : 시작문자 지정

b = re.compile("^a")
b.search("ab")
b.search("ba")

# $ : 끝나는 문자 지정

b = re.compile("c$")
b.search("abc")
b.search("cba")

# 추가 함수

# findall

re.findall("\d+", "이 제품의 가격은 13900원입니다.")
re.findall("\d+", "이 제품의 가격은 13,900원입니다.")

# split
re.split("[:]+", "제품명 : 가격 : 후기")
re.split("[ ]+", "제품명 : 가격 : 후기")

#sub
re.sub("@", " , ", "imyeonn@gmail.com")
