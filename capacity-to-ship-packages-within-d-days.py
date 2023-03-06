class Solution:
    # function to calculate the days
    def calculateDays(self, mid, weights):
        day = 1
        w = 0
        for weight in weights:
            if w + weight <= mid:
                w += weight
            else:
                day += 1
                w = weight
        return day
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # initializing the binary search list the minimum value it can be
        # is the maximum wight of the goods in the list while its maximum is
        # the sum of all weights of the goods
        right = sum(weights)
        left = max(weights)

        # perform binary search
        while left <= right:
            # calculate the middle value
            mid = (left + right) // 2
            # calculate the days spent to transport the goods with the given mid weight 
            day = self.calculateDays(mid, weights)
            # if the calulated day is greater than the given day weight should be increased to 
            # finish transporting the goods fast and decrease the day
            if day > days:
                left = mid + 1
            # if the calulated day is less than the given day weight should be decreased to 
            # extend the time transporting the goods
            else:
                right = mid - 1
            
        return left