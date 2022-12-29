class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        regex = "\(\w*\)"
        filesList = defaultdict(list)
        answer = []
        
        for path in paths:
            contents = re.findall(regex, path)
            filePaths = path.split(" ")
            root = filePaths[0]
            
            for index, content in enumerate(contents):
                filesList[content].append(root+'/'+filePaths[index+1].split('(')[0])
                
        for path in filesList.values():
            if(len(path)>1):
                answer.append(path)
                
        return answer