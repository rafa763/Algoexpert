# O(n) time | O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for n in nums:
            if n in di:
                return True
            di[n] = True
        return False
