def main(L,T):
    pairs = []
    for i in range(len(L)):
        pairs.append((L[i],T[i],i+1))

    pairs.sort(reverse=True,key = lambda x: x[0]/x[1])
    def printNumber(n):
        return n[2]
    x = map(printNumber,pairs)
    print(list(x))


if __name__ == '__main__':
     L = [1, 2, 3, 5, 6]
     T = [2, 4, 1, 3, 2]
     main(L,T)