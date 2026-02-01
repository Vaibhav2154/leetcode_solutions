from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        left = 0
        window = set()

        for right in range(n):
            if right - left > k:
                 window.remove(nums[left])
                 left +=1
            if nums[right] in window:
                return True
            window.add(nums[right])
            # print(window)
        
        return False