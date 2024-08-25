class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            second_val = target - nums[i]
            if second_val in temp:
                return [temp[second_val],i]
            temp[nums[i]] = i