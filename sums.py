from typing import List

class Sums:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return [] 
'''
def test_sums():
    sums_calculator = Sums()

    # Test threeSum
    nums_three_sum = [-1, 0, 1, 2, -1, -4]
    result_three_sum = sums_calculator.threeSum(nums_three_sum)
    expected_three_sum = [[-1, -1, 2], [-1, 0, 1]]
    assert result_three_sum == expected_three_sum, f"Test failed for threeSum. Expected {expected_three_sum}, got {result_three_sum}"

    # Test twoSum
    nums_two_sum = [2, 7, 11, 15]
    target_two_sum = 9
    result_two_sum = sums_calculator.twoSum(nums_two_sum, target_two_sum)
    expected_two_sum = [0, 1]
    assert result_two_sum == expected_two_sum, f"Test failed for twoSum. Expected {expected_two_sum}, got {result_two_sum}"

    print("All tests passed successfully!")

test_sums()
'''    
def test_sums():
    sums_calculator = Sums()

    # Test threeSum with user input
    nums_three_sum = [int(x) for x in input("Enter a list of integers for threeSum (comma-separated): ").split(",")]
    result_three_sum = sums_calculator.threeSum(nums_three_sum)
    print(f"threeSum result: {result_three_sum}")

    # Test twoSum with user input
    nums_two_sum = [int(x) for x in input("Enter a list of integers for twoSum (comma-separated): ").split(",")]
    target_two_sum = int(input("Enter the target sum for twoSum: "))
    result_two_sum = sums_calculator.twoSum(nums_two_sum, target_two_sum)
    print(f"twoSum result: {result_two_sum}")

test_sums()

