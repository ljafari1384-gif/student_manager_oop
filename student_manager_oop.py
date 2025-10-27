def get_valid_name():
    while True:
        name=input("please enter name:").strip()
        if not name:
            print("Name cannot be empty.")
        elif name.isdigit():
            print("Name cannot be a number.")
        else:
            return name
class Student:
    def __init__(self, name, math, physics, art ):
        self.name=name
        self.math=math
        self.physics=physics
        self.art=art
        self.average=(self.math+self.physics+self.art)/3
        if self.average>=10:
            self.status="passed"
        else:
            self.status="failed"
    def info(self):
        return(f"name of student: {self.name} and average is: { self.average} and status is: {self.status}")
students=[]  
while True:
    y_or_n=input("do you want to continue?(yes/no)").lower()
    if y_or_n!="yes":
        break
    student_i={}
    lesson=["math","physics","art"]
    student_i["name"]=get_valid_name()
    for l in lesson:
        while True:
            try:
                score=int(input(f"please enter the score of {l}:"))
                if 0<=score<=20:
                    student_i[l]=score
                    break
                else:
                    print("Score must be between 0 and 20.")
            except ValueError:
                print("Please enter a valid number.")
    student_obj=Student(student_i["name"],student_i["math"],student_i["physics"],student_i["art"])
    students.append(student_obj)
if len(students)>0:
    total_average = sum(s.average for s in students)
    passed_count=sum(1 for s in students if s.status=="passed")
    print(f"Number of students who passed: {passed_count}")
    class_average=total_average/len(students)
    print(f"The average of all students is: {round(class_average,2)}")
    student_sort=sorted(students, key=lambda s : s.average, reverse=True)
    for s in student_sort:
        print(s.info())
    with open("report.txt", "w", encoding="utf-8") as f:
        for s in student_sort:
            f.write(s.info()+"\n")
else:
    print("No student data entered.")
            