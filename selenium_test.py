import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def main():

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

if __name__ == '__main__':
    main()