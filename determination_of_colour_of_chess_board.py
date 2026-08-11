'''
Code
Test Result
Testcase
Testcase
1812. Determine Color of a Chessboard Square
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false
 

Constraints:

coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
'''


class Solution(object):
    def squareIsWhite(self, coordinates):
        constrains={"a2","a4","a6","a8","b1","b3","b5","b7","c2","c4","c6","c8","d1","d3","d5","d7","e2","e4","e6","e8","f1","f3","f5","f7","g2","g4","g6","g8","h1","h3","h5","h7"}
        for i in constrains:
            if i == coordinates:
                return True
        return False