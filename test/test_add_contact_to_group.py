from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, orm, json_groups):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    free_groups = []
    for group in groups:
        if len(orm.get_contacts_not_in_group(group)) != 0:
            free_groups.append(group)
    if len(free_groups) == 0:
        group = json_groups
        app.group.create(group)
    else:
        group = random.choice(free_groups)
    contact = random.choice(orm.get_contacts_not_in_group(group))
    count_groups_old = len(orm.get_groups_on_contact(contact))
    app.contact.add_contact_to_some_group(group, contact)
    assert count_groups_old+1 == len(orm.get_groups_on_contact(contact))
    assert orm.contact_in_group(group,contact)
