# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application_contact import  Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="ff", lastname="ff", middlename="ff", nickname="ff", company="ff", address="ff", home="ff", mobile="33", work="44", fax="44", email="1@mail.ru", email2="2@mail.ru",
                            email3="3@mail.ru", homepage="fff", bday="17", bmonth="December", byear="2000", aday="18", amonth="December", ayear="2015", address2="hhh", phone2="hhh", notes="hhh",
                            title1="title"))
        app.session.logout()


def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", lastname="", middlename="", nickname="", company="", address="", home="", mobile="", work="", fax="", email="", email2="",
                            email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="",
                            title1=""))
        app.session.logout()

