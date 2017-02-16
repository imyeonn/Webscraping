# for 질문
for i in range(1, 6) :
        for j in range(i) :
            print( "*", end = "", )

        print()

# 가변 매개변수(*: 튜플)
def merge_string(*text_list):
    result = ' '
    for s in text_list:
        result = result + s
    return result

merge_string('아버지가', '방에', '들어가신다.')

# 가변 매개변수(**: 딕셔너리)
def print_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))

print_team(카시야스='GK', 호날두='FW', 알론소='MF', 패패='DF')

# 일반매개변수+키워드매개변수
def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args(3, 'arg1', 'arg2', 'arg3')

# 키워드매개변수+일반매개변수
def print_args(*argc, argv):
    for i in range(argc):
        print(argv[i])

print_args('arg1', 'arg2', 'arg3', argc=3)
