'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        result = []
        for i in range(len(nums) - 1):
            other = target - nums[i]
            if other in nums[i+1:]:
                result.append(i)
                result.append(nums[i+1:].index(other) + i + 1)
        return result

solution = Solution()
nums = [3, 3]
target = 6
print(solution.twoSum(nums, target))