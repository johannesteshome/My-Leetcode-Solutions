class Solution:
    def lastRemaining(self, n: int) -> int:
        # leftRight = True
        def remaining():
            nonlocal leftRight
            nonlocal iteration
            nonlocal left
            nonlocal right
            if left == right:
                return left
            else:
                size = ((right - left) // iteration) + 1
                if size % 2 == 0:
                    if leftRight:
                        left += iteration
                        leftRight = False
                    else:
                        right -= iteration
                        leftRight = True
                    iteration *= 2
                else:
                    left += iteration
                    right -= iteration
                    leftRight = not leftRight
                    iteration *= 2
                return remaining()



        iteration = 1
        left = 1
        right = n
        leftRight = True
        return remaining()