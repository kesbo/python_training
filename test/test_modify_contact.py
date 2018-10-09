from model.contact import Contact

def test_edit_first_contact_firstname(app):
    app.contact.modifay_first_contact(Contact(firstname="New contact"))


def test_edit_first_contact_lastname(app):
    app.contact.modifay_first_contact(Contact(lastname="New contact"))
