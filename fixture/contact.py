from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        self.fill_contact_form(contact)

    def fill_contact_form(self, contact):
        self.change_field_valuee("firstname", contact.first_name)
        self.change_field_valuee("lastname", contact.last_name)
        self.change_field_valuee("address", contact.address)
        self.change_field_valuee("home", contact.phone_home)
        self.change_field_valuee("mobile", contact.phone_mobile)
        self.change_field_valuee("work", contact.phone_work)
        self.change_field_valuee("email", contact.email)
        self.change_field_valuee("email2", contact.email2)
        self.change_field_valuee("email3", contact.email3)

    def change_field_valuee(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cell_list = element.find_elements_by_tag_name("td")
                last_name = cell_list[1].text
                first_name = cell_list[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_emails = cell_list[4].text
                all_phones = cell_list[5].text
                self.contact_cache.append(Contact(lastname=last_name, firstname=first_name, id=id,
                                                  all_phones_home_page=all_phones, all_emails_home_page=all_emails
                                                  ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")[7]
        cells.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
            wd = self.app.wd
            self.open_home_page()
            row = wd.find_elements_by_name("entry")[index]
            cells = row.find_elements_by_tag_name("td")[6]
            cells.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=first_name, lastname=last_name, id=id, phone_home=phone_home,
                       phone_mobile=phone_mobile, phone_work=phone_work, email=email, email2=email2, email3=email3)

    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        all_emails = wd.find_elements_by_css_selector('a[href*="mailto:email"]')
        return Contact(phone_home=phone_home,
                       phone_mobile=phone_mobile, phone_work=phone_work, all_emails_from_view_page=all_emails)
