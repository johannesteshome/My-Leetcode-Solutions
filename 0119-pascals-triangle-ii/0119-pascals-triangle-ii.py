class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.row = 2
        self.rowIndex = rowIndex
        self.aboveRow = [1,1]
        
        return self.calculateRow(self.row)
        
    def calculateRow(self, row):
        if self.rowIndex == 0:
            return [1]
        elif self.rowIndex == 1:
            return [1, 1]
        else:
            newRow = []
            for i in range(len(self.aboveRow) - 1):
                newRow.append(self.aboveRow[i] + self.aboveRow[i+1])
            self.aboveRow = [1]
            self.aboveRow[1:1] = newRow
            self.aboveRow.append(1)

            if self.row == self.rowIndex:
                return self.aboveRow
            else:
                self.row += 1
                return self.calculateRow(self.row)
                