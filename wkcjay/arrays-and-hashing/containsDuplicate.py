class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num in temp:
                return True    
            temp.add(num)
        return False