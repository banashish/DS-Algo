def main(arr):
    return mergeSort(arr,0,len(arr))

def mergeSort(arr,start,end):
    inversion = 0
    if start < end:
        mid = (start+end) // 2
        inversion+=mergeSort(arr,start,mid)
        inversion+=mergeSort(arr,mid+1,end)
        inversion+=merge(arr,start,mid,end)

    return inversion

def merge(arr,start,mid,end):
    temp_arr = [0]*len(arr)
    i = start
    j = mid+1
    k = start
    inv = 0

    while i <= mid and j < end:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k] = arr[j]
            k+=1
            j+=1
            inv+=(mid - i + 1)
    
    while i<= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1

    while j< end:
        temp_arr[k] = arr[j]
        j+=1
        k+=1

    for x in range(start,end):
        arr[x] = temp_arr[x]
    
    return inv




if __name__ == '__main__':
    # arr = list(map(int,input().strip().split(" ")))
    arr = [2,5,1,3,4,6]
    ans = main(arr)
    print(ans)