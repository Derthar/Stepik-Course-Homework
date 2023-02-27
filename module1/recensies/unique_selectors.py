import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    LINK = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys("ss@asd.sa")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations!" == welcome_text #  AssertionError
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



    Пара комментариев чисто от себя. Понимаю что основа кода была взята от авторов курса, но тем не менее 

Это никак не влияет на оценки выполнения задачи, просто небольшой совет на будущее начинающему автоматизатору :)  

    Строки 16-17:

Нет необходимости складывать поиск элемента в переменную и потом вызывать click по этой переменной. Можно сделать также как в строках 11-13. Например,

"browser.find_element(By.CSS_SELECTOR, 'button').click()"

    Строки 23-30:

Нет прямой необходимости вытаскивать с сайта содержимое заголовка и сравнивать с ним большое приветственное сообщение, вполне достаточно более лаконичного : 

assert "Welcome" in browser.title
    Еще Питон ругается на строчку browser.quit() в блоке finally, так как обьявление браузера происходит в блоке try.

Блок finally должен выполняться в любом случае, независимо от того будет ошибка в блоке try или нет. Но если поместить инициализацию браузера в блок try вполне вероятно это может привести к ошибке до момента выполнения строки 7, и тогда у нас упадет вторая ошибка, так как в строке 36 питон не будет знать что такое этот browser и что он должен сделать. Фиксится это просто : нужно строки 6 и 7 поставить перед блоком try
