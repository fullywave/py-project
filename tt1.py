# 请在...补充一行或多行代码

def prime(m):
    num=[];
    pri=0;
    while pri<=5:
        for j in range(2,m):
            if(m%j==0):
                break
        else:
            pri=pri+1
            num.append(m)
        m=m+1
    return ",".join(str(i) for i in num);
   
    


n = eval(input())
print(prime(n))
