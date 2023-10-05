import re


class Solution(object):

    def chessSquare(self, s):
        return re.match("^[A-H][1-8]$", s) is not None

    def phoneNumber(self, s):
        return (re.match(r'^\d{3}-\d{3}-\d{4}$', s) is not None) or re.match(r'^\d{3}.\d{3}.\d{4}$', s) is not None

    def ipAddress(self, s):
        return re.match(r'^[0-255]..[0-255]..[0-255]..[0-255]$', s) is not None


test = Solution()
print(test.chessSquare("C4"))
print(test.phoneNumber("669.333.1065"))
print(test.ipAddress("192.0.2.146"))
