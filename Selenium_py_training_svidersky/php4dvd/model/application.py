from php4dvd.model.user import User
from selenium.webdriver.common.keys import Keys
from php4dvd.model.film import Film
from php4dvd.pages.page import Page
from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.user_management_page import UserManagementPage
from php4dvd.pages.add_film_page import AddFilmPage
from php4dvd.pages.film_description_page import FilmDescriptionPage
from php4dvd.pages.main_page import MainPage
from php4dvd.pages.user_profile_page import UserProfilePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import time


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.page = Page(driver, base_url)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_profile_page = UserProfilePage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)
        self.add_film_page = AddFilmPage(driver, base_url)
        self.film_description_page = FilmDescriptionPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_login_as(self, user):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return User(username=upp.user_form.username_field.get_attribute("value"),
                    email=upp.user_form.email_field.get_attribute("value"))

    def add_user(self, user):
        self.internal_page.user_management_link.click()
        ump = self.user_management_page
        ump.is_this_page
        ump.user_form.username_field.send_keys(user.username)
        ump.user_form.email_field.send_keys(user.email)
        ump.user_form.password_field.send_keys(user.password)
        ump.user_form.password1_field.send_keys(user.password)
        #ump.user_form.role_select.select_by_visible_text(user.role)
        ump.user_form.submit_button.click()

    def add_film(self, film):
        self.internal_page.add_film_button.click()
        self.add_film_page.film_title_field.send_keys(film.title)
        self.add_film_page.film_year_field.send_keys(film.year)
        self.add_film_page.add_film_submit.click()
        assert film.title in self.add_film_page.result_text

    def search_film(self, film):
        self.page.go_to_main()
        self.main_page.film_search_field.send_keys(film.title)
        self.main_page.film_search_field.send_keys(Keys.RETURN)
        time.sleep(1)
        film_title_on_search_page = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.title")))
        assert film.title in film_title_on_search_page.text

    def remove_film(self):
        self.film_description_page.film_remove_button.click()
        self.wait.until(alert_is_present()).accept()