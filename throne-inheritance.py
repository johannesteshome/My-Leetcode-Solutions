class ThroneInheritance:

    def __init__(self, kingName: str):
        self.royalFamily = defaultdict(list)
        self.deaths = set()
        self.king = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.royalFamily[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.deaths.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        inheritance = []
        def dfs(member):
            if member not in self.deaths:
                inheritance.append(member)
            
            if member in self.royalFamily:
                for children in self.royalFamily[member]:
                    dfs(children)
        
        dfs(self.king)
        return inheritance
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()