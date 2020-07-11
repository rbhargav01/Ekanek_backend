class Student:
    def __init__(self,name,age,marks,rollNumber):
        self.name=name
        self.age=age
        self.marks=marks
        self.rollNumber=rollNumber

#input_array: Array of Student objects
#sort_criteria: List of strings ("name","age","marks","rollNumber" restricted to these values only)
#sort_criteria can be given in any order but the input is case sensitive
def sort_function(input_array,sort_criteria):
    temp=[]
    for i in range(len(input_array)):                       #Creating an empty array for each student
        temp.append([])
    for i in range(len(sort_criteria)+1):
        if(i==len(sort_criteria)):
            for j in range(len(input_array)):               #Append the index of the each student at the end of jth row
                temp[j].append(j)
            break
        if(sort_criteria[i]=="name"):                       #Add name of each student to the jth row as the ith element to be sorted
            for j in range(len(input_array)):
                temp[j].append(input_array[j].name)
        if(sort_criteria[i]=="age"):                        #Add age of each student to the jth row as the ith element to be sorted
            for j in range(len(input_array)):
                temp[j].append(input_array[j].age)
        if(sort_criteria[i]=="marks"):                      #Add marks of each student to the jth row as the ith element to be sorted
            for j in range(len(input_array)):
                temp[j].append(input_array[j].marks)
        if(sort_criteria[i]=="rollNumber"):                 #Add rollNumber of each student to the jth row as the ith element to be sorted
            for j in range(len(input_array)):
                temp[j].append(input_array[j].rollNumber)
    temp.sort()                                             #Sorting the created array according to the given criteria
    for i in range(len(temp)):                              #Adding the whole object as the answer instead of the specified criteria
        temp[i]=input_array[temp[i][-1]]
    return temp


input_array=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    inp=input("Enter details of student"+str(i+1)+" : ".split()
    s=Student(inp[0],inp[1],inp[2],inp[3])
    input_array.append(s)
sort_criteria=input("Enter sort criteria : ").split()
print(sort_function(input_array,sort_criteria))
