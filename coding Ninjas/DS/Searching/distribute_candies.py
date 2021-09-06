class Solution:
    def main(self,arr,k):
        max_value = max(arr)
        return self.binarySearch(arr,0,max_value,k)
    
    def binarySearch(self,arr,start,end,k):
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if self.check_distribution(arr,mid,k):
                ans = mid
                start = mid+1
            else:
                end = mid-1

        return ans

    def check_distribution(self,arr,val,k):
        count = 0
        for i in range(len(arr)):
            count+=(arr[i]//val)
            if count >= k:
                return True
        else:
            return False
    

if __name__ == '__main__':

    # input here
    t = int(input())
    for i in range(t):
        n, k = map(int,input().strip().split(" "))
        arr = list(map(int,input().strip().split(" ")))
        sol = Solution()
        answer = sol.main(arr,k)
        print(answer)