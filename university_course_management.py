from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, instructor, content):
        self.name = name  
        self.instructor = instructor  
        self.content = content  
        self.students = [] 

    def enroll_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} signed up for the course {self.name}")

    @abstractmethod
    def display_course_info(self):
        pass

class UndergraduateCourse(Course):
    def __init__(self, name, instructor, content):
        super().__init__(name, instructor, content)
        self.assignments = [] 

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def display_course_info(self):
        print("Information about the Bachelor's course")
        print(f"Course name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Content: {self.content}")

class GraduateCourse(Course):
    def __init__(self, name, instructor, content):
        super().__init__(name, instructor, content)
        self.research_topic = ""  

    def set_research_topic(self, topic):
        self.research_topic = topic

    def display_course_info(self):
        print("Information about the postgraduate course")
        print(f"Course name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Content: {self.content}")
        print(f"Research topic: {self.research_topic}")

class Assignment(ABC):
    @abstractmethod
    def submit(self, student):
        pass

class HomeworkAssignment(Assignment):
    def __init__(self, title):
        self.title = title

    def submit(self, student):
        print(f"Student {student.name} sent his homework: {self.title}")

class ExamAssignment(Assignment):
    def __init__(self, title):
        self.title = title

    def submit(self, student):
        print(f"Student {student.name} sent his exam: {self.title}")

class Student:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def view_course_progress(self, course):
        pass
    
    def complete_assignment(self, assignment):
        assignment.submit(self)

class Professor:
    def __init__(self, name, contact_info):
        self.name = name  
        self.contact_info = contact_info  

    def create_course(self, name, instructor, content, course_type):
        if course_type == "undergraduate":
            return UndergraduateCourse(name, instructor, content)
        elif course_type == "graduate":
            return GraduateCourse(name, instructor, content)
        else:
            raise ValueError("Incorrect course type")

    def add_assignment_to_course(self, course, assignment):
        if isinstance(course, Course):
            course.add_assignment(assignment)
            print(f"Assignment '{assignment.title}' added to the course '{course.name}'")
        else:
            raise TypeError("Incorrect course")



professor = Professor("Nyuton", "Nyuton@example.com")
course = professor.create_course("Informatika", "Mark Luts", "Python oop", "undergraduate")
course.display_course_info()

assignment1 = HomeworkAssignment("Python oop")
assignment2 = ExamAssignment("Midterm exam")

professor.add_assignment_to_course(course, assignment1)
professor.add_assignment_to_course(course, assignment2)

student1 = Student("Alex", "alex@example.com")
student2 = Student("Maria", "maria@example.com")

course.enroll_student(student1)
course.enroll_student(student2)

student1.complete_assignment(assignment1)
student2.complete_assignment(assignment1)


