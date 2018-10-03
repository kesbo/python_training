def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit()
    app.session.logout()