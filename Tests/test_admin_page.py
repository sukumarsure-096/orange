import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from playwright.sync_api import Playwright, expect
from Pages.AdminPage import AdminPage
from Pages.LoginPage import LoginPage
import pytest

# @pytest.mark.skip
def test_admin_page(page):
    ap = AdminPage(page)
    lp = LoginPage(page)
    lp.enter_username('Admin')
    lp.enter_password('admin123')
    lp.click_login_button()
    ap.admin_page()
    ap.enter_user_name('Admin')
    ap.select_user_role('Admin')
    ap.enter_employee_name('Lisa')
    ap.click_search()
    lp.click_profile_icon()
    lp.click_logout_button()
