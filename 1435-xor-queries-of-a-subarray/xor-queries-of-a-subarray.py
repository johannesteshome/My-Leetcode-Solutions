class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        arrXor = [arr[0]]

        for i in range(1, len(arr)):
            arrXor.append(arrXor[i-1] ^ arr[i])
        
        # print(arrXor)
        
        for query in queries:
            before = len(arr) - (len(arr) - query[0])
            # print(before, query[1])
            if query[0] == 0:
                answer.append(arrXor[query[1]])
            elif query[0] == query[1]:
                answer.append(arr[query[0]])
            else:
                answer.append((arrXor[before - 1]) ^ arrXor[query[1]] )

        return answer