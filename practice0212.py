# 170212
a = 4/3
print(a)
b = "이름"
print(type(b))
print(0x14)

# 계산기는 decimal로. 파이썬은 소수점계산안됨.
print(10.2-10.1)
print(round(2.500000000000001))
print(round(2.5000000000000001))

# 0:0:0 에서 마지막 0은 뽑아내는 간격임.
a = 'hellooooo'
print(a[::2])

# .format
# {} 안에 내용은 맘대로. 없어도 됨. 기억하기 편하려고.
b = 'today is {0}'.format('12')
print(b)

# 자르고 합치기
csv = "가, 나, 다"
splited = csv.split(', ')
', '.join(splited)

list = ['1 이름', 2, 3]
print(list)
list2 = list[0].split(' ')
list.insert(0, list2)
print(list)

print(type(list[2]))

# 파이썬 변수 한글도 됨. 숫자로 시작하면 안됨.
삼 = 3
print(삼 + 3)
