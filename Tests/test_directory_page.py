import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Pages.LoginPage import LoginPage
from Pages.DirectoryPage import Directory

def test_directory_page(page):
    lp = LoginPage(page)
    dp = Directory(page)
    lp.login('Admin', 'admin123')
    dp.click_directory_link()
    # dp.enter_employee_name('test')
    dp.select_jobtitle()
    dp.select_location()
    dp.click_search_button()
    lp.click_profile_icon()
    lp.click_logout_button()

