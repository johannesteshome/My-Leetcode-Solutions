class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False

        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            pos = ord(char) - 97
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]
        curr.isEndOfWord = True
        curr.value = val
        

    def sum(self, prefix: str) -> int:
        curr = self.root        
        answer = 0
        for char in prefix:
            pos = ord(char) - 97
            if not curr.children[pos]:
                return answer
            if curr.isEndOfWord:
                answer = curr.value
            curr = curr.children[pos]
        if curr.isEndOfWord:
            answer = curr.value
        
        def dfs(curr):
            nonlocal answer
            if curr.isEndOfWord:
                answer += curr.value
            
            for s in curr.children:
                if s:
                    dfs(s)

        for s in curr.children:
            if s:
                dfs(s)
        return answer


        # return 1

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)