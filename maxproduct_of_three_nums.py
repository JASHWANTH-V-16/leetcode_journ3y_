'''628. Maximum Product of Three Numbers
Solved
Easy
Topics
premium lock icon
Companies
You are given an integer array nums.

Find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]

Output: 6

Explanation:

The only three numbers are 1, 2, and 3, so the maximum product is 1 * 2 * 3 = 6.

Example 2:

Input: nums = [1,2,3,4]

Output: 24

Explanation:

The largest product comes from the three greatest numbers: 2 * 3 * 4 = 24.

Example 3:

Input: nums = [-1,-2,-3]

Output: -6

Explanation:

The only three numbers are -1, -2, and -3, so the maximum product is (-1) * (-2) * (-3) = -6.

 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''


class Solution(object):
    def maximumProduct(self, nums):
        # We start with infinity to be completely safe, replacing the -999
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        # ONE loop instead of three!
        for n in nums:
            # Logic to find the three biggest numbers
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            
            # Logic to find the two smallest (most negative) numbers
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        
        # Calculate the only two possible maximum products
        product1 = max1 * max2 * max3
        product2 = min1 * min2 * max1
        
        # Your exact original return logic
        if product1 > product2:
            return product1
        else:
            return product2