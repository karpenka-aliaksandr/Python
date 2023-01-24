import os
path = 'HomeWork07/Telephones_.txt'

def get_all():
    list_data = ['']
    with (open(path, 'r', encoding='utf-8')) as f:
        list_data = f.readlines()
    dict_data={}
    for record in list_data:
        dict_data[int(record[0:record.find(' ')])] = record[record.find(' ')+1:-1] 
    return dict_data


def add_record(dict_data:dict,id,s_name,s_number,s_note):
    dict_data[id] = ' '.join([s_name,s_number,s_note])
    lines=[]
    for id, record in dict_data.items():
        lines.append(' '.join([str(id),record]))
    with (open(path, 'w', encoding='utf-8')) as f:
        f.writelines(f'{line}\n' for line in lines)
    
def delete_record(dict_data:dict,id:int):
    del dict_data[id]
    lines=[]
    for id, record in dict_data.items():
        lines.append(' '.join([str(id),record]))
    with (open(path, 'w', encoding='utf-8')) as f:
        f.writelines(f'{line}\n' for line in lines)

def delete_all_record():
    lines=[]
    with (open(path, 'w', encoding='utf-8')) as f:
        f.writelines(f'{line}\n' for line in lines)

