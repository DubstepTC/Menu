import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from menu import menu

def selenium_det_cookies():

    # Настройки
    options = Options()
    options.headless = False
    # циганская магия которая помогла обойти защиту
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # прокси для избежания блокировки
    # options.add_argument(f"--proxy-server-{proxies['https']}")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    driver.maximize_window()

    # Запускаем селениум
    driver.get("https://ras.arbitr.ru")

    # Находим кнопку
    btn_submit = driver.find_element(By.XPATH, "//*[@id=\"b-form-submit\"]/div/button")
    btn_submit.click()

    # Получаем куки
    time.sleep(7)
    cookiess = driver.get_cookies()
    cookies = {}
    for ck in cookiess:
        cookies[ck["name"]] = ck['value']
    # проверка получили ли мы нужные куки
    if "wasm" in cookies.keys():
        print("Нужные куки получены")
        return cookies
    else: print("Что-то пошло не так")


def courts_into_code(courts_name):
    with open("static_data/courts_list.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    for key, value in data.items():
        if courts_name == value:
            return key



def get_context_25(cookies, text, courts, date_from, date_to):

    headers_1 = {
        'authority': 'ras.arbitr.ru',
        'accept': 'application/json, text/javascript, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'CUID=6f8302f1-1b0d-4972-a63e-d452ffe37471:ouexLSV98QYuZFAeidMBHA==; _ga=GA1.2.2137527451.1670217850; _ym_uid=1670217850106978457; _ym_d=1670217850; ASP.NET_SessionId=w1tpo30qwcwzxmm1pv1d0n4u; is_agree_privacy_policy=true; __ddg1_=b4jlbszVg4mIWLkVIGFf; pr_fp=991ff8667cb35dc80204e4a53fbf748c0599ecfaba096a1783fb4a1bc1b0b4f3; _gid=GA1.2.1433893127.1671430957; rcid=2af6eeb8-169a-4dd8-a2b3-f8a6326df2d0; _ym_isad=2; wasm=582b2b282a6d602294ecbf51dfc6e027',
        'origin': 'https://ras.arbitr.ru',
        'referer': 'https://ras.arbitr.ru/',
        'sec-ch-ua': '"Opera";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 02)',
        'x-requested-with': 'XMLHttpRequest',
    }

    if date_from == '':
        date_from = "2000-01-01T00:00:00"
    else:
        date_from = date_from.split()
        date_from = date_from[0] + "T" + "00:00:00"

    if date_to == '':
        date_to = "2030-01-01T23:59:59"
    else:
        date_to = date_to.split()
        date_to = date_to[0] + "T" + "00:00:00"

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

    if courts != '':
        json_data["Courts"] = [courts_into_code(courts)]

    # запрос для получения всех совпадений от ras.arbitr.ru
    response = requests.post('https://ras.arbitr.ru/Ras/Search',
                             cookies=cookies,
                             headers=headers_1,
                             json=json_data,
                             # proxies=proxies
                             )
    answer = response.json()
    print(answer['Result']['PagesCount'], answer['Result']['TotalCount'])
    return answer

def get_into_and_search(text, parent_context, cookies):

    headers_2 = {
        'authority': 'ras.arbitr.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'CUID=6f8302f1-1b0d-4972-a63e-d452ffe37471:ouexLSV98QYuZFAeidMBHA==; _ga=GA1.2.2137527451.1670217850; _ym_uid=1670217850106978457; _ym_d=1670217850; ASP.NET_SessionId=w1tpo30qwcwzxmm1pv1d0n4u; is_agree_privacy_policy=true; __ddg1_=b4jlbszVg4mIWLkVIGFf; pr_fp=991ff8667cb35dc80204e4a53fbf748c0599ecfaba096a1783fb4a1bc1b0b4f3; _gid=GA1.2.1433893127.1671430957; rcid=2af6eeb8-169a-4dd8-a2b3-f8a6326df2d0; _ym_isad=2; wasm=b9dcaac2a6024df09f5398f14ea4b639',
        'origin': 'https://ras.arbitr.ru',
        'recaptchatoken': 'undefined',
        'referer': 'https://ras.arbitr.ru/',
        'sec-ch-ua': '"Opera";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 02)',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'hilightText': text,
    }

    json_answer_data = []

    text_split_search = text.split()

    for i in parent_context['Result']['Items']:

        response_2 = requests.post(
            'https://ras.arbitr.ru/Ras/HtmlDocument/' + i['Id'],
            cookies=cookies,
            headers=headers_2,
            data=data,
            # proxies=proxies
        )
        with open('pars_data/index.html', 'w', encoding="utf-8") as file:
            file.write('')
            file.write(response_2.text)
        with open('pars_data/index.html', 'r', encoding="utf-8") as file:
            hilight_text_data = file.read()

        soup = BeautifulSoup(hilight_text_data, "lxml")
        search_words = soup.find_all("span", class_="g-highlight")
        for j in range(len(search_words)):
            search_words[j] = search_words[j].text
        for j in range(len(search_words) - len(text_split_search)):
            if search_words[j:j + len(text_split_search)] == text_split_search:
                print("успех")
                json_answer_data.append(i)
                break
        print("Итерация...")
        time.sleep(1)
    return json_answer_data


def main():

    values = menu()
    text_search = values[0]
    courts_search = values[1]
    date_from = values['-IN-']
    date_to = values['-IN2-']


    cookies = selenium_det_cookies()
    data_page_1 = get_context_25(cookies, courts_search, text_search, date_from, date_to)
    answer = get_into_and_search(text_search, data_page_1, cookies)
    print(answer)



if __name__ == '__main__':
    main()
