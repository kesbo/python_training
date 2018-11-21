from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, phone_home=None,
                 phone_mobile=None, phone_work=None, phone_secondary=None, email=None,
                 email2=None, email3=None, id=None, all_phones_home_page=None, all_emails_home_page=None,
                 all_emails_from_view_page=None):
        self.first_name = firstname
        self.last_name = lastname
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_secondary = phone_secondary
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_home_page = all_phones_home_page
        self.all_emails_home_page = all_emails_home_page
        self.all_emails_from_view_page = all_emails_from_view_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
