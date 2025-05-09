
# Approach 1: Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in visited:
                return [visited[pair], i]
            visited[nums[i]] = i


# Approach 2: Two Pointers after Sorting
class SolutionSorted:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = [(num, idx) for idx, num in enumerate(nums)]
        sorted_nums.sort()

        i = 0
        j = len(nums) - 1

        while i < j:
            total = sorted_nums[i][0] + sorted_nums[j][0]
            if total == target:
                return sorted([sorted_nums[i][1], sorted_nums[j][1]])
            elif total > target:
                j -= 1
            else:
                i += 1
