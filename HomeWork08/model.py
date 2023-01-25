students ={}
courses={}
path = 'HomeWork08/students.txt'


def get_students():
    return students

def get_courses():
    return courses
 
def add_student(name:str):
    students[name] = courses

def add_cours(cours):
    courses[cours] = [] 
    for value in students.values():
        value[cours]=[]
def add_grade(name:str,course:str,grade:int):
    students[name][course].append(str(grade))

def save():
    list_save = []
    for name,value in students.items():
        course_grades=[]
        for course,grades in value.items():
            course_grades.append('='.join([course,','.join(map(str,grades))]))
        list_save.append(':'.join([name,';'.join(course_grades)]))
    with (open(path, 'w', encoding='utf-8')) as f:
        f.writelines(f'{line}\n' for line in list_save)

def load():
    global students
    data = ['']
    with (open(path, 'r', encoding='utf-8')) as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i]=data[i][:-1]
    # print(data)
    dict_data={}
    is_courses=False
    for record in data:
        name,course_grades = record.split(':')
        # print(name,course_grades)
        l_course_grades = course_grades.split(';')
        # print(l_course_grades)
        d_course_grades={}
        for s_course_grades in l_course_grades:
            course,s_grades = s_course_grades.split('=')
            if not is_courses:
                courses[course]=[]
                # print(courses)
            if s_grades:
                grades=list(map(int,s_grades.split(',')))
            else:
                grades=[] 
            # print('grades = ',grades)
            d_course_grades[course]=grades
        dict_data[name]=d_course_grades
        # print(d_course_grades)
        is_courses=True
    students = dict_data
    # print(students)  
    # print(courses)  
    # __=input()

        