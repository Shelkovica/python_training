from model.contact import Contact


#def test_modify_first_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test contact"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(firstname="new", lastname="new", middlename="new", nickname="", company="", address="", home="", mobile="",
 #                                            work="", fax="", email="", email2="",
 #                                            email3="", homepage="", bday="10", bmonth="April", byear="2001", aday="13", amonth="May", ayear="2002", address2="",
 #                                            phone2="", notes="",
 #                                            title=""))
  #  new_contacts = app.contact.get_contact_list()
   # assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test contact 0", lastname="000"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="contact firstname1", lastname="contact lastname1")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_aday(app):
 #   if app.contact.count() == 0:
 #       app.contact.create(Contact(firstname="test contact"))
 #   old_contacts = app.contact.get_contact_list()
 #   app.contact.modify_first_contact(Contact(aday="15"))
 #   new_contacts = app.contact.get_contact_list()
 #   assert len(old_contacts) == len(new_contacts)
