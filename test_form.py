import allure

from demoqa_test.pages.registration_page import RegistrationPages

def test_form():
    registration_page = RegistrationPages()
    with allure.step("Открываем demoqa"):
        registration_page.browser_open("https://demoqa.com/automation-practice-form")

    with allure.step("Заполняем имя"):
        registration_page.fill_first_name("Daniil")
    with allure.step("Заполняем фамилию"):
        registration_page.fill_last_name("Efimow")
    with allure.step("Заполняем почту"):
        registration_page.fill_email("daniil.efimow@mail.ru")

    with allure.step("Выбираем gender"):
        registration_page.choice_gender()

    with allure.step("Заполняем номер телефона"):
        registration_page.fill_number("8888888888")

    with allure.step("Заполняем дату рождения"):
        registration_page.fill_date_of_birth('2003', 'May', 14)

    with allure.step("Выбираем subject"):
        registration_page.fill_subject("math")

    with allure.step("Выбираем чекбоксы"):
        registration_page.fill_checkbox()

    with allure.step("Загружаем картинку"):
        registration_page.upload_file("cat.jpeg")

    with allure.step("Заполняем адрес"):
        registration_page.fill_current_address("Orel")

    with allure.step("Выбираем state"):
        registration_page.fill_state("Haryana")

    with allure.step("Выбираем city"):
        registration_page.fill_city("Karnal")

    with allure.step("Кликаем кнопку submit"):
        registration_page.click_submit()

    registration_page.should_registered_user_with(
        "Daniil Efimow",
        "daniil.efimow@mail.ru",
        "Male",
        "8888888888",
        "14 May,2003",
        "Maths",
        "Sports, Reading, Music",
        "cat.jpeg",
        "Orel",
        "Haryana Karnal"
    )