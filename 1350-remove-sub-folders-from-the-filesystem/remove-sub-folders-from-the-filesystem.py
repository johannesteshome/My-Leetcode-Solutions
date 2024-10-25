class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        paths = []
        trie = Trie()
        answer = []

        for path in folder:
            paths.append(path.split('/')[1:])
        
        for path in paths:
            trie.insert(path)
        
        # print(paths, trie)
        trie.dfs(trie.root, '')

        return trie.answer


class TrieNode:
    def __init__(self):
        self.children = defaultdict(str)

        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()  
        self.answer = []      

    def insert(self, path: List[str]) -> None:
        # print(path)
        curr = self.root
        # curr.children['a'] = TrieNode()
        # print(curr.children)
        for p in path:
            if not curr.children or not curr.children[p]:
                curr.children[p] = TrieNode()
            curr = curr.children[p]
        curr.isEndOfWord = True
                    

    def dfs(self, trie: TrieNode, s: str) -> None:
        # print(trie.children)
        for child in trie.children:
            # print(child, trie.isEndOfWord)
            if not trie.isEndOfWord:
                self.dfs(trie.children[child], s + '/' + child)
            else:
                self.answer.append(s)
                return
        if trie.isEndOfWord:
            self.answer.append(s)
        
        