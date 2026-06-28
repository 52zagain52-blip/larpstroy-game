import random

print("Larpstroy-Games — это терминальный симулятор азарта, вдохновлённый Mellstroy Game — реальным онлайн-казино стримера Андрея Бурима. Только у нас всё скромнее: никаких 9000+ слотов, никаких 660% бонусов и никакого вывода денег за 5 минут. Зато есть чёрный экран, зелёный текст и искренние попытки начинающего программиста повторить успех кумира.")
print(" ██▓     ▄▄▄       ██▀███   ██▓█████  ██████ ▄▄▄█████▓ ██▀███   ██▓  ██████  ██▓   ██▓")
print("▓██▒    ▒████▄    ▓██ ▒ ██▒▓██▒█ █ ██▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▒██    ▒ ▓██▒  ▓██▒")
print("▒██░    ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒   ░ ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒██░  ▒██░")
print("▒██░    ░██▄▄▄▄██ ▒██▀▀█▄  ░██░   ░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░  ▒   ██▒▒██░  ▒██░")
print("░██████▒ ▓█   ▓██▒░██▓ ▒██▒░██░   ░ ██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██████▒▒░██████░██████▒")
x = int(input("..."))
y = 0
if x == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
elif x == 2:
    if y == 0:
        global balance
        y = y + 5
        print("вы успешно поплнили баланс на 5р")
    else:
        print("у вас достаточно р чтоб играть")
else:
    print("1 - игра")
    print("2 - поплнить бесплатно счет (если нет денег)")
vvv = int(input("..."))
if vvv == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
elif vvv == 2:
    if y == 0:
        global balance
        y = y + 5
        print("вы успешно поплнили баланс на 5р")
    else:
        print("у вас достаточно р чтоб играть")
else:
    print("1 - игра")
    print("2 - поплнить бесплатно счет (если нет денег)")
vvc = int(input("..."))
if vvc == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
elif vvc == 1: 
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
vvc = int(input("..."))
if vvc == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
elif vvc == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
vvv = int(input("..."))
if vvv == 1:
    if y != 0:    
        zyx = int(input("выбери 1, 2 или 3"))
        xyz = random.choice([1, 2, 3])
        if xyz == zyx:
            global balance
            y = y + 10
            print("you win")
        else:
            global balance
            y = y - 5
            print("ты проиграл")
    else:
        print("у вас нет денег")
elif vvv == 2:
    if y == 0:
        global balance
        y = y + 5
        print("вы успешно поплнили баланс на 5р")
    else:
        print("у вас достаточно р чтоб играть")
else:
    print("1 - игра")
    print("2 - поплнить бесплатно счет (если нет денег)")

