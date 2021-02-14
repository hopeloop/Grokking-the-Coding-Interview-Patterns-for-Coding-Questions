'''
Problem Challenge 2

String Anagrams (hard) 
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''


# mycode
def find_string_anagrams(str, pattern):
  window_start, matched = 0,0
  char_dict ={}
  result=[]

  for char in pattern :
    if char not in char_dict:
      char_dict[char]=0
    char_dict[char] += 1

  for window_end in range(len(str)):
    if str[window_end] in char_dict:
      char_dict[str[window_end]] -= 1
    if char_dict[str[window_end]] == 0:
      matched += 1

    if matched == len(pattern):
      result.append(window_start)

    if window_end >= len(pattern)-1:
      if char_dict[str[window_start]] == 0:
        matched  -= 1
      char_dict[str[window_start]] += 1
      window_start+=1

  return result



# answer
def find_string_anagrams(str, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  result_indices = []
  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      # Decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):  # Have we found an anagram?
      result_indices.append(window_start)

    # Shrink the sliding window
    if window_end >= len(pattern) - 1:
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        char_frequency[left_char] += 1  # Put the character back

  return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input 
string and the pattern respectively.

Space Complexity 
The space complexity of the algorithm is O(M) since in the worst case, the whole 
pattern can have distinct characters which will go into the HashMap. 
In the worst case, we also need O(N) space for the result list, this will happen 
when the pattern has only one character and the string contains only that character.
'''
