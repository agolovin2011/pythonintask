﻿#Задача 9. Вариант 7.
#1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

#Cherniy F. Y.
#22.04.2016

import random
words = ("мир", "труд", "майские", "праздники", "скоро")
word = random.choice(words)
proverka = word
letters = len(word)
letter = random.randrange(letters)
i = 4
print("Я загадал некоторое слово на русском языке. В нём ", letters, " букв(/-ы).")
print("У Вас есть 5 попыток угадать буквы в этом слове!")
guess = input("Введите букву: ")
while i > 0:
	if guess in word:
		print("Есть такая буква!")
	else: print("Такой буквы нет, крутите барабан!")
	i -= 1
	guess = input("Введите ещё одну букву: ")
guess = input("Назовёте слово целиком? Хотя бы попытайтесь: ")
if guess == word:
	print("Всё верно! Это слово", word)
else:
	print("Вы даже не старались...")
input ("\nНажмите Enter для выхода.")