from selene import browser, have, be


def test_practice_form(open_browser):
    browser.element('#First Name').type('Klochko')
    browser.element('#Last Name').type('Ivan')


    browser.quit()