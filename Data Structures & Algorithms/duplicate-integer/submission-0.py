class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        nums2 = list(mySet)
        if len(nums) != len(nums2):
            return True

        else:
            return False
        