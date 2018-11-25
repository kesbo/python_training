# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="",
                      phone_home="", phone_mobile="", phone_work="",
                      email="", email2="", email3="")] + [
    Contact(firstname=random_string("first_name", 10), lastname=random_string("header", 20),
            address=random_string("address", 20), phone_home=random_string("phone_home", 20),
            phone_mobile=random_string("phone_mobile", 20), phone_work=random_string("phone_work", 20),
            email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


