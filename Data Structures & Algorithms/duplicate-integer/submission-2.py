class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = list(set(nums))
        return len(nums) != len(dup)