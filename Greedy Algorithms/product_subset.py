def main(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    
    prod = 1
    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    for i in arr:
        if i == 0:
            count_zero+=1
            continue
        if i < 0:
            count_neg+=1
            max_neg = max(i,max_neg)
        prod = prod * i

    if count_zero == n:
        return 0
    
    if prod < 0:
        if count_neg == 1 and count_zero > 0 and count_neg + count_zero == n:
            return 0
        prod = int(prod/max_neg)
    return prod

    


if __name__ == '__main__':
    a = [-1,-1,-2,4,3]
    print(main(a))