import pandas as pd
import matplotlib as mpl
import numpy as np
from nltk.probability import FreqDist
import time

from data_utils import get_qa_data
from jieba_utils import Seg
from sentence_sim import SentenceSimilarity

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # enable chinese


def read_corpus():
    qList = []
    # 问题的关键词列表
    qList_kw = []
    aList = []
    path = './WebQA.v1.0/me_train.json'
    data = get_qa_data(path)
    for t in data:
        qList.append(t[0])
        qList_kw.append(seg.cut(t[0]))
        aList.append(t[1])
    return qList_kw, qList, aList


def plot_words(wordList):
    fDist = FreqDist(wordList)
    # print(fDist.most_common())
    print("单词总数: ", fDist.N())
    print("不同单词数: ", fDist.B())
    fDist.plot(10)


if __name__ == '__main__':
    # 设置外部词
    seg = Seg()
    # seg.load_userdict('userdict.txt')
    # 读取数据
    List_kw, questionList, answerList = read_corpus()
    # 初始化模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(questionList)
    ss.TfidfModel()  # tfidf模型
    # ss.LsiModel()         # lsi模型
    # ss.LdaModel()         # lda模型

    while True:
        question = input("请输入问题(q退出): ")
        if question == 'q':
            break
        time1 = time.time()
        question_k = ss.similarity_k(question, 5)
        print("亲，我们给您找到的答案是： {}".format(answerList[question_k[0][0]]))
        for idx, score in zip(*question_k):
            print("same questions： {},                score： {}".format(questionList[idx], score))
        time2 = time.time()
        cost = time2 - time1
        print('Time cost: {} s'.format(cost))
