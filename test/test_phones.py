import re
from random import randrange
from fixture.orm import ORMFixture
from model.contact import Contact


#def test_phones_on_home_page(app):
 #   contact_from_home_page = app.contact.get_contact_list()[0]
 #   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
 #   assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
 #   contact_from_view_page = app.contact.get_contact_from_view_page(0)
  #  contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
  #  assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
   # assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
   # assert contact_from_view_page.workphone == contact_from_edit_page.workphone
   # assert contact_from_view_page.homephone == contact_from_edit_page.homephone


def test_all_data_contact_on_home_page(app, orm):
    contacts_from_bd = orm.get_contact_list()
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test contact 0", lastname="000"))
    contacts_on_home_page = sorted(app.contact.get_contact_list(),  key=Contact.id_or_max)
    contacts_from_bd = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    index = len(orm.get_contact_list())
    for i in [0, index-1]:
        assert contacts_on_home_page[i].lastname == contacts_from_bd[i].lastname
        assert contacts_on_home_page[i].firstname == contacts_from_bd[i].firstname
        assert contacts_on_home_page[i].all_phones_from_home_page == merge_phones_like_on_bd(contacts_from_bd[i])
        assert contacts_on_home_page[i].lastname == contacts_from_bd[i].lastname
        assert contacts_on_home_page[i].firstname == contacts_from_bd[i].firstname
        assert contacts_on_home_page[i].address == contacts_from_bd[i].address
        assert contacts_on_home_page[i].all_emails_from_home_page == merge_emails_like_on_bd(contacts_from_bd[i])


def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: x, filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_bd(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_bd(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: x, filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

#def test_all_data_contact_on_home_page_orm(app, orm):
 #   if len(orm.get_contact_list()) == 0:
  #      app.contact.create(Contact(firstname="test contact 0", lastname="000"))
  #  contact_old = sorted(app.contact.get_contact_list(),  key=Contact.id_or_max)
  #  contact_orm = sorted(orm.get_contact_list(), key=Contact.id_or_max)
  #  index = len(contact_old)
  #  for i in [0, index-1]:
  #      assert contact_old[i].lastname == contact_orm[i].lastname
  #      assert contact_old[i].firstname == contact_orm[i].firstname




