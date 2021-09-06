# this is a modification in count inversion problem

def countInversionUsingMergeSort(arr):
    temp_arr = [0]*len(arr)
    ans = [0]*len(arr)
    return mergeSort(arr,temp_arr,0,len(arr)-1,ans)

def mergeSort(arr,temp_arr,left,right,answer):
    inv_count = 0
    li,ri,mi = 0,0,0
    if left < right:
        mid = (left + right) // 2

        li = mergeSort(arr,temp_arr,left,mid,answer)
        ri = mergeSort(arr,temp_arr,mid+1,right,answer)

        mi = merge(arr,temp_arr,mid,left,right,answer)

    answer[left] = ri+mi
    print(answer)
    return inv_count

def merge(arr,temp_arr,mid,left,right,answer):
    i = left
    j = mid + 1
    k = left
    inv = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k] = arr[j]
            inv+=(mid - i + 1)
            # answer[k]+=inv
            k+=1
            j+=1

    while i <= mid:
        temp_arr[k] = arr[i]
        k+=1
        i+=1

    while j <= right:
        temp_arr[k] = arr[j]
        k+=1
        j+=1

    for w in range(left,right+1):
        arr[w]  = temp_arr[w]

    return inv
        


if __name__ == "__main__":
    arr = list(map(int,input().split(" ")))
    answer = countInversionUsingMergeSort(arr)
    print(answer)
