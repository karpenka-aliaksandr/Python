# 42)Имеется упорядоченный список:

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.

def main_line_list_of_lists(ll:list) -> None:
    for ind, lst in enumerate(ll):
        lst[ind] = 0

d,e,f = [1, 2, 3], [4, 5, 6], [7, 8, 9]
g=[d,e,f]
main_line_list_of_lists(g)


# for indx,value in enumerate(A):
#     value[indx] = 0
# print(A)
