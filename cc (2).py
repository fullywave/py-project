txt=open('data.csv','r',encoding='utf-8')
ls=txt.readlines()
ls=ls.reverse()
txt.close()
for line in ls:

    item=(line.replace('\n','')).replace(',',';')
    print(item[::-1])