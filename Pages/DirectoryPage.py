from playwright.sync_api import Playwright, Page
from random import *

class Directory:

    def __init__(self, page:Page):
        self.page = page
        self.directory_link = self.page.locator("//span[text()='Directory']")
        self.emp_name = self.page.get_by_placeholder('Type for hints...')
        self.job_title = self.page.locator("div.oxd-select-text-input").nth(0)
        self.location = self.page.locator("div.oxd-select-text-input").nth(1)
        self.search = self.page.locator("//button[text()=' Search ']")
        self.reset_button = self.page.get_by_text(' Reset ')
        self.profile_picture = self.page.locator("div.orangehrm-profile-picture")
        self.list_selection = self.page.locator("//div[@role='listbox']")
        self.records_not_found = self.page.get_by_text("No Records Found")
        self.records_found = self.page.locator("div.orangehrm-horizontal-padding>span")


    def click_directory_link(self):
        try:
            self.directory_link.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def enter_employee_name(self, empname):
        try:
            self.emp_name.type(empname, delay=2)
            self.page.wait_for_timeout(2000)
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('Enter')
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def select_jobtitle(self):
        try:
            self.job_title.click()
            self.page.wait_for_timeout(2000)
            designation = choice([jd.split('\n').remove('-- Select --') for jd in self.list_selection.all_inner_texts()])
            self.page.get_by_role('listbox', name=designation).click()
            self.page.wait_for_timeout(4000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def select_location(self):
        try:
            self.location.click()
            self.page.wait_for_timeout(2000)
            place = choice([loc.split('\n').remove('-- Select --') for loc in self.list_selection.all_inner_texts()])
            self.page.get_by_role('listbox', name=place).click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def click_search_button(self):
        self.search.click()
        self.page.wait_for_timeout(10000)

    def click_reset_button(self):
        try:
            self.reset_button.click()
        except Exception as e:
            print(f"exception while clicking on reset as {e}")
            raise        
    


        