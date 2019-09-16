# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    email_address = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    email_domain = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return email_address+"@"+email_domain+"."+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =  [Contact(firstname="", lastname="", address="",
            homephone="", mobilephone="", workphone="", email="", email2="", email3="", secondaryphone="")]+ [
    Contact(firstname=random_string("first",10), lastname=random_string("las",10),
            address=random_string("addr",10), homephone=random_string("",10), mobilephone=random_string("",10),
            workphone=random_string("",10), secondaryphone=random_string("",10), email=random_email(5), email2=random_email(6),
            email3=random_email(5))
for i in range (10)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


