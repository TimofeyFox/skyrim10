__author__ = 'fox'

import random
# -*- coding: utf-8 -*-
a = [0]*20

def ras(n): #Google
    return {
        1 :   "Нолда",
        2 :   "Палмареца",
        3 :   "Саджита",
        4 :   "Норгнияна",
        5 :   "Империйца"
    }.get(n, "ERROR!!!")

def die(): #Saushkin
    f=open('files/1.g')
    print("Вы умерли")
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line, end='')
    print("\n")
    f.close()

def dragon(): #Bannikov
    f=open('files/2.g')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line, end='')
    f.close()

def fox(): #Ushanov
    f=open('files/3.g')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end='')
    f.close()

while True:
    a[2]=100
    print("Welcome to SkyRim 10\n")

    print("Вас везут на ладье\n")

    print("Ты кто?\n")

    print("1)Нолд \n 2) Палмарец\n 3)Саджиты \n 4)Норгнияне \n 5)Имперци\n")
    a[0]=int(input())

    a[1]=input("Ваше имя - ")

    print("*Появляется Бог* и говорит: Ты убил короля и ты за это поплатишься!\n")
    print("Вы: Господи, не убивай меня, помоги мне сбежать\n")
    print("Чувак, ты с кем разговариваешь? Ты сколько лунного сахара сожрал? Я вообще то стражник! *уходит*\n")
    print("Ваши глаза закрываются\n")
    print("Вы просыпаетесь, вокруг суматоха, вы видите, что дракон Гоша напал на корабль\n")
    dragon()
    chooze=int(input("Ваши действия: 1) Ничего не делать \n 2) Выломать дверь \n 3)Попросить стражника открыть дверь\n"))
    if(chooze==1):
        print("На вас сваливается дракон Гоша\n")
        die()
        break
    elif(chooze==2):
        print("Дверь с грохотом падает и вы успеваете отбежать от клетки до того, как на неё падает дракон Гоша\n")
    if(chooze==3):
        print("У тебя тепловой удар, чувак? Ладно, времени нету, держи отмычку\n")
        r=int(random.randint(1, 9))
        vzlom=int(input("Выберете число от 1 до 9, и если вам повезёт, то вы сможете взломать замок\n"))
        print(r)
        if (r==vzlom):
            print("Дверь открывается и вы выбегаете, но вам не хватает 10 метров и дракон Гоша грохает на вас хвост\n")
            a[2]=a[2]-30
            if(a[2]<=0):
                die()
                print("HP - %d \n" %a[2])
        if(vzlom != r):
            print("Дверь не открылась и вы сломали отмычку. На вас падает дракон Гоша\n")
            die()
            break
    chooze=0
    chooze=int(input("1) Прыгнуть в воду и плыть на берег \n2)Найти лодку и плыть на берег на ней \n3)Схватиться за первую попавшуюся верёвку и попытаться перепрыгнуть на берег\n"))
    if(chooze==1):
        print("Вы прыгаете в воду и вспоминаете, что не умеете плавать. Вы утонули\n")
        die()
        break
    elif(chooze==2):
        print("Вы нашли лодку и успешно добираетесь до берега\n")
    if(chooze==3):
        verevka=int(random.randint(1, 3))
        if(verevka==1):
            print("Вы падаете в воду\n")
            die()
            break
        elif(verevka==2):
            print("Вы достигли берега, но что-то сломали\n")
            a[2] = a[2]-random.randint(1,60)
            if(a[2]<=0):
                die()
            if(a[2]>0):
                print("HP - %d \n" %a[2])
        if(verevka==3):
            print("Вы успешно достигли берега\n")
    chooze=0
    chooze=int(input("1)Бежать в горы \n 2)Бежать в пещеру\n 3) Бежать в город\n 4)Бежать в поле\n"))
    if(chooze==1):
        print("Вы побежали в горы и вас убил падающий камень\n")
    elif(chooze==2):
        print("Вас атакует ИГИЛ\n")
        a[2]=a[2]-random.randint(10,60)
        if(a[2]<=0):
            die()
            break
        elif(a[2] > 0):
            print("Вы победили ИГИЛ\n")
            print("HP - %d" %a[2])
            print("Я: Вот тут и остановлоюсь на ночь")
            print("Происходит яркая вспышка и вас перебрасывает на поле")
    if(chooze==3):
        print("Вас поймали и повесили\n")
        die()
        break
    elif(chooze==4):
        print("Вы выжили\n")
    print("Тут появляется дракон Гоша")
    chooze=0
    chooze=random.randint(1,3)
    if(chooze==1):
        print("И падает на вас!")
        a[2]=0
        die()
    elif(chooze==2):
        print("Дракон Гоша приземляется и с него спускается антропоморфный лис.\n")
        fox()
        print("Лис: *протягивает лапу* Пошли со мною, я тебе покажу рай скумы и лунного сахара.\n Я: *взял лапу и пошёл за лисом*. \n *Дракон Гоша с двумя пасажирами улетел в горизонт* \n Happy End) ")
    if(chooze==3):
        print("Вы отрубаетесь. \n Когда вы просыпаетесь над вами стоит старик. \n Старик: Я тебя уже 15 минут пинаю вставай. Ты первый, кто ночевал в этом поле, ты избранный. \n Я приглашаю тебя колегию ViewSonic. \n *Идёте за ним* \n Старик: Размещайся в общежитии и иди в 0 кабинет, у тебя там первая пара \n *Размещаетесь и идёте в нулевой кабинет* \n Лектор: Алгебраическая, геометрическая и физическая магия - это самое главное, а ваша экономическая магия говно! Маги экономики некому не нужны! \n Так и начались суровые будни %s %s" %(ras(a[0]), a[1]))
    print("Goodbay!")
    break
