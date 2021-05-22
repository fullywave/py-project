import jieba
import wordcloud
txt="程序设计语言是计算机能够理解\
    识别用户操作意图的一种交互体系，它按照\
    特定规则组织计算机指令。能够使计算机自动\
        进行个只能怪运算处理"
w=wordcloud.WordCloud( width=1000,height=700,font_path="msyh.ttc")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")