def main(arr):
    arr.sort()
    i = 0
    j = len(arr)-1
    arr2 = []
    ans = 0
    while i < j:
        arr2.append(arr[i])
        arr2.append(arr[j])
        i+=1
        j-=1
    if i == j:
        arr2.append(arr[i])
    print(arr)

    for i in range(0,len(arr2)-1):
        ans+=abs(arr2[i]-arr2[i+1])
    ans+=abs(arr2[len(arr2)-1]-arr2[0])

    print(ans)
        



if __name__ == '__main__':
    arr = [1, 2, 4, 8]
    main(arr)