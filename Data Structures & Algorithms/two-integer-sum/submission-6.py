class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            check = target - value
            if check in hash_map:
                return [hash_map[check], index]
            else:
                hash_map[value] = index
        return None