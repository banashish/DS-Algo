arr = [4,5,6]
target = 9

def handler(arr,target):
    answer = targetProblem(arr,target)
    result = []
    for i in answer:
        if(sum(i) == target):
            result.append(i)

    print(result)

def targetProblem(inputArr,target):
    if(len(inputArr) == 0):
        return [[]]

    smallAns = targetProblem(inputArr[1:],target)

    arr = []
    for i in smallAns:
        arr = arr + [i]
        arr = arr + [i + [inputArr[0]]]

    return arr



handler(arr,target)

