'''
Problem Statement
Leetcode 75 Sort colors (Dutch National Flag problem)
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
'''


# mycode
# 双指针一次遍历 见resolution
# 单指针，两次遍历
def dutch_flag_sort(nums):
    ptr = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[ptr], nums[i] = nums[i], nums[ptr]
            ptr += 1

    for j in range(len(nums)):
        if nums[j] == 1:
            nums[ptr], nums[j] = nums[j], nums[ptr]
            ptr += 1

    return


#forward-backward 两次遍历，双指针
def dutch_flag_sort(nums):
    pivot_value = 1

    left = 0
    for i in range(len(nums)):
        if nums[i] < pivot_value:
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp
            left += 1

    right = len(nums) - 1
    for j in range(-1, -len(nums) - 1, -1):
        if nums[j] > pivot_value:
            temp = nums[j]
            nums[j] = nums[right]
            nums[right] = temp
            right -= 1

    return


# resolution
def dutch_flag_sort(nums):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1

    low, high = 0, len(nums) - 1
    i = 0
    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            i += 1
            low += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[high] = nums[high], nums[i]
            # decrement 'high' only, after the swap the number at index could be 0,1,2
            high -= 1
    return


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)


main()

'''
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

Space complexity #
The algorithm runs in constant space O(1).
'''
