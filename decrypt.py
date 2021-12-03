import argparse

parser = argparse.ArgumentParser(description="encriptare xor")

parser.add_argument("fisier_input", help="fisierul text de intrare")
parser.add_argument("parola", help="parola")
parser.add_argument("fisier_output", help="fisierul output")
args = parser.parse_args()

# v = list(map(str, input().split()))

key = args.parola
N = len(key)

try:
    in_f = open(args.fisier_input)
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

g = open(args.fisier_output, "w")

ans = []
for i in range(len(pars)):
    ans.append(chr(ord(key[i % N]) ^ pars[i]))

for i in ans:
    print(i, sep="", end="", file=g)
