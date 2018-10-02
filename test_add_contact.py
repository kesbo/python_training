# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="qwe", middlename="qwe", lastname="qwe"))
    app.logout()

