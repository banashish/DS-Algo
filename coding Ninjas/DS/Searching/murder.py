class Solution:
    def main(self,arr,n):
        return self.mergeSort(arr,0,n-1)

    def mergeSort(self,arr,start,end):
        count = 0
        if start < end:
            mid = (start + end) // 2
            count+=(self.mergeSort(arr,start,mid))
            count+=(self.mergeSort(arr,mid+1,end))
            count+=(self.merge(arr,start,mid,end))

        return count

    def merge(self,arr,start,mid,end):
        count = 0
        temp = [0]*len(arr)

        i = start
        j = mid+1
        k = start

        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                count+=((end-j+1)*arr[i])
                temp[k] = arr[i]
                i+=1
                k+=1
            else:
                temp[k] = arr[j]
                j+=1
                k+=1

        while i <= mid:
            temp[k] = arr[i]
            i+=1
            k+=1

        while j <= end:
            temp[k] = arr[j]
            j+=1
            k+=1

        for i in range(start,end+1):
            arr[i] = temp[i]

        return count


        
        

if __name__ == '__main__':

    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split(" ")))
        sol = Solution()
        answer = sol.main(arr,n)
        print(answer)