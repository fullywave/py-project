#汉罗塔问题
count = 0
def hannoi(n,src,dst,mid):
    global count
    if n==1 :
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else :
        hannoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hannoi(n-1,mid,dst,src)

hannoi(3,"A","C","B")
print(count)