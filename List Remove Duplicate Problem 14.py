def List(dup):
   elements = []
   for i in dup:
       if i not in elements:
           elements.append(i)
   return elements

def Better_List(dup):
    return list(set(dup))
some_list = [1, 5, 7, 7, 2, 5, 3, 4, 9, 9, 8, 6, 9]
print(some_list)
print(List(some_list))
print(Better_List(some_list))