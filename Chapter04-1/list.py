list_a = [1, 2, "문자", True, [4, 5]]
list_b = [0, ' ']   

# list + list
print(list_a + list_b)

# list * num
print(list_a * 3)

# len()

# append(), insert()
# 리스트.append(원소)
print(list_a)
list_a.append(10)
print(list_a)
# 리스트.insert(위치, 원소)
list_a.insert(3, False)
print(list_a)
