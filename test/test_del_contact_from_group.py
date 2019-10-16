from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test contact"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_some_group(group, contact)
    else:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_some_group(group, contact)
    count_groups_old = len(orm.get_groups_on_contact(contact))
    app.contact.del_contact_from_group(group, contact)
    count_groups_new = len(orm.get_groups_on_contact(contact))
    assert count_groups_old-1 == count_groups_new
    assert orm.contact_in_group(group,contact) is False