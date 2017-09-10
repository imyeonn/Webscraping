from konlpy.tag import Twitter

sentence = '아버지가 방에 들어 가신다.'
twt = Twitter()
tagging = twt.pos(sentance)
tagging
