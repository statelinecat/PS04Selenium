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
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import random


browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(5)
action1 = input("\nВведите запрос: ")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(action1)
search_box.send_keys(Keys.RETURN)
time.sleep(10)
a = browser.find_element(By.LINK_TEXT, action1)
a.click()

while True:
    action2 = input("\nВыберите действие:\n"
                "1. Листать параграфы текущей статьи\n"
                "2. Перейти на одну из связанных страниц\n"
                "3. Выйти\n")

    if action2 == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            per = input("\nНажмите Enter для продолжения или 0 для выхода: ")
            if per == "0":
                break

    elif action2 == "2":
        hatnotes = []
        links = browser.find_elements(By.TAG_NAME, "div")
        for link in links:
            cl = link.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(link)
        print(hatnotes)
        if len(hatnotes) == 0:
            print("Нет связанных страниц")
        else:
            hatnote = random.choice(hatnotes)
            link1 = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link1)

    elif action2 == "3":
        time.sleep(2)
        browser.quit()
        exit()







