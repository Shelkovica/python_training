from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.contact import ContactHelper


class ApplicationContact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()