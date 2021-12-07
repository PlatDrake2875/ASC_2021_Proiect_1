import argparse

parser = argparse.ArgumentParser(description="encriptare xor")

# citesc argumentele din linia de comanda
parser.add_argument("fisier_binar", help="fisierul binar de intrare")
parser.add_argument("fisier_text", help="fisierul text de intrare")
args = parser.parse_args()

# citesc input-urile din fisiere
f = open(args.fisier_binar, "rb")
text_encriptat = f.read()
f.close()
f = open(args.fisier_text, "r")
text_necriptat = f.read()
f.close()

# creez listele si variabilele necesare
lungime_text = len(text_necriptat)
lista_binar = [int(byte) for byte in text_encriptat]
lista_text = [int(ord(caracter)) for caracter in text_necriptat]
lista_output = []
parola = ""
contor = 0

# decriptez cu xor si pun rezultatul in lista_output
for i in range(0, lungime_text):
    lista_output.append(chr(lista_binar[contor] ^ lista_text[i]))
    contor += 1

# scriu parola in fisierul output)
fisier_output = open("parola_recuperata.txt", "w")
fisier_output.write(parola.join(lista_output))
