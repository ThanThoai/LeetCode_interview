class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        ans = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(ans) <= len(s[i:]):
                if s[i : j] == s[i : j][: : -1] and len(s[i : j]):
                    ans = s[i : j]
        return ans
    