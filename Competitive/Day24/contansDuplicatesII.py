class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dics = {}
        for i in range(len(nums)):
            if nums[i] in dics.keys() and abs(dics[nums[i]] - i) <= k:
                return True
            else:
                dics[nums[i]] = i
        return False
                
