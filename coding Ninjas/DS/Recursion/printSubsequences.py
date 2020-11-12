#not needed to return subsequences instead we need to print them

string = "xy"

def handler(string):
    #here empty string is the output string
    printSubsequences(string,"")

def printSubsequences(input,outputHandler):
    if(len(input) == 0):
        print(outputHandler)
        return

    #case when we chose not to include the first char of input string
    printSubsequences(input[1:],outputHandler)

    #case when we chose to include the first char of input string
    printSubsequences(input[1:],outputHandler + input[0])

handler(string)