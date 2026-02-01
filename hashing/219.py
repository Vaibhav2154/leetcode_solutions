from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = {}
        for i,num in enumerate(nums):
            if num in seen:
                if abs(i - seen[num]) <= k:
                    return True
            seen[nums[i]] = i
        return False
