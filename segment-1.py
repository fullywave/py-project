from jpype import * 
from pyhanlp import *
import time


#完全切分
#完全切分指的是，找出一段文本中的所有单词。
def fully_segment(text,dic):
    word_list=[];
    for i in range(len(text)):
        for j in range(i+1,len(text)+1):
            word=text[i:j]
            if word in dic:
                word_list.append(word)

    return word_list

def load_dictionary():
    """
    加载hanlp的mini词库
    ：return:一个set形式词库
    """
    IOUtil=JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path=HanLP.Config.CoreDictionaryPath.replace('.txt','.mini.txt')
    dic=IOUtil.loadDictionary([path])
    return set(dic.keySet())





def forward_segment(text,dic):
    word_list=[]
    i=0
    while i<len(text): 
        longest_word=text[i]
        for j in range(i+1,len(text)+1):
            word=text[i:j]
            if word in dic:
                if len(word)>len(longest_word):
                    longest_word=word
        word_list.append(longest_word)
        i+=len(longest_word)
    return word_list



#逆向最长匹配


def backward_segment(text,dic):
    word_list=[]
    i=len(text)-1
    while i>=0:
        longest_word=text[i]
        for j in range(0,i):
            word=text[j:i+1]
            if word in dic:
                if len(word)>len(longest_word):
                    longest_word=word
                    break
        word_list.insert(0,longest_word)
        i-=len(longest_word)
    return word_list

#统计单字成词的个数
def count_single_char(word_list:list):
    return sum(1 for word in word_list if len(word)==1)

#词数更少优先级更高
def bidirectional_segment(text,dic):
    f=forward_segment(text,dic)
    b=backward_segment(text,dic)
    if len(f)<len(b) :#词数少优先级高
        return f
    elif len(f)>len(b):
        return b

    else:
        if count_single_char(f)<count_single_char(b): #单字更少优先级更高
            return f
        else:
            return b
            



#速度评测
def evaluate_speed(segment,text,dic):
    startTime=time.time()
    for i in range(10000):
        segment(text,dic)
    elapsed_time=time.time()-startTime
    print('%.2f 万字每秒'%(len(text)*pressure/10000/elapsed_time))
       


if __name__ == '__main__':
    dic=load_dictionary()
    text='江西鄱阳湖干枯，中国最大淡水湖变最大草原'
    pressure=10000
    evaluate_speed(forward_segment,text,dic)
    evaluate_speed(backward_segment,text,dic)
    evaluate_speed(bidirectional_segment,text,dic)







    