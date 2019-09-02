from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test contact"))
    app.contact.modify_first_contact(Contact(firstname="new", lastname="new", middlename="new", nickname="", company="", address="", home="", mobile="",
                                             work="", fax="", email="", email2="",
                                             email3="", homepage="", bday="10", bmonth="April", byear="2001", aday="13", amonth="May", ayear="2002", address2="",
                                             phone2="", notes="",
                                             title=""))


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test contact"))
    app.contact.modify_first_contact(Contact(firstname="new firstname"))


def test_modify_first_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test contact"))
    app.contact.modify_first_contact(Contact(aday="15"))
