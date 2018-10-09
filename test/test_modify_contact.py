from model.contact import Contact

def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modifay_first_contact(Contact(firstname="New contact"))
    app.session.logout()

def test_edit_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modifay_first_contact(Contact(lastname="New contact"))
    app.session.logout()