class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_from(contact)
        # submit creation contact
        wd.find_element_by_name("submit").click()

    def fill_contact_from(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()

    def modifay_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_from(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

