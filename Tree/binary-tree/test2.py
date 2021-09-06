# input List("abc","bac","def","edf","sdf")
# output List(List ("abc","bac"),List("def","edf"),List("sdf"))

from collections import Counter
def main(arr):
    res = []
    counter = sorted(list(map(sorted,arr)))
    start,end = 0,0
    last = counter[0]
    for i in range(1,len(counter)):
        if last == counter[i]:
            end+=1
        else:
            last = counter[i]
            res.append(counter[start:end+1])
            start = i
            end =start
    
    res.append(counter[start:end+1])

    print(res)

            



if __name__ == '__main__':
    arr = ["abc","bac","def","edf","sdf","cab"]
    main(arr)