from selene import browser
from selene import be, have, command


#locators
first_name_locator = '//input[@id="firstName"]'
last_name_locator = '//input[@id="lastName"]'
email_locator = '//input[@id="userEmail"]'

gender_male_locator = '//input[@id="gender-radio-1"]'
gender_female_locator = '//input[@id="gender-radio-2"]'
gender_other_locator = '//input[@id="gender-radio-3"]'

mobile_locator = '//input[@id="userNumber"]'

date_of_birth_locator = '//input[@id="dateOfBirthInput"]'
month_locator = '//select[@class="react-datepicker__month-select"]'
year_locator = '//select[@class="react-datepicker__year-select"]'
day_container_locator = '//select[@class="react-datepicker__month-container"]'

subjects_locator = '//input[@id="subjectsContainer"]'

hobbies_sports_locator = '//input[@id="hobbies-checkbox-1"]'
hobbies_reading_locator = '//input[@id="hobbies-checkbox-2"]'
hobbies_music_locator = '//input[@id="hobbies-checkbox-3"]'

picture_locator = '//input[@id="uploadPicture"]'
address_locator = '//input[@id="currentAddress"]'

select_state_locator = '//input[@id="state"]'
select_city_locator = '//input[@id="city"]'

submit_button_locator = '//button[@id="submit"]'
submitting_form_locator = '//div[@id="example-modal-sizes-title-lg"]'


def test_5():

    first_name = 'Ivan'
    last_name = 'Ivanov'
    email = 'asdfg@mail.ru'
    mobile = '0123456789'
    birth_month = 'jan'
    birth_year = '1988'
    birth_date = '14'
    address = 'city One and street Two'
    state = 'NCR'
    city = 'Noida'
    submitting_text = 'Thanks for submitting the form'

    #открытие нужной страницы
    browser.open('/automation-practice-form')

    #Ввод имени и фамилии
    browser.element(first_name_locator).should(be.blank).type(first_name)
    browser.element(last_name_locator).should(be.blank).type(last_name)

    #Ввод емейла
    browser.element(email_locator).should(be.blank).type(email)

    #Выбор пола
    browser.element(gender_male_locator).click()

    #Ввод номера мобильного телефона
    browser.element(mobile_locator).should(be.blank).type(mobile)

    #Открытие календаря и выбор даты рождения
    browser.element(date_of_birth_locator).click()
    browser.element(month_locator).type(birth_month).press_enter()
    browser.element(year_locator).type(birth_year).press_enter()
    browser.all(day_container_locator).element_by(have.text(birth_date)).click()

    #Выбор хобби
    browser.element(hobbies_reading_locator).should(be.disabled).click()

    #Отправка картинки
    browser.element(picture_locator).send_keys('../date_for_sending/for_send.bmp')

    #Ввод адреса
    browser.element(address_locator).should(be.blank).type(address)

    #Выбор штата и города
    browser.element(select_state_locator).type(state).press_enter()
    browser.element(select_city_locator).type(city).press_enter()

    #Подтверждение формы
    browser.element(submit_button_locator).click()

    #Проверка на наличие формы подтверждения регистрации
    browser.element(submitting_form_locator).should(have.text(submitting_text))








