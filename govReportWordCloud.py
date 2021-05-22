import jieba
import wordcloud
from scipy.misc import imread
mask=imread("cloud_1.png")
f=open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(max_words=50,mask=mask,font_path="msyh.ttc",background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")