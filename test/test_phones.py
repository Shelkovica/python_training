import re
from random import randrange
from fixture.orm import ORMFixture




def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
 #   contact_from_view_page = app.contact.get_contact_from_view_page(0)
  #  contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
  #  assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
   # assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
   # assert contact_from_view_page.workphone == contact_from_edit_page.workphone
   # assert contact_from_view_page.homephone == contact_from_edit_page.homephone


def test_all_data_contact_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: x, filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_all_data_contact_on_home_page_orm(app, orm):
    contact_old = app.contact.get_contact_list()
    contact_orm =orm.get_contact_list()
    print(contact_orm)

  #  c for c in list(app.contact.get_contact_list()):
#        contact_from_home_page = app.contact.get_contact_list()[0]
   # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
   # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
   # assert contact_from_home_page.lastname == contact_from_edit_page.lastname
   # assert contact_from_home_page.firstname == contact_from_edit_page.firstname
   # assert contact_from_home_page.address == contact_from_edit_page.address
   # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
