class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for ch in operations:
            if ch=="C":
                record.pop()
            elif ch=="+":
                record.append(record[-1]+record[-2])
            elif ch=="D":
                record.append(record[-1]*2)
            else:
                record.append(int(ch))
        return sum(record)


        