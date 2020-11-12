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

def handler(number):
    printCombination(number,"")

def printCombination(input,output):
    if(input == 0):
        print(output)
        return 
    
    string = helper(int(input%10))

    for i in string:
        printCombination(int(input/10),i+output) 

handler(23)