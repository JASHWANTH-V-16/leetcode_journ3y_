'''504. Base 7
Solved
Easy
Topics
premium lock icon
Companies
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
 

'''




class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
        
       
        orginal_num=num
        num=abs(num)
        org=[]

        while num>0:
            rem=num%7
            org.append(str(rem))
            num//=7

        if orginal_num<0:
            org.append('-')
        org.reverse()
        return  ''.join(org)