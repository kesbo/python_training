from model.contact import Contact
from random import randrange
import random


def test_modify_contact(app, db, check_ui):
    app.contact.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_edit_page()
        app.contact.create(Contact(firstname="Kate", middlename="K.Smith", lastname="Smith", nickname="Katty", photo="/Users/i.mamutkina/Desktop/photo.png", title="Dev",
                               company="Google", address="12 Main str, 5 apr, Menlo park", home="123456789", mobile="123456788", work="12346777",
                               fax="fax-123-456-789", email="kate1@gmail.com", email2="kate2@gmail.com", email3="kate3@gmail.com", homepage="Test homepage",
                               bday="12", bmonth="May", byear="1990", aday="17", amonth="June", ayear="1995", address2="10 Main str, 8 apr, Fremont",
                               phone2="987654321", notes="Have a good day! Well done!"))
    app.contact.open_home_page()
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat", photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
                               company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554", work="99887744556",
                               fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com", email3="cat_3@gmail.com", homepage="Changed homepage",
                               bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999", address2="123 Main str, 40 apr, San Carlos",
                               phone2="385263354", notes="New changed notes!")
    #contact.id = old_contacts[index].id
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact)
    app.contact.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)