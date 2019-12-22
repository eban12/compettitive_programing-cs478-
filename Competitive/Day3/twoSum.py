def twoSum(nums, target):
        compliments = {}
        for i in range(len(nums)):
            compliments[target - nums[i]] = i
        
        for j in range(len(nums)):
            if nums[j] in compliments and j != compliments[nums[j]]:
                return [compliments[nums[j]],j]
        return