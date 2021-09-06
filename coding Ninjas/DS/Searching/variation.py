class Solution:
    def main(self,nums,k):
        variation = 0
        nums.sort()
        n = len(nums)
        i = 0;
        j = 1
        # for i  in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[j] - nums[i] >= k:
        #             variation+=(n-j)
        #             break
        
        # print(variation)

        while j < n:
            if nums[j] - nums[i] >= k:
                variation+=(n-j)
                i+=1
            else:
                j+=1

        print(variation)




if __name__ == '__main__':

    # input here
    n,k = map(int,input().strip().split(" "))
    nums = list(map(int,input().strip().split(" ")))
    sol = Solution()
    sol.main(nums,k)