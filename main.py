from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f)
    contacts_list = list(rows)
##pprint(contacts_list)
##выполните пункты 1-3 ДЗ

##создаем шаблон поиска телефонов
pattern = r"(\+7\s|8\s|\+7|8)\(?(\d{3})\)?\s?[-]?(\d{3})[-]?(\d{2})[-]?(\d{2})\s?\(?(доб.)?\s?(\d{4})?\)?"

##создаем шаблон для приведения телефонов к виду, указанному в задании
new_pattern = r"+7(\2)\3-\4-\5 \6\7"

##создаем новый список абонентов

new_list = list()
for collumn in contacts_list:
    ##объединяем элементы в collumn и разбиваем на части для формирования нового списка
    full_name = ' '.join(collumn).split(' ')
    ##заполняем список по-новому
    result = [full_name[0], full_name[1], full_name[2], collumn[3], collumn[4],
              re.sub(pattern, new_pattern, collumn[5]), collumn[6]]
    new_list.append(result)
##print(new_list)

##заполняем все столбцы списка
for number in new_list:
    last_name = number[0]
    first_name = number[1]
    for new_number in new_list:
        new_last_name = new_number[0]
        new_first_name = new_number[1]
        if last_name == new_last_name and first_name == new_first_name:
            if number[2] == "":
                number[2] = new_number[2]
            if number[3] == "":
                number[3] = new_number[3]
            if number[4] == "":
                number[4] = new_number[4]
            if number[5] == "":
                number[5] = new_number[5]
            if number[6] == "":
                number[6] = new_number[6]

##print(new_list)

##удаляем из списка дублирующиеся записи
final_list = [] #формируем итоговый список
for record in new_list:
    if record not in final_list:
        final_list.append(record)
##print(final_list)


##сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_final.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_list)

