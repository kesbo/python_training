from model.contact import Contact
from random import randrange


def test_edit_contact_firstname_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Test'))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="qwe", lastname="qwe", phone_home="99999", email="test@test.test")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

# def test_edit_first_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname='Test'))
#     old_contact = app.contact.get_contact_list()
#     contact = Contact(firstname="qwe", lastname="qwe")
#     contact.id = old_contact[0].id
#     app.contact.modify_first_contact(Contact(lastname="New contact"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)
#     old_contact[0] = contact
#     assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
