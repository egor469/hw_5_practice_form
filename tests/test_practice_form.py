from selene import browser, have, be, command
import os


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Klochko')
    browser.element("#lastName").type('Ivan')
    browser.element("#userEmail").type('xpan12344@yandex.ru')
    browser.element('[for = "gender-radio-2"]').click()
    browser.element("#userNumber").type('7903369856')
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click().element('option[value="8"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1989"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element("#subjectsInput").type('Maths').press_enter()
    browser.element("[for = 'hobbies-checkbox-1']").click()
    browser.element('#uploadPicture').type(f"{os.path.dirname(os.getcwd())}/123456789.jpeg")
    browser.element('#currentAddress').type('Moscow City, Big street, life House')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element(".table").should(have.text('Klochko Ivan'))
    browser.element(".table").should(have.text('xpan12344@yandex.ru'))
    browser.element(".table").should(have.text('Female'))
    browser.element(".table").should(have.text('7903369856'))
    browser.element(".table").should(have.text('17 September,1989'))
    browser.element(".table").should(have.text('Maths'))
    browser.element(".table").should(have.text('Sports'))
    browser.element(".table").should(have.text('123456789.jpeg'))
    browser.element(".table").should(have.text('Moscow City, Big street, life House'))
    browser.element(".table").should(have.text('NCR Delhi'))

    browser.element('#closeLargeModal').should(be.clickable).click()

    browser.quit()