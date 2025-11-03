class Course:
    def __init__(self, course_number, course_title):
        self.course_number = course_number
        self.course_title = course_title

    # TODO: Define print_info()
    def print_info(self):
        print('Course Information:')
        print(f'   Course Number: {self.course_number}')
        print(f'   Course Title: {self.course_title}')

class OfferedCourse(Course):
    def __init__(self, course_number, course_title, instructor_name, location, class_time):
        super().__init__(course_number, course_title)
        self.instructor_name = instructor_name
        self.location = location
        self.class_time = class_time

    def print_info(self):
        super().print_info()
        print(f'   Instructor Name: { self.instructor_name }')
        print(f'   Location: { self.location }')
        print(f'   Class Time: { self.class_time }')

if __name__ == "__main__":
    course_number = input("Input course number: ")
    course_title = input("Input course title: ")

    o_course_number =  input("Input offered course number: ")
    o_course_title =  input("input offered course title: ")
    instructor_name = input("Input instructor name: ")
    location = input("Input class location: ")
    class_time = input("Input class time: ")
   
    my_course = Course(course_number, course_title)
    my_course.print_info()
   
    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, location, class_time)
    my_offered_course.print_info()