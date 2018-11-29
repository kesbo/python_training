
from fixture.db import DbFixture
# from fixture.orm import ORMFixture


# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(l)
    print(len(l))
finally:
    db.destroy()