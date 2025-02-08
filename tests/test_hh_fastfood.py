from selene import browser, be, have, by
import time

from mixins.config import Config

"""
Открыть сайт ХХ - https://spb.hh.ru/
Нажать помощь
Выбрать вариант "связаться с нами" - вызвать чат с ботом
Написать сообщение боту: "Привет, робот! Как найти работу?"
В ответ ожидаем текст со ссылкой на https://spb.hh.ru/search/vacancy/advanced

"""
def test_find_search_vacancy_via_bot():
    browser.open(Config.BASE_URL)
    browser.element(by.xpath('//*[@id="HH-React-Root"]/div/div[3]/div/div/div/div/div[1]/button')).click()
    browser.element(by.xpath("/html/body/div[12]/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div[1]/div/div/div/div")).click()

    time.sleep(2)
    text_area = browser.element(by.css('textarea[data-qa="chatik-new-message-text"]'))
    text_area.click()
    # text_area = browser.element(by.xpath('//*[@id="chatik-layout"]/div/div/div/div/div/div[3]/div/div[2]/div[2]/textarea'))
    # browser.wait()
    # text_area = browser.element(by.)
    text_area.type("Привет, робот! Как найти работу?")
    browser.element(by.css('span[data-qa="chat-bubble-text"]')).should(have.url_containing('https://spb.hh.ru/search/vacancy/advanced'))
    # browser.all('#rso>div').should(have.size_greater_than(5))\
    #     .first.should(have.text('Selenium automates browsers'))