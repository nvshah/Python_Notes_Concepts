class Employee:
    
    # Class Variable
    appraisal = 1.5 

    def __init__(self, name, salary) -> None:
        self.name = name 
        self.salary = salary 

if __name__ == '__main__':
    e1 = Employee('Nipun', 100)
    print(Employee.appraisal)
    # it first look at instance level & if not available then it will look at class level
    print(e1.appraisal)  
    print(e1.__dict__)
 
    Employee.appraisal = 2.5  # class method setting val
    e1.appraisal = 3.5        # Monkey Pathcing on instance & not on class

    print(Employee.appraisal)
    # it first look at instance level & if not available then it will look at class level
    print(e1.appraisal)  
    print(e1.__dict__)