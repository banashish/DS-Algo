# Array is without duplicates.

arr = [1,2,3]

def callRecursiveSum(arr,n):
    result = []
    subset = []
    call(arr,0,result,subset)

def call(arr,n,result,subset):

    subset = []

    if(len(arr) == 0):
        return 
    
    for i in range(len(n,arr)):
        subset.append(arr[i])
        

    


def printSubset(arr):
    
    arr = sorted(arr)
    n = len(arr)
    callRecursiveSum(arr,n)

