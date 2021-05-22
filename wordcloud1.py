import wordcloud

#配置对象参数
#加载词云文件
#输出词云文件
txt="life is short, you need python"
c = wordcloud.WordCloud(background_color="red")
c.generate(txt)
c.to_file('pycloud.png')