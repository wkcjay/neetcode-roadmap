class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity = O(N)Log
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j<k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return res
