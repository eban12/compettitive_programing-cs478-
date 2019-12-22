def sortColors(nums):
        count = {0:0,1:0,2:0}
        for i in nums:
            count[i] += 1

        idx = 0
        for key in count:
            for i in range(count[key]):
                nums[idx] = key
                idx += 1