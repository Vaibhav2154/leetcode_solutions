from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in mpp:
                return [mpp[num2],i]
            mpp[num] = i
        return []
