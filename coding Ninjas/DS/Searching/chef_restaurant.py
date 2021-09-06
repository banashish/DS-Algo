import bisect
class Solution:
    def main(self,timeinterval,times):
        timeinterval.sort(key=lambda x : x[0])
        self.chefRes(timeinterval,times)
    
    def chefRes(self,timeinterval,times):
        min_values = []
        largest = timeinterval[-1][1]
        for interval in timeinterval:
            min_values.append(interval[0])
        
        for i in range(len(times)):
            ans = -1
            index = bisect.bisect_right(min_values,times[i])
            if index == 0:
                    ans = timeinterval[index][0] - times[i]
                    print(ans)
                    continue
            else:
                if times[i] < timeinterval[index - 1][1]:
                    ans = 0
                    print(ans)
                    continue
                else:
                    if index < len(timeinterval):
                        ans = timeinterval[index][0] - times[i]
            print(ans)
        

if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        n,m = map(int,input().strip().split(" "))
        timeinterval = []
        time = []
        for j in range(n):
            timeinterval.append(tuple(map(int,input().strip().split(" "))))
        for _ in range(m):
            time.append(int(input().strip()))
    sol = Solution()
    answer = sol.main(timeinterval,time)