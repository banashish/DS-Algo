def main(arr,space):
    police = []
    thieves = []
    j = 0
    k = 0
    answer = 0
    for i in range(len(arr)):
        if arr[i] == 'P':
            police.append(i)
        elif arr[i] == 'T':
            thieves.append(i)

    while j < len(police) and k < len(thieves):
        if (abs(thieves[k] - police[j])) <= space:
            j+=1
            k+=1
            answer+=1

        elif thieves[k] < police[j]:
            k+=1
        else:
            j+=1

    return answer

if __name__ == '__main__':
    arr = ['P', 'T', 'T', 'P', 'T']
    k = 2
    answer = main(arr,k)
    print(answer)