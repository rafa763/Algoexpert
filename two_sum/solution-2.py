# O(n) time | O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      di = {}
      for i in range(len(nums)):
        y = target - nums[i]
        if y in di:
          return [i, di[y]]
        di[nums[i]] = i
