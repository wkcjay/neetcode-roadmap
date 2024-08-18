class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for i in nums:
            if i in tracker:
                return True
            tracker.add(i)
        return False
