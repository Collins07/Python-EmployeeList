from secrets import choice


class Employee:
    employeeList = list()
    def __init__(self, empNo, empName,empDes, empSal):
        self.empNo, self.empName, self.empDes, self.empSal = empNo, empName, empDes, empSal
    def addNewEmployee(self):
        Employee.employeeList.append(self) 
    def getEmpList(self):
        return Employee.employeeList
    def getEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
               return emp
        return False 
    def updateEmpById(selfy, empNo, empName, empDes, empSal):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                emp.empNo, emp.empName, emp.Des, emp.Sal = empNo, empName, empDes, empSal
                return True
        return False        

    def setEmpNo(self, empNo):
        self.empNo = empNo
    def getEmpNo(self) :
        return self.empNo 
    def setEmpName(self, empName):
        self.empName = empName
    def setEmpName(self):
         return self.empName
    def setEmpDes(self, empDes):
        self.empDes = empDes
    def setEmpDes(self):
         return self.empDes
    def setEmpSal(self, empSal):
        self.empSal = empSal
    def setEmpSal(self):
         return self.empSal
    def __str__(self):
         return ("%d %s %s %d"%(self.empNo, self.empName, self.empDes, self.empSal))


choice = 1
employee = Employee(0,"","",0.0)
while choice >= 1 and choice <=3:
    print("\n\n1.Add New Employee\n2. Get All Employee List\n3. Get Employee by ID\n4. Update Employee by ID\n\n")
    choice = int(input("Enter Your Choice: "))
    if(choice ==1):
        empNo = int(input("Enter Employee No; "))
        empName = input("Enter Employee Name; ")
        empDes = input("Enter Employee Designation; ")
        empSal = float(input("Enter Employee Salary; "))
        emp = Employee(empNo, empName, empDes, empSal)
        emp.addNewEmployee()
    elif(choice == 2):
        print("\n")
        for emp in employee.getEmpList():
            print(emp)
    elif(choice == 3):
       empNo = int(input("Enter Employee No; "))
       employee.getEmpById(empNo)
       if(emp == False):
           print("\nSorry!! Emplolyee not founfd by ID:", empNo)
       else:
           print(emp)
    elif(choice == 4):
        empNo = int(input("Enter Employee No; "))
        empName = input("Enter Employee Name; ")
        empDes = input("Enter Employee Designation; ")
        empSal = float(input("Enter Employee Salary; "))
        emp = employee.updateEmpById(empNo, empName, empDes, empSal)
        if(emp == False):
            print("\nSorry!! Update Failed, Emplolyee not founfd by ID:", empNo)
        else:
            print("Successfully Updated Employee For ID;", empNo)    

