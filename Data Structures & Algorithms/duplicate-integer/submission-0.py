class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        if len(set(nums))==len(nums):
            return False
        else:
            return True
        