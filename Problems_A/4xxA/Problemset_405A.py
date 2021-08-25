n = int(input())

array = [int(x) for x in input().split()]

array = sorted(array)

for elem in array:
    print(elem, end= " ")
