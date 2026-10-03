import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Pages.LoginPage import LoginPage
from Pages.AdminPage import AdminPage
import pytest
from DataDriven.data_driven import import_data_from_json, import_data_from_csv
from playwright.sync_api import expect
from DataDriven.faker_data import FakeData


data = import_data_from_json('TestData/login_data.json')

# @pytest.mark.skip
@pytest.mark.parametrize('testcase, un, pwd, results', data)
def test_login_with_valid_and_invalid_data(page, testcase, un, pwd, results):
    lp = LoginPage(page)
    lp.login(un,pwd)
    if results == 'success':
        lp.click_profile_icon()
        lp.click_logout_button()
    else:
        expect(lp.invalid_credentials).to_be_visible()

def test_login_invalid_data(page):
    lp = LoginPage(page)
    fd = FakeData()
    un = fd.get_user_name()
    pwd = fd.get_password()
    lp.login(un, pwd)
    expect(lp.invalid_credentials).to_be_visible()

def test_forgot_password(page):
    lp = LoginPage(page)
    lp.click_forgot_password()
    lp.enter_username__forgot_password('xyz')
    lp.click_cancel_button()
    expect(lp.username).to_be_visible()


# def test_login_for_admin(page):
#     lp = LoginPage(page)
#     ap = AdminPage(page)
#     lp.login('Admin','admin123')
#     ap.admin_page()
#     ap.enter_user_name('Admin')
#     ap.select_user_role('Admin')