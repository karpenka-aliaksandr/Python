def GP(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for param, item in kwargs.items():
        print(param, item)
        print(type(param),type(item))

GP (name = 'Sasha', age = 41, height = 182)