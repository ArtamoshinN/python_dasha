def sort2(a, b):
    if a < b:
        return a, b
    return b, a

min, max = sort2(5, 4)
print(min, max)
