def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if(size%2==0):
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med =numbers[size//2]
    return med



n=[1,2,3,4,5,6]
print(median(n))
