# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        r = [1, n]
        while(r[0] <= r[1]):
            i = r[0] + int((r[1] - r[0]) / 2)
            g = guess(i)
            if g == -1:
                r[1] = i - 1
            elif g == 1:
                r[0] = i + 1
            else:
                return i
