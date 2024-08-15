# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
#
# 1. Спрашивать у пользователя первоначальный запрос.
#
# 2. Переходить по первоначальному запросу в Википедии.
#
# 3. Предлагать пользователю три варианта действий:
#
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
#
# - перейти на одну из внутренних статей.
#
# выйти из программы.


from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(5)
action1 = input("\nВведите запрос: ")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(action1)
search_box.send_keys(Keys.RETURN)
a = browser.find_element(By.LINK_TEXT, action1)
#Добавляем клик на элемент
a.click()

action2 = input("\nВыберите действие:\n"
               "1. Листать параграфы текущей статьи\n"
               "2. Перейти на одну из связанных страниц\n"
               "3. Выйти\n")

if action2 == "1":
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("\nНажмите Enter для продолжения...")





time.sleep(10)
browser.quit()

