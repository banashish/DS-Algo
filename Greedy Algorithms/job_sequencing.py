def main(arr,maxTime):
    jobs = []
    for i in arr:
        jobs.append(tuple(i))

    jobs.sort(reverse=True,key= lambda x : x[2])
    
    busy = [False]*(maxTime)
    jobs_done = []

    for i in range(len(jobs)):
        for j in range(jobs[i][1]-1,-1,-1):
            if not busy[j]:
                busy[j] = True
                jobs_done.append(jobs[i][0])
                break

    print(jobs_done)


if __name__ == '__main__':
    arr = [[1, 9, 15],  # Job Array
       [2, 2, 2],
       [3, 5, 18],
       [4, 7, 1],
       [5, 4, 25],
       [6, 2, 20],
       [7, 5, 8],
       [8, 7, 10],
       [9, 4, 12],
       [10, 3, 5]
       ]
    main(arr,9)