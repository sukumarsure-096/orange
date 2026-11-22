import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Pages.DirectoryPage import Directory
import pytest
from playwright.sync_api import expect

# @pytest.mark.skip
def test_directory_page(page):
    dp = Directory(page)
    dp.click_directory_link()
    dp.enter_employee_name('Mac')
    dp.select_jobtitle()
    dp.select_location()
    dp.click_search_button()

# @pytest.mark.skip
def test_directory_with_employee_name(page):
    dp = Directory(page)
    dp.click_directory_link()
    dp.click_reset_button()
    dp.enter_employee_name('a')
    dp.click_search_button()
    if dp.records_found.inner_text() == 'No Records Found':
        expect(page.locator("div.orangehrm-container")).to_be_visible()
    else:
        expect(dp.records_found).to_be_visible()

def test_directory_with_job_title(page):
    dp = Directory(page)
    dp.click_directory_link()
    dp.click_reset_button()
    dp.select_jobtitle()
    dp.click_search_button()
    if dp.records_found.inner_text() == 'No Records Found':
        expect(page.locator("div.orangehrm-container")).to_be_visible()
    else:
        expect(dp.records_found).to_be_visible()

# @pytest.mark.skip
def test_directory_with_location(page):
    dp = Directory(page)
    dp.click_reset_button()
    dp.select_location()
    dp.click_search_button()
    if dp.records_found.inner_text() == 'No Records Found':
        expect(page.locator("div.orangehrm-container")).to_be_visible()
    else:
        expect(dp.records_found).to_be_visible()


