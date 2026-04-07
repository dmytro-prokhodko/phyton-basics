numbers1 = [5, 10 , 15, 20, 25, 30, 35]
numbers2 = [3, 6,9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
print("Вывод первого списка через for: ")
for x in numbers1:
    print (x)
print ("Вывод второго списка через While: ")
i = 0 
while i < len (numbers1):#пока i меньше длины списка
    print (numbers2[i]) #печатаем число под номером i
    i = i + 1 #сдвигаем счетчик на 1 вперед
print ("\nСчитаем сумму:")
total_sum = 0 
for num in numbers1:
    total_sum = total_sum + num #добавляем число которое сейчас к общей сумме 
print ("Сумма всех чисел первого списка:", total_sum)
print ("\nИщем максимум:")
max_num = numbers2[0]

for num in numbers2:
    if num >  max_num: #если нашли число больше максимального значения
        max_num = num  #то теперь оно становится максимальным
print  ("Максимальное число во втором списке:", max_num)
