import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
   print("El archivo no EXISTE")
