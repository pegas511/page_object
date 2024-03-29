from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        print(self.browser.current_url)
        assert "login" in self.browser.current_url, \
        "Is not Login link"
        

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
        "Email form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
        "Password form is not presented"
        
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), \
        "Email registration form  is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_1), \
        "Password1 registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2), \
        "Password2 registration form is not presented"

    def register_new_user(self, email, password):

        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_2).send_keys(password)
        #Нажатие кнопки регистрации
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()