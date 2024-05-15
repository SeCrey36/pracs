""" NEED TO INSTALL pydocxtpl!!!
JSON:
    ФИО
    Группа
    Номер зачетки
    Институт
    Кафедра

Обновляемые (вводятся):
    Тема
    Номер практической

Выборочные (выбираются из списка):
    ФИО препода

Автоматические:
    Дата
"""


from pydocxtpl import DocxWriter
from datetime import date
import json
import sys


def cfg_create():  # create json
    name = input('Введите ваше ФИО в формате "Иванов И.И.": ')
    book_id = input('Номер зачетной книжки: ')
    group = input('Группа (пример: КИ23-17/1Б): ')
    department = input('Кафедра: ')
    institute = input('Институт: ')

    temp = {'name': name, 'group': group, 'book_id': book_id, 'institute': institute, 'department': department}
    with open("data.json", "w") as fh:
        json.dump(temp, fh)


def cfg_export():  # return list info
    with open("data.json", "r") as fh:
        return json.load(fh)


def create_doc():  # work with docx
    lessons = ['ВВПД', 'Информатика']
    teachers = ['Пересунько П.В.', 'Пупков А.Н.']
    if 1:
        temp = cfg_export()
        current_date = str(date.today().strftime("%d-%m-%Y")).replace('-', '.')
        for i in range(len(lessons)):
            print(i+1, lessons[i])
        lesson = lessons[int(input('Какой предмет из списка? (номер): '))-1]
        teacher = teachers[lessons.index(lesson)]
        theme = input('Тема практической: ')
        number = input('Номер: ')
        filename = 'template.docx'
        doc = DocxWriter(filename)
        context = {'institute': temp['institute'], 'department': temp['department'],
                   'num': number, 'theme': theme, 'group': temp['group'], 'name': temp['name'],
                   'book_id': temp['book_id'], 'date': current_date,
                   'teacher': teacher}
        doc.render(context)
        save_name = lesson+'_'+number+' '+temp['name']
        doc.save(save_name+'.docx')


def main():
    print('Приветствую в AutoReport! Для начала работы '
          'необходимо заполнить конфиг, чтобы запомнить Ваши данные. \n'
          'Если вы уже смешарик, пропустите этот пункт.')

    while True:
        com = input('''
    Команды: 
        1 - Заполнить конфиг
        2 - Отобразить конфиг
        3 - Перейти к генерации шаблона
        4 - Выйти из программы
            ''')
        if com == '4':
            sys.exit()
        elif com == '1':
            cfg_create()
        elif com == '2':
            print(cfg_export())
        elif com == '3':
            try:
                create_doc()
                print('Done!')
            except:
                print('CFG Error')
        else:
            print('Некорректный ввод команды!')


if __name__ == '__main__':
    main()
