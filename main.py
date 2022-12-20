import PySimpleGUI as sg

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Добро пожаловать в наше приложение')],
            [sg.Text('Введите текст', size = (13, 1)), sg.MLine(size=(43,6), enter_submits=True)],
            [sg.Text('Суд', size = (13, 1)), sg.Combo(
             ['Верховный Суд РФ', 'Высший Арбитражный Суд РФ','АС Волго-Вятского округа',
              'АС Восточно-Сибирского округа','АС Дальневосточного округа','АС Западно-Сибирского округа',
              'АС Московского округа','АС Поволжского округа','АС Северо-Западного округа',
              'АС Северо-Кавказского округа','АС Уральского округа','АС Центрального округа',
              '1 арбитражный апелляционный суд','2 арбитражный апелляционный суд', "3 арбитражный апелляционный суд",
              "4 арбитражный апелляционный суд", "5 арбитражный апелляционный суд", "6 арбитражный апелляционный суд",
              "7 арбитражный апелляционный суд", "8 арбитражный апелляционный суд", "9 арбитражный апелляционный суд",
              "10 арбитражный апелляционный суд", "11 арбитражный апелляционный суд", "12 арбитражный апелляционный суд",
              "13 арбитражный апелляционный суд", "14 арбитражный апелляционный суд", "15 арбитражный апелляционный суд",
              "16 арбитражный апелляционный суд", "17 арбитражный апелляционный суд", "18 арбитражный апелляционный суд",
              "19 арбитражный апелляционный суд", "20 арбитражный апелляционный суд", "21 арбитражный апелляционный суд",
              "АС Алтайского края", "АС Амурской области", "АС Архангельской области", "АС Астраханской области",
              "АС Белгородской области", "АС Брянской области", "АС Владимирской области", "АС Волгоградской области",
              "АС Вологодской области", "АС Воронежской области", "АС города Москвы", "АС города Санкт-Петербурга и Ленинградской области",
              "АС города Севастополя", "АС Донецкой Народной Республики", "АС Еврейской автономной области", "АС Забайкальского края",
              "АС Запорожской области", "АС Ивановской области", "АС Иркутской области", "АС Кабардино-Балкарской Республики",
              "АС Калининградской области", "АС Калужской области", "АС Камчатского края", "АС Карачаево-Черкесской Республики",
              "АС Кемеровской области", "АС Кировской области", "АС Коми-Пермяцкого АО", "АС Костромской области",
              "АС Краснодарского края", "АС Красноярского края", "АС Курганской области", "АС Курской области",
              "АС Липецкой области", "АС Луганской Народной Республики", "АС Магаданской области", "АС Московской области",
              "АС Мурманской области", "АС Нижегородской области", "АС Новгородской области", "АС Новосибирской области",
              "АС Омской области", "АС Оренбургской области", "АС Орловской области", "АС Пензенской области", "АС Пермского края",
              "АС Приморского края", "АС Псковской области", "АС Республики Адыгея", "АС Республики Алтай", "АС Республики Башкортостан",
              "АС Республики Бурятия", "АС Республики Дагестан", "АС Республики Ингушетия", "АС Республики Калмыкия",
              "АС Республики Карелия", "АС Республики Коми", "АС Республики Крым", "АС Республики Марий Эл",
              "АС Республики Мордовия", "АС Республики Саха", "АС Республики Северная Осетия", "АС Республики Татарстан",
              "АС Республики Тыва", "АС Республики Хакасия", "АС Ростовской области", "АС Рязанской области",
              "АС Самарской области", "АС Саратовской области", "АС Сахалинской области", "АС Свердловской области",
              "АС Смоленской области", "АС Ставропольского края", "АС Тамбовской области", "АС Тверской области",
              "АС Томской области", "АС Тульской области", "АС Тюменской области", "АС Удмуртской Республики",
              "АС Ульяновской области", "АС Хабаровского края", "АС Ханты-Мансийского АО", "АС Херсонской области",
              "АС Челябинской области", "АС Чеченской Республики", "АС Чувашской Республики", "АС Чукотского АО",
              "АС Ямало-Ненецкого АО", "АС Ярославской области", "ПСП Арбитражного суда Пермского края",
              "ПСП Арбитражный суд Архангельской области", "Суд по интеллектуальным правам"], size = (43,1), readonly=True)],
            [sg.Text('Период', size = (16, 1)), sg.CalendarButton('С', close_when_date_chosen=True,  target='-IN-', location=(0,0), no_titlebar=False, size =(5,1)),
             sg.Input(key='-IN-', size=(9,1), readonly=True, disabled_readonly_background_color='#335267'), sg.CalendarButton('По', close_when_date_chosen=True,  target='-IN2-', location=(0,0), no_titlebar=False, size =(5,1)),
             sg.Input(key='-IN2-', size=(9,1), readonly=True,disabled_readonly_background_color='#335267')],
            [sg.Button('Ok'), sg.Button('Cancel')],]

# Create the Window
window = sg.Window('Aequum', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Текст', values[0])
    print('Суд', values[1])
    print('Период', 'C', values['-IN-'], 'По', values['-IN2-'])
window1.close()
