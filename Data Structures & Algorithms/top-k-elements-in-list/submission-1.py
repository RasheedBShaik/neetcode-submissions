class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        '''

        dici = {}

        for num in nums:
            dici[num] = dici.get(num,0)+1

        sorted_dici = sorted(dici,key = dici.get, reverse = True)
        return sorted_dici[:k]