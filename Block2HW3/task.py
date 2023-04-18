'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
'''
import random

def task16():
  useNumber = int(input("Input size of the list: "))
  list_user = [random.randint(0,30) for _ in range(useNumber)]
  print(f'Your list_user is: ')
  print(*list_user)
  disared_Number = int(input("Enter disared number, please: "))
  repeatsNumber = list_user.count(disared_Number)
  print(f"Your number repeats -> {repeatsNumber} times!")
'''
Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
def task18():
  useNumber = int(input("Input size of the list: "))
  list_user = [random.randint(-30,30) for _ in range(useNumber)]
  print(f'Your list_user is: ')
  print(*list_user)
  disared_Number = int(input("Enter disared number, please: "))
  min_Difference = abs(disared_Number - list_user[0])
  close_Number = list_user[0]
  for value in list_user[1:]:
    difference = abs(disared_Number - value)
    if min_Difference > difference:
     min_Difference = difference
     close_Number  = value
  print(f"Your approximate number -> {close_Number}")
'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.
*Пример:*
ноутбук
    12
'''
def value_Letters(use_string: str):
  v1 = 1
  v2 = 2
  v3 = 3
  v4 = 4
  v5 = 5
  v8 = 8
  v10 = 10
  new_string = (use_string.replace(" ","")).upper()
  sum = 0
  alphabet = {"A":v1,"E":v1,"I":v1,"O":v1,"U":v1,"L":v1,"N":v1,"S":v1, "T":v1,"R":v1,
              "D":v2,"G":v2,
              "B":v3,"C":v3,"M":v3,"P":v3,
              "F":v4,"H":v4,"V":v4,"W":v4,"Y":v4,
              "K":v5,
              "J":v8,"X":v8,
              "Q":v10,"Z":v10,
              "А":v1,"В":v1,"Е":v1,"И":v1,"Н":v1,"О":v1,"Р":v1,"С":v1,"Т":v1,
              "Д":v2,"К":v2,"Л":v2,"М":v2,"П":v2,"У":v2,
              "Б":v3, "Г":v3,"Ё":v3,"Ь":v3,"Я":v3,
              "Й":v4,"Ы":v4,
              "Ж":v5,"З":v5,"Х":v5,"Ц":v5,"Ч":v5,
              "Ш":v8,"Э":v8,"Ю":v8,
              "Ф":v10,"Щ":v10,"Ъ":v10}
  for i in new_string:
    sum += alphabet[i]
  return sum

def task20():
  use_Word = input("Input your word, please: ")
  print(f"Your word is worth it -> {value_Letters(use_Word)} points")

task16()
task18()
task20()