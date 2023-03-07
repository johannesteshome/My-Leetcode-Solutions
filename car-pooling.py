class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = defaultdict(int)
        for trip in trips:
            location[trip[1]] += trip[0] 
            location[trip[2]] -= trip[0]
        locationList = [0 for l in range(max(location.keys())+1)]
        print(locationList)
        for l in location:
            locationList[l] += location[l]
        for index in range(len(locationList)-1):
            locationList[index+1] += locationList[index]
        
        if max(locationList) > capacity:
            return False
        else:
            return True