def main(arr,k):
    while k > 0:
        smallest = min(arr)
        if smallest == 0:
            break
        idx = arr.index(smallest)
        arr[idx] = -smallest
        k-=1
    print(sum(arr))



if __name__ == '__main__':
    arr = [9,8,8,5]
    k = 3
    main(arr,k)