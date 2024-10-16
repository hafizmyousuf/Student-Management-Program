class Student_data():
    def __init__(self,name,roll_number, clas):
        self.name= name
        self.roll_number=roll_number
        self.clas=clas
        
        self.marks={}
        
        


    def add_marks(self, subject,marks):

        if subject in self.marks:
            print(f"{subject} is already exist")
        else:
            self.marks[subject]= marks
        
    def total_marks(self):

        totalmarks = sum(self.marks.values())
        avemarks = totalmarks/len(self.marks)
        return avemarks
        
        
    
    def show_details(self):

        print (f"Student Name is {self.name}")
        print(f"Student class is {self.clas}")
        print(f"Roll number is {self.roll_number}")
        print(f"Total marks of {self.name} is {sum(self.marks.values())} out of {len(self.marks)*100}")
        print(f"Percentege of Your marks is {self.total_marks()}")


std1 = Student_data("Ali", 23, "10th")
std1.add_marks("physics", 45)
std1.add_marks("math", 35)


std1.show_details()