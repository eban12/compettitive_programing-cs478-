class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = None
        for j in employees:
            if j.id == id:
                emp = j
                
        importance = emp.importance
        for i in employees:
            if i.id in emp.subordinates:
                importance += self.getImportance(employees, i.id)
                
        return importance
