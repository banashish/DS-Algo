# Link: https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = { word : 1 for word in words }
        words.sort(key = lambda word: len(word))
        answer = 1
    
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[prev] + 1,dp[word])
                    answer = max(answer,dp[word])
                    
        return answer
                    
        