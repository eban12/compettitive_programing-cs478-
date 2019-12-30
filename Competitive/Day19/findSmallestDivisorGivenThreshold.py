class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        small = max(nums)
        while l <= r:
            mid = (l + r) // 2
            temp = 0
            for i in nums:
                temp = temp + (-(-i//mid))
            if temp <= threshold and mid < small:
                small = mid
                r = mid - 1
            else:
                l = mid + 1
        return small
