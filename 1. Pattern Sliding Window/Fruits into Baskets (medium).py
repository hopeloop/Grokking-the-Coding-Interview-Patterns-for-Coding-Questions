'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''


# mycode
def fruits_into_baskets(fruits):
    windowStart = 0
    fruitFrequency = {}
    maxSize = 0

    for windowEnd in range(len(fruits)):
        right = fruits[windowEnd]
        if right not in fruitFrequency.keys():
            fruitFrequency[right] = 0
        fruitFrequency[right] += 1

        while len(fruitFrequency) > 2:
            left = fruits[windowStart]
            fruitFrequency[left] -= 1
            if fruitFrequency[left] == 0:
                del fruitFrequency[left]
            windowStart += 1

        maxSize = max(maxSize,sum(fruitFrequency.values()))

    return maxSize


# answer
# def fruits_into_baskets(fruits):
#     window_start = 0
#     max_length = 0
#     fruit_frequency = {}
#
#     # try to extend the range [window_start, window_end]
#     for window_end in range(len(fruits)):
#         right_fruit = fruits[window_end]
#         if right_fruit not in fruit_frequency:
#             fruit_frequency[right_fruit] = 0
#         fruit_frequency[right_fruit] += 1
#
#         # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
#         while len(fruit_frequency) > 2:
#             left_fruit = fruits[window_start]
#             fruit_frequency[left_fruit] -= 1
#             if fruit_frequency[left_fruit] == 0:
#                 del fruit_frequency[left_fruit]
#             window_start += 1  # shrink the window
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N)which is asymptotically equivalent to O(N).

Space Complexity 
The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.

Similar Problems 
Problem 1: Longest Substring with at most 2 distinct characters

Given a string, find the length of the longest substring in it with at most two distinct characters.

Solution: This problem is exactly similar to our parent problem.
'''
