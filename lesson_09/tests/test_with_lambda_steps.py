import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_with_lambda_steps():
    with allure.step("Открываем главную страницу GitHub"):
        browser.open("https://github.com")

    with allure.step("Вводим в строку поиска 'eroshenkoam/allure-example'"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").press_enter()

    with allure.step("Переходим в репозиторий 'eroshenkoam/allure-example'"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим в 'Issues'"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие текста"):
        s(by.partial_text("#76")).should(be.visible)
