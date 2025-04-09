class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        print(count)

        heap = []
        ans = []

        for key in count:
            heap.append((-count[key], key))
        
        heapify(heap)

        while heap:
            popped = []
            while ans and (ans[-1] == heap[0][1]):
                popped.append(heappop(heap))
                if not heap:
                    return ''
            
            # print('here', heap)
            char = heappop(heap)
            ans.append(char[1])
            if char[0] != -1:
                heappush(heap, (char[0] + 1, char[1]))
            
            for i in range(len(popped)):
                heappush(heap, popped[i])

        
        return ''.join(ans)

            

