def view_data(data, title):
    print(f'{title} = {data}')

def get_value(type):
    if type:
        return int(input('int = '))
    else:
        return complex(input("Enter a complex: "))

def get_type():
    return int(input("type - ? 0 - complex, 1 - integer "))

def get_operator(type):
    if type:
        return input("operator - ? * , + , - , / , // , % ")
    else:
        return input("operator - ? * , + , -, /  ")