# leetcode 75..

# Time Complexity :: O(n)
# Space Complexity :: O(1)

def sort_colors(nums):

    left = 0
    cur = 0
    right = len(nums)-1

    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            left += 1
            cur += 1

        elif nums[cur] == 2:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1

        else:
            cur += 1

    return nums


print(sort_colors([2, 0, 2, 1, 1, 0]))
print(sort_colors([2, 0, 1]))
print(sort_colors([0]))
print(sort_colors([1]))
