# cook your dish here
from collections import deque

a = int(input())
b = int(input())
c = int(input())

array = [a*b*c, a+b+c, (a+b)*c, a*(b+c), a+b*c, a*b+c]

print(max(array))
