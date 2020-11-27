class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        while sum(nums) > 0:
            divided = False
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    operations += 1
                    nums[i] -= 1
                
                if nums[i] != 0:
                    divided = True
                    
                nums[i] = nums[i] // 2
                
            if divided:
                operations += 1
        return operations
