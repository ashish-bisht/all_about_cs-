# Leetcode 66

# Time complexity O(n)
# Space complexity O(1)

def plus_one(nums):
    nums[-1] += 1

    for i in reversed(range(1, len(nums))):
        if nums[i] == 10:
            nums[i-1] += 1
            nums[i] = nums[i] % 10

    if nums[0] == 10:
        nums[0] = 1
        nums.append(0)

    return nums


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([0]))
print(plus_one([9, 9, 9]))
