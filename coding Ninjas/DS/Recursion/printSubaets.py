arr = [1,3,4]

def handler(arr):
    ans = []
    printSubset(arr,ans)

def printSubset(inputArr,result):
    if(len(inputArr) == 0):
        print(">>>>>>>>>>>",inputArr,result)
        return

    # print(inputArr,result)
    printSubset(inputArr[1:],result)

    # result.append(inputArr[0]) // can't use append operator ? don't know why?
    # print(inputArr,result)
    printSubset(inputArr[1:],[*result, inputArr[0]]) # * is termed as splat operator


handler(arr)
