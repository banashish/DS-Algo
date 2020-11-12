# [15, 2, 8, 9, 10, 11, 16] sa = true bit it return false
# [2, 8, 9, 10, 11, 16] sa = true
# [8, 9, 10, 11, 16] sa = true
# [9, 10, 11, 16] sa = true
# [10, 11, 16] sa = true
# [11, 16]  sa = true
# [16]

arr = [15,2,8,9,10,11,16]

def checkSorted(arr):
    print(arr)
    if(len(arr) <= 1):
        return True
    smallAnswer = checkSorted(arr[1:len(arr)])
    # check if previous iteration had returned false so it need not check for further recursions
    if(smallAnswer == False):
        return False
    if(arr[0] <= arr[1]):
        return True
    else:
        return False

answer = checkSorted(arr)
print(answer)