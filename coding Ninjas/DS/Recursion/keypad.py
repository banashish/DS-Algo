def helper(number):
    dictionary = {
        2 : "abc",
        3 : "def",
        4 : "ghi",
        5 : "jkl",
        6 : "mno",
        7 : "pqrs",
        8 : "tuv",
        9 : "wxyz" 
    }

    return dictionary.get(number)

def findKeypadPatterns(number):
     
     ans = recursiveCall(number)
     print(ans)

def recursiveCall(num):
    if(num == 0):
        return [""]
    
    ans = recursiveCall(int(num/10))

    string = helper(int(num%10))

    arr = []

    for i in ans:
        for j in string:
            arr.append(i+j)


    return arr

findKeypadPatterns(247)




