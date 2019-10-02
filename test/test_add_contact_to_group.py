from model.contact import Contact
from random import randrange

def test_add_contact_to_group(app, orm):

    #проверяем наличие контактов. если нет - то создаем

    print(len(orm.get_contact_list()))
  #  assert False
#проверяем наличие групп. если нет - то создаем
    contacts = orm.get_contact_list()
    index = randrange(len(app.contact.get_contact_list()))
    id = contacts[index].id
    count_groups_old = orm.get_groups_on_contact(contacts[index])

    app.contact.add_contact_to_some_group_by_id(id)

# сравниваем количество групп у контакта со старым.


