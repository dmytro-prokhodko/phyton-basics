numbers1 = [5, 10, 15, 20, 25, 30, 35]
numbers2 = [3, 6,9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

common_numbers = [] # создаем пустой список для результата
for num in numbers1:
    if num in numbers2:
        common_numbers.append(num)
print ("Common numbers", common_numbers)
combined_numbers  = numbers1.copy()

for num in numbers2:
    if num not in combined_numbers: #если числа нет в списке
        combined_numbers.append(num) #добавляем его
print ("Combined list without duplicates: ", combined_numbers)
even_count1 = 0
odd_count1 = 0

for num in numbers1:
    if num % 2 == 0:
        even_count1 = even_count1 + 1 
    else:
        odd_count1 = odd_count1 + 1
print ("\nВ numbers1 четных: ", even_count1, "нечетных", odd_count1)
doubled_numbers1 = []
for num in numbers1:
    doubled_numbers1.append(num * 2)
print ("Doubled numbers1:", doubled_numbers1)
even_count2 = 0
odd_count2 = 0

for num in numbers2:
    if num % 2 == 0:
        even_count2 = even_count2 + 1
    else:
        odd_count2 = odd_count2 + 1
print ("\nВ numbers2 четных: ", even_count2, "нечетных", odd_count2)
