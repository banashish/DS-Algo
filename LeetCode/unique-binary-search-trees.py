# Link: https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        return self.dp_helper(n)
        
    def rec_helper(self,n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        unique = 0
        
        for i in range(1,n+1):
            left = self.rec_helper(i-1)
            right = self.rec_helper(n-i)
            unique += left*right
            
        return unique
    
    def dp_helper(self,n):
        cache = [0]*(n+1)
        cache[0] = 1
        cache[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                cache[i] +=cache[j]*cache[i-j-1]
                
        return cache[-1]
        