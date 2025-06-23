from demoqa_test.pages.registration_page import RegistrationPages

def test_form():
    registration_page = RegistrationPages()

    registration_page.browser_open("https://demoqa.com/automation-practice-form")
    registration_page.fill_first_name("Daniil")
    registration_page.fill_last_name("Efimow")
    registration_page.fill_email("daniil.efimow@mail.ru")

    registration_page.choice_gender()

    registration_page.fill_number("8888888888")

    registration_page.fill_date_of_birth('2003', 'May', 14)

    registration_page.fill_subject("math")

    registration_page.fill_checkbox()

    registration_page.upload_file("cat.jpeg")

    registration_page.fill_current_address("Orel")

    registration_page.fill_state("Haryana")
    registration_page.fill_city("Karnal")

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