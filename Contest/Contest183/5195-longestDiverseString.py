
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = sorted([['a', a], ['b', b], ['c', c]], key = lambda x: x[1], reverse = True)
        s = ""
        length = 0
        while freq[0][1] > 0 or freq[1][1] > 0 or freq[2][1] > 0:
            i = 0
            length = len(s)
            while i < 3:
                if len(s) <= 0 or s[-1] != freq[i][0]:
                    if freq[i][1] > 0:
                        s += freq[i][0]
                        freq[i][1] -= 1
                        if i == 0 and freq[i][1] > 0:
                            s += freq[i][0]
                            freq[i][1] -= 1
                        break
                i += 1
            if len(s) == length:
                break
            freq = sorted(freq, key = lambda x: x[1], reverse = True)
        return s

print(Solution().longestDiverseString(1, 1, 7))
print(Solution().longestDiverseString(2, 2, 1))
print(Solution().longestDiverseString(7, 1, 0))
print(Solution().longestDiverseString(0, 0, 0))
print(Solution().longestDiverseString(0, 8, 11))    # "ccbccbbccbbccbbccbc"
