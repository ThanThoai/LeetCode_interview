
def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    m = {}
    j = 0
    for i in range(1, n + 1):
        if s[i - 1] in m.keys():
            j = max(max(m[s[i - 1]]), j)
        else:
            m[s[i - 1]] = []
        ans = max(ans, i - j)
        m[s[i - 1]].append(i)
    return ans
            
            
            