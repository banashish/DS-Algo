import bisect
class Solution:
    def main(self,costs,day):
        # idx = bisect.bisect_right(costs,day)
        # print(idx,day-costs[idx-1])

        start = 0
        end = len(costs) - 1
        ans = 0
        while start <= end:
            mid = (start+end) // 2
            if day < costs[mid]:
                ans = mid
                end = mid -1
            else:
                start = mid + 1
        print(start,day-costs[start-1])




if __name__ == '__main__':

    # input here
    shops = int(input().strip())
    arr = list(map(int,input().strip().split(" ")))
    costs = [arr[0]]
    for i in range(1,shops):
        costs.append(costs[i-1]+arr[i])
    ndays = int(input().strip())
    for _ in range(ndays):
        sol = Solution()
        answer = sol.main(costs,int(input().strip()))