class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        exp = x

        binary = format(n, "b")

        if binary[len(binary) - 1] == "1":
            res = x
        else:
            res = 1
        print(binary)
        for i in range(len(binary)-2, -1, -1):
            exp *= exp
            if binary[i] == "1":
                res *= exp
        if n < 0:
            return 1/res
        return res
        