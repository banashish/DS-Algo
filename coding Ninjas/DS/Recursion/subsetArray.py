arr = [15,20,12]

def handler(arr):
    ans = subsetArray(arr)
    print(ans)

def subsetArray(arr):
    if(len(arr) == 0):
        return [[]]

    smallAns = subsetArray(arr[1:])
    # print(smallAns)
    ans =  []
    print(smallAns)

    for i in smallAns:
        ans.append(i)
        # print(type(i))
       
        # x = i.append(arr[0])
        if(ans == None):
            print("hello i am none")
        # print(ans,type(ans))
        # ans.append(x) 
    
    # print(ans)
    # z = []
    # for i in range(len(ans)):
    #     z.append(ans[i])
    #     z[i].append(arr[0])
    #     # ans.append(i.append(arr[0]))
        
    # for i in z:
    #     ans.append(z)
    # print(ans)
    return ans

handler(arr)


