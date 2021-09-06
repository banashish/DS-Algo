def main(cows,minDistance,arr):
    arr.sort()
    ans = binarySearch(0,arr[cows-1],arr,minDistance)
    return ans

def binarySearch(start,end,arr,minDis):
    while start <=  end:
        mid = (start + end) // 2
        print(mid)
        if checkExists(arr,mid,minDis):
            # print(mid)
            d = mid
            start = mid+1
        else:
            end = mid -1
    
    return d

def checkExists(arr,mid,cows):
    j = 0
    for i in range(cows-1):
        x = j+1
        if x >= len(arr):
            return False
        while arr[x] - arr[j] < mid:
            if x >= len(arr)-1:
                return False
            x+=1
        j = x
    else:
        return True



if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
        # l,cows = map(int,input().split(" "))
        # stalls = list(map(int,input().strip().split(" ")))
    l = 6
    cows = 6
    stalls = sorted([6,5,12,1,7,9])
    ans = main(l,cows,stalls)
    print(ans)