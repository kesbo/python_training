from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    app.contact.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.open_edit_page()
        app.contact.create(Contact(firstname="Kate", middlename="K.Smith", lastname="Smith", nickname="Katty", photo="/Users/i.mamutkina/Desktop/photo.png", title="Dev",
                               company="Google", address="12 Main str, 5 apr, Menlo park", home="123456789", mobile="123456788", work="12346777",
                               fax="fax-123-456-789", email="kate1@gmail.com", email2="kate2@gmail.com", email3="kate3@gmail.com", homepage="Test homepage",
                               bday="12", bmonth="May", byear="1990", aday="17", amonth="June", ayear="1995", address2="10 Main str, 8 apr, Fremont",
                               phone2="987654321", notes="Have a good day! Well done!"))
    app.contact.open_home_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.contact.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        # contact_list = db.get_contact_list_with_merged_emails_and_phones()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
