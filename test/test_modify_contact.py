from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new", lastname="new", middlename="new", nickname="", company="", address="", home="", mobile="",
                                             work="", fax="", email="", email2="",
                                             email3="", homepage="", bday="10", bmonth="April", byear="2001", aday="13", amonth="May", ayear="2002", address2="",
                                             phone2="", notes="",
                                             title=""))
    app.session.logout()


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new firstname"))
    app.session.logout()


def test_modify_first_contact_aday(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(aday="15"))
    app.session.logout()