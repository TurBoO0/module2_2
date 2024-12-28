def func(first, second, third):
    if first == second and first == third:
        return 3
    elif first == second or second == third or first == third:
        return 2
    else:
        return 0
print(func(1,2,3))