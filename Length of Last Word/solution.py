# O(n) time | O(1) space

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(s):
            if i == ' ' and count == 0:
                continue
            elif i != ' ':
                count += 1
            else:
                return count
        return count
