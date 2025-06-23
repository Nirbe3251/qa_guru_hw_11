import os

from selene import browser, have

class RegistrationPages:
    def browser_open(self, value):
        browser.open(value)

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def choice_gender(self):
        browser.element("[for=gender-radio-1]").click()

    def fill_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def fill_checkbox(self):
        browser.element("[for=hobbies-checkbox-1]").click()
        browser.element("[for=hobbies-checkbox-2]").click()
        browser.element("[for=hobbies-checkbox-3]").click()

    def upload_file(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    def fill_state(self, value):
        browser.element("#react-select-3-input").type(value).press_enter()

    def fill_city(self, value):
        browser.element("#react-select-4-input").type(value).press_enter()

    def click_submit(self):
        browser.element("#submit").click()

    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth, subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city,
            )
        )