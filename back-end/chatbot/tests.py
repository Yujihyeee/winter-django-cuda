from konlpy.tag import Okt
from konlpy.tag import Komoran
import numpy as np
from konlpy.tag import Kkma


class Chatbot(object):
    def __init__(self):
        pass

    def kkma_execute(self):
        # 꼬꼬마 형태소 분석기 객체 생성
        kkma = Kkma()
        text = "아버지가 방에 들어갑니다."

        # 형태소 추출
        morphs = kkma.morphs(text)
        print(morphs)

        # 형태소와 품사 태그 추출
        pos = kkma.pos(text)
        print(pos)

        # 명사만 추출
        nouns = kkma.nouns(text)
        print(nouns)

        # 문장 분리
        sentences = "오늘 날씨는 어때요? 내일은 덥다던데."
        s = kkma.sentences(sentences)
        print(s)

    def okt_execute(self):
        # Okt 형태소 분석기 객체 생성
        okt = Okt()
        text = "아버지가 방에 들어갑니다."

        # 형태소 추출
        morphs = okt.morphs(text)
        print(morphs)

        # 형태소와 품사 태그 추출
        pos = okt.pos(text)
        print(pos)

        # 명사만 추출
        nouns = okt.nouns(text)
        print(nouns)

        # 정규화, 어구 추출
        text = "오늘 날씨가 좋아욬ㅋㅋ"
        print(okt.normalize(text))
        print(okt.phrases(text))

    def koran_execute(self):
        komoran = Komoran()
        text = "우리 챗봇은 엔엘피를 좋아해."
        pos = komoran.pos(text)
        print(pos)

    def koran_execute_2(self):
        komoran = Komoran()
        text = "오늘 날씨는 구름이 많아요."

        # 명사만 추출
        nouns = komoran.nouns(text)
        print(nouns)

        # 단어 사전 구축 및 단어별 인덱스 부여
        dics = {}
        for word in nouns:
            if word not in dics.keys():
                dics[word] = len(dics)
        print(dics)

        # 원-핫 인코딩
        nb_classes = len(dics)
        targets = list(dics.values())
        one_hot_targets = np.eye(nb_classes)[targets]
        print(one_hot_targets)


if __name__ == '__main__':
    c = Chatbot()
    # c.kkma_execute()
    # c.okt_execute()
    c.koran_execute_2()
