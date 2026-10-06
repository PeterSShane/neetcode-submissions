class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for i in range(len(nums)):
            real_target = target - nums[i]
            if real_target in n_map:
                return [n_map[real_target], i]
            n_map[nums[i]] = i



