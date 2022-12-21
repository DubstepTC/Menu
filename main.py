import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main():
    # Запускаем селениум
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    driver.set_window_size(1440, 900)
    driver.get("https://ras.arbitr.ru")
    btn_submit = driver.find_element(By.ID, "b-form-submit")
    btn_submit.click()
    time.sleep(10)
    cookiess = driver.get_cookies()
    cookies = {}
    for ck in cookiess:
        print(ck)
        if ck['name'] != 'tmr_lvidTS' and ck['name'] != 'tmr_lvid' and  ck['name'] != 'tmr_detect':
            cookies[ck["name"]] = ck['value']
        elif ck['name'] == 'tmr_lvid':
            cookies["wasm"] = ck['value']
    print(cookies)

    # Для отправки запроса
    # cookies = {
    #     'CUID': '6f8302f1-1b0d-4972-a63e-d452ffe37471:ouexLSV98QYuZFAeidMBHA==',
    #     '_ga': 'GA1.2.2137527451.1670217850',
    #     '_ym_uid': '1670217850106978457',
    #     '_ym_d': '1670217850',
    #     'ASP.NET_SessionId': 'w1tpo30qwcwzxmm1pv1d0n4u',
    #     'is_agree_privacy_policy': 'true',
    #     '__ddg1_': 'b4jlbszVg4mIWLkVIGFf',
    #     'pr_fp': '991ff8667cb35dc80204e4a53fbf748c0599ecfaba096a1783fb4a1bc1b0b4f3',
    #     '_gid': 'GA1.2.1433893127.1671430957',
    #     'rcid': '2af6eeb8-169a-4dd8-a2b3-f8a6326df2d0',
    #     '_gat': '1',
    #     '_gat_FrontEndTracker': '1',
    #     '_dc_gtm_UA-157906562-1': '1',
    #     '_ym_isad': '2',
    #     'wasm' : "7c006427cb6caaee999cd70042a15979"
    # }
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

    text_search = input("Введите слово которое хотите искать: ")

    json_data = {
        'GroupByCase': False,
        'Count': 25,
        'Page': 1,
        'DateFrom': '2000-01-01T00:00:00',
        'DateTo': '2030-01-01T23:59:59',
        'Sides': [],
        'Judges': [],
        'Cases': [],
        'Text': text_search,
    }

    # запрос для получения всех совпадений от ras.arbitr.ru
    response = requests.post('https://ras.arbitr.ru/Ras/Search', cookies=cookies, headers=headers_1, json=json_data)
    print(response.text)

    with open('json_response.json', 'a', encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

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
        'hilightText': text_search,
    }

    with open('json_response.json', 'r', encoding="utf-8") as file:
        json_response_data = json.load(file)

    json_answer_data = []

    text_split_search = text_search.split()

    for i in json_response_data['Result']['Items']:

        response_2 = requests.post(
            'https://ras.arbitr.ru/Ras/HtmlDocument/' + i['Id'],
            cookies=cookies,
            headers=headers_2,
            data=data,
        )
        with open('index.html', 'w', encoding="utf-8") as file:
            file.write('')
            file.write(response_2.text)
        with open('index.html', 'r', encoding="utf-8") as file:
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



    print(json_answer_data)




if __name__ == '__main__':
    main()
