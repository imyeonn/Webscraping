# """ 형태소 분석기
#     명사 추출 및 빈도수 체크
#     python [모듈 이름] [텍스트 파일명.txt] [결과파일명.txt]
# """

# import sys
from konlpy.tag import Twitter
from collections import Counter


def get_tags(text, ntags=50):
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    return return_list

def main():
    text_file_name = "out.txt"
    # 분석할 파일
    noun_count = 20
    # 최대 많은 빈도수 부터 20개 명사 추출
    output_file_name = "count.txt"
    # count.txt 에 저장
    open_text_file = open(text_file_name, 'r',-1,"utf-8")
    # 분석할 파일을 open
    text = open_text_file.read() #파일을 읽습니다.
    tags = get_tags(text, noun_count) # get_tags 함수 실행
    open_text_file.close()   #파일 close
    open_output_file = open(output_file_name, 'w',-1,"utf-8")
    # 결과로 쓰일 count.txt 열기
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))
    # 결과 저장
    open_output_file.close()

if __name__ == '__main__':
    main()

# def main(argv):
#     if len(argv) != 4:
#         print('python [모듈 이름] [텍스트 파일명.txt] [단어 개수] [결과파일명.txt]')
#         return
#     text_file_name = argv[1]
#     noun_count = int(argv[2])
#     output_file_name = argv[3]
#     open_text_file = open(text_file_name, 'r')
#     text = open_text_file.read()
#     tags = get_tags(text, noun_count)
#     open_text_file.close()
#     open_output_file = open(output_file_name, 'w')
#     for tag in tags:
#         noun = tag['tag']
#         count = tag['count']
#         open_output_file.write('{} {}\n'.format(noun, count))
#     open_output_file.close()
#
#
# if __name__ == '__main__':
#     main(sys.argv)
