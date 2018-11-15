#Программа отгадай число
import random

def chislo():
   print('Добро пожаловать в игру "Отгадай число"')
   print('Я загадаю чтсло от 1 до 100')
   print('Постарайся отгадать его за 10 попыток')
   chislo = random.randint(1,100)
   chislo1 = int(input('Ваш вариант: '))
   popitka = 1

   
   while chislo1 != chislo:
      
      if chislo1 > chislo:
         print('Число меньше чем вы ввели')
         
      else:
         print('Число больше чем вы ввели')
         
      popitka += 1
      chislo1 = int(input('Ваш вариант: '))
      if popitka == 10:
         print('Ты тупой неудачник))))))')
         input('Нажмите ентер что бы посмотреть результат')
         print('Число которое я загадал ',chislo)
         break
      if chislo1 == chislo:
      
         print('Вам удалось отгадать число,это',chislo)
         print('Вам понадобилось',popitka,' попыток')
         
chislo()
print('Спасибо что играли в эту игру')
input('Нажмите Enter что бы выйти из игры')



   
