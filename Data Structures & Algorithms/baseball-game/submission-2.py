class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mystack = []
        i = 0

        def checkNum(val):
            try:
                int(val)
                return True
            except ValueError:
                return False
            
        while i < len(operations):
            if checkNum(operations[i]):
                mystack.append(int(operations[i]))
        
            elif(operations[i] == "+"):
                operations[i] = int(operations[i-1]) + int(operations[i-2])
                mystack.append(operations[i])

            elif(operations[i] == "C"):
                operations = operations[:i-1] + operations[i+1:]
                mystack = mystack[:-1]
                i-=1
                continue

            elif(operations[i]=="D"):
                operations[i] = int(operations[i-1])*2
                mystack.append(operations[i])
            i+=1           

        return sum(mystack)