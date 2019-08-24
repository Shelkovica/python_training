# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")


    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()


    def create_contact(self, wd, firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", home="home",
                       mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                       homepage="homepage", bday="bday", bmonth="bmonth", byear="byear", aday="aday", amonth="amonth",
                       ayear="ayear", address2="address2", phone2="phone2", notes="notes"):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name(firstname).click()
        wd.find_element_by_name(firstname).clear()
        wd.find_element_by_name(firstname).send_keys("ff")
        wd.find_element_by_name(middlename).click()
        wd.find_element_by_name(middlename).clear()
        wd.find_element_by_name(middlename).send_keys("ff")
        wd.find_element_by_name(lastname).click()
        wd.find_element_by_name(lastname).clear()
        wd.find_element_by_name(lastname).send_keys("ff")
        wd.find_element_by_name(nickname).click()
        wd.find_element_by_name(nickname).clear()
        wd.find_element_by_name(nickname).send_keys("ff")
        wd.find_element_by_name(title).click()
        wd.find_element_by_name(title).clear()
        wd.find_element_by_name(title).send_keys("ff")
        wd.find_element_by_name(company).click()
        wd.find_element_by_name(company).clear()
        wd.find_element_by_name(company).send_keys("ff")
        wd.find_element_by_name(address).click()
        wd.find_element_by_name(address).clear()
        wd.find_element_by_name(address).send_keys("ff")
        wd.find_element_by_name(home).click()
        wd.find_element_by_name(home).clear()
        wd.find_element_by_name(home).send_keys("ff")
        wd.find_element_by_name(mobile).click()
        wd.find_element_by_name(mobile).clear()
        wd.find_element_by_name(mobile).send_keys("33")
        wd.find_element_by_name(work).click()
        wd.find_element_by_name(work).clear()
        wd.find_element_by_name(work).send_keys("44")
        wd.find_element_by_name(fax).click()
        wd.find_element_by_name(fax).clear()
        wd.find_element_by_name(fax).send_keys("44")
        wd.find_element_by_name(email).click()
        wd.find_element_by_name(email).clear()
        wd.find_element_by_name(email).send_keys("1@mail.ru")
        wd.find_element_by_name(email2).click()
        wd.find_element_by_name(email2).clear()
        wd.find_element_by_name(email2).send_keys("2@mail.ru")
        wd.find_element_by_name(email3).click()
        wd.find_element_by_name(email3).clear()
        wd.find_element_by_name(email3).send_keys("3@mail.ru")
        wd.find_element_by_name(homepage).click()
        wd.find_element_by_name(homepage).clear()
        wd.find_element_by_name(homepage).send_keys("fff")
        wd.find_element_by_name(bday).click()
        Select(wd.find_element_by_name(bday)).select_by_visible_text("17")
        wd.find_element_by_css_selector("option[value=\"17\"]").click()
        wd.find_element_by_name(bmonth).click()
        Select(wd.find_element_by_name(bmonth)).select_by_visible_text("December")
        wd.find_element_by_css_selector("option[value=\"December\"]").click()
        wd.find_element_by_name(byear).click()
        wd.find_element_by_name(byear).clear()
        wd.find_element_by_name(byear).send_keys("2000")
        wd.find_element_by_name(aday).click()
        Select(wd.find_element_by_name(aday)).select_by_visible_text("18")
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"18\"]").click()
        wd.find_element_by_name(amonth).click()
        Select(wd.find_element_by_name(amonth)).select_by_visible_text("December")
        wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"December\"]").click()
        wd.find_element_by_name(ayear).click()
        wd.find_element_by_name(ayear).clear()
        wd.find_element_by_name(ayear).send_keys("2015")
        wd.find_element_by_name(address2).click()
        wd.find_element_by_name(address2).clear()
        wd.find_element_by_name(address2).send_keys("hhh")
        wd.find_element_by_name(phone2).click()
        wd.find_element_by_name(phone2).clear()
        wd.find_element_by_name(phone2).send_keys("hhh")
        wd.find_element_by_name(notes).click()
        wd.find_element_by_name(notes).clear()
        wd.find_element_by_name(notes).send_keys("hhh")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
