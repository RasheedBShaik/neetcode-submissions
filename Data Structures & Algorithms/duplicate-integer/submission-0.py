class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        for i in range(len(nums)):
            if nums[i] not in li:
                li.append(nums[i])
            else:
                return True
        return False