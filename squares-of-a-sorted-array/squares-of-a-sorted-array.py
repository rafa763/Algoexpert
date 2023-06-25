# O(n) time | O(n) space

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftIdx = 0
        rightIdx = len(nums) - 1
        result = [0] * len(nums)

        for idx in reversed(range(len(nums))):
            leftValue = abs(nums[leftIdx])
            rightValue = abs(nums[rightIdx])
            if leftValue > rightValue:
                result[idx] = leftValue ** 2
                leftIdx += 1
            else: 
                result[idx] = rightValue ** 2
                rightIdx -= 1
        return result
