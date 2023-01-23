

listNames=["Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
print(listNames)
dictSurname = {}
for Surname in listNames:
    firstLetterSurname=Surname.split()[1][0]
    # if firstLetterSurname in dictSurname:#.keys():
    #     dictSurname[firstLetterSurname].append(Surname)
    # else:
    #     dictSurname[firstLetterSurname]=[Surname]
    dictSurname.setdefault(firstLetterSurname,[])
    dictSurname[firstLetterSurname].append(Surname)


for firstLetterSurname,listNames in dictSurname.items():
    # print(listNames)
    setNames=sorted(set(listNames))
    # print(setNames)
    dictNames = {}
    for Name in setNames:
        # if Name[0] in dictNames:#.keys():
        #     dictNames[Name[0]].append(Name)
        # else:
        #     dictNames[Name[0]]=[Name]

        dictNames.setdefault(Name[0],[])
        dictNames[Name[0]].append(Name)

    # print(dictNames)
    dictSurname[firstLetterSurname] = dictNames
print(dictSurname)

