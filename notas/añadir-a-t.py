f = open("trabajo.txt", "a")
f.write("Este es un archivo de ejemplo.")
f.close()
f = open("trabajo.txt", "r")
print(f.read())