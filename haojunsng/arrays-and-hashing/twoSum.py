# Time: O(N)
# Space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = dict()
        for index, val in enumerate(nums):
            temp = target - val
            if temp in tracker:
                return [tracker.get(temp), index]
            tracker[val] = index
