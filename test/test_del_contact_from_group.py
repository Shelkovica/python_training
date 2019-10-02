from model.contact import Contact
from model.group import Group
from random import randrange

def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    print(len(orm.get_contact_list()))
    contacts = orm.get_contact_list()
    index = randrange(len(app.contact.get_contact_list()))
    id = contacts[index].id
    count_groups_old = len(orm.get_groups_on_contact(contacts[index]))
    app.contact.add_contact_to_some_group_by_id(id)
    count_groups_new = len(orm.get_groups_on_contact(contacts[index]))
    assert count_groups_old+1 == count_groups_new