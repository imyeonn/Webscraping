text = readLines("http://www.naver.com/")
Encoding(text) = "UTF-8"

text_sub = text[589:608]

for(n in 1:length(text_sub)){
  start_p = gregexpr(text_sub[n], pattern = ">")[[1]][1] + 1 # 시작위치
  end_p = gregexpr(text_sub[n], pattern = "<")[[1]][2] - 1 #종료위치
  text_sub[n] = substr(text_sub[n], start_p, end_p)
}
text_sub