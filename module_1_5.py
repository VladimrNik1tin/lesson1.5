immutable_var = 1, 2, 3, 'z', 'x', 'z'
print(immutable_var)
# immutable_var[1:4] = 5, 6, 'h'  - нельзя изменить значения элементов кортежа, т.к. кортеж является неизменяемым (immutable) типом.
mutable_list = [1, 2, 3, 'z', 'x', 'z']
mutable_list[1:4] = 5, 6, 'h'
print(mutable_list)