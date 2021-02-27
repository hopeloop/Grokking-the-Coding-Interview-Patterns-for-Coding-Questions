'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''


# mycode
def search_triplets(arr):
    arr.sort()  # 排序
    res = []

    for i in range(len(arr)):
        # 如果元素大于0，由于是排序数组，则后面不可能再有解
        if arr[i] > 0:
            break
        # 跳过重复的第一个数
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i+1, len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s < 0:
                left += 1
                while arr[left] == arr[left - 1] and left < right:
                    left += 1
            if s > 0:
                right -= 1
                while arr[right] == arr[right + 1] and left < right:
                    right -= 1
            if s == 0:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while arr[left] == arr[left - 1] and left < right:
                    left += 1
                while arr[right] == arr[right + 1] and left < right:
                    right -= 1

    return res


'''
思路：
1.排序
2.第一个数索引为k,遍历整个数组
    ~当元素>0时，跳出遍历
    ~遇到相同的元素，跳过
    ~双指针 i,j = k,len(arr),交替向中间移动（类似Sliding window)
      s=nums[k]+nums[left]+nums[right]
      while(left<right):
        ①当s<0时，左指针右移并跳过所有重复的元素
        ②当s>0时，右指针左移并跳过所有重复元素
        ③当s==0时，将值append到res数组，左右指针同时移动并跳过所有重复元素

*注意极端情况
'''


# answer
def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([0, 0]))
    print(search_triplets([-2,-3,0,0,-2]))


main()

'''
Time complexity 
Sorting the array will take O(N * logN). 
The searchPair() function will take O(N). 
As we are calling searchPair() for every number in the input array, 
this means that overall searchTriplets() will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2).

Space complexity 
Ignoring the space required for the output array, 
the space complexity of the above algorithm will be O(N) which is required for sorting.
'''
