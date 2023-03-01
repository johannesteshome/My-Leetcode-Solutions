class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:       
        def theWinner(start, end, turn):
            if start == end:
                # print("Equal")
                if turn:
                    return [nums[start], 0]
                else:
                    return [0, nums[start]]

            elif turn:
                # print("One")
                ans1 = theWinner(start+1, end, not turn)
                ans1[0] += nums[start]
                ans2 = theWinner(start, end-1, not turn)
                ans2[0] += nums[end]
                
                if ans1[0] < ans2[0]:
                    return ans2
                else:
                    return ans1
            elif not turn:
                # print("Two")
                ans1 = theWinner(start+1, end, not turn)
                ans1[1] += nums[start]
                ans2 = theWinner(start, end-1, not turn)
                ans2[1] += nums[end]
                
                if ans1[1] < ans2[1]:
                    return ans2
                else:
                    return ans1
                            
        result = theWinner(0,len(nums)-1, True)
                            
        if result[0] < result[1]:
            return False
        else:
            return True