import pytest
from selene import be, have
from selene.support.shared import browser


def test_1(web_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
    browser.quit()


def test_2(web_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qweqweq1231231weqweqwe').press_enter()
    browser.element('.card-section [aria-level="3"]').should(have.text('По запросу qweqweq1231231weqweqwe ничего не найдено. '))
    browser.quit()


print('Ещё раз поменял пользователем два для конфликта')

