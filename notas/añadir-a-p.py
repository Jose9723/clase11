f = open("personal.txt", "a")
f.write("Este es un archivo de ejemplo.")
f.close()
f = open("personal.txt", "r")
print(f.read())

f = open("personal.txt", "a")
f.write("Hola Mundo.")
f.close()
f = open("personal.txt", "r")
print(f.read())