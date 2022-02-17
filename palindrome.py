class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s:
            result = []
            for c in s.lower():
                if c.isalnum():
                    result.append(c)
            return result[::-1] == result
        else:
            return True

