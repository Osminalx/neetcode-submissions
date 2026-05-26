class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_locator = {}
        for i in range(len(nums)):
            if nums[i] in num_locator:
                return [num_locator[nums[i]], i]

            complement = target - nums[i]
            num_locator[complement] = i