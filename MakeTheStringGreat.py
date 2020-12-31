class Solution(object):
    def makeGood(self, s : str) -> str:
        # print(s)
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            if s.islower() or s.isupper():
                return s
            idx = -1
            for i in range(len(s) - 1):
                # print(s[i])
                if s[i].islower() and s[i + 1].isupper() and s[i] == s[i + 1].lower():
                    idx = i
                    break
                elif s[i].isupper() and s[i + 1].islower() and s[i].lower() == s[i + 1]:
                    idx = i
                    break
            if idx >= 0:
                return self.makeGood(s[:i] + s[i + 2:])
            else:
                return s


if __name__ == "__main__":
    test_str = 'abBAcC'
    sol = Solution()
    print(sol.makeGood(test_str))


        