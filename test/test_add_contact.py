# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ff", lastname="ff", middlename="ff", nickname="ff", company="ff", address="ff", home="ff",
                mobile="33", work="44", fax="44", email="1@mail.ru", email2="2@mail.ru",
                email3="3@mail.ru", homepage="fff", bday="17", bmonth="December", byear="2000", aday="18",
                amonth="December", ayear="2015", address2="hhh", phone2="hhh", notes="hhh",
                title="title")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
 #   old_contacts = app.contact.get_contact_list()
 #   contact = Contact(firstname="", lastname="", middlename="", nickname="", company="", address="", home="", mobile="",
 #               work="", fax="", email="", email2="",
 #               email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
 #               phone2="", notes="",
  #              title="")
  #  app.contact.create(contact)
  #  new_contacts = app.contact.get_contact_list()
  #  assert len(old_contacts) + 1 == len(new_contacts)
  #  old_contacts.append(contact)
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)