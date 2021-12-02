key = input()
N = len(key)
file_name = input()
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

file_out = open("output", "w")

for i in ans:
    x = int(i)
    for j in range(7, -1, -1):
        if (1 << j) & x:
            print(1, sep="", end="", file=file_out)
        else:
            print(0, sep="", end="", file=file_out)
