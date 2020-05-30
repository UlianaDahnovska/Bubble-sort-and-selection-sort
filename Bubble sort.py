def bubble_sort(nums):
#Ми встановлюємо swapped на True, щоб цикл відбувався хоч раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                #Міняємо елементи місцями
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                #swapped встановлюємо на True на продовжуємо цикл
                swapped = True
#Приклад
random_list_of_nums = [10, 6, 38, 8, 34]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
