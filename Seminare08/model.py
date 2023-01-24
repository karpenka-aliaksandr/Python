data = {}


def get_data():
    return data

def a_data(record): # запись данных
    data.append(record)
    
def add_student(name):
    data[name] = {}

def add_lesson(lesson):
    # print(lesson)
    # print(data)
    for key,value in data.items():
        value[lesson]=0
        # les = {lesson:0}
        # print(les)
    # for key in data.keys():
    #     data[key]=data[key][lesson]=0
    print(data)
