class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sol = []
        # for i in range(len(nums)):
        #     y = target - nums[i]
        #     slce = nums[i+1:]
        #     if y in slce:
        #         sol.append(i)
        #         sol.append(i+1+slce.index(y))
        # return sol
        abc = {}

        for i in range(len(nums)):
            y = target - nums[i]
            if y in abc:
                return [abc[y], i]
            abc[nums[i]] = i
        return []