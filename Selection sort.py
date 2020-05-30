def selection_sort(nums):
    #значення i дорівнює тому, скількі значень було відсортовано
    for i in range(len(nums)):
        #Ми припускаємо, що перший елемент несортованого сегмента є найменшим
        lowest_value_index = i
        #Цей цикл перебирає несортовані елементи
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        #Поміняти місцями значення найнижчого несортованого елемента з першим несортованим
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#Приклад
random_list_of_nums = [34, 7, 2, 16, 32]
selection_sort(random_list_of_nums)
print(random_list_of_nums)
