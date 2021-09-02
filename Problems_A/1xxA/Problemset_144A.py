n = int(input())

array = [int(x) for x in input().split()]

min_ = 100
max_ = 0 

for index, elem in enumerate(array):
    if elem > max_:
        max_ = elem
        max_index = index

    if elem <= min_:
        min_ = elem
        min_index = index

# print(min_, max_)
# print(min_index, max_index)

if max_index > min_index:
    print(max_index + len(array) - min_index - 2)
else:
    print(max_index + len(array) - min_index - 1)
