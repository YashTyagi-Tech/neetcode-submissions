class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for person in details:
            age=int(person[11:13])
            if age>60:
                count+=1
        return count
            
        