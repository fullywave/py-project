txt=open('data.csv','r',encoding='utf-8')
ls=txt.readlines()
ls.reverse()
for line in ls:
    item=(line.replace('\n','')).replace(',',';')
    item=item.replace(' ','')
    print(item[::-1])