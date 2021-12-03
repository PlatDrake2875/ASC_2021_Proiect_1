v = list(map(str, input().split()))

key = v[0]
N = len(key)

try:
    in_f = open(v[1])
except FileNotFoundError:
    print("File not found!")

pars = []
x = in_f.readline()
M = len(x)

for i in range(0, M, 8):
    nr = 0
    for j in range(8):
        if i + j < M and (ord(x[i + j]) - 48) & 1:
            nr += (1 << (7 - j))
    pars.append(nr)

g = open(v[2], "w")

ans = []
for i in range(len(pars)):
    ans.append(chr(ord(key[i % N]) ^ pars[i]))

for i in ans:
    print(i, sep="", end="", file=g)
