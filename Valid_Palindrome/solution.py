# O(n) time | O(1) space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftIdx = 0
        rightIdx = len(s) - 1

        while leftIdx < rightIdx:
            if not s[leftIdx].isalnum():
                leftIdx += 1
            elif not s[rightIdx].isalnum():
                rightIdx -= 1
            elif s[leftIdx].lower() == s[rightIdx].lower():
                leftIdx += 1
                rightIdx -= 1
            else:
                return False
        return True
