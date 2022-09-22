

print("Добро пожаловать в дешифровщик Цезаря!")
alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alp2 = alp
out1, out2, out3, out4 = "","","",""

enc = input("Введите зашифрованный текст: ")

print("\nВариант 1, используются ё и й")
for key in range(0,33):
    for l in enc:
        if not l.isalpha():    # skip if not letter
            out1 += l
            continue

        pos = alp.find(l)
        newp = pos - key
        if newp < 0:
            newp = len(alp) - abs(newp)
        out1 += alp[newp]
    print(out1, end="\t")
    out1 = ""

print("\n\n\nВариант 2, не используется только ё")
alp = alp.replace("ё", "")
for key in range(0,33):
    for l in enc:
        if not l.isalpha():    # skip if not letter
            out2 += l
            continue

        pos = alp.find(l)
        newp = pos - key
        if newp < 0:
            newp = len(alp) - abs(newp)
        out2 += alp[newp]
    print(out2, end="\t")
    out2 = ""

print("\n\n\nВариант 3, не используется только й")
alp = alp2
alp = alp.replace("й", "")
for key in range(0,33):
    for l in enc:
        if not l.isalpha():    # skip if not letter
            out3 += l
            continue

        pos = alp.find(l)
        newp = pos - key
        if newp < 0:
            newp = len(alp) - abs(newp)
        out3 += alp[newp]
    print(out3, end="\t")
    out3 = ""

print("\n\n\nВариант 4, не используются ни ё, ни й")
alp = alp.replace("ё", "")
for key in range(0,33):
    for l in enc:
        if not l.isalpha():    # skip if not letter
            out4 += l
            continue

        pos = alp.find(l)
        newp = pos - key
        if newp < 0:
            newp = len(alp) - abs(newp)
        out4 += alp[newp]
    print(out4, end="\t")
    out4 = ""

# print("Результат: \'{0}\'".format(encrypted))
