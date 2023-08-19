import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step("Открываем главную страницу GitHub")
def open_page():
    browser.open("https://github.com")


@allure.step("Вводим в строку поиска {search_repo}")
def input_repo_in_search_field(search_repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(search_repo)
    s("#query-builder-test").press_enter()


@allure.step("Переходим в репозиторий {repo}")
def go_to_required_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим в 'Issues'")
def go_to_issues(issue):
    s(issue).click()


@allure.step("Проверяем наличие текста")
def check_text(text):
    s(by.partial_text("#76")).should(be.visible)


def test_github_with_lambda_steps():
    open_page()
    input_repo_in_search_field('eroshenkoam/allure-example')
    go_to_required_repo("eroshenkoam/allure-example")
    go_to_issues("#issues-tab")
    check_text("#76")

