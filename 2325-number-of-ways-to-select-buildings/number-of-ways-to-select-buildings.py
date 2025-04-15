class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        state = (numOfBldg, lastEl)
        0 0 1 1 0 1
        
        0 = [0], [1], [1], [0], [1]
                [0, 1] [0, 1]

    go through each possiblities
    build the building collections so far
    if I collected 3 bulding and I will store the result in hashmap
    count the number of ways
    """
        count = 0
        totalOne = 0
        totalZero = 0
        prefixOne = [0] * (len(s) + 1)
        prefixZero = [0] * (len(s) + 1)

        for i in range(len(s)):
            if s[i] == '0':
                totalZero += 1
                prefixZero[i+1] = prefixZero[i] + 1
                prefixOne[i+1] = prefixOne[i]
            else:
                totalOne += 1
                prefixOne[i+1] = prefixOne[i] + 1
                prefixZero[i+1] = prefixZero[i]
        
        for i in range(len(s)):
            if s[i] == '0':
                onesBefore = prefixOne[i+1]
                onesAfter = totalOne - prefixOne[i+1]
                count = count + (onesBefore * onesAfter)
            else:
                zerosBefore = prefixZero[i+1]
                zerosAfter = totalZero - prefixZero[i+1]
                count = count + (zerosBefore * zerosAfter)
        
        return count
