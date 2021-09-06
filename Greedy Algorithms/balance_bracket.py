def main(arr):
    pos = []
    for i in range(len(arr)):
        if arr[i] == '[':
            pos.append(i)
    
    p = 0
    count = 0
    sum = 0

    for i in range(len(arr)):
        if arr[i] == '[':
            p+=1
            count+=1
        elif arr[i] == ']':
            count-=1

        if count < 0:
            sum+=pos[p]-i
            arr[i],arr[pos[p]] = arr[pos[p]],arr[i]

            p+=1
            count = 1

    return sum 

    


if __name__ == '__main__':
    s = "[[][]]"
    answer = main(list(s))
    print(answer)