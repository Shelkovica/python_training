from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    app.wd.implicitly_wait(5)
    new_contacts = app.contact.get_contact_list()
   # assert len(old_contacts) - 1 == len(new_contacts)
