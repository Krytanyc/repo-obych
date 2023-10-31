# TODO Напишите функцию find_common_participants
def fcp(participants_first_group, participants_second_group, sep='|'):
    pfg = participants_first_group.split(sep)
    psg = participants_second_group.split(sep)
    pfgg = set(pfg)
    classe = pfgg.intersection(psg)
    classe = list(classe)
    classe.sort()
    return classe

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(fcp(participants_first_group, participants_second_group), sep='|')
# TODO Провеьте работу функции с разделителем отличным от запятой
