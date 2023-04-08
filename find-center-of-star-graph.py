class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        for edge in edges:
            freq[edge[0]] += 1
            freq[edge[1]] += 1
        for key, values in freq.items():
            if values == len(edges):
                return key