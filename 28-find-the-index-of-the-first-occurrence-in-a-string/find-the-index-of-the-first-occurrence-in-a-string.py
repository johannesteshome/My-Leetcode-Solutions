class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        nee = 0
        hay = 0
        mod = 10**9+7

        if len(needle) > len(haystack):
            return -1

        for i in range(length):
            nee += ((ord(needle[i]) - 97 + 1) * 26 ** (length-i-1))
            hay += ((ord(haystack[i]) - 97 + 1) * 26 ** (length-i-1))
        print(nee, hay)
        if nee % mod == hay % mod:
            return 0
        j = 1
        for i in range(length, len(haystack)):
            hay -= ((ord(haystack[j-1]) - 97 + 1) * 26 ** (length -1))
            hay *= 26
            hay += ord(haystack[i]) - 97 + 1 

            if nee % mod == hay % mod:
                return j
            j += 1
            # print(nee, hay, length)
        
        return -1
        