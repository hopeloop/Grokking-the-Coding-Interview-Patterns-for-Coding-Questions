'''
Problem Challenge 3

Minimum Window Sort (medium)

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''


# mycode
def shortest_window_sort(nums):
    sorted_arr = sorted(nums)
    count = 0

    for left in range(len(nums)):
        if nums[left] == sorted_arr[left]:
            count += 1
        else:
            break
        if count == len(nums):
            return 0

    for right in range(len(nums) - 1, -1, -1):
        if nums[right] == sorted_arr[right]:
            count += 1
        else:
            break

    return len(nums) - count


# answer
'''
算法：
1.找到左右两边第一个破坏顺序的数的位置，为left,right
2.找出[left,right]数组的最大值和最小值
3.找出[:left]和[right:]中第一个大于最大值和第一小于最小值的元素
'''
import math


def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1
    # find the first number out of sorting order from the beginning
    while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
        low += 1

    if low == len(arr) - 1:  # if the array is sorted
        return 0

    # find the first number out of sorting order from the end
    while (high > 0 and arr[high] >= arr[high - 1]):
        high -= 1

    # find the maximum and minimum of the subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while (low > 0 and arr[low - 1] > subarray_min):
        low -= 1
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while (high < len(arr) - 1 and arr[high + 1] < subarray_max):
        high += 1

    return high - low + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()

'''
Time complexity 
The time complexity of the above algorithm will be O(N).

Space complexity 
The algorithm runs in constant space O(1).
'''
