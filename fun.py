#fun.py
def fact(n,m=1):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m

print(fact(4))
print(fact(4,2))