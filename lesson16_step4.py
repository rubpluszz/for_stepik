
from selenium import webdriver


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("I")#ввод имени
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("P")#ввод фамилии
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("S")#ввод города
    input4 = browser.find_element_by_id("country")
    input4.send_keys("R")#ввод стрвны
    button = browser.find_element_by_xpath("//div[6]/button[contains(text(), 'Submit')]")
    button.click()#отправка

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    webdriver.quit()
