class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False

        self.index = []

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        def insert(word, index):
            curr = self.root
            self.suffix[index].add(word)
            for i in range(len(word)):
                pos = ord(word[i]) - 97
                if not curr.children[pos]:
                    curr.children[pos] = TrieNode()
                curr = curr.children[pos]
                self.suffix[index].add(word[i+1:])
                curr.index.append(index)
            curr.isEndOfWord = True
        self.suffix = defaultdict(set)
        for i in range(len(words)):
            insert(words[i], i)
        

    def f(self, pref: str, suff: str) -> int:
        # print("Starts")
        curr = self.root
        for char in pref:
            pos = ord(char) - 97
            if not curr.children[pos]:
                return -1
            curr = curr.children[pos]
        
        # print(self.suffix)
        for i in range(len(curr.index)-1, -1,-1):
            if suff in self.suffix[curr.index[i]]:
                # print(suff)
                return curr.index[i]
        return -1
        
        # return True
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)