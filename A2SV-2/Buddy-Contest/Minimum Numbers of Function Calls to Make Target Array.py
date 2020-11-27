class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        for num in nums:
            binary_num = bin(num)
            count += binary_num.count("1")
            max_length = max(max_length, len(binary_num))
        return count + max_length - 3
