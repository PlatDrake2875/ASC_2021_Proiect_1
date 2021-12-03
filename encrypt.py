import argparse

parser = argparse.ArgumentParser(description="decriptare xor")
parser.add_argument("parola", help="parola")
parser.add_argument("fisier_text", help="fisierul text initial")
parser.add_argument("fisier_codat", help="fisierul text codat, trecut prin cheie")
args = parser.parse_args()

# v = list(map(str, input().split()))

key = args.parola
N = len(key)
file_name = args.fisier_text

try:
    file = open(file_name)
except FileNotFoundError:
    print("File not found!")

ans = []
j, k = 0, 0
new_line = ord(key[0]) ^ ord('\n')

for linie in file.readlines():

    for i in range(len(linie)):
        j = (k + i) % N
        ans.append(str(ord(key[j]) ^ ord(linie[i])))
    k = j + 1

file_out = open(args.fisier_codat, "w")

for i in ans:
    x = int(i)
    for j in range(7, -1, -1):
        if (1 << j) & x:
            print(1, sep="", end="", file=file_out)
        else:
            print(0, sep="", end="", file=file_out)
