from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url, local_url, username, password, local_group_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.local_url = local_url
        self.username = username
        self.password = password
        self.group = GroupHelper(self, local_url, local_group_url)
        self.contact = ContactHelper(self, local_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith(self.local_url) and len(wd.find_elements_by_name("add")) > 0):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()