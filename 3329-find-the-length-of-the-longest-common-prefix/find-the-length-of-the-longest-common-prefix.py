class TrieNode:
    def __init__(self):
        self.children = {i: [None, set()] for i in range(10)}
        self.isEndOfWord = False
        # self.array = set()


class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str, arr: str) -> None:
        curr = self.root
        for char in word:
            pos = int(char)
            if not curr.children[pos][0]:
                curr.children[pos][0] = TrieNode()
            # curr.array.add(arr)
            curr.children[pos][1].add(arr)
            curr = curr.children[pos][0]
        curr.isEndOfWord = True
    


class Solution:
    
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        Max = 0

        for num in arr1:
            trie.insert(str(num), '1')

        for num in arr2:
            trie.insert(str(num), '2')

        # print(trie.root.children[3])
        

        def dfs(node, level):
            nonlocal Max
            Max = max(Max, level)
            
            for i in range(10):
                if node.children[i][0]:
                    if len(node.children[i][1]) == 2:
                        dfs(node.children[i][0], level + 1)
        
        dfs(trie.root, 0)

        return Max



        