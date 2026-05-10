class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_list = list(set(nums))

        if len(nums_list) == len(nums):
            return False

        r = 0

        while r < len(nums):
            window = nums[r:(k + r + 1)]

            if len(set(window)) != len(window):
                return True

            r += 1

        return False