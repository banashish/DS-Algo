def checkNumber(arr,x):
    if(len(arr) == 1):
        if(arr[0] == x):
            return True
        else:
            return False

    if(arr[0] == x):
        return True
    smallAnswer = checkNumber(arr[1:],x)
    return smallAnswer
    # if(smallAnswer == True):
    #     return True
    # else:
    #     return False



ans = checkNumber([1,2,3,4,5],1)
print(ans)