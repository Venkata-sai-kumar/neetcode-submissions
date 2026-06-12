class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            if not num in duplicate:
                duplicate[num] = 1
            else: 
                duplicate[num] += 1
        for num, k in duplicate.items():
            if k > 1:
                return True
        return False