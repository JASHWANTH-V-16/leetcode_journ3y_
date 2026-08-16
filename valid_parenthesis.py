'''20. Valid Parentheses
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''



class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket...
            if char in bracket_map:
                # 1. If the stack is empty, we can't pop. It's invalid!
                if not stack:
                    return False
                
                # 2. Now it's safe to pop
                top_element = stack.pop()
                
                # 3. Check if they match
                if bracket_map[char] != top_element:
                    return False
            
            # If it's an opening bracket...
            else:
                stack.append(char)

        return not stack