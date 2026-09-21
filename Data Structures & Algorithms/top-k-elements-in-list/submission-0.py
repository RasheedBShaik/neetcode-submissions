class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dici = {}
        for num in nums:
            dici[num] = dici.get(num, 0) + 1
            
        # Sort keys based on their values (frequencies) in descending order
        sorted_nums = sorted(dici.keys(), key=lambda x: dici[x], reverse=True)
        
        # Return the first k elements
        return sorted_nums[:k]
