class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heap size to store the heights managed by the ladders i.e. maximum heights of size ladder
        heap = []
        # the rest of heights beyond those managed by the ladder, the number of bricks needed to cross them
        bricksize = 0

        for i in range(len(heights) - 1):
            # if the height needs brick or ladder
            if heights[i] < heights[i+1]:
                # push th height into the heap
                heappush(heap, heights[i+1] - heights[i])

                # if the number of heights that can be managed by the ladder is full meaning er have found ladder size of max heights, the rest can be managed by bricks
                if len(heap) > ladders:
                    bricksize += heappop(heap)
                
                # if the number of bricks to cross the building exceeds the amount we have we finish
                if bricksize > bricks:
                    return i
        
        # if we finish crossing all buildings we return the last index value
        return len(heights)-1