class Student:
    def __init__(self,name,age,marks,rollNumber):
        self.name=name
        self.age=age
        self.marks=marks
        self.rollNumber=rollNumber
        
def sort_function(input_array,sort_criteria):
    temp=[]
    for i in range(len(input_array)):
        temp.append([])
    for i in range(len(sort_criteria)+1):
        if(i==len(sort_criteria)):
            for j in range(len(input_array)):
                temp[j].append(j)
            break
        if(sort_criteria[i]=="name"):
            for j in range(len(input_array)):
                temp[j].append(input_array[j].name)
        if(sort_criteria[i]=="age"):
            for j in range(len(input_array)):
                temp[j].append(input_array[j].age)
        if(sort_criteria[i]=="marks"):
            for j in range(len(input_array)):
                temp[j].append(input_array[j].marks)
        if(sort_criteria[i]=="rollNumber"):
            for j in range(len(input_array)):
                temp[j].append(input_array[j].rollNumber)
    temp.sort()
    for i in range(len(temp)):
        temp[i]=input_array[temp[i][-1]]
    return temp


input_array=[]
n=int(input())
for i in range(n):
    inp=input().split()
    s=Student(inp[0],inp[1],inp[2],inp[3])
    input_array.append(s)
sort_criteria=input().split()
sort_function(input_array,sort_criteria)
