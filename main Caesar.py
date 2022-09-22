

print("Добро пожаловать в шифровальщик Цезаря!")
alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

useYo = input("Хотите использовать ё? (д/н): ")
if(useYo == "н"):
    alp = alp.replace("ё", "")
useI = input("Хотите использовать й? (д/н): ")
if(useI == "н"):
    alp = alp = alp.replace("й", "")

encrypting = input("Введите фразу, которая будет зашифрована: ")
key = int(input("Введите ключ Шифрования (1-32): "))
encrypting = encrypting.lower()
encrypted = ""

for l in encrypting:
    if not l.isalpha():    # skip if not letter
        encrypted += l
        continue

    pos = alp.find(l)
    newp = pos + key
    if newp > len(alp):
        newp -= len(alp)
    encrypted += alp[newp]

print("Результат: \'{0}\'".format(encrypted))

