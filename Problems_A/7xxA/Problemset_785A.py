polyhedrons = {
    "Tetrahedron": 4, 
    "Cube": 6, 
    "Octahedron": 8, 
    "Dodecahedron": 12,
    "Icosahedron": 20
}

n = int(input())
sum_ = 0

for i in range(n):
    text = input()
    sum_ += polyhedrons[text]

print(sum_)
