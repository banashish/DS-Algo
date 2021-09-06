class Solution:
    def main(self,windows):
        start = 0
        end = max(windows)
        ans = 0
        while start <= end:
            mid = (start+end) // 2
            if self.check(windows,mid):
                ans = mid
                end = mid-1
            else:
                start = mid + 1
        

if __name__ == '__main__':

    # input here
    number = int(input().strip())
    windows = list(map(int,input().strip().split(" ")))
    sol = Solution()
    answer = sol.main(windows)
    print(answer)