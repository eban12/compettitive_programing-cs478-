class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[nums[0]]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

        hare = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise
