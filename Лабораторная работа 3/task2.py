# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, splitter= ','):
    participants_1_group=set(str1.split(splitter))
    participants_2_group=str2.split(splitter)
    intersection_list = participants_1_group.intersection(participants_2_group)
    return list(intersection_list)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, splitter="|"))