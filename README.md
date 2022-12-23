### Установка
К сожалению не удалось переместить проект в исполняемый файл exe
```
git clone https://github.com/DubstepTC/Menu.git
```
Создаем виртуальное окружение
Устанавливаем нужные библиотеки
```
pip install selenium requests bs4 lxml pandas openpyxl PySimpleGUI
```

### Архитектура


Aequum v.1.1 представляет из себя парсер написанный на языке Python с использованием таких библиотек как Selenium, Request, bs4,  а также pandas и PySimpleGUI

Программа разбита на 6 частей:
1.	Запускается меню, в котором пользователя просят ввести данные для поиска:
Текст для поиска: - без ограничений
Суд – если выбор не произведен, ищет по всем судам
Дата С, По – если не указаны ищет по всей базе данных
Если указана только «Дата С» ищет с указанной даты и далее
Если указана только «Дата По» ищет не позднее указанной даты 

2.	Запускается имитатор браузера Selenium и отправляет на сайт https://ras.arbitr.ru запрос, после запроса генерируются cookies которые нужны для идентификации пользователя и работы сайта, а именно “wasm”. С помощью команды считывания cookies файлов мы забираем нужные нам cookies.
3.	
4.	Далее мы подставляем нужные нам cookies в запрос типа:
```python
response = requests.post('https://ras.arbitr.ru/Ras/Search',
                             cookies=cookies,
                             headers=headers,
                             json=json_data)
```

Где json_data данные, которые мы вбили в меню, в формате
```
json_data = {
    'GroupByCase': False,
    'Count': 25,
    'Page': 1,
    'DateFrom': date_from,
    'DateTo': date_to,
    'Sides': [],
    'Judges': [],
    'Cases': [],
    'Text': text,
}
```
Результатом запроса будет json в котором будут все документы с найденной строкой с учетом склонений падежей и т.п

4. Далее мы с учетом полученных данных делаем второй запрос, который используется для просмотра конкретного дела, он имеет вид:
```python
response = requests.post(
    'https://ras.arbitr.ru/Ras/HtmlDocument/' + Id документа,
    cookies=cookies,
    headers=headers,
    data=data)
```
где data:
```
data = {
    'hilightText': text,
}
```
Дело в том, что при указании этого параметра, в браузере найденные совпадения по строке, которую мы ввели, подсвечиваются желтым цветом 

5.	На четвертом этапе мы считываем html страницу и ищем теги <span> которому присвоен класс “g-highlight”. В итоге мы получаем массив слов, и чтобы проверить совпадает ли полностью наша строка тому, что написано на сайте мы ищем подмассив слов (который является нашей строкой поиска) в массиве найденых слов, и если получено точное совпадение, данные о документе записываются в результирующий массив
  
6.	Данные из результирующего массива записываются в Excel файл
 
### Ограничения, проблемы, баги

На данный момент программа работает в тестовом режиме и может обработать только 25 документов
Так-как программа представляет из-себя парсер, то велика вероятность что сайт вас обнаружит и заблокирует доступ.
Этому есть несколько способов противодействия:
1.	Программа пытается имитировать скорость человека, чтобы сайт не сразу понял, что вы программа поэтому периодичность запросов снижена, 1 запрос в 1-2 секунды (реализовано)
2.	Авторизация через госуслуги, чтобы дать понять сайту то, что вы реальный человек (не реализовано в v.1.1)
3.	Отправка запросов используя proxy человек (не реализовано в v.1.1)

  
### Данные для проверки
  
Для того чтобы с первого раза убедиться в работе программы, лучше вбить данные, который 100% найдут совпадения например  
```
Текст - мясной продукции
Дата С - 20.12.2022
```
  
### Техподдержка (еслим ее можно так назвать) 
Александр Журавлев - тег takeshidze (в любых соц сетях), тел +7**********
