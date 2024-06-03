def merge_and_sort_desc(list1, list2):
    i, j = 0, 0
    res = []

    # Слияние двух отсортированных списков в один
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    # Добавление оставшихся элементов
    while i < len(list1):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1

    return res


# Ввод данных от пользователя
list1 = list(map(int, input("Введите элементы первого списка, разделенные пробелом: ").split()))
list2 = list(map(int, input("Введите элементы второго списка, разделенные пробелом: ").split()))

# Проверка, что списки отсортированы по возрастанию
list1.sort()
list2.sort()

result = merge_and_sort_desc(list1, list2)
print("Результирующий список:", result)
