from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    contacts = orm.get_contact_list()
    max_group = orm.get_group_list()
    for c in contacts:
        g = orm.get_groups_on_contact(c)
        if len(g) < len(max_group):
            count_groups_old = len(orm.get_groups_on_contact(c))
            name_group = orm.select_group_for_add(c)
            app.contact.add_contact_to_some_group_by_name(c.id, name_group)
            break
    assert len(count_groups_old)+1 == len(orm.get_groups_on_contact(contacts[index]))
