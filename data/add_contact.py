import random
import string
from model.contact import Contact


constant = [
    Contact(firstname="first_name1", lastname="last_name1", address="address1",
            phone_home="phone_home1", phone_mobile="phone_mobile1", phone_work="phone_work1",
            email="email1", email2="email21", email3="email31"),
    Contact(firstname="first_name2", lastname="last_name2", address="address2",
            phone_home="phone_home2", phone_mobile="phone_mobile2", phone_work="phone_work2",
            email="email2", email2="email22", email3="email32")
]


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
