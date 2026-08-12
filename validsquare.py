'''67. Valid Perfect Square
Solved
Easy
Topics
premium lock icon
Companies
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
978,449/2.2M
Acceptance Rate
45.1%
Topics
icon
Companies
Similar Questions
Discussion (135)


Choose a type



Copyright © 2026 LeetCode. All rights reserved.'''


class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True

        low = 1
        high = num // 2

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1

        return False