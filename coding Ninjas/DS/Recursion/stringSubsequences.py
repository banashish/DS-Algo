# xyz =====> substing goes to  "" in recursive stack
# xyz return ["","z",'yz',"y","x","xz","xyz","xy"]


# yz return ["","z","yz","y"]

# z append empty string and empty string combined with z and return ["","z"]

# "" return empty string


string = "xyz"

def findSubstring(string):
    ans = subSequence(string)
    print(ans)

def subSequence(string):
    #base case
    if(len(string) == 0):
        return [""]

    #smaller problem
    smallAns = subSequence(string[1:])
    arr = []
    for i in smallAns:
        arr.append(i)
        arr.append(string[0]+i)

    return arr

findSubstring(string)
    
    
