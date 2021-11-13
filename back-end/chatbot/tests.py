from konlpy.tag import Okt
from konlpy.tag import Komoran
import numpy as np
from konlpy.tag import Kkma
from gensim.models import Word2Vec


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

    def load_word2vec(self):
        model = Word2Vec.load('nvmc.model')
        print("corpus_total_words : ", model.corpus_total_words)

        # '사랑'이란 단어로 생성한 단어 임베딩 벡터
        print('사랑 : ', model.wv['사랑'])

        # 단어 유사도 계산
        print("일요일 = 월요일\t", model.wv.similarity(w1='일요일', w2='월요일'))
        print("안성기 = 배우\t", model.wv.similarity(w1='안성기', w2='배우'))
        print("대기업 = 삼성\t", model.wv.similarity(w1='대기업', w2='삼성'))
        print("일요일 != 삼성\t", model.wv.similarity(w1='일요일', w2='삼성'))
        print("히어로 != 삼성\t", model.wv.similarity(w1='히어로', w2='삼성'))

        # 가장 유사한 단어 추출
        print(model.wv.most_similar("안성기", topn=5))
        print(model.wv.most_similar("시리즈", topn=5))

    def word_ngram(bow, num_gram):
        text = tuple(bow)
        ngrams = [text[x:x + num_gram] for x in range(0, len(text))]
        return tuple(ngrams)

    # 음절 n-gram 분석
    def phoneme_ngram(bow, num_gram):
        sentence = ' '.join(bow)
        text = tuple(sentence)
        slen = len(text)
        ngrams = [text[x:x + num_gram] for x in range(0, slen)]
        return ngrams

    # 유사도 계산
    def similarity(doc1, doc2):
        cnt = 0
        for token in doc1:
            if token in doc2:
                cnt = cnt + 1

        return cnt / len(doc1)

    sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학하였다'
    sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학하였다'
    sentence3 = '나는 맛잇는 밥을 뉴턴 선생님과 함께 먹었습니다.'

    komoran = Komoran()
    bow1 = komoran.nouns(sentence1)
    bow2 = komoran.nouns(sentence2)
    bow3 = komoran.nouns(sentence3)

    doc1 = word_ngram(bow1, 2)
    doc2 = word_ngram(bow2, 2)
    doc3 = word_ngram(bow3, 2)

    print(doc1)
    print(doc2)
    print(doc3)

    r1 = similarity(doc1, doc2)
    r2 = similarity(doc3, doc1)
    print(r1)
    print(r2)


if __name__ == '__main__':
    c = Chatbot()
    # c.kkma_execute()
    # c.okt_execute()
    # c.koran_execute_2()
    # c.load_word2vec()
    c.similarity()
