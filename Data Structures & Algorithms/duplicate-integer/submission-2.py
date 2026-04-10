class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        n_set = len(nums_set)
        n = len(nums)
        if n != n_set:
            return True
        return False