<h1 align="center">Проект "Autoavia"</h1>

![Иллюстрация](papich.jpg)

<h1 align="center">...utoavia</h1>

# Контент

- [Дальнейшее развитие проекта](#дальнейшее-развитие-проекта)
- [Переделать функционал](#переделать-функционал)
- [Расчет стоимости билета по формуле](#расчет-стоимости-билета-по-формуле)
- [Статьи для чтения](#статьи-для-чтения)


# Дальнейшее развитие проекта

* [ ] GUI-интерфейс
* [x] DATABASE для запоминания информации о текущих самолетах
* [ ] **_Интерфейс_** для пользователя в WEB без админских прикольчиков
* [ ] Купить мини системный блок с **минимальным** потреблением для использования в роли сервера
* [ ] Базу данных и веб страничку грузить на сервер


# Переделать функционал
         ```def select_airplane(self):
                """
                Select airplane.

                This function selects an airplane for further operation
                from the list of airplanes

                Raises:
                    IndexError, ValueError

                Examples:
                    airplanes = [plane1, plane2]
                    airplane = None
                    >>> select_airplane()
                    '0 plane1
                    1 plane2'
                    >>> 'Input number of plane: 0'
                    airplanes = [plane1, plane2]
                    airplane = plane1
                """
                try:
                    for i, pl_class in enumerate(self.airplanes):
                        print(i, pl_class.name)
                    self.airplane = self.airplanes[int(input('Input number of plane: '))]
                except IndexError:
                    print('Index Error / 0 airplanes')
                except ValueError:
                    print('Input must be int')```

# Расчет стоимости билета по формуле

$`эконом = коэф.востребованности * 10`$<br>
$`бизнес = коэф.востребованности * 20`$<br>
$`элита = коэф.востребованности * 30`$

## Статьи для чтения

- [Базы данных](https://habr.com/ru/companies/amvera/articles/754702/)
- [Сервер](https://habr.com/ru/articles/724650/)

![Иллюстрация](smileface.jpg)
