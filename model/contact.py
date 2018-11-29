from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, photo=None, title=None, company=None, nickname=None, address=None, home=None,
                 mobile=None, work=None, fax=None, phone2=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address2=None, notes=None, id=None, all_phones_home_page=None, all_emails_home_page=None,
                 all_emails_from_view_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.home = home
        self.photo = photo
        self.title = title
        self.fax = fax
        self.company = company
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_home_page = all_phones_home_page
        self.all_emails_home_page = all_emails_home_page
        self.all_emails_from_view_page = all_emails_from_view_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and\
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
