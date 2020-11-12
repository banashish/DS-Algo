def findNumber(arr,x,startIndex):
    if(startIndex == len(arr)-1):
        if arr[startIndex] == x:
            return startIndex
        else:
            return -1

    if(arr[startIndex] == x):
        return startIndex
    else:
        found = findNumber(arr,x,startIndex+1)

    return found

arr = [1,2,3,4]
print(findNumber(arr,1,0))