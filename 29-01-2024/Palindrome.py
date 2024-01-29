'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original_x = x
        reverse_x = 0

        while x > 0:
            digit = x % 10
            reverse_x = reverse_x * 10 + digit
            x //= 10

        return original_x == reverse_x

# Example usage:
solution = Solution()

x1 = 121
result1 = solution.isPalindrome(x1)
print(result1)  # Output: True

x2 = -121
result2 = solution.isPalindrome(x2)
print(result2)  # Output: False

x3 = 10
result3 = solution.isPalindrome(x3)
print(result3)  # Output: False
