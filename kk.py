#定义数据文件格式
#编写程序，根据文件接口解析参数绘制图形
#绘制数据文件
import turtle as t
t.title('自动绘制轨迹')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
#数据读取
datals=[]
f=open('data.txt')
for line in f:
    line=line.replace('\n',"")
    datals.append(list(map(eval,line.split(","))))
f.close()

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.right(datals[i][2])