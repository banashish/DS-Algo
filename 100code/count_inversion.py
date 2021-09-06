def countInversion(arr):
    inversions = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                inversions+=1

    return inversions

def countInversionUsingMergeSort(arr):
    temp_arr = [0]*len(arr)
    ans = [0]*len(arr)
    return mergeSort(arr,temp_arr,0,len(arr)-1)

def mergeSort(arr,temp_arr,left,right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count+= mergeSort(arr,temp_arr,left,mid)
        inv_count+= mergeSort(arr,temp_arr,mid+1,right)

        inv_count+=merge(arr,temp_arr,mid,left,right)

    return inv_count

def merge(arr,temp_arr,mid,left,right):
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
            k+=1
            j+=1
            inv+=(mid - i + 1)

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
    answer = countInversion(arr)
    answer = countInversionUsingMergeSort(arr)
    print(answer)
