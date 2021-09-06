def main(start,end,k):
    pairs = []
    selected = []
    for i in range(len(start)):
        pairs.append((start[i],end[i]))
    pairs.sort(key=lambda x : x[1])
    i = 0
    selected.append(pairs[i])
    for x in range(1,len(pairs)):
        if pairs[x][0] > pairs[i][1]:
            selected.append(pairs[x])
            i = x

    print(selected)

    


if __name__ == '__main__':
    start = [1,8,3,2,6]
    end = [5,10,6,5,9]
    k = 2
    main(start,end,k)