file_to_open = input("Δώσε αρχείο:")
try:
    file = open(file_to_open, "r")
except FileNotFoundError:
    print("Το αρχειό δεν υπάρχει. Προσπαθήστε ξανά.")
    exit(1)
string = file.read().replace("\n", " ")
string = string[::-1]
file.close()

final=''
for i in string:
    i=chr(128-ord(i))
    final=final+i

print(final)
