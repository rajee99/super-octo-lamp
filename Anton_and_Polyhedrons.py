Tetrahedron = 4
Cube = 6
Octahedron = 8 
Dodecahedron = 12
Icosahedron = 20

n = int(input())
goons = [input() for i in range(n)]
total = 0
for i in range(n):
    if goons[i] == 'Tetrahedron' :
        total+=Tetrahedron
    elif goons[i] == 'Cube':
        total+=Cube
    elif goons[i] == 'Octahedron':
        total+=Octahedron
    elif goons[i] == 'Dodecahedron':
        total+=Dodecahedron
    elif goons[i] == 'Icosahedron':
        total+=Icosahedron

print(total)

