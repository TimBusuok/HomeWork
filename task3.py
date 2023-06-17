# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

luckyNum = input("Введите номер билета: ")

firstNum = int(luckyNum[0]) + int(luckyNum[1]) + int(luckyNum[2])
lastNum = int(luckyNum[3]) + int(luckyNum[4]) + int(luckyNum[5])

if firstNum == lastNum:
    print(f"{luckyNum} -> yes")
else:
    print(f"{luckyNum} -> no")