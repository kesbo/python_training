from model.contact import Contact

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Test'))
    app.contact.modify_first_contact(Contact(firstname="New contact"))


def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Test'))
    app.contact.modify_first_contact(Contact(lastname="New contact"))
